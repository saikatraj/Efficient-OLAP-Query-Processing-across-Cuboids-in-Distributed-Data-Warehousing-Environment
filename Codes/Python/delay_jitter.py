import pyshark
import statistics
# Create an empty dictionary to store the packets
server_packet_dict = {}

# Open the PCAP file using pyshark's FileCapture function
server_capture = pyshark.FileCapture('G:\WireSharkFilesAndCodes\CAP\Europe\HighLoad\E_2.pcapng')

# Iterate through each packet in the PCAP file
for packet in server_capture:
    try:
        # Extract the IP ID from the packet
        ip_id = packet.ip.id
        # Add the packet to the dictionary using the IP ID as the key
        server_packet_dict[ip_id] = packet
    except:
        continue

client_packet_dict = {}

# Open the PCAP file using pyshark's FileCapture function
client_capture = pyshark.FileCapture('G:\WireSharkFilesAndCodes\CAP\Europe\HighLoad\C_2.pcapng')

# Iterate through each packet in the PCAP file
for packet in client_capture:
    try:
        # Extract the IP ID from the packet
        ip_id = packet.ip.id
        # Add the packet to the dictionary using the IP ID as the key
        client_packet_dict[ip_id] = packet
    except:
        continue

common_ids = []

# Iterate through the keys (i.e., IP IDs) in the server packet dictionary
for ip_id in server_packet_dict:
    # Check if the IP ID is also present in the client packet dictionary
    if ip_id in client_packet_dict:
        # If it is, add the IP ID to the common_ids list
        common_ids.append(ip_id)

# Print the list of common IP IDs
#print(len(common_ids))


#Create empty list to store delay
delay = []

for id in common_ids:
    server_time = server_packet_dict[id].sniff_time
    client_time = client_packet_dict[id].sniff_time
    delta = abs(server_time - client_time)
    delay.append(delta)

#print(delay)

delay_seconds = [td.total_seconds() for td in delay]
#print(delay_seconds)


jitter_list = []
for i in range(len(delay_seconds) - 1):
    jitter = abs(delay_seconds[i+1] - delay_seconds[i])
    jitter_list.append(jitter)

print("Number of Packets: " + str(len(delay_seconds)))
#print(len(jitter_list))

print("Average Delay: " + str(statistics.mean(delay_seconds)) + "s")
print("Average Jitter: " + str(statistics.mean(jitter_list)) + "s")