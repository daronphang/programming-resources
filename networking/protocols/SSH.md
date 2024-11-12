## SSH (Secure Socket Shell)

Network protocol that gives users a secure way to access a computer over an unsecured network. Provides strong password authentication and public key authentication, including encrypted data communications between computers connecting over an open network. Standard for strong authentication.

Protocol which allows you to connect securely to a remote Linux computer or server by using a text-based interface. When a secure SSH connection is established, a shell session will be started, and you will be able to manipulate the server by typing commands within the client on your local computer.

Two most commonly used protocols for accessing remote machines are:

- SSH for linux-based
- Remote Desktop Protocol (RDP) for Windows

### How SSH works

Establishing an SSH connection requires two components:

- Client: An application you install on the computer which you will use to connect to another server
- Server: SSH daemon that is constantly listening to a specific TCP/IP port for possible client connection requests

Need to ensure both client and server components are installed on local and remote machine. OpenSSH is a widely-used open-source SSH tool for Linux distro. For Windows, can install PuTTY. Most linux distro already have SSH client installed (except for Ubuntu).

## Installation

### Installing OpenSSH client

For Windows, need to install a version of OpenSSH such as MobaXTerm. To have a full Linux environment available, can setup WSL which has SSH by default.

```sh
$ ssh   # check for ssh client
$ sudo apt-get install openssh-client
```

### Installing OpenSSH server

On most Linux environments, the ssh server 'sshd' should start automatically.

```sh
$ sudo systemctl start ssh      # for ubuntu distro, to manually start ssh

$ ssh localhost
$ sudo apt-get install openssh-server ii.
$ sudo service ssh status       # check if SSH server is running
```

## Configuration

### Configuring SSH on server

Config file is located at `/etc/ssh/sshd_config` whereby you can change the settings.

```conf
Port 22

HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_dsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key

SyslogFacility AUTH
LogLevel INFO

LoginGraceTime 120          # keep connection alive without successfully logging in
PermitRootLogin yes         # tells whether root user is allowed to login
StrictModes yes             # disable login attempt if auth files are readable by everyone

X11Forwarding yes           # allows you to view a remote system's GUI on the local system
X11DisplayOffset 10

PasswordAuthentication no
PubkeyAuthentication yes
ChallengeResponseAuthentication no
```

```sh
$ sudo service ssh restart         # need to restart everytime a change is made
$ sudo systemctl reload ssh        # alternative for restart
```

### Connecting via SSH

```sh
$ ssh your_username@host_ip_address
$ ssh your_username@host_ip_address -p 8080
$ ssh our_username@host_ip_address command_to_run
$ ssh -X remote_host        # X11 forwarding
$ exit
```

### User configuration for client

Location of file is at `~/.ssh/config`. For multiple matches, it will merge the options.

```
Host hostname1
    SSH_OPTION value
    SSH_OPTION value

Host targaryen
    HostName 192.168.1.10
    User daenerys
    Port 7654
    IdentityFile ~/.ssh/targaryen.key

Host tyrell
    HostName 192.168.10.20

Host martell
    HostName 192.168.10.50

Host *ell
    user oberyn

Host * !martell
    LogLevel INFO

Host *
    User root
    Compression yes
```

Running `ssh tyrell` will use the following options:

```
HostName 192.168.10.20
User oberyn
LogLevel INFO
Compression yes
```

```
Host *
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no
Host 10.*
    StrictHostKeyChecking no
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

# same as ssh daron.phang@git.byted.org -p 29418
Host git.byted.org
    Hostname git.byted.org
    Port 29418
    User daron.phang
Host review.byted.org
    Hostname git.byted.org
    Port 29418
    User daron.phang
Host *.byted.org
    GSSAPIAuthentication yes
    User daron.phang
```

## Security hardening

- Change default TCP port from 22 to higher i.e. 24596
- Use SSH key pairs for authentication for password-less SSH login
- Disable password-based logins on your server (need ensure key pair is working properly)
- Disable root access to your server
- Use TCP wrappers to restrict access to certain IP addresses by editing '/etc/hosts.allow' and '/etc/hosts.deny' files

For TCP wrappers, allowed hosts supersede denied hosts.

```
# etc/hosts.deny
sshd: ALL
ALL: ALL

# etc/hosts.allow
sshd: 10.10.0.5, LOCAL
```

## SSH keys

SSH key authentication is a more robust and secure alternative to logging in with password. Relies on asymmetric cryptographic algorithms than generate a pair of separate keys that **is generated on the client/local computer**. Private key is kept as a secret on client's machine and stored on the computer you use to connect to the remote system. Public key can be shared with anyone and stored on the remote system in .ssh/authorized_keys directory.

Server will use public key to create a message for the client computer that can only be read with the private key. Client sends the appropriate response back to the server and the server will know the client is legitimate. Remote system must have a version of SSH installed.

Though you may be prompted to set a password on the key files themselves, it is an uncommon practice i.e. accepting defaults is sufficient.

### How to generate

- Two keys are generated: public (`~/.ssh/id_rsa.pub`) and private (`~/.ssh/id_rsa`)
- Existing private keys are located at `~/.ssh/`
- Public keys are stored in server at `~/.ssh/authorized_keys`

```sh
$ ssh-keygen -t rsa     # -t flag to specify type
$ ssh-keygen -b 4096    # -b flag to specify the length of key

$ ssh-keygen -b 4096 -t rsa             # open SSH private key
$ ssh-keygen -b 4096 -t rsa -m PEM      # rsa private key

$ ssh-keygen -p -m PEM -f ~/.ssh/id_rsa     # downgrade from OpenSSH to RSA private key

$ # after generating, prompts to enter location of file and passphrase
$ # press enter to accept default filename and location
$ # default is ~/.ssh/id_rsa

$ cd ~/.ssh
$ ls -l
```

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAA....0g1bMv+p11K8MDH sanjaydev
```

### Transferring public key to server

Uploading public key to compute/server instance. To use public key authentication, the public key must be copied to a server and installed in an authorized_keys file.

```sh
$ # from local Linux
$ ssh-copy-id server_username@192.0.2.1
```

```sh
$ # for windows

$ # on windows local computer
$ scp C:\Users\MyUserName\.ssh/id_rsa.pub example_user@192.0.2.1:~/.ssh/authorized_keys

$ # on linux server
$ mkdir -p ~/.ssh && sudo chmod -R 700 ~/.ssh/
```

```sh
$ # setting permissions for public key directory in server
$ sudo chmod -R 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
```

### Logs

```sh
$ sudo vim /var/log/auth.log
$ sudo journalctl -t sshd
```

### Folder permissions

```
~/.ssh 700
~/.ssh/authorized_keys 600
```
