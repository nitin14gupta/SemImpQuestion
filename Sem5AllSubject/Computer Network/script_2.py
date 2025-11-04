
# Now let's create the top 20-30 most important questions based on frequency and importance
import csv

important_questions = [
    # Based on OSI & TCP/IP (6 times)
    "1. Explain OSI/ISO reference model with a neat diagram and compare it with TCP/IP reference model. (10 marks)",
    
    # Based on SDN (8 times) 
    "2. What is SDN? Explain SDN architecture along with Operations of control and data planes. (10 marks)",
    
    # Based on Sliding Window Protocol (6 times)
    "3. Explain sliding window protocol using GO Back-N technique with suitable example. (10 marks)",
    
    # Based on IP Addressing (7 times)
    "4. Explain IPv4 classful and classless addressing with their differences. State disadvantages of classful addressing. (10 marks)",
    
    # Based on CSMA/CD (4 times) and Channel Allocation (4 times)
    "5. What is Channel Allocation problem? Explain CSMA/CD protocol. A network with CSMA/CD has 100 Mbps bandwidth and 25.60 microsecond maximum propagation delay. What is the minimum frame size? (10 marks)",
    
    # Based on CRC (4 times)
    "6. A bit stream 10011101 is transmitted using the standard CRC method. The generator polynomial is x^4+x^2+1. What is the actual bit transmitted? If the third bit is inverted, how will the receiver detect this error? (10 marks)",
    
    # Based on NOX and POX (4 times)
    "7. Elaborate the architectures of NOX and POX controllers of SDN with their comparison. (10 marks)",
    
    # Based on TCP vs UDP (6 times)
    "8. Differentiate between TCP and UDP protocols with suitable examples. (5 marks)",
    
    # Based on Routing - Distance Vector (3 times)
    "9. What is Routing? What are desirable characteristics of routing algorithms? Explain distance vector routing with suitable example. (10 marks)",
    
    # Based on Routing - Link State (2 times)
    "10. Explain Link State Routing (Dijkstra's algorithm) as shortest path routing with suitable example. (10 marks)",
    
    # Based on Transmission Media (4 times)
    "11. Describe the different guided transmission medias used in the network. Illustrate with diagram the details for Co-axial cable and state comparative characteristics with fiber optics and twisted pair cables. (10 marks)",
    
    # Based on Cisco PPDIOO (3 times)
    "12. Explain in brief Cisco PPDIOO Network design Methodology. (10 marks)",
    
    # Based on Cisco SONA (4 times)
    "13. Elaborate Cisco SONA (Service Oriented Network Architecture) in detail. (10 marks)",
    
    # Based on Cisco Hierarchical Model (2 times)
    "14. Explain in brief classic three-layer Hierarchical model for network design by Cisco. (10 marks)",
    
    # Based on Subnetting (2 times)
    "15. What is subnetting? Given the class C network 192.168.10.0, use the subnet mask 255.255.255.192 to create subnets and calculate: (i) Number of subnets (ii) Hosts per subnet (iii) IP address of first host, last host and broadcast address. (10 marks)",
    
    # Based on TCP Three-Way Handshake (2 times)
    "16. Explain Three Way Handshaking for connection establishment and TCP connection management with suitable diagrams. (10 marks)",
    
    # Based on ALOHA (2 times)
    "17. What is ALOHA? Explain Pure ALOHA and Slotted ALOHA in detail with throughput analysis. (10 marks)",
    
    # Based on DNS (4 times)
    "18. Write notes on DNS and explain components of DNS in detail. (5 marks)",
    
    # Based on Error Detection - Hamming/Parity (3 times)
    "19. A 4-bit data bits with binary value 1010 is to be encoded using even parity Hamming code. What is the binary value after encoding? Explain the error detection mechanism. (5 marks)",
    
    # Based on Data Link Layer (3 times)
    "20. What are the different DLL (Data Link Layer) design issues? Describe them in brief. Enumerate the main responsibilities of the DLL. (10 marks)",
    
    # Based on Network Devices (3 times)
    "21. Explain Repeater, Hub, Bridge, Switch & Routers with their functionalities and differences. (5 marks)",
    
    # Based on NAT (3 times)
    "22. Write a short note on NAT (Network Address Translation) with its working principle. (5 marks)",
    
    # Based on Circuit vs Packet Switching (2 times)
    "23. Compare and contrast Circuit switched network and Packet switched network. (5 marks)",
    
    # Based on Connection Oriented vs Connectionless (2 times)
    "24. Compare and contrast between Connection oriented protocol vs Connectionless protocol. (5 marks)",
    
    # Based on IPv6 (included in IP addressing questions)
    "25. Compare and contrast between IPv4 vs IPv6 addressing schemes. (5 marks)",
    
    # Based on Network Topologies (2 times)
    "26. List and describe the different network connection topologies with diagrams. (5 marks)",
    
    # Based on LAN, MAN, WAN (5 times)
    "27. Explain LAN, MAN and WAN with their characteristics and differences. (5 marks)",
    
    # Based on OpenFlow (2 times)
    "28. Write a short note on OpenFlow messages and OpenFlow Controllers of SDN. (5 marks)",
    
    # Based on DHCP (2 times)
    "29. Write a short note on DHCP (Dynamic Host Configuration Protocol). (5 marks)",
    
    # Based on TCP Timers, TCP Flow Control
    "30. Explain in brief: (i) TCP Timers (ii) TCP flow control mechanism with example. (10 marks)"
]

# Additional important questions
additional_questions = [
    "31. Explain IPv4 header format with a neat diagram. (10 marks)",
    "32. Differentiate between Routed and Routing protocols and depict the classification of routing algorithms. (10 marks)",
    "33. Write short notes on: (i) FTP (ii) SMTP (iii) Telnet. (5 marks each)",
    "34. Explain why there is need for layered designing for networking and communication. (5 marks)",
    "35. Write short notes on: (i) Static routing vs Dynamic routing (ii) Control and Data planes in SDN. (5 marks each)"
]

# Combine all important questions
all_important_questions = important_questions + additional_questions[:5]

print("=" * 80)
print("TOP 30 MOST IMPORTANT QUESTIONS FOR COMPUTER NETWORK EXAM")
print("=" * 80)
for q in all_important_questions[:30]:
    print(q)
    print()

# Save to CSV for reference
csv_data = []
for i, q in enumerate(all_important_questions[:30], 1):
    csv_data.append([i, q])

with open('top_30_important_questions.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Sr. No.', 'Question'])
    writer.writerows(csv_data)

print("\n" + "=" * 80)
print("File saved: top_30_important_questions.csv")
