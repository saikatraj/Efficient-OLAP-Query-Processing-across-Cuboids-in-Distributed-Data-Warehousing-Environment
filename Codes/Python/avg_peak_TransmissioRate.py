import pyshark
import datetime

# Open the PCAP file
capture = pyshark.FileCapture("G:\WireSharkFilesAndCodes\Captures\Single Query\C_2167636__1_1.pcapng")

# Calculate the duration of the capture in seconds
start_time = float(capture[0].sniff_time.timestamp())
end_time = float(capture[-1].sniff_time.timestamp())
duration = end_time - start_time

# Initialize variables for average and peak transmission rates
total_data = 0
max_data_rate = 0

# Iterate through the packets
for packet in capture:
  # Add the size of the packet to the total data transmitted
  total_data += int(packet.length)

  # Calculate the data rate for this packet
  try:
    data_rate = int(packet.length) / (float(packet.sniff_time.timestamp()) - start_time)
  except ZeroDivisionError:
    # Set the data rate to 0 if a division by zero error occurs
    data_rate = 0

  # Update the maximum data rate if necessary
  if data_rate > max_data_rate:
    max_data_rate = data_rate

print("Peak transmission rate:", max_data_rate, "bytes/sec")
