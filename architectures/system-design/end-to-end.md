## End-to-end arguments in system design

End-to-end arguments are often applied to error control and correctness in application systems. The principle of end-to-end argument suggests that **functions placed at low levels of a system may be redundant** or of little value when compared with the cost of providing them at that low level. Examples include bit error recovery, security using encryption, duplicate message suppression, recovery from system crashes, and delivery acknowledgement. Low level mechanisms to support these functions are justified only as **performance enhancements**.

## End-to-end caretaking of providing reliable data transmission

Considering the problem of file transfer, where the objective is to move file from computer A into computer B without damage:

1. At host A the file transfer program calls upon the file system to read the file from the disk, where it resides on several tracks, and the file system passes it to the file transfer program in fixed-size blocks chosen to be disk-format independent
2. The file transfer program at host A asks the data communication system to transmit the file using some communication protocol (e.g. TCP) that involves splitting the data into packets. The packet size is typically different from the file block size and the disk track size
3. The data communication network moves the packets from computer A to computer B
4. At host B a data communication program removes the packets from the data communication protocol and hands the contained data on to a second part of the file transfer application, the part that operates within host B
5. At host B, the file transfer program asks the file system to write the received data on the disk of host B

However, there are some threats to the transaction that a designer might be concerned about:

- The file may be stored correctly in host A. However, upon reading, it may contain incorrect data due to hardware faults in the disk storage system
- The file transfer program or the data communication system might make a mistake in buffering and copying the data of the file, either at host A or host B
- The hardware processor or its local memory might have a transient error while doing the buffering and copying, either at host A or host B
- The communication system might drop or change the bits in a packet, or lose a packet or deliver a packet more than once
- Either host may crash part way during the transaction

### Coping with threats

One approach might be to reinforce each of the steps along the way using duplicate copies, timeout and retry, carefully located redundancy for error detection, crash recovery, etc. The goal would be to **reduce the probability of each individual threats to an acceptably small value**. However, brute force countermeasures appear uneconomical.

An alternate approach is called **end-to-end check and retry**. For example, stored with each file is a checksum that has sufficient redundancy to reduce the chance of an undetected error in the file to an acceptably negligible value. After the file has been transferred from A to B, a final step of the application in B reads the file, recalculates the checksum and compares with the original.

One would take it further by guaranteeing a reliable data transmission from the communication system, which could be accomplished by providing selective redundancy in the form of packet checksums, sequence number checking, etc. However, though this may guarantee the file is not corrupted, the **application still has counter remaining threats**. Hence, this does not reduce the burden on the application program to ensure reliability.

### Pitfall of low-level functions

Consider a network system that uses a packet checksum on each hop from one gateway to the next:

- Application programmers that are aware of the checksum may assume the network provides reliable transmission, and hence no checksumming is performed at application level
- A transient error with a very low frequency may arise from a defective gateway, during copying of data from an input to an output buffer e.g. **byte pair interchanging**, which happens once in every million bytes passed
- Data passed over the defective gateway will be corrupted but undetected at application level

### Performance aspects

However, it would be too simplistic to conclude that lower levels should play no part in obtaining reliability.

For example, a network that is unreliable, dropping one message of every hundred messages sent: checksumming at application level would perform very poorly as the length of file increases.

This shows that efforts at lower levels to improve network reliability can have a significant effect on application **performance**. Key idea is that lower levels **need not provide perfect reliability**.

## Examples

The basic argument that a lower-level subsystem that supports a distributed application may be wasting its effort providing a function that must by nature be implemented at the application level anyway can be applied to a variety of functions in addition to reliable data transmission.

### Delivery guarantees

Knowing for sure that the message was delivered to the target host is not very important; instead, it is more important for the application to know that the host **acted on the message**.

### Secure transmission of data

If the data transmission system performs encryption and decryption:

1. It must be trusted to manage encryption keys securely
2. Authenticity of message must still be checked by the application

If the application performs end-to-end encryption:

1. It obtains its required authentication check
2. It handles key management to its satisfaction
3. Data is never exposed outside of the application

Automatic encryption of all traffic by the communication system may be called for something else e.g. that a misbehaving user or application program does not deliberately transmit information that should not be exposed. Network-level encryption is different from authentication: it is simpler that the same keys can be used by all hosts.

### Duplicate message suppression

Even if the network suppresses duplicates, the application itself may accidentally duplicate requests in its own failure/retry procedures. Hence, suppression must be accomplished by the application itself with knowledge of how to detect its own duplicates.
