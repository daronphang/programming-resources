## SMTP (Simple Mail Transfer Protocol)

The SMTP is an application layer protocol that is used in sending and receiving email over TCP/IP. Sender-SMTP initiates a two-way connection with the receiver-SMTP.

### SMTP Server

An SMTP server is an application that sends, receives and relays email. It receives electronic messages from email clients (Gmail, Yahoo, etc.) and transfers them to other servers. These can be other SMTP servers or an incoming mail server.

SMTP servers are set to an always-on listening mode and as soon as the server detects a TCP connection from a client, the SMTP process initiates a connection to send the email.

Every email message passes through the mail server before reaching its destination. Without them, you would only be able to send emails to people whose addresses matched your domain i.e. gmail to gmail only.

### Procedure

1. Your mail client connects to the SMTP server over TCP/IP using port 25 (by default)
2. Mail client has a conversation with the server and performs verification and authentication corresponding to the active account, and then relaying the message information i.e. sender address, recipient, message, etc.
3. SMTP server takes the message information and repeats the conversation process with the recipient's mail server
4. The recipient's mail server validates the message information and delivers the message to the intended recipient

## MIME (Multipurpose Internet Mail Extensions)

The MIME standard was developed to extend the functionality of SMTP and use character sets other than ASCII. It is used to send attachments, message bodies exceeding the character limits imposed by SMTP, languages, and HTML/CSS formats.

MIME is an extension protocol and does not operate separately.
