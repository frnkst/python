from scapy.all import *
import pandas
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', required=True, help="the interface to sniff on")
parser.add_argument('-s', '--seconds', required=True, type=int, help="the number of seconds you want to sniff")
args = parser.parse_args()

total_packets = {}


def count_packets(pkt):
    if 'IP' and 'TCP' in pkt:
        ip_dst = str(pkt['IP'].dst)

        if ip_dst in total_packets:
            total_packets[ip_dst] = total_packets[ip_dst] + 1
        else:
            total_packets[ip_dst] = 1


sniff(iface=args.interface, prn=count_packets, filter="ip", store=0, timeout=args.seconds)
sorted_packets = [(k, total_packets[k]) for k in sorted(total_packets, key=total_packets.get, reverse=True)]
print(pandas.DataFrame(sorted_packets, columns=["IP Address", "Number of packets"]).to_string(index=False))
