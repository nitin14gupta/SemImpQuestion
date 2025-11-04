
# Let me analyze all the question papers and extract all questions with their frequency

# Paper 1: Dec 2022
paper_2022_dec = {
    "Q1a": "Compare and contrast Circuit switched network and Packet switched network",
    "Q1b": "Describe the different guided transmission medias used in the network",
    "Q1c": "What is Channel Allocation problem? explain in short pure and slotted ALOHA",
    "Q1d": "Obtain the 4-bit CRC code for the data bit sequence 10011011100 using the polynomial x4 +x2+1",
    "Q2a": "Describe in detail OSI reference model with a neat diagram",
    "Q2b": "What is Channel allocation problem? Explain CSMA/CD protocol. A network with CSMA/CD has 10 Mbps bandwidth and 25.6ms maximum propagation delay. What is the minimum frame size?",
    "Q3a": "Compare and contrast between (i) IPv4 vs IPv6 (ii) Connection oriented protocol vs Connectionless protocol",
    "Q3b": "Explain in brief Cisco PPDIOO Network design Methodology",
    "Q4a": "What is SDN? Explain SDN architecture along with Operations of control and data planes",
    "Q4b": "What is Routing? What are desirable characteristics of routing algorithms? Explain distance vector routing with suitable example",
    "Q5a": "Elaborate the architectures of NOX and POX controllers of SDN with their comparison",
    "Q5b": "Elaborate Cisco SONA Architecture in detail",
    "Q6a": "Sliding Window Protocol",
    "Q6b": "OpenFlow messages",
    "Q6c": "NAT",
    "Q6d": "DHCP"
}

# Paper 2: May 2023
paper_2023_may = {
    "Q1a": "List and describe the different network connection topologies",
    "Q1b": "Describe the different guided transmission medias used in the network",
    "Q1c": "What is subnetting? What are the default subnet mask?",
    "Q1d": "Explain Three Way Handshaking for connection establishment in TCP",
    "Q2a": "Describe in detail OSI reference model with a neat diagram",
    "Q2b": "A bit stream 10011101 is transmitted using standard CRC method. The generator polynomial is X3 +1",
    "Q3a": "Compare and contrast between (i) IPv4 vs IPv6 (ii) Connection oriented protocol vs Connectionless protocol",
    "Q3b": "Explain in brief Cisco PPDIOO Network design Methodology",
    "Q4a": "Write notes on DNS and Explain components on DNS",
    "Q4b": "What is Routing? What are desirable characteristics of routing algorithms? Explain distance vector routing with suitable example",
    "Q5a": "What is SDN? Explain the concept of control plane and data plane with respect to SDN",
    "Q5b": "Elaborate Cisco SONA Architecture in detail",
    "Q6a": "Sliding Window Protocol",
    "Q6b": "OpenFlow messages",
    "Q6c": "NAT",
    "Q6d": "DHCP"
}

# Paper 3: Dec 2023
paper_2023_dec = {
    "Q1a": "Describe the different guided transmission medias used in the network",
    "Q1b": "Explain Repeater, Hub, Bridge, Switch & Routers",
    "Q1c": "Enumerate the main responsibilities of the DLL",
    "Q1d": "Differentiate between TCP and UDP",
    "Q2a": "Explain TCP/IP reference model & compare it with OSI reference model",
    "Q2b": "With the help of suitable example explain sliding window protocol using Go-Back-N technique",
    "Q3a": "Consider an error detecting CRC With the generator10101. (i) Compute the transmitted bit sequence for the data bit sequence 110010101. (ii) The string of bits 110011001100 is received. Check whether there are errors in the received code word",
    "Q3b": "What is routing? what are desirable characteristics of routing algorithm? Explain Dijkstra's algorithm as shortest path routing with suitable example",
    "Q4a": "What is subnetting? Given the class C network 192.168.10.0 use the subnet mask 255.255.255.192 to create subnets",
    "Q4b": "Explain in brief classic three-layer Hierarchical model for network design by Cisco",
    "Q5a": "Explain with the help of suitable diagram TCP connection management and release",
    "Q5b": "Elaborate the architecture of Nox and Pox controller of SDN with their comparison",
    "Q6a": "DNS",
    "Q6b": "SDN",
    "Q6c": "PPDIOO Network design Methodology",
    "Q6d": "NAT"
}

