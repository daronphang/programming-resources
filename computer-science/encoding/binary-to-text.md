## Binary-to-text Encoding

Binary-to-text encodings are designed to turn bits into human-printable ouput.

## Base64

Base64 encoding allows us to convert bytes containing binary or text data into ASCII characters i.e. encoding a byte sequence to a string. This is useful when dealing with files or images.

By encoding our data, we improve the chances of it being processed correctly by various systems. Each Base64 character represents 6 bits of information. **As this is not an encryption algorithm, it should not be used for security purposes**.

Base64 is a subset of ASCII, containing 64 of the 128 ASCII characters:

- 26 uppercase letters
- 26 lowercase letters
- 10 numbers
- `-` and `/` for new lines

### Why use Base64 Encoding

All data of different types are transmitted as 1s and 0s; however, some communication channels and applications are not able to understand if the data has to be processed differently i.e. images, emails.

To work around this limitation, you can encode your data to text, improving the chances of it being transmitted and processed correctly as ASCII characters are widely understood by the majority of networks and applications.

```html
<!--images converted to base64 in emails and decoded in applications-->
<img src="data:image/png;base64,aVRBOw0AKg1mL9..." />
```

### Encoding String to Base64

1. Take the ASCII value of each character in the string
2. Calculate the 8-bit binary equivalent of the ASCII values
3. Convert the 8-bit chunks of 6 bits by re-grouping the digits
4. Convert the 6-bit groups to their respective decimal values
5. Using a Base64 encoding table, assign the respective Base64 character for each decimal value

```
string = 'python'

15 50 45 33 40 39

01010000 01111001 01110100 01101000 01101111 01101110

010100 000111 100101 110100 011010 000110 111101 101110

20 7 37 52 26 6 61 46

UHl0aG9u
```

## Example

### Encoding

```py
import base64

message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)
```

### Decoding

```py
import base64

base64_message = 'UHl0aG9uIGlzIGZ1bg=='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)
```
