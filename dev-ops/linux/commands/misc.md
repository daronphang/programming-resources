## References

```
~/        Refers to current user's home directory i.e. /home/daronphang or /root if root user
ctrl+L    Clear terminal
```

## Pipe operator

Lets you use two or more commands such that the output of one command serves as input to the next.

```sh
$ cat filename | less
$ cat sample | grep Apple
```

## Echo

Used to display line of text to screen/file. Typically used in scripting language and batch files.

```sh
$ echo [option] [string(s)]
$ echo "hello world!"
$ echo -e "hello \bworld"    e flag acts as an interpretor of escaped characters
```

## CPU load

```sh
$ cat /proc/stat
```

## Aliases

Can create aliases for most used commands. Custom shortcuts used to represent a command or set of commands executed with or without custom options. Can create temporary (available for current terminal session) or permanent.

```sh
$ alias BYCPU='ps aux --sort -%cpu'
```

To keep aliases permanently, can save them in your user's shell configuration profile file.

```
~/.bashrc
~/.zshrc
~/.config/fish/config.fish

$ source ~/.bashrc
```

## Hard/Soft links

Link command creates a **'hard'** link named FILE2, which shares the same index node as existing file FILE1. Both share the same index node and hence, point to the same data on the disk. Modifying one is functionally the same as modifying the other.

```sh
$ echo "This is a file." > FILE1.txt
$ link FILE1.txt FILE2.txt
$ cat FILE1.txt     # same as cat FILE2.txt
```

## Symlinks

**'Soft'** symbolic linnks are different than 'hard' links; they link to another link instead of linking to the data of a file.

'ln' by default creates a hard link, but has the option of creating symbolic links with -s. Symlinks can link to directories, cross file system boundaries, and are useful to make shortcuts to long, complicated filenames.

Removing the file that a symlink points to breaks the link.

```sh
$ ln FILE1.txt FILE2.txt
$ ln -s FILE1.txt FILE2.txt

$ ln -s documents/ dox-sym-link
$ ls documents
$ ls dox-sym-link
```

## nohup (no hang up)

Keeps processes running even after exiting the shell or terminal. Processes running with this command will ignore the SIGHUP signal even after exiting the shell. Once a job is started, stdin will not be available to the user.
