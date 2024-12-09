## Never reuse field IDs

You must never reuse a field ID as this is essentially changing the type of a field which is not a compatible change.

## Everything is optional

This approach seems counter-intuitive that an RPC query being processed should not include any field that is "required". This validation should be done in the application level, but not in RPC protocol itself for the following reasons:

- RPC is wire transmission; it should be agnostic of what is required by a particular query
- Makes unit testing more difficult
- No backward compatibility if you need to change data type
