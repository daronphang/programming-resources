## Contracts

<img src="./assets/contracts.png">

### Strict

A strict contract requires adherence to names, types, ordering, and all other details, leaving no ambiguity.

Many architects like strict contracts because they model the identical semantic behavior of internal method calls. However, strict contracts create brittleness in integration architecture. The more frequently they must change, the more rippling problems they cause for other services. However, architects aren’t forced to use strict contracts and should do so only when advantageous.

A common anti-pattern that some architects fall victim to is to assume that the contract provided by a service needs all other parts, and so architects include them in the contract from the outset. This is an example of **stamp coupling** and an anti-pattern in most cases, as it introduces breaking changes where they aren’t needed, making the architecture fragile yet providing little benefit.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>

<tr>
<th>Guaranteed contract fidelity</th>
<th>Tight coupling</th>
</tr>

<tr>
<th>Versioned</th>
<th>Versioned</th>
</tr>

<tr>
<th>Easier to verify at build time</th>
<th></th>
</tr>

<tr>
<th>Better documentation</th>
<th></th>
</tr>
</table>

### Loose

Loose contracts offer the least coupled integration points.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>

<tr>
<th>Highly decoupled</th>
<th>Contract management</th>
</tr>

<tr>
<th>Easier to evolve</th>
<th>Requires fitness functions</th>
</tr>
</table>
