## Working effectively with legacy code

Designs that cannot tolerate changing requirements are poor designs to begin with. It is the goal of every competent software developer to **create designs that tolerate change**. Many teams are trying very hard, but because of schedule pressure, the weight of history, or lack of better code to compare their efforts to, lead them to writing legacy code.

To many, legacy code refers to the tangled, unintelligible structure, code that you have to change but don’t really understand. Features that should have been easy to add becomes difficult. Code can degrade in many ways, and many of them have nothing to do with whether the code came from another team. Ultimately, legacy code is simply **code without tests**.

When we have legacy code, making changes can be difficult and take a much longer time. We have to hunt through the code, understand all of the ramifications of a change, and then make the change.

Many of us have tried to discover ways to prevent code from becoming legacy, such as following books on principles, patterns and practices. However, clean code without tests still requires incredible skill and a clear understanding of what can happen at every step. Moreover, even the most disciplined team will create messes from time to time. Hence, it is more important to reverse it, rather than preventing it. However, reversing is not easy: it takes time, work, endurance and care.

## Changing software

There are four primary reasons to change software:

1. Adding a feature
2. Fixing a bug
3. Improving the design
4. Optimizing resource usage

### Improving design (refactoring)

When we want to alter software’s structure to make it more maintainable, generally we want to keep its behavior intact also. Ultimately, we don’t want ourselves or anyone else to have to go through the work we are doing to try to understand it. When we drop behavior in that process, we often call that a bug. One of the main reasons why many programmers don’t attempt to improve design often is because it is relatively easy to lose behavior or create bad behavior in the process of doing it.

The act of improving design without changing its behavior is called refactoring. The idea behind refactoring is that we can make software more maintainable without changing behavior if we write tests to make sure that existing behavior doesn’t change and take small steps to verify that all along the process.

Refactoring differs from general cleanup in that we aren’t just doing low-risk things such as reformatting source code, or invasive and risky things such as rewriting chunks of it. Instead, we are making a series of small structural modifications, supported by tests to make the code easier to change. The key thing about refactoring from a change point of view is that there aren’t supposed to be any functional changes when you refactor.

### Putting it all together

<table>
<tr>
<th></th>
<th>Adding a Feature</th>
<th>Fixing a Bug</th>
<th>Refactoring</th>
<th>Optimizing</th>
</tr>
<tr>
<td>Structure</td>
<td>Changes</td>
<td>Changes</td>
<td>Changes</td>
<td>-</td>
</tr>
<tr>
<td>New Functionality</td>
<td>Changes</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Functionality</td>
<td>-</td>
<td>Changes</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Resource Usage</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>Changes</td>
</tr>
</table>

## Preserving behavior

When we change software, we also have to figure out how to preserve the rest of the behavior. We have to know that the behavior isn’t changing, and that can be tough. The amount of behavior that we have to preserve isn't the big deal; the big deal is that we often don't know how much of that behavior is at risk when we make changes.

## Risky change

It’s tempting to think that we can minimize software problems by avoiding them, but, unfortunately, it always catches up with us. When we avoid creating new classes and methods, the existing ones grow larger and harder to understand.

The difference between good systems and bad ones is that, in the good ones, you feel pretty calm after you’ve done that learning, and you are confident in the change you are about to make. We can make functional changes that deliver value while bringing more of the system under test. In poorly structured code, the move from figuring things out to making changes feels like jumping off a cliff to avoid a tiger; you hesitate.

Avoiding change has other bad consequences. When people don’t make changes often they get rusty at it. Breaking down a big class into pieces can be pretty involved work unless you do it a couple of times a week. When you do, it becomes routine. You get better at figuring out what can break and what can’t, and it is much easier to do.

## Working with feedback

Changes in a system can be made in two primary ways:

1. Edit and pray
2. Cover and modify

### Edit and pray

In this mode, you carefully plan the changes you are going to make, you make sure that you understand the code you are going to modify, and then you start to make the changes. When you’re done, you run the system to see if the change was enabled, and then you poke around further to make sure that you didn’t break anything.

### Cover and modify

The idea behind it is that it is possible to work with a safety net when we change software. Covering software means covering it with tests. When we have a good set of tests around a piece of code, we can make changes and find out very quickly whether the effects were good or bad.
