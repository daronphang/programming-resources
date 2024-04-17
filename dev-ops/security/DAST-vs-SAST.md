## Overview

As security threats become more commonplace, dev teams that rely on just one type of testing leave their applications vulnerable to attack.

Functional testing, which consists of unit and integration tests, is helpful but only checks for problems you thought of in advance, and is focused on meeting business objectives. It does not check for security flaws leading to data breaches.

## SAST (Static Application Security Testing)

SAST is open-box testing that scans a software application from the inside out **before it is compiled or executed** i.e. does not execute the application. It analyzes program source code to identify security vulnerabilities. These include SQL injection, buffer overflows, XML attacks, and other OWASP Top 10 security risks.

The SAST methodology guides developers to begin testing their application at **early development stages** without executing a functional component. This approach discovers application source code security flaws early and avoids leaving security issues to later development phases. This decreases development time and enhances overall program security.

As SAST is scanning your source code, it is specific to the programming languages and development frameworks used, and the SAST tools you use needs to support the programming language you are using.

## DAST (Dynamic Application Security Testing)

DAST testing simulates the actions of a malicious actor trying to break into your application from the outside (closed-box). It scans running software applications in real-time against leading vulnerability sources, and has **no access to its source code**.

DAST assumes the tester does not know the application's inner functions. It can detect security vulnerabilities that SAST cannot, such as those that **appear only during program runtime**.

As DAST tests require a complete working application, reserve them for a later phase in your application development process. Testers need to interact with the application: provide inputs, check outputs, and simulate other actions typical of user interactions.
