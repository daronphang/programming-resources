## Ubuntu Installation

- Install Third-party apps for broadcom driver
- Partition disk with EFI and mount at /

## Drivers

```bash
$ sudo ubuntu-drivers list
$ sudo ubuntu-drivers devices
$ sudo ubuntu-drivers autoinstall
$ dkms status
```

### Graphics card

```bash
$ sudo apt install hwinfo
$ hwinfo --gfxcard --short # sudo lshw -c display
```

If display is UNCLAIMED, it means there was no driver loaded for the graphics card.

```bash
$ sudo apt remove --purge nvidia*
$ sudo ubuntu-drivers autoinstall
$ reboot
```

### Network

Install BCM4352 802.11ac Wireless Network Adapter and bcmwl-kernel-source driver.
