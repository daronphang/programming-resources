## CI with Jenkins

You use Karma to run your unit tests. Karma takes care of starting a browser, connecting to it, and running your tests there. As Karma runs your unit tests in a real browser, your tests have access to a real DOM and your client code runs exactly as it will in production.

Jenkins expects tests results to be in an XML file with the same format the JUnit would use to report Java test results. This format has become the de-facto standard, and test frameworks and a variety of languages can now report test results in this JUnit-XML style.
