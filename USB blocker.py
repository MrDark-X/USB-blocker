import os
import re

# Function to check USB port status
def check_usb_port_status():
    result = os.popen('REG QUERY "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR" /v Start').read()
    match = re.search(r"Start\s+REG_DWORD\s+(\w+)", result)
    if match:
        status = int(match.group(1), 16)
        return status
    return None

# Function to block USB ports
def block_usb_ports():
    result = os.system('REG ADD HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR /v Start /t REG_DWORD /d 4 /f')
    return result == 0

# Function to unblock USB ports
def unblock_usb_ports():
    result = os.system('REG ADD HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR /v Start /t REG_DWORD /d 3 /f')
    return result == 0

# Check USB port status
current_status = check_usb_port_status()
if current_status is not None:
    if current_status == 3:
        print("All USB ports are currently unblocked.")
    elif current_status == 4:
        print("All USB ports are currently blocked.")

    user_option = input("Do you want to block or unblock USB ports? [block/unblock]: ")
    if user_option.lower() == "block":
        if current_status == 3:
            if block_usb_ports():
                print("USB ports have been blocked successfully.")
            else:
                print("Failed to block USB ports.")
        else:
            print("USB ports are already blocked.")
    elif user_option.lower() == "unblock":
        if current_status == 4:
            if unblock_usb_ports():
                print("USB ports have been unblocked successfully.")
            else:
                print("Failed to unblock USB ports.")
        else:
            print("USB ports are already unblocked.")
    else:
        print("Choose the correct option. [block/unblock]")
else:
    print("Failed to retrieve USB port status or Start value is not found in the registry.")

input("Press Enter to continue...")
