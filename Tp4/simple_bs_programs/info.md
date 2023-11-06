```
[logards@server]$ sudo firewall-cmd --add-port=13337/tcp --permanent
[sudo] password for logards: 
success
[logards@server]$ sudo firewall-cmd --reload
success
[logards@server]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources: 
  services: cockpit dhcpv6-client ssh
  ports: 13337/tcp
  protocols: 
  forward: yes
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
[logards@server Tp4]$ python bs_server_I1.py 
Connected by ('10.1.1.12', 53576)
Données reçues du client : b'MEOOOOOOOOO'
[logards@server ~]$ sudo ss -alutnp | grep python
tcp   LISTEN 0      1            0.0.0.0:13337      0.0.0.0:*    users:(("python",pid=6609,fd=3))
```

```
[logards@client Tp4]$ python bs_client_I1.py 
Le serveur a répondu b'Hi Mate !'
```

