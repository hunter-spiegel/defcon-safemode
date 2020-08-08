from ipaddress import IPv4Address, IPv4Network

valid_ips = 0
filename = "ips.txt"

with open(filename) as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]  #remove whitespaces

for line in lines:
    pair = line.split(',')
    ip = IPv4Address(pair[0])
    subnet = IPv4Network(pair[1])

    if ip in subnet:
        valid_ips += 1

print("Valid IPs: {}".format(valid_ips))
