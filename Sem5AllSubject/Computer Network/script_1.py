
# Now let's extract topics and their frequency
import pandas as pd
from collections import defaultdict

# Define topic categories and keywords for each question
topics_frequency = defaultdict(int)
question_topics_map = {}

# Function to categorize questions into topics
def categorize_topic(question):
    question_lower = question.lower()
    topics = []
    
    if "osi" in question_lower or "tcp/ip" in question_lower or "reference model" in question_lower:
        topics.append("OSI & TCP/IP Reference Models")
    if "transmission media" in question_lower or "guided" in question_lower or "coaxial" in question_lower or "fiber" in question_lower:
        topics.append("Transmission Media")
    if "sliding window" in question_lower or "go back" in question_lower or "go-back-n" in question_lower:
        topics.append("Sliding Window Protocol")
    if "crc" in question_lower or "cyclic redundancy" in question_lower:
        topics.append("CRC (Error Detection)")
    if "hamming" in question_lower or "parity" in question_lower:
        topics.append("Error Detection (Hamming/Parity)")
    if "ipv4" in question_lower or "ipv6" in question_lower or "ip address" in question_lower or "classful" in question_lower or "classless" in question_lower:
        topics.append("IP Addressing (IPv4/IPv6)")
    if "subnet" in question_lower:
        topics.append("Subnetting")
    if "routing" in question_lower and "distance vector" in question_lower:
        topics.append("Distance Vector Routing")
    if "routing" in question_lower and ("dijkstra" in question_lower or "link state" in question_lower or "shortest path" in question_lower):
        topics.append("Link State Routing (Dijkstra)")
    if "routing" in question_lower and "algorithm" in question_lower and "distance" not in question_lower and "dijkstra" not in question_lower:
        topics.append("Routing Algorithms")
    if "sdn" in question_lower:
        topics.append("SDN (Software Defined Networking)")
    if "nox" in question_lower or "pox" in question_lower:
        topics.append("NOX and POX Controllers")
    if "openflow" in question_lower:
        topics.append("OpenFlow")
    if "cisco" in question_lower and ("ppdioo" in question_lower or "design methodology" in question_lower):
        topics.append("Cisco PPDIOO Methodology")
    if "cisco" in question_lower and ("sona" in question_lower or "service oriented" in question_lower):
        topics.append("Cisco SONA Architecture")
    if "cisco" in question_lower and ("hierarchical" in question_lower or "three-layer" in question_lower):
        topics.append("Cisco Hierarchical Model")
    if "tcp" in question_lower and ("handshake" in question_lower or "handshaking" in question_lower or "three way" in question_lower):
        topics.append("TCP Three-Way Handshake")
    if "tcp" in question_lower and ("connection" in question_lower or "management" in question_lower or "release" in question_lower):
        topics.append("TCP Connection Management")
    if "tcp" in question_lower and ("flow control" in question_lower):
        topics.append("TCP Flow Control")
    if "tcp" in question_lower and ("timer" in question_lower):
        topics.append("TCP Timers")
    if ("tcp" in question_lower or "udp" in question_lower) and ("differentiate" in question_lower or "difference" in question_lower or "compare" in question_lower or "vs" in question_lower):
        topics.append("TCP vs UDP")
    if "dns" in question_lower:
        topics.append("DNS")
    if "dhcp" in question_lower:
        topics.append("DHCP")
    if "nat" in question_lower:
        topics.append("NAT")
    if "ftp" in question_lower:
        topics.append("FTP")
    if "smtp" in question_lower:
        topics.append("SMTP")
    if "telnet" in question_lower:
        topics.append("Telnet")
    if "aloha" in question_lower:
        topics.append("ALOHA Protocol")
    if "csma" in question_lower or "collision" in question_lower:
        topics.append("CSMA/CD Protocol")
    if "channel allocation" in question_lower:
        topics.append("Channel Allocation Problem")
    if "circuit switch" in question_lower or "packet switch" in question_lower:
        topics.append("Circuit vs Packet Switching")
    if "connection oriented" in question_lower or "connectionless" in question_lower:
        topics.append("Connection Oriented vs Connectionless")
    if "topology" in question_lower or "topologies" in question_lower:
        topics.append("Network Topologies")
    if "lan" in question_lower or "man" in question_lower or "wan" in question_lower:
        topics.append("LAN, MAN, WAN")
    if "dll" in question_lower or "data link layer" in question_lower:
        topics.append("Data Link Layer (DLL)")
    if "repeater" in question_lower or "hub" in question_lower or "bridge" in question_lower or "switch" in question_lower or "router" in question_lower:
        topics.append("Network Devices")
    if "layered" in question_lower and "design" in question_lower:
        topics.append("Layered Network Design")
    if "header" in question_lower and "ipv4" in question_lower:
        topics.append("IPv4 Header Format")
    if "routed" in question_lower and "routing protocol" in question_lower:
        topics.append("Routed vs Routing Protocols")
    if "static routing" in question_lower or "dynamic routing" in question_lower:
        topics.append("Static vs Dynamic Routing")
    if "control plane" in question_lower or "data plane" in question_lower:
        topics.append("Control and Data Planes")
    
    return topics if topics else ["Other"]

# Combine all papers
all_papers = {
    "Dec 2022": paper_2022_dec,
    "May 2023": paper_2023_may,
    "Dec 2023": paper_2023_dec,
    "May 2024": paper_2024_may,
    "Dec 2024": paper_2024_dec,
    "CN 2025": paper_2025_cn
}

# Count topic frequencies
all_questions = []
for paper_name, questions in all_papers.items():
    for q_num, question in questions.items():
        topics = categorize_topic(question)
        all_questions.append({
            "Paper": paper_name,
            "Question": q_num,
            "Question Text": question,
            "Topics": ", ".join(topics)
        })
        for topic in topics:
            topics_frequency[topic] += 1

# Create DataFrame
df_questions = pd.DataFrame(all_questions)

# Sort topics by frequency
sorted_topics = sorted(topics_frequency.items(), key=lambda x: x[1], reverse=True)

print("=" * 80)
print("TOP TOPICS BY FREQUENCY")
print("=" * 80)
for i, (topic, freq) in enumerate(sorted_topics[:30], 1):
    print(f"{i:2d}. {topic:50s} - Appeared {freq} times")

print("\n" + "=" * 80)
print(f"Total unique topics identified: {len(sorted_topics)}")
print(f"Total questions analyzed: {len(all_questions)}")
