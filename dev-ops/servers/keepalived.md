## Keepalived

Keepalived is a routing software written in C. The main goal is provide simple and robust facilities for **load balancing (active/active)** and **high-availability (active/passive)** to Linux system and Linux based infrastructures.

Load balancing framework relies on LVS module providing Layer 4 load balancing (TCP/UDP). Keepalived implements a set of checks to dynamically and adaptively maintain and manage load-balanced server pool according to their health. Keepalived provides a strong and robust health checking for LVS clusters.

Keepalived also provides high availability that is achieved using VRRP protocol. It implements a set of hooks to the VRRP finite state machine providing low-level and high-speed protocol interactions. In order to offer faster network failure detection, Keepalived implements **BFD protocol**.

Accessing the virtual IP from the load balancers or one of the real servers is not supported. Likewise, configuring a load balancer on the same machines as a real server is not supported.

## LVS (Linux Virtual Server)

LVS is a patched Linux kernel that adds a load balancing facility. LVS acts as a network bridge (using NAT) to load balance TCP/UDP stream.

### Algorithms

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/load_balancer_administration/ch-initial-setup-vsa

### Components

#### VIP (Virtual IP)

the VIP is the IP address that will be accessed by all clients.

#### Real server

A real server hosting the application accessed by client requests.

#### Server pool

A farm of real servers.

#### Virtual server

The access point to a Server pool.

#### Virtual service

A TCP/UDP service associated with the VIP.

## VRRP (Virtual Router Redundancy Protocol)

VRRP is the protocol implemented for the director's failover/virtualization. VRRP is a fundamental brick for router failover.

### Components

#### Sync group

Defines the VRRP group that stays together through any state changes i.e. failover.

#### Instance

The VRRP instance details the virtual interface configuration for the VRRP service daemon, which creates virtual IP instances.

#### Priority

The priority specifies the order in which the assigned interface takes over in a failover. Higher number has higher priority.

#### MASTER state

VRRP instance state when it is assuming the responsibility of forwarding packets sent to the IP addresses associated with the VRRP instance. All requests are served only by the active server.

#### BACKUP state

VRRP instance state when it is capable of forwarding packets in the event that the current VRRP instance MASTER fails.

#### Real load balancer

An LVS director running one or many VRRP instances.

#### Virtual load balancer

A set of real load balancers.

## Configuration

Keepalived is configured by means of the keepalived.conf file in each system configured as a load balancer.

Example configuration:

- 2 load balancers
- 4 web servers running httpd
- Real IP addresses numbered 192.168.1.20 to 192.168.1.24
- Virtual IP of 10.0.0.1
- Load balancer has two interfaces: eth0 and eth1
- eth0 for handling external internet traffic
- eth1 for routing requests to real servers

```sh
vi /etc/keepalived/keepalived.conf
```

```conf
global_defs {

   notification_email {
       admin@example.com
   }
   notification_email_from noreply@example.com
   smtp_server 127.0.0.1
   smtp_connect_timeout 60
}
```

```conf
// LB1 (active)
vrrp_sync_group VG1 {
   group {
      RH_EXT // external
      RH_INT // internal
   }
}

vrrp_instance RH_EXT {
    state MASTER
    interface eth0
    virtual_router_id 50
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass passw123
    }
    virtual_ipaddress {
    10.0.0.1
    }
}

vrrp_instance RH_INT {
   state MASTER
   interface eth1
   virtual_router_id 2
   priority 100
   advert_int 1
   authentication {
       auth_type PASS
       auth_pass passw123
   }
   virtual_ipaddress {
       192.168.1.1
   }
}

// LB2 (passive)
vrrp_sync_group VG1 {
   group {
      RH_EXT
      RH_INT
   }
}

vrrp_instance RH_EXT {
    state BACKUP
    interface eth0
    virtual_router_id 50
    priority 99
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass passw123
    }
    virtual_ipaddress {
    10.0.0.1
    }
}

vrrp_instance RH_INT {
   state BACKUP
   interface eth1
   virtual_router_id 2
   priority 99
   advert_int 1
   authentication {
       auth_type PASS
       auth_pass passw123
   }
   virtual_ipaddress {
       192.168.1.1
   }
}
```

```conf
virtual_server 10.0.0.1 80 {
    delay_loop 6 // time in seconds between health checks
    lb_algo rr  // round-robin
    lb_kind NAT
    protocol TCP

    real_server 192.168.1.20 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
    real_server 192.168.1.21 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
    real_server 192.168.1.22 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
    real_server 192.168.1.23 80 {
        TCP_CHECK {
                connect_timeout 10
        }
    }
}
```
