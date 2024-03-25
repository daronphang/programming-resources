## CR (Carriage Return) and LF (Line Feed)

CR and LF are control characters, respectively coded `0x0D` and `0x0A`. They are used to mark a line break in a text file.

Windows uses two characters in the CRLF sequence, while Unix uses only LF. In the HTTP protocol, CRLF sequence is always used to terminate a line.

### Bash scripts

When editing a bash script file on Windows and porting over to Linux, the editor may throw an error of bad interpreter. It can be resolved by converting CRLF to LF.

```sh
sed -i -e 's/\r$//' scriptname.sh
```
