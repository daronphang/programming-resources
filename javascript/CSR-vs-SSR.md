## SSR (Server Side Rendering)

SSR is when you render your website's HTML on the server. This is opposed to CSR (Client Side Rendering) whereby the website in the browser by manipulating the DOM with Javascript.

When a page is rendered into HTML on the server, all of the heavy-lifting is taken care of. When the client receives the response, it is ready to display the page.

Benefit of SSR is faster page load speed when is an important metric for user experience and technical SEO.

### Checking for SSR

View the page source and if the HTML code is complete with all the content, the site is likely using SSR.

### SSR Benefits

- Facilitate web crawlers through search engine optimization (SEO)
- Improve performance on mobile and low-powered devices
- Show the first page quickly with a first-contentful paint (FCP)

## Code Splitting and Hydration

To make pages interactive while preserving the benefits of SSR, an added layer of complexity known as code-splitting and hydration can help.

SSR frameworks such as Next.js and Astro allow us to build an HTML only page on the server that can be sent to the client fast, while allowing for specific bundles of Javascript to be sent to the client after the initial HTML has loaded.

In React, this process is known as hydration. The code is split into manageable chunks that can then be requested on as needed basis and injected/hydrated into the client page to add interactivity and functionality.

## Angular Universal

Displaying the first page quickly can be critical for user engagement. Your application might have to launch faster to engage these users before they decide to do something else.

With Angular Universal, you can generate landing pages for the application that look like the complete application. The pages are pure HTML, and can display even if JavaScript is disabled. The pages don't handle browser events, but they do support navigation through the site using routerLink.

In practice, you'll serve a static version of the landing page to hold the user's attention. At the same time, you'll load the full Angular application behind it. The user perceives near-instant performance from the landing page and gets the full interactive experience after the full application loads.
