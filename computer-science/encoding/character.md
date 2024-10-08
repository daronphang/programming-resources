## Character encodings

Character encodings used to turn bits into characters that are human-readable output. Character encodings are stored on disk.

## ASCII

The first character set of encoding standard between computers on the internet. 128 characters containing 0-9, A-Z in upper and lower case, and some special characters. Each character is represented by a number between 32-127. Each character requires 7 bits. Character sets used in modern computers and HTML are based on ASCII.

As ASCII characters utilize 7 bits, there are still 127 more combinations to be represented; this gave birth to extended ASCII. However, different organizations came up with their own variants; this led to conflicted character encodings, and each extended ASCII was platform dependent.

```
Dec	Hex	Binary    HTML	Char
00  00  00000000  &#0   Null
01  01  00000001  &#1   SOH
42  2A  00101010  &#42  *
48	30	00110000  &#48;	0
49	31	00110001  &#49;	1
50	32	00110010  &#50;	2
51	33	00110011  &#51;	3
65	41	01000001  &#65;	A
66	42	01000010  &#66;	B
67	43	01000011  &#67;	C
68	44	01000100  &#68;	D
```

### Example (Character B)

To represent a character in binary, simply work in base2.

```
Character B = 66 = 64 + 2 = 01000000 + 00000010 = 01000010
```

```
Power   Base2   Binary
0       1       00000000
1       2       00000010
2       4       00000100
3       8       00001000
4       16      00010000
5       32      00100000
6       64      01000000
7       128     10000000
8       255     11111111
```

## Unicode

Universal character standard that assigns a codepoint to every character, number and symbol in every language in the world. Unicode characters can be referenced by their codepoint. Has backwards compatability with ASCII. Total of 143,859 characters. **Unicode uses hexadecimal base**.

```
U+<hex-code> from U+0000 to U+10FFFF
Computer Hope
U+0043 U+006F U+006D U+0070 U+0075 U+0074 U+0065 U+0072 U+00A0 U+0048 U+006F U+0070 U+0065
```

First 128 characters of Unicode are the same as ASCII character set.

```
Unicode ASCII Char
U+0041	65    A
U+0042	66    B
U+0043	67    C
U+0044	68    D
U+0045	69    E
```

### Unicode Transformation Format (UTF)

Problem with Unicode is that to represent 100,000 characters (or 100,000 numbers equivalent), need 32 bits per character. However, first 128 characters of ASCII need only 7 bits. To eliminate wastage, different UTF encodings were introduced. To represent Unicode characters as binary data (raw 8-bit values).

Without UTF formatting, character A would be equivalent to:
00000000 00000000 00000000 001000001

```
UTF-8       Each symbol represented by 1-to-4 bytes code. Standard encoding on web.
UTF-16      Fixed width encoding scheme in which each symbol is represented by two-byte code.
```

### UTF-8 encoding (8 bits)

World Wide Web's most common character encoding. It can translate any Unicode character to a matching unique binary string. Each character is represented by one to four bytes (saving memory) and has backwards compatibility with ASCII.

Leading bits of bytes contain metadata specific to UTF. For instance, two-byte UTF-8 representation:

- First byte has 110; 11 indicates two-byte sequence, 0 indicates code bits will follow
- Second byte has 10: signals that it is a continuation in UTF-8 sequence

```
One-byte        0XXXXXXX                For first 128 ASCII characters
Two-bytes       110XXXXX 10XXXXXX
Three-bytes     1110XXXX 10XXXXXX 10XXXXXX
```

```
Char Dec Unicode UTF-8             Binary
ç    231 U+0347  11000011 10100111 00011100111 = 11100111
ã    227 U+0343  11000011 10100011 00011100011 = 11100011
```

### UTF-16 (2 bytes)

Encodes a Unicode character into a string of either two or four bytes. **UTF-16 is not compatible with UTF-8** as they use different algorithms to map code points back to binary strings.

## Unicode vs ASCII

ASCII is designed to represent basic English characters (128 characters). Uses one byte to represent each character.

Unicode designed to support characters from all languages across the world (1,000,000 characters). Supports up to four bytes per character.
