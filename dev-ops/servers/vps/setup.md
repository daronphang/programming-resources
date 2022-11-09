## Cloud Vendors

AWS, GCP, Linode.

## Setup

Configure SSH, Nginx, Supervisor, Gunicorn, Hostname, Firewall. To always apt update and upgrade before performing any configurations.

https://www.linode.com/docs/guides/set-up-and-secure/

## Timezone

```console
$ timedatectl set-timezone 'Asia/Singapore'
$ echo date
```

## SSH

1. Add user to sudo group and disable root login.
2. Disable password login and enable public key authentication. Generate keys on your local system before enabling this feature.

```console
$ vi /etc/ssh/sshd_config
```

## Firewall

Good security practice to setup firewall for inbound/outbound connections. Blocking inbound help sin protecting your network from getting compromised or leaking information. Blocking outbound is more of a preventive measure in case your network gets compromised and will help protect others.

https://www.linode.com/docs/products/networking/cloud-firewall/get-started/

### Outbound

- Machine is in a corporate environment where outbound web traffic via proxy is permitted.
- Migitation against code flaws in executable code or compromised by malware (DDOS).
- Preventing unwanted behavior.

### Ports

```
# Inbound
SSH     TCP     22
HTTPS   TCP     443
HTTP    TCP     80
MYSQL   TCP     3306

# Outbound
SSH     TCP     22
HTTPS   TCP     443
HTTP    TCP     80
DNS     TCP     53
```
