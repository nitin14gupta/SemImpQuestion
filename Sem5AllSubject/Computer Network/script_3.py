
import csv

# Create a comprehensive analysis CSV
analysis_data = [
    ["COMPUTER NETWORK - QUESTION PAPER ANALYSIS", "", "", ""],
    ["Mumbai University | Subject Code: 48891 | Semester V", "", "", ""],
    ["", "", "", ""],
    ["TOPIC FREQUENCY ANALYSIS", "", "", ""],
    ["Rank", "Topic", "Frequency", "Marks Type"],
    ["1", "SDN (Software Defined Networking)", "8", "10 marks"],
    ["2", "IP Addressing (IPv4/IPv6)", "7", "10 marks"],
    ["3", "OSI & TCP/IP Reference Models", "6", "10 marks"],
    ["4", "Sliding Window Protocol", "6", "10 marks"],
    ["5", "TCP vs UDP", "6", "5 marks"],
    ["6", "LAN, MAN, WAN", "5", "5 marks"],
    ["7", "Transmission Media", "4", "10 marks"],
    ["8", "Channel Allocation Problem", "4", "10 marks"],
    ["9", "CRC (Error Detection)", "4", "10 marks"],
    ["10", "CSMA/CD Protocol", "4", "10 marks"],
    ["11", "NOX and POX Controllers", "4", "10 marks"],
    ["12", "Cisco SONA Architecture", "4", "5-10 marks"],
    ["13", "DNS", "4", "5 marks"],
    ["14", "Network Devices", "3", "5 marks"],
    ["15", "Cisco PPDIOO Methodology", "3", "10 marks"],
    ["16", "Distance Vector Routing", "3", "10 marks"],
    ["17", "NAT", "3", "5 marks"],
    ["18", "Data Link Layer (DLL)", "3", "10 marks"],
    ["19", "Error Detection (Hamming/Parity)", "3", "5 marks"],
    ["20", "Circuit vs Packet Switching", "2", "5 marks"],
    ["21", "ALOHA Protocol", "2", "10 marks"],
    ["22", "Connection Oriented vs Connectionless", "2", "5 marks"],
    ["23", "Control and Data Planes", "2", "10 marks"],
    ["24", "OpenFlow", "2", "5 marks"],
    ["25", "DHCP", "2", "5 marks"],
    ["26", "Network Topologies", "2", "5 marks"],
    ["27", "Subnetting", "2", "10 marks"],
    ["28", "TCP Three-Way Handshake", "2", "10 marks"],
    ["29", "TCP Connection Management", "2", "10 marks"],
    ["30", "Link State Routing (Dijkstra)", "2", "10 marks"],
    ["", "", "", ""],
    ["", "", "", ""],
    ["PAPERS ANALYZED", "", "", ""],
    ["Sr. No.", "Paper Name", "Date", "QP Code"],
    ["1", "December 2022", "22/11/2022", "10014058"],
    ["2", "May 2023", "May 2023", "10026348"],
    ["3", "December 2023", "22/11/2023", "10038971"],
    ["4", "May 2024", "03/06/2024", "10056909"],
    ["5", "December 2024", "11/11/2024", "10065193"],
    ["6", "CN 2025 Practice", "Practice Paper", "N/A"],
    ["", "", "", ""],
    ["Total Papers Analyzed: 6", "", "", ""],
    ["Total Questions Analyzed: 95", "", "", ""],
    ["Total Unique Topics: 42", "", "", ""],
]

with open('question_paper_analysis.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(analysis_data)

print("Analysis CSV created successfully!")

# Create formulas quick reference
formulas_data = [
    ["COMPUTER NETWORK - IMPORTANT FORMULAS", ""],
    ["", ""],
    ["Topic", "Formula"],
    ["CSMA/CD Minimum Frame Size", "Minimum Frame Size (bits) = 2 × Propagation Time × Bandwidth"],
    ["", "Propagation Time = Distance / Propagation Speed"],
    ["Pure ALOHA Throughput", "S = G × e^(-2G), Maximum at G=0.5, Smax = 0.184 (18.4%)"],
    ["Slotted ALOHA Throughput", "S = G × e^(-G), Maximum at G=1, Smax = 0.368 (36.8%)"],
    ["Hamming Code Parity Bits", "2^r ≥ m + r + 1, where m=data bits, r=parity bits"],
    ["Subnetting - Number of Subnets", "Number of subnets = 2^n, where n = borrowed bits"],
    ["Subnetting - Hosts per Subnet", "Hosts per subnet = 2^h - 2, where h = host bits"],
    ["Efficiency of Stop-and-Wait", "Efficiency = 1 / (1 + 2a), where a = Tp/Tt"],
    ["Propagation Time", "Tp = Distance / Propagation Speed"],
    ["Transmission Time", "Tt = Frame Size / Bandwidth"],
    ["Bandwidth-Delay Product", "BDP = Bandwidth × Round Trip Time"],
    ["TCP Window Size", "Window Size ≥ Bandwidth × RTT"],
    ["", ""],
    ["CONVERSIONS", ""],
    ["1 Byte", "8 bits"],
    ["1 KB", "1024 bytes"],
    ["1 MB", "1024 KB"],
    ["1 Gbps", "10^9 bps"],
    ["1 Mbps", "10^6 bps"],
    ["1 Kbps", "10^3 bps"],
]

with open('important_formulas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(formulas_data)

print("Formulas CSV created successfully!")
print("\n✓ All files created successfully!")
print("\nGenerated Files:")
print("1. question_paper_analysis.csv - Topic frequency analysis")
print("2. important_formulas.csv - Quick formula reference")
print("3. top_30_important_questions.csv - List of important questions")
