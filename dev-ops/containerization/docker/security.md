## Docker Security

Each container spawned by Docker will run as the root user by default. However, Docker starts the containers with a **restricted set of capabilities**.

Typical servers run several processes as root i.e. SSH daemon, CRON daemon, logging daemons, kernel modules, network configuration tools, etc. However, a container is different as almost all of those tasks are handled by the infrastructure around the container. Hence, containers do not need 'real' root privileges, and can run with a reduced capability set.

One primary risk with running Docker containers is that the default set of capabilities and mounts given may provide incomplete isolation.

Docker supports the addition and removal of capabilities, allowing the use of a non-default profile.
