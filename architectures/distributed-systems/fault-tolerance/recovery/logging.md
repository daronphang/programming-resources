## Message logging

Checkpointing allows the recovery to a previous, correct state. However, taking a checkpoint is often a costly operation and may have a severe performance penalty. To reduce the number of checkpoints, many fault-tolerant distributed systems **combine checkpointing with message logging**.

The basic idea underlying message logging is that if the transmission of messages can be replayed, we can still reach a globally consistent state, but without having to restore that state from local storage. Instead, a checkpointed state is taken as a starting point, and all messages that have been sent since are simply retransmitted and handled accordingly.

In order to correctly replay messages, each message is considered to have a header that contains all information necessary to retransmit it i.e. sender, receiver, sequence number, etc.

After a checkpoint has been taken, there are two forms of performing message logging:

- **Sender-based**: A process logs its messages before sending them off
- **Receiver-based**: The receiving process first logs an incoming message before delivering it to the application it is executing

When a receiving process crashes, it is necessary to restore the most recently checkpointed state, and from there on replay the messages that have been sent.
