### Conditions

Use '-a' and '-o' for AND and OR comparisons.

In an if statement, grep returns exit 0 (true) if it found something, and otherwise exit 1 (false).

```sh
read x
read y

if [ $x -gt $y ]
then
echo X is greater than Y
elif [ $x -lt $y -a $x -lt 5 ]
then
echo X is less than Y
elif [ $x -eq $y ]
then
echo X is equal to Y
fi
```

### Looping

```sh
for i in {1..5}
do
    echo $i
done

for X in cyan magenta yellow
do
	echo $X
done

$ words="foo bar baz"
for word in $words; do
  echo "$word"
```

For iterating over arguments, can use @.

```sh
VAR1=$1
VAR2=$2
for arg in $@; do
  echo $arg
  done
```

### While Loop

```sh
i=1
while [[ $i -le 10 ]] ; do
   echo "$i"
  (( i += 1 ))
done
```
