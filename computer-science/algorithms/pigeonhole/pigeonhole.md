## Pigeonhole Principle

The pigeonhole principle is one of the simplest but most useful ideas in mathematics. It says that if N+1 pigeons occupy N holes, then some hole must have at least 2 pigeons.

### Theorem

Given m items and n containers, if m > n:

- At least one container contains m/n items (ceiling)
- Remaining containers contain at least one item (floor)

For a given problem, the key is to **reverse engineer, compute the edge case, and find such that the ceiling of m/n is 2**.

### Formula

```
For Kn + 1 pigeons kept in n pigeon holes, where K is a positive integer:
avg = (Kn + 1) / n = K + 1/n
```

## Examples

### Example 1

A bag contains 10 red marbles, 10 white marbles, and 10 blue marbles. What is the minimum no. of marbles you have to choose randomly from the bag to ensure that we get 4 marbles of same color?

```
n = 3 (number of colors or pigeonholes)
K + 1 = 4
ans = Kn + 1 = 3*3 + 1 = 10
```

### Example 2

How many people are required to have at least two people with the same birthday?

```
ceil(n/365) = 2
n = 366
```

### Example 3

There are 35 different time periods during which classes at a local college can be scheduled. If there are 679 different classes, what is the minimum number of rooms needed?

```
ans = ceil(679/35) = 19.4 = 20
```

### Example 4

A box contains 6 red, 8 green, 10 blue, 12 yellow and 15 white balls. What is the minimum no. of balls we have to choose randomly from the box to ensure that we get 9 balls of same color?

```
// cannot blindly apply pigeon principle
// as there are balls containing less than 9
// apply pigeon principle to blue, yellow and white balls

n = 3
K + 1 = 9

ans = 3*8 + 1 + 6 + 8 = 39
```

### Example 5

In a computer science department, a student club can be formed with either 10 members from first year or 8 members from second year or 6 from third year or 4 from final year. What is the minimum no. of students we have to choose randomly from department to ensure that a student club is formed?

```
n = 4

ans = 10 + 8 + 6 + 4 - 4 + 1 = 25
```

### Example 6

Given a set from 1 to 20, what is the minimum count of numbers we need to pick to guarantee that the sum of two picked numbers is 21?

```
1,2,3,4,5,...,20
{1,20}
{2,19}
{3,18}
{4,17}
{5,16}
{6,15}
{7,14}
{8,13}
{9,12}
{10,11}

ceil(n/10) = 2
n = 11
```

### Example 7

Given a 8cm by 8cm grid, how many dots are needed such that 2 dots will have a distance less than square root of 8cm?

```
Using pythagoras theorem, each square must be 2x2 (square root of 2^2 + 2^2)
Grid size = 16

ceil(n/16) = 2
n = 17
```

### Example 8

How many students do you need in a school to guarantee that there are at least 2 students who have the same first two initials?

```
number of possible sets = 26 * 26 = 676
ceil(n/676) = 2
n = 677
```
