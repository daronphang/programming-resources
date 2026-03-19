## Reading files

### cat

'cat' allows us to create single or multiple files, view content of a file, concatenate files and redirect output in terminal or files.

```sh
$ cat filename          # Displays complete contents without using inputs to scroll through it
$ cat file1 file2
$ cat -n file           # view contents preceding with line numbers

$ cat testfile testfile1    # Outputs contents of both files
$ cat /etc/file1
$ $cat > test2       # Creates a file
$ cat -n song.txt    #Displays line numbers of file

$ head filename
$ tail filename
$ tail filename -n3     # -n flag outputs the number of lines to display
$ tail -f /var/log/syslog
```

### more

'more' displays a file in the terminal, one page at a time if the text passed is too large to fit on one screen. 'Enter' key scrolls through the file line by line, while 'space' key scrolls one full screen at a time. File is closed by pressing 'q' key. Can only scroll down but not up. However, after closing the file, its contents stay written in the terminal window.

```sh
$ more filename
```

### less

'less' has the added benefit of not keeping the contents after the file is closed. It does not load the entire file into memory at once, making it faster for viewing large files.

'less' also has support for different file formats including jar, war, zip, pdf, gif, png, etc i.e. reading metadata whereas 'more' would print binary data.

```sh
$ less filename

$ tac filename          # reverses order, starts from last line
$ tac filename | less
```

## grep (Global Regular Expression Print)

Grep utilities are a family that includes grep, egrep, and fgrep for searching files.

```sh
$ grep 'word' filename
$ grep -i 'bar' file1         # Perform case-insensitive search
$ grep -R 'httpd'             # Look for all files in current directory and subdirectories
$ grep -c 'hello' file1       # Search and display total number of times word appears
$ grep 'word' *               # Search all files in current directory
$ grep 'str1\|str2' file1
$ grep -nr word ~/

$ grep 'redeem reward' ~/*.txt
$ tail -f /var/log/file.log | grep search_ter

$ grep '\word\>' filename       # exact match
```

```
-w          Exact match
-c          This prints only a count of the lines that match a pattern
-h          Display the matched lines, but do not display the filenames
-i          Ignores, case for matching
-l          Displays list of a filenames only
-n          Display the matched lines and their line numbers
-v          This prints out all the lines that do not matches the pattern
-e exp      Specifies expression with this option. Can use multiple times
-f          File takes patterns from file, one per line
-E          Treats pattern as an extended regular expression (ERE)
-w          Match whole word
-o          Print only the matched parts of a matching line
-A n        Prints searched line and nlines after the result
-B n        Prints searched line and n line before the result
-C n        Prints searched line and n lines after before the result
-r          Recursively search subdirectories listed
-q          Quiet, to not output matched text but return exit status code
```

## awk

awk is a powerful text-processing command in Linux used to analyze, filter, and manipulate structured data such as logs, CSV files, and command output. It works by scanning input line by line and performing actions based on patterns and fields.

```sh
$ awk 'condition {print $1}'

$ awk '{print}' employee.txt # prints all lines

$ awk '{print $1 $4}' employee.text # prints first and fourth column

$ kubectl get nodes --context gru3a --no-headers | awk '$1 ~ /^cache/ && $2 == "NotReady" {print $1}'
```

## xargs

xargs takes input from stdin and passes it as arguments for another command.

```sh
$ kubectl get pods | awk '{print $1}' | xargs kubectl delete pod # single execution

$ echo "a b c d" | xargs -n 2 echo # explicit batching
```
