## VSCode

Stable version: January 2021, version 1.53.2

### Extensions

1. AREPL for real-time evaluation
2. Kite AutoComplete AI Code (need install Kite Engine)
3. Monokai Dimmed
4. Code Runner
5. Jupyter (need pip install ipykernel)
6. Live Server for js
7. Prettier
8. Error Lens
9. Auto Rename Tag
10. Bracket Pair Colorizer
11. Live Server
12. ES7-Snippets
13. Debugger for Chrome
14. ESLint
15. Remote Development
16. TODO Highlight
17. dotENV

### JS Prettier and ESLint Setup

### Angular

1. Npm install prettier.
2. Create .prettierrc.json/.prettierrc and .prettierignore files.
3. Configure JSON settings for VSCode.

```
$npm install --save-dev --save-exact prettier tslint-config-prettier

# .prettierignore
$/dist
$package-lock.json
$package.json
```

```json
// .prettierrc.json
{
    "printWidth": 100,
    "tabWidth": 2,
    "singleQuote": true,
    "bracketSpacing": true,
    "semi": true
}

// VSCode JSON Settings
{
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.formatOnPaste": false,
}
```

### Golang

Install all tools and restart VS code: Command + Shift + P -> Go: Install/update tools.

### Remote Development

When cloning a repo, can run in container instead of running npm install locally. Container contains all node_modules dependencies. Main difference is that need to specify "host" parameter to tell Angular/React to connect to IP address. Also unable to use certain Windows commands in terminal as container is running in Linux (debian).

### Linting

Need to install pylint in virtual environment; activation depends on autosave function.

### Customization in settings.json

```json
{
  "python.pythonPath": "venv\\Scripts\\python.exe",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "editor.lineHeight": 20,
  "editor.letterSpacing": -0.7,
  "editor.renderIndentGuides": true,
  "python.linting.pycodestyleEnabled": true,
  "python.linting.flake8Enabled": true,
  "editor.rulers": [80],
  "kite.codefinder.enableLineDecoration": false,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "code-runner.clearPreviousOutput": true,
  "code-runner.executorMap": {
    "python": "C:\\financial_analysis\\venv\\Scripts\\python.exe"
  },
  "editor.codeActionsOnSave": { "source.fixAll.eslint": true },
  "editor.formatOnSave": true,
  "eslint.alwaysShowStatus": true,
  "todohighlight.isEnable": true,
  "todohighlight.include": [
    "**/*.js",
    "**/*.jsx",
    "**/*.ts",
    "**/*.tsx",
    "**/*.html",
    "**/*.php",
    "**/*.css",
    "**/*.scss",
    "**/*.py"
  ],
  "todohighlight.exclude": [
    "**/node_modules/**",
    "**/bower_components/**",
    "**/dist/**",
    "**/build/**",
    "**/.vscode/**",
    "**/.github/**",
    "**/_output/**",
    "**/*.min.*",
    "**/*.map",
    "**/.next/**",
    "**/venv/**"
  ]
}
```
