## CI with Jenkins

You use Karma to run your unit tests. Karma takes care of starting a browser, connecting to it, and running your tests there. As Karma runs your unit tests in a real browser, your tests have access to a real DOM and your client code runs exactly as it will in production.

Jenkins expects tests results to be in an XML file with the same format the JUnit would use to report Java test results. This format has become the de-facto standard, and test frameworks and a variety of languages can now report test results in this JUnit-XML style.

## Configuration

### Scripts

```json
{
  "scripts": {
    "ng": "ng",
    "test": "ng test",
    "test:ci": "ng test --code-coverage --no-progress --browsers=ChromeHeadlessNoSandbox --watch=false"
  }
}
```

### karma.conf.js

Create a custom launcher called ChromeHeadlessNoSandbox.

```js
// Karma configuration file, see link for more information
// https://karma-runner.github.io/1.0/config/configuration-file.html

module.exports = function (config) {
  config.set({
    basePath: "",
    frameworks: ["jasmine", "@angular-devkit/build-angular"],
    plugins: [
      require("karma-jasmine"),
      require("karma-chrome-launcher"),
      require("karma-jasmine-html-reporter"),
      require("karma-coverage"),
      require("@angular-devkit/build-angular/plugins/karma"),
    ],
    client: {
      jasmine: {
        // you can add configuration options for Jasmine here
        // the possible options are listed at https://jasmine.github.io/api/edge/Configuration.html
        // for example, you can disable the random execution with `random: false`
        // or set a specific seed with `seed: 4321`
      },
      clearContext: false, // leave Jasmine Spec Runner output visible in browser
    },
    jasmineHtmlReporter: {
      suppressAll: true, // removes the duplicated traces
    },
    coverageReporter: {
      dir: require("path").join(__dirname, "./coverage/orderapp"),
      subdir: ".",
      reporters: [{ type: "html" }, { type: "text-summary" }],
    },
    junitReporter: {
      outputDir: "build/test-results/karma",
      outputFile: "karma-test.xml",
      useBrowserName: true,
    },
    reporters: ["progress", "kjhtml"],
    browsers: [" Chrome"],
    restartOnFileChange: true,
    customLaunchers: {
      ChromeHeadlessNoSandbox: {
        base: "ChromeHeadless",
        flags: ["--no-sandbox"],
      },
    },
  });
};
```

### Dockerfile

Split the build into different stages, and switch between testing and production environments with base image. Requires installation of Chrome.

```dockerfile
ARG WORKINGPATH=/orderapp
ARG ENTRYPATH=/orderapp
ARG PORT=80
ARG CONFIG=development
ARG BASEHREF=/orderapp/
ARG DEPLOYMENT_IMAGE=nginx:1.25.4-alpine

# Stage: BUILD
# Install dependencies first to maximize Docker layer caching.
FROM node:21 AS build
ARG WORKINGPATH
ARG CONFIG
ARG BASEHREF
WORKDIR ${WORKINGPATH}

# Install packages.
COPY package.json package-lock.json kendo-ui-license.txt ./
# Dev is chosen over Prod as build requires dev config for angular dependencies.
RUN npm ci && npm cache clean --force && \
    npx kendo-ui-license activate && \
    npm link @angular/cli

# Install Chrome for running UI tests.
RUN apt-get install -y gnupg wget curl unzip --no-install-recommends; \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | \
    gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/google.gpg --import; \
    chmod 644 /etc/apt/trusted.gpg.d/google.gpg; \
    echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list; \
    apt-get update -y; \
    apt-get install -y google-chrome-stable;

# Build from source code.
COPY . .
RUN ng build --configuration=$CONFIG --base-href=$BASEHREF

# Stage: RUN APPLICATION
FROM $DEPLOYMENT_IMAGE
ARG ENTRYPATH
ARG PORT
WORKDIR ${ENTRYPATH}

COPY nginx/default.conf /etc/nginx/conf.d/
COPY --from=build ${ENTRYPATH}/dist/orderapp/browser /usr/share/nginx/html/orderapp
EXPOSE ${PORT}
CMD ["nginx", "-g", "daemon off;"]
```

### Pipeline

```groovy
stage('Test Image Build') {
    steps {
        // Specify DEPLOYMENT_IMAGE as build.
        // If omitted, it will use nginx base image instead.
        sh 'docker build --build-arg CONFIG=testing --build-arg BASEHREF=$BASEHREF --build-arg DEPLOYMENT_IMAGE=build -t $IMAGE_BUILD_TAG_LATEST .'
    }
}

stage('Run Tests in Image') {
  steps {
    sh '''
    docker run -d -v $WORKSPACE:/coverage:rw --name test-$SERVICE_NAME $IMAGE_BUILD_TAG_LATEST sleep 5m
    docker exec test-$SERVICE_NAME sh -c "npm run test:ci && cp /orderapp/coverage/lcov.info /coverage/lcov.info"
    '''
  }
  post {
    always {
      sh 'docker rm -f test-$SERVICE_NAME'
    }
    failure {
      sh 'docker rmi $IMAGE_BUILD_TAG_LATEST'
    }
  }
}
```