# Paper 4: May 2024
paper_2024_may = {
    "Q1a": "Explain different network topologies",
    "Q1b": "Differentiate between TCP and UDP",
    "Q1c": "4-bit data bits with binary value 1010 is to be encoded using even parity Hamming code. What is the binary value after encoding?",
    "Q1d": "Explain IPv4 classful addressing and state its disadvantages",
    "Q1e": "Enlist and explain in brief different design issues in data link layer",
    "Q2a": "Explain OSI reference model and compare it with TCP/IP reference model",
    "Q2b": "Explain in brief Cisco PPDIOO network design methodology",
    "Q3a": "What is Channel Allocation problem? Explain CSMA/CD protocol in detail",
    "Q3b": "Explain IPv4 header format with a neat diagram",
    "Q4a": "A bit stream 10011101 is transmitted using the standard CRC method. The generator polynomial is 1001",
    "Q4b": "Elaborate the architecture of NoX and PoX controller of SDN with their comparison",
    "Q5a": "Explain Distance Vector Routing algorithm with an example",
    "Q5b": "Explain three way handshaking technique in TCP",
    "Q6a": "DNS",
    "Q6b": "Sliding window protocols"
}

# Paper 5: Dec 2024
paper_2024_dec = {
    "Q1a": "Explain LAN, MAN and WAN",
    "Q1b": "4-bit data bits with binary value 1010 is to be encoded using even parity Hamming code what is the binary value after encoding?",
    "Q1c": "Find the error, if any, in the following IPV4 address",
    "Q1d": "Explain Simple Mail Transfer Protocol (SMTP)",
    "Q2a": "Explain OSI/ISO reference model & compare it with TCP/IP reference model",
    "Q2b": "Define guided transmission media? Illustrate with diagram the details for Co-axial cable? State any 5 comparative characteristics of co-axial cable with fiber optics and twisted pair cables",
    "Q3a": "Explain sliding window protocol using GO Back-N technique",
    "Q3b": "Explain Classful and Classless IPV4 addressing",
    "Q4a": "Explain how collision handled in CSMA/CD? A 2km long broadcast LAN uses CSMA has 107 bps bandwidth and uses CSMA/CD. The signal travels along the wire at 2 x 108m/s what is the minimum packet size that can be used on this network?",
    "Q4b": "Explain in Brief: (i) Telnet (ii) TCP Timers",
    "Q5a": "Explain Link State Routing with suitable example",
    "Q5b": "Explain in brief classic three-layer Hierarchical model for network design by Cisco",
    "Q6a": "FTP",
    "Q6b": "Cisco SONA Architecture",
    "Q6c": "Open Flow Controllers of SDN",
    "Q6d": "Architecture of NoX with its functionality"
}

# Paper 6: CN 2025 QP (seems to be a practice paper)
paper_2025_cn = {
    "Q1a": "Explain why there is need for layered designing for networking and communication",
    "Q1b": "Explain the functionality of Sliding window protocol",
    "Q1c": "Explain the different classes of IPV4 addressing technique",
    "Q1d": "Write Short note on Parity check",
    "Q2a": "Compare between layers of OSI model and TCP/IP model with a neat diagram",
    "Q2b": "What are the different DLL design issues? Describe them in brief",
    "Q3a": "What is Channel allocation problem? Explain CSMA/CD protocol. A network with CSMA/CD has 100 Mbps bandwidth and 25.60 micro second maximum propagation delay. What is the minimum frame size?",
    "Q3b": "Explain Cisco Service Oriented Network Architecture in detail",
    "Q4a": "What is ALOHA? Explain Pure ALOHA and Slotted ALOHA in detail",
    "Q4b": "Differentiate between Routed and Routing protocols and also depict the classification of routing algorithms",
    "Q5a": "What is SDN? Explain SDN Building Blocks with different Open flow messages",
    "Q5b": "Elaborate TCP flow control mechanism with example",
    "Q6a": "TCP Timers",
    "Q6b": "DNS",
    "Q6c": "Static routing and Dynamic routing",
    "Q6d": "Packet Switched vs Circuit Switched Network"
}

print("Question papers analyzed successfully!")
print(f"Total papers: 6")
