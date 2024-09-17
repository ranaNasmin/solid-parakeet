# This is a script to scan a range of ip addresses
# First let's import nmap module
import nmap

# Then import re module to ensure that our address is correctly formated
import re

# Regular Expression pattern for ip address
ip_address_pattern = re.compile("^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$")

# Regular Expression pattern for range of ports
# We have to specify min and max port numbers
ports_range_pattern = re.compile("([0-9]+)-([0-9]+)")

# Initialize min and max port numbers
port_min = 0
port_max = 65535

open_ports = []

# Ask the user to input ip address
while True:
    ip_address_entered = input("Please enter the ip address to be scanned: ")
    if ip_address_pattern.search(ip_address_entered):
        print(f"{ip_address_entered} is a valid ip address ")
        break

# Ask the user to enter the port number now
# And check whether the port range is valid

while True:
    print("Enter range of port numbers you want to scan in the format <int>-<int>")
    port_range = input("Enter port range: ")
    port_range_valid = ports_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break


nm = nmap.PortScanner()
# We are looping all over all of the ports in the specified range.

for port in range(port_min, port_max+1):
    try:
        result = nm.scan(ip_address_entered, str(port))
        # print(result)
        # We return the port status from the returned object
        port_status = (result['scan'][ip_address_entered]['tcp'][port]['state'])
        print(f"{port} is {port_status}")
    except:
        print(f"we cannot scan this port{port}")