## Basics

Text editor used in CLI.

```
vim <filename>    Start in command mode i.e. cannot edit; need to insert
h,j,k,l           Move left, down, up right
:q                Warns about unsaved changes before exiting
:qa               Quits all buffers with warning and exit vim
:qa!              Quits all buffers without saving and without warning
0, $              Move to beginning of line, end of line
w, b              Move forward/backward one word
gg                Move to beginning of file
shift+g           Move to last line in file
ctrl+o            Go back to previous location (not necessarily a buffer)
tab               Go next location
:E                Go directory listing of opened file
backspace         Go directory listing of opened file
ctrl+o            Go back to previous directory/buffer
:Ex               Go back to previous directory
:b#               Go to previously edited buffer
:e <filename>     Go directly to file
shift+h           Move to top of screen
shift+m           Move to middle of screen
shift+l           Move to bottom of screen

// can preface movement number of times i.e. 6k to move up six lines

// can use in combination with above i.e. d$ will delete to end of line
:i            Edit file content
:w            Save
:wq           Save and exit
:q            Exit

d             Delete
!             Force
o             Insert text at beginning of following line

v             Visual mode for copying, selects character
y             Copy/yank while visual mode is active, selects highlighted text rows
p             Paste

d             Cut
dd            Cut/delete line

:x            Save file and exit
:q!           Quit without saving file

/text         Search text in document
n, N          Next instance, previous instance
```

## Buffer

An in-memory text of a file. Anytime an existing file is opened or created using Vim, a buffer will be allocated as the in-memory representation of said file. Any changes made will be tracked within the buffer.

```
:ls       View buffer
1 %a  "file.md"       line 1

1       buffer number
%       Corresponds to buffer in current window
a       Active buffer that is loaded and visible
line    Where the cursor is located at
```

## Viewports

```
ctrl+w  v       Open a new VIM window
ctrl+w  l       Move to right window
ctrl+w  h       Move to left window
ctrl+w  q       Close window

ctrl+w  +       Increase window height
ctrl+w  -       Decrease window height
ctrl+w  =       Reset window height
```

## Indenting

```
:set paste    # turn off auto indenting
:set nopaste

>10>            # indent 10 lines to the right
<5<             # indent 5 lines to the left
```
