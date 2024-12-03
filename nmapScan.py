import nmap

scanner = nmap.PortScanner()

host = input("Enter the host or IP address to check: ")

print(f"The entered host or IP address was: {host}\n")
type(host)

menu = input(
    "Choose the type of scan to perform\n"
    "1 - SYN Type Scan\n"
    "2 - UDP Type Scan\n"
    "3 - Intense Type Scan\n"
    "Enter the chosen option: "
)

print(f"The chosen option was: {menu}\n")

if menu == "1":
    print("Nmap version", scanner.nmap_version())
    scanner.scan(host, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Status IP address requested: ", scanner[host].state())
    print(scanner[host].all_protocols())
    print ("Open ports:  ", scanner[host]['tcp'].keys())
    print("Scan SYN Completed")

elif menu == "2":
    print("Nmap version", scanner.nmap_version())
    scanner.scan(host, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status IP address requested: ", scanner[host].state())
    print(scanner[host].all_protocols())
    print ("Open ports:  ", scanner[host]['udp'].keys())
    print("Scan UDP Completed")

elif menu == "3":
    print("Nmap version", scanner.nmap_version())
    scanner.scan(host, '1-1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status IP address requested: ", scanner[host].state())
    print(scanner[host].all_protocols())
    print ("Open ports:  ", scanner[host]['tcp'].keys())
    print("Scan Intense Completed")

else:
    print("Please choose a valid option")