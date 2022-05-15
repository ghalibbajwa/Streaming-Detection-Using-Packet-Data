
from scapy.all import *
from threading import Thread
from time import sleep

count = 0

class Sniffer(Thread):
    def  __init__(self, interface="Wi-Fi"):
        super().__init__()

        self.interface = interface

    def run(self):
        sniff(iface=self.interface, prn=self.print_packet)

    def print_packet(self, packet):
        
        # if packet.sport != 443:
        #     packet['IP'].dst='1.1.1.1'
            sendp(packet, iface='Wi-Fi')
        
        #ip_layer = packet.getlayer(IP)
        #print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

sniffer = Sniffer()


sniffer.start()

try:
    while True:
        sleep(100)
except KeyboardInterrupt:
    print("[*] Stop sniffing")
    sniffer.join()


# t= Thread(target=sniff(iface='Wi-Fi'))
# t.start()

# def filter_packets():

#     for pkt in sniff:
#     # if IP in pkt and pkt[IP].src.endswith('5'):
#     #     pkt[IP].dst = '1.1.1.1'
#     #     sendp(pkt, iface='eth2')
#         #if pkt.sport != 443:
#             print(pkt.sport)
#             pkt[IP].dst = '1.1.1.1'
#             sendp(pkt, iface='Local Area Connection* 10')

# # t=Thread(target=filter_packets)
# # t.start()
# filter_packets()