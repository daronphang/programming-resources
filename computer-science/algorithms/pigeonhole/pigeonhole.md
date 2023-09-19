## Pigeonhole Principle

The pigeonhole principle is one of the simplest but most useful ideas in mathematics. It says that if N+1 pigeons occupy N holes, then some hole must have at least 2 pigeons.

### Theorem

If 'A' is the average number of pigeons per hole, where A is not an integer:

- At least one pigeon hole contains ceil['A'] pigeons
- Remaining pigeon holes contain at most floor['A'] pigeons

### Formula

```
For Kn + 1 pigeons kept in n pigeon holes, where K is a positive integer:
avg = (Kn + 1) / n = K + 1/n
```

## Examples

### Drawing Marbles

A bag contains 10 red marbles, 10 white marbles, and 10 blue marbles. What is the minimum no. of marbles you have to choose randomly from the bag to ensure that we get 4 marbles of same color?

Solution is 10.

```
n = 3 (number of colors or pigeonholes)
K + 1 = 4
ans = Kn + 1 = 3*3 + 1 = 10
```

### Birthday

How many people are required to have at least two people with the same birthday?

Solution is 367.

```
n = 366 (number of days)
K + 1 = 2
ans = Kn + 1 = 366 + 1 = 367
```

### Class schedule

There are 35 different time periods during which classes at a local college can be scheduled. If there are 679 different classes, what is the minimum number of rooms needed?

Solution is 20.

```
ans = 679 / 35 = 19.4 = 20
```
