## Eslint

A tool to report patterns within JavaScript (ECMAScript standard in general) in order to identify potential problems and make code more consistent across entire applications.

https://github.com/angular-eslint/angular-eslint

1. Install Eslint in project

```sh
$ ng add @angular-eslint/schematics

$ ng lint --fix
```

2. Install Eslint extension for VSCode

## Prettier

An opinionated code formatter (removes your initially written code styling and applies consistent style, across all your project files), which supports many programming languages.

https://github.com/prettier/eslint-config-prettier

1. Install Prettier and eslint-compatible plugins to ensure there are no overlapping rules

```sh
$ npm install prettier --save-dev
$ npm install prettier-eslint eslint-config-prettier eslint-plugin-prettier —-save-dev
```

2. Install Prettier plugin for VSCode
3. Add .prettierrc in root directory

```json
{
  "tabWidth": 2,
  "useTabs": false,
  "singleQuote": true,
  "semi": true,
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "trailingComma": "es5",
  "bracketSameLine": true,
  "printWidth": 120,
  "endOfLine": "auto",
  "overrides": [
    {
      "files": "*.html", // prettier should not parse html files due to conflicts
      "options": {
        "parser": "angular"
      }
    }
  ]
}
```

4. Add .prettierignore file in root directory (copy from .gitignore)
5. Add Prettier plugin in eslintrc.json

```json
{
  "root": true,
  "ignorePatterns": ["projects/**/*"],
  "overrides": [
    {
      "files": ["*.ts"],
      "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/recommended",
        "plugin:@angular-eslint/recommended",
        "plugin:@angular-eslint/template/process-inline-templates",
        "plugin:prettier/recommended" // last to override other configs
      ],
      "rules": {
        "@angular-eslint/directive-selector": [
          "error",
          {
            "type": "attribute",
            "prefix": "app",
            "style": "camelCase"
          }
        ],
        "@angular-eslint/component-selector": [
          "error",
          {
            "type": "element",
            "prefix": "app",
            "style": "kebab-case"
          }
        ]
      }
    },
    {
      "files": ["*.html"],
      "extends": [
        "plugin:@angular-eslint/template/recommended",
        "plugin:@angular-eslint/template/accessibility",
        "plugin:prettier/recommended" // last to override other configs
      ],
      "rules": {}
    }
  ]
}
```

## VSCode

1. Add the following to settings.json file

```json
{
  // ,,,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

## lint-staged

https://github.com/lint-staged/lint-staged

1. Install lint-staged for pre-commit hooks

```sh
$ npm install --save-dev lint-staged
```

2. Add .lintstagedrc file

```json
{
  "*.{css,scss,less,ts,html}": ["prettier --write", "eslint"],
  "*.{json,md}": ["prettier --write"]
}
```

## Husky

1. Download husky

```sh
$ npm install husky --save-dev
```

2. Update package.json and install husky

```sh
$ npm pkg set scripts.prepare="husky install"
$ npm run prepare
```

```json
{
  // ...
  "scripts": {
    "prepare": "husky install"
  }
}
```

3. Add pre-commit hooks

```sh
$ npx husky add .husky/pre-commit "npm test"
```

4. Modify pre-commit file as necessary in `.husky/pre-commit`

```sh
. "$(dirname -- "$0")/_/husky.sh"

npx lint-staged
```
