## Unicode encoding and decoding

```
encode('utf-8')     convert str into bytes
decode('utf-8')     convert bytes into str
```

## Bytes

A string object is made up of Unicode characters that is only human readable. Each Unicode character is assigned a code point which can be expressed as a sequence of hex digits.  
A byte object is a sequence of bytes. Machine readable and can be saved into memory. Can be used in applications that process pure ASCII instead of unicode text.

```py
stringobject = 'ant'    # unicode characters are a, n, t

stringobject = '\u0061\u006E\u0074'   # Unicode codepoints, a hexadecimal number

>>> b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-16')
'蓏콯캁澽苏'
>>> b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-8')
'τoρνoς'
```

## Hexadecimals

Hexadecimal has base 16 and is represented with prefix 0x.

```
1 digit = 4 bits
binary(8) = 8 bytes = 64 bits = 16 digits
```

### Bytes to string

```py
string = "DARONPHANG_B16A"
string_bytes = string.encode('utf-8')
string_hex_str = string_bytes.hex()
print(string_hex_str)   # 4441524f4e5048414e475f42313641

# short form
str_hex = hex(int(string.encode('utf-8').hex(), 16))

add_oid = ['0x{}'.format(secrets.token_hex(7)) for item in range(len(payload['add_entries']))]
```

```py
numbers = [2, 3, 5, 7]
str = 'hello world'

byte_arr = bytearray(numbers)
byte_arr = bytearray(str, 'utf-8')
```

### String to bytes

```py
# when removing 0x, function also remooves leading 0s, need to add back
key = '0x0F5B109D55FB25F2'
bytes.fromhex(key[2:].zfill(16))  # need remove 0x
```
