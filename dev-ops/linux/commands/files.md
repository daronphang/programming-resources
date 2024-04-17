## File management

### Listing

List files or directories (similarly to file explorer) from CLI.

```sh
$ ls [flags] [directory]
$ ls            # Current working directory
$ ls /          # Root directory
$ ls *          # Subdirectories
$ ls -R         # Recursive i.e. list all files with corresponding subdirectories down to last file
$ ls -l         # Table format (permissions, owner, size, last modified date, file name)
$ ls -lh        # Table format with readable file sizes
$ ls -a         # All files including hidden file (starts with .)
$ ls -a -lh
$ ls -S         # Sort by
```

### Finding

```sh
$ find . -name "*.log"
$ find /Path -name " file_name*"        # Find all files in /Path with file_name*
$ find /Path/bar* -name "file_name*"    # Find all files with pattern in bar* subdirectory
```

### Reading

'cat' allows us to create single or multiple files, view content of a file, concatenate files and redirect output in terminal or files.

'more' displays a file in the terminal, one page at a time if the text passed is too large to fit on one screen. 'Enter' key scrolls through the file line by line, while 'space' key scrolls one full screen at a time. File is closed by pressing 'q' key. Can only scroll down but not up.

However, after closing the file, its contents stay written in the terminal window. 'less' has the added benefit of not keeping the contents after the file is closed.

'less' also has support for different file formats including jar, war, zip, pdf, gif, png, etc i.e. reading metadata whereas 'more' would print binary data.

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

$ more filename
$ less filename

$ tac filename          # reverses order, starts from last line
$ tac filename | less
```

### Creating

```sh
$ cat > newfile         # creates a new file called newfile
$ cat copied-file > destination-file    # copying content

$ touch /path/to/file filename.txt
```

### Copying

```sh
$ scp filename username@IPaddress:path
$ scp readme.md roo@45.79.185.156:/home/daronphang

$ scp roo@45.79.185.156:readme.md .     # copy from server to local pc
```

### Emptying

```sh
$ > test.log
$ : > test.log
$ true > test.log
```

### Extracting/Compressing

tar.gz (gzip) file contains compressed files to save storage space and bandwidth during downloading process. It is a combination of .tar file and .gz file.

```
x   instructs tar to extract the files from zipped file
v   verbose
z   instructs tar to decompress files
f   filename to work on
```

```sh
$ gzip test.txt     # compress file, outputs test.txt.gz
```

```sh
$ tar -xvzf documents.tar.gz
tar –xvzf documents.tar.gz –C /home/user/destination    # put files to specific directory
```

### Installing

dpkg is a tool to install, build, remove and manage Debian packages.

```sh
$ sudo dpkg -i package_file.deb     # for ubuntu debian, to install dependencies automatically
$ sudo dpkg -r package.deb  # remove program
$ sudo dpkg --update-avail  # updating repositories
```

## Directories

```sh
$ pwd   # Present working directory
$ mkdir -p test1/test2/test3 # Creates parent directory 'test1' if doesn't exist
```

## File permissions

### Check File/Folder Permissions

```sh
$ ls -l filename

$ ls -ld /data    # d flag for directory and not contents
$ ls -ld /data | head
```

### Folder Ownership

```sh
$ls -la
```

### File Ownership

For numeric IDs that exist as username, it should be prefixed with the + symbol.

- USER: If only user is specified, specified user will become the owner of files.
- USER: User will become owner of files and file group ownership is changed to user.
- USER:GROUP: user and group will be changed by specified users.
- :GROUP: Only group ownership of files is changed.
- : : if only colon is given, no change is made.

```sh
$ ls -l filename.txt                      Find out who owns a file and what group it belongs to

$ chown [OPTIONS] USER[:GROUP] FILE(s)    Changing onwership of file
$ chown -R USER:GROUP DIRECTORY           Recursive, changes ownership of all files and subdirectories
```

### File Mode

Dictates what the user/group that owns a file can do with it i.e. read, write, execute.

```
$ ls -l filename
# -rw-rw-rw- 1 cooluser cooluser 0 Jun 7 19:47 learningnotes.txt

1   File type, '-' for regular, 'd' for directories, 'l' for symlinks
2   Permissions, (user)-(group)-(all other users and groups)
3   Number of links to the file
4   User that owns the file
5   Group that owns the file
6   Size of file in bytes
7   Date and time that the file was created or last modified
8   Filename
```

### Absolute Mode

```
0       No permission
1       Execute
2       Write
3       Execute + write
4       Read
5       Read + execute
6       Read + write
7       Read + write + execute
```

```
# total of 3 parameters

---       No permission
-x        Execute only
-w-       Write only
r--       Read only
-wx       Write and execute
r-x       Read and execute
rwx       Read, write and execute
```

```sh
$ chmod 400 learningnotes.txt       # user has read access
$ chmod 600 learningnotes.txt       # user has read and write
$ chmod 664 learningnotes.txt       # user and group has read+write, others have read-only
```

### Symbolic Method

```
u     User that owns the file
g     Group that owns the file
o     All other users and groups
a     All users and groups
r     Read permission
w     Write permission
x     Execute permission
-     Remove permission
+     Add permission
=     Make permissions exact
```

### Example

```sh
$ chmod [uago][+-=][rwx] filename
$ chmod o+w learningnotes.txt
$ chmod go-rw myfile
```
