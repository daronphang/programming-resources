## Consistency

Consistency refers to the strictness of transactional integrity that communication calls must adhere to. Atomic transactions (all-or-nothing transactions requiring consistency during the processing of a request) lie on one side of the spectrum, whereas different degrees of eventual consistency lie on the other side.

Transactionality, where having several services participate in an all-or-nothing transaction, is one of the most difficult problems to model in distributed architectures, resulting in the general advice to try to avoid cross-service transactions.
