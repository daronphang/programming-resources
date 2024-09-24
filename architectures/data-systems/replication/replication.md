## Replication

There are two primary reasons for replicating data:

1. To increase the reliability of a system from failures, corrupted data, etc.
2. To improve performance by dividing the workload among the processes accessing the data (scaling)

Unfortunately, there is a price to be paid when data are replicated. The problem with replication is that having multiple copies may lead to **consistency problems**. Whenever a copy is modified, that copy becomes different from the rest. Consequently, modifications have to be carried out on all copies to ensure consistency. Exactly when and how those modifications need to be carried out determines the price of replication.

### Synchronous replication

Synchronous replication ensures tight consistency between replicas. The key idea is that an update is performed at all copies as a single atomic operation, or transaction. Unfortunately, implementing atomicity involving many replicas that may be widely dispersed across a large-scale network is inherently difficult when operations are also required to complete quickly.

### Asynchronous replication

To avoid global synchronizations, a method is to relax the consistency constraints in order to gain performance. The price paid is that copies may not always be the same everywhere.

## Choosing a replication strategy

<table>
<tr>
<th>Strategy</th>
<th>Consistency</th>
<th>Write Availability</th>
<th>Complexity</th>
</tr>

<tr>
<td>Leader-follower</td>
<td>Strong</td>
<td>Low (depends on leader)</td>
<td>Low</td>
</tr>

<tr>
<td>Multi-leader</td>
<td>Weak</td>
<td>High</td>
<td>High</td>
</tr>

<tr>
<td>Leaderless</td>
<td>Low</td>
<td>High</td>
<td>Moderate</td>
</tr>
</table>
