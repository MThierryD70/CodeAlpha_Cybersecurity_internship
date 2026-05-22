from scapy.all import IP,TCP,UDP, sniff
import logging
import datetime


# ___________  Logger configuration  ______________________________
logging.basicConfig(
    filename="capture.log",
    level = logging.INFO,
    format = "%(asctime)s   |   %(message)s",
    datefmt = "%Y-%m-%d  %H:%M:%S"
)


# ______________ KNOWN PORTS ______________________________________
KNOWN_PORTS = {
    80: "HTTP",
    443: "HTTPS",
    53: "UDP",
    22: "SSH",
    21: "FTP",
    25: "SMTP",
    110: "POP3",
    143: "IMAP",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

#  __________________ Identify service _________________________
def identify_service(port):
    return KNOWN_PORTS.get(port, f"Port - {port}")


#  _______________ Analyse and log packets __________________
def analyse_packet(packet):
    print("\n")

    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        if packet.haslayer(TCP):
            type_proto = "TCP"
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport
            service = identify_service(packet[TCP].dport)
        
        elif packet.haslayer(UDP):
            type_proto = "UDP"
            port_src = packet[UDP].sport
            port_dst = packet[UDP].dport
            service = identify_service(packet[UDP].dport)
        
        else:
            type_proto = "ICMP"
            port_src = "-"
            port_dst = "-"
            service = "PING"
    

        message = f"[{type_proto}]  {ip_src}:{port_src}  --->  {ip_dst}:{port_dst}  [{service}]"
        
        print(message)
        logging.info(message)





#  __________ Launching _______________________________
if __name__ == "__main__":
    
    print("\n\n")

    print("_____________ Network Sniffer - CodeAlpha Internship \n")
    print(f"_____________ Starting ............................ \n")
    print(datetime.datetime.now().strftime('%Y-%m-%d    %H:%M:%S'))

    sniff (count = 25, prn = analyse_packet)

    print("\n\n")

    print("Logs are saved in : capture.log\n")
    print("_____________   Capture finished  _______________")

    print("\n\n")








