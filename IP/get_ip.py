import psutil

ip_a = psutil.net_if_addrs()
wlo1 = ip_a['wlo1']
address = wlo1[0]
print(address[1])