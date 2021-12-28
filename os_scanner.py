import os
import time
import psutil
import pyautogui
import socket
from datetime import timedelta, datetime
from PIL import Image
from requests import get
from uuid import getnode as get_mac

start_time = time.monotonic()

get_os_type = str(os.name)
get_current_user = str(os.getlogin())
get_os_info = str(os.uname())
get_cpu_cores = psutil.cpu_count()
get_disk_usage = psutil.disk_usage("/")
get_amount_memory = (int(psutil.virtual_memory().total) >> 30)
get_mac_address = get_mac()

# Get private IP address
get_private_ip_address = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
get_private_ip_address.connect(("8.8.8.8", 80))
# Get public IP address using api.ipify.org web site
get_public_ip = get("http://api.ipify.org").text


# Get system uptime
def uptime():
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    return (str(uptime).split('.')[0])


get_screenshot = pyautogui.screenshot("Screenshot.jpg")

print("*" * 5, "OS Details", "*" * 5)
print("OS type:", get_os_type)
print("Current logged user:", get_current_user)
print("There are", get_cpu_cores, "CPU cores in the system")
print("Current disk usage:", get_disk_usage)
print("The total amount of RAM:", get_amount_memory, "GB")
print("The private IP address is:", get_private_ip_address.getsockname()[0])
print("The public IP address is:", get_public_ip)
print("The current MAC address is:", get_mac_address)
print("The current uptime is:", (uptime()))

print("\n")
print("All results are saved to results.txt file")

end_time = time.monotonic()

print("Time spend:", timedelta(seconds=end_time - start_time))

new_file = open("results.txt", "w")

new_file.write("***System scan results***\n" + "OS type: " + get_os_type + "\n" + "Current logged user: " + get_current_user + "\n" +
"Current disk usage: " + str(get_disk_usage) + "\n"+ "The total amount of RAM: " + str(get_amount_memory) + "GB" + "\n" +
"The private IP address is: " + str(get_private_ip_address.getsockname()[0]) + "\n" + "The public IP address is: " + get_public_ip +
"\n" + "The current MAC address is: " + str(get_mac_address) + "\n" + "The current uptime is: " + str(uptime()))

new_file.close
