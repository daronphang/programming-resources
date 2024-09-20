## Protecting DNS users

In general, one can state that information stored in DNS is public. However, DNS queries should be kept confidential.

## DNS over TLS

Systems today allow applications to set up a secure channel to a remote DNS resolver through TLS, mostly by that application’s local resolver. Having DNS over TLS prevents a third party from discovering to which Websites an application is actually referring.

## DNS over HTTPS

Many modern browsers support issuing DNS queries over HTTPS. the browser is configured to directly access a remote DNS resolver that supports DNS over HTTPS. As HTTPS runs over TLS, this mechanism essentially offers the same protection as DNS over TLS. A major difference is that DNS queries are now completely handled out of the control of local administrators. This also means that local policies concerning allowing or denying access to certain sites are bypassed.
