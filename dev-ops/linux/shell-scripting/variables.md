### Shell Variables

As general rule, use quotes if the variable can either be empty or contain spaces.

```sh
#! /bin/sh
variable ="Hello"
variable2 = 3
echo $variable
echo "$variable"
echo `variable`     # all 3 forms work

var=$((3+9))
echo $var
```

### Passing Commands

In Bash, there are reserved variables which we can use to recall user-defined arguments i.e. $1, $2, $3. $0 cannot be used as it references your Bash script itself.

```console
$ sh some_script.sh apple orange pear
```

```sh
echo "The first fruit is: $1"
echo "The second fruit is: $2"
echo "The third fruit is: $3"
```

### Read User Input

Read command looks for space or tab separator in input text in order to split the text into multiple values.

Can use silent flag '-s' to hide input characters from screen i.e. password.

```sh
echo "what is your name?"
read first
echo "How do you do, $first?"
read second
echo "I am $second too!"

read -p "Enter your age" variable_name    # -p flag to prompt user with a custom msg

echo -n "Please state your name and your surname: "
read name surname
```

```sh
#!/bin/bash

VAR1="Mihalis"  # assignment
myVar="$(pwd)"  # output of external program

echo -n "My name is ${VAR1}"  # -n prevents echo from printing a newline character
echo " and I work from "
echo $myVar

myVar=`pwd` # equivalent to $(pwd)
echo $myVar
```

### Using UNIX Environment Variables

```sh
#!/bin/bash

# Read
if [[ -z "${PATH}" ]]; then # -z flag tests whether a variable has length of 0
    echo "PATH is empty!"
else
    echo "PATH: $PATH"
fi

# Change
PATH=${PATH}:/tmp
echo "PATH: $PATH"

# Delete
export PATH=""    # export creates an env variable i.e. global
if [[ -z "${PATH}" ]]; then
    echo "PATH is empty!"
else
    echo "PATH: $PATH"
fi

# Create
MYPATH="/bin:/sbin:/usr/bin"
echo "MYPATH: ${MYPATH}"
```
