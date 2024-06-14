## Code replication

In code replication, shared code is copied into each source code repository for the corresponding service. While this technique preserves the bounded context, it should be approached with **extreme caution** for the obvious reason that if a bug is found in the code or an important change to the code is needed, it would be very difficult and time-consuming to update all services containing the replicated code.

At times, however, this technique can prove useful, particularly for highly static one-off code that most services need.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>
<tr>
<td>
• Preserves the bounded context </br>
• No code sharing</br>
</td>
<td>
• Difficult to apply code changes </br>
• Code inconsistency across services </br>
• No versioning capabilities across services </br>
</td>
</tr>
</table>
