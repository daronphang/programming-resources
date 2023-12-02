## Why need preprocessors

CSS is a style sheet language that determines the way a document is presented. However, there are certain features that CSS does not offer including inheritance selector, mixin, etc. To get access to these features, developers use **CSS preprocessors**. A CSS preprocessoris an application that lets you generate CSS from its own unique syntax, and they make it easy and more efficient to work with CSS. SASS and SCSS are the most popular CSS preprocessors.

## SASS (Syntactically Awesome Style Sheets)

SASS is a preprocessor scripting language that is either intepreted or compiled into a CSS file. It extends CSS by adding features of traditional programming langauges i.e. OOP. It uses SassScript, which is a dynamically-typed scripting langauge.

SASS was originally written in Ruby, and was required to have Ruby installed on the system. However, with the decreasing popularity of Ruby, it became obsolete in 2019. LibSass is another implementation in C but it also became deprecated. If you wish to use SASS on a JS-based system, you need to integrate **Dart Sass** as a JS library.

### Syntax

SASS consists of two syntaxes. The older one is called the indented syntax and is similar to Haml, which is a templating system aimed at generating clean HTML code.

The other syntax is SCSS which uses CSS-like block formatting.

## SCSS (Sassy CSS)

SCSS is a different syntax for using SASS. SCSS is built on top of CSS and contains more features i.e. superset of CSS. The main aim of SCSS is to bridge the gaps between CSS and SASS. However, a few features that give it an edge over SASS include:

- Using all CSS features
- Allows inline documentation i.e. adding comments alongside code
- Handle many classes and nested styles
- Gives you more control over code as its syntax is more expressive
