## MTU (Maximum Transmission Unit)

Docker has a known issue where it seems to ignore the network's maximum packet size (MTU) and sets a default of 1500. This results in situations where the docker container is expecting to be able to send larger packets than the underlying network, but parts of the packet will get trimmed resulting in packet loss or no response from the server.

```yaml
networks:
  backend:
    driver: bridge
    driver_opts:
      com.docker.network.driver.mtu: 1400
```
