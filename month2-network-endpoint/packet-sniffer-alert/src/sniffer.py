from scapy.all import sniff, TCP, IP
import re
SUSPICIOUS_FLAGS = {'F':'FIN', 'S':'SYN', 'R':'RST', 'P':'PSH', 'A':'ACK', 'U':'URG', 'E':'ECE', 'C':'CWR'}
def handle(pkt):
    if IP in pkt and TCP in pkt:
        flags = pkt[TCP].flags
        # Simple rule: excessive SYNs without ACK -> potential scan
        if flags == 0x02:  # SYN
            print(f"[ALERT] SYN from {pkt[IP].src} to {pkt[IP].dst}:{pkt[TCP].dport}")
if __name__ == "__main__":
    print("Sniffing... (requires root/admin)")
    sniff(prn=handle, store=False)
