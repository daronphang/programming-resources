## Byzantine faults (arbitrary faults)

A process is said to fail in an arbitrary manner if it may deviate in any conceivable way from the algorithm assigned to it. No assumptions are made on the behavior of faulty processes, which are allowed any kind of output and, therefore, can send any kind of message.

Byzantine faults are the most expensive to tolerate. This can occur when:

- Bug in the implementation of language or compiler
- Process is controlled by malicious user to deliberately try and prevent correct system operation
- Messages exchanged being eavesdropped by attackers, who may access, insert or modify messages of their own

## Byzantine fault tolerance (BFT)

Byzantine fault tolerance is a feature of a distributed network to reach consensus even when some of the nodes in the network fail to respond or respond with incorrect information. The object of a BFT mechanism is to safeguard against system failures by employing collective decision making (correct and faulty nodes) which aims to reduce the influence of faulty nodes.

It can be theoretically proven that a system with byzantine nodes can tolerate up to 1/3 of faulty nodes and still operate correctly.

### Byzantine general's problem

The byzantine problem refers to a group of generals. Each general has an army and a location surrounding a fortress, and they must decide as a group to attack or retreat.

If they all make the same decision, they are successful. However, if there's a miscommunication or treachery causing some generals to attack while the others retreat, then the battle is lost. These types of problems are known as Byzantine faults.
