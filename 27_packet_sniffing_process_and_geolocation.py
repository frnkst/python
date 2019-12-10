# Usage: python3 26_packet_sniffing_with_process.py -i en0 -s 30

from scapy.all import *
import argparse
import os
from prettytable import PrettyTable
import requests
import json


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', required=True, help="the interface to sniff on")
parser.add_argument('-s', '--seconds', required=True, type=int, help="the number of seconds you want to sniff")
args = parser.parse_args()

all_packets = {}


class Packet:
    def __init__(self, pid, process, source_port, ip, country, city, destination_port, count):
        self.pid = pid
        self.process = process
        self.source_port = source_port
        self.ip = ip
        self.country = country
        self.city = city
        self.destination_port = destination_port
        self.count = count


def find_pid_using_port(port):
    fp = os.popen("lsof -i :%s" % port)
    lines = fp.readlines()
    fp.close()
    pid = None
    if len(lines) >= 2:
        pid = int(lines[1].split()[1])
    return pid


def find_process_using_pid(pid):
    if pid is None:
        return

    fp = os.popen("ps -p %s" % pid)
    lines = fp.readlines()
    fp.close()
    process_name = 'No process found for pid ' + str(pid)
    if len(lines) >= 2:
        process_name = lines[1].split()[3]
    return process_name


def get_process_information(port):
    pid = find_pid_using_port(port)
    process_name = find_process_using_pid(pid)
    return pid, process_name


def get_location(ip):
    r = requests.get("http://ip-api.com/json/" + ip)
    json_response = json.loads(r.content)
    if 'country' and 'city' in json_response:
        return json_response['country'], json_response['city']
    else:
        return "None", "None"


def count_packets(pkt):
    if 'IP' and 'TCP' in pkt:
        ip_dst = str(pkt['IP'].dst)

        tcp_source_port = pkt['TCP'].sport
        tcp_destination_port = pkt['TCP'].dport

        if ip_dst in all_packets:
            all_packets[ip_dst].count += 1
        else:
            pid, process_name = get_process_information(tcp_source_port)
            country, city = get_location(ip_dst)
            all_packets[ip_dst] = Packet(
                pid,
                process_name,
                tcp_source_port,
                ip_dst,
                country,
                city,
                tcp_destination_port,
                1
            )


def sort_result(all_packets):
    return [(k, all_packets[k]) for k in sorted(all_packets, key=lambda k: all_packets[k].count, reverse=True)]


def print_results(all_packets):
    table = PrettyTable()
    table.field_names = ["PID", "Process", "Source port", "Destination address", "Location", "Destination port",  "# Packets captured"]

    for item in sort_result(all_packets):
        ip = item[0]
        packet = item[1]
        table.add_row([packet.pid, packet.process, packet.source_port, ip, packet.city + " (" + packet.country + ")", packet.destination_port, packet.count])

    print(table)


sniff(iface=args.interface, prn=count_packets, filter="ip", store=0, timeout=args.seconds)
print_results(all_packets)
