'''this code is for checking system details 
'''
import speedtest
import psutil
import ctypes
import screeninfo
import platform
import subprocess
import re
import uuid



# function to get list of installed softwares in the device

def find_installed_software():
    software_list = []
    for software in psutil.process_iter(['name']):
        software_list.append(software.info['name'])
    return software_list

# function to get connected internet speed of device
def check_internet_speed():
    try:
        speed_test = speedtest.Speedtest()
        download_speed = speed_test.download() // 1000000
        upload_speed = speed_test.upload() // 1000000

        return download_speed,upload_speed
    except:
        return "Was unable to get Internet speed"


# function to get screen resolution of device
def screen_resolution():
    monitors = screeninfo.get_monitors()
    resolutions = []
    for monitor in monitors:
        resolutions.append((monitor.width, monitor.height))
    return resolutions

# CPU model, No of core and threads of CPU

def cpu_details():
    cpu_info = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    return cpu_info, cpu_cores, cpu_threads

# GPU 
def gpu_details():
    try:
        gpu_info = subprocess.check_output(['wmic', 'path', 'win32_VideoController', 'get', 'name']).decode('utf-8').split('\n')[1:-2]
        return gpu_info[0]
    except:
        return "No GPU found"

#  function to get Ram details of device
def ram_size():
    ram_size = round(psutil.virtual_memory().total / (1024.0 **3), 2)
    return ram_size

# function to get Screen dimensions of device
def get_screen_dimensions():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    dpi = user32.GetDpiForSystem()
    screen_size = round(screensize[0] / dpi * 25.4, 2), round(screensize[1] / dpi * 25.4, 2)
    return screen_size

#  function to get MAC addres details of device
def mac_address():
    try: 
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        return mac_address
    except:
        return "Was unable to get Mac Address because not conected to network"

#  function to get Public IP details of device
def public_ip():
    try: 
        public_ip = subprocess.check_output(['curl', 'ifconfig.me']).decode('utf-8').strip()
        return public_ip
    except:
            return "Was unable to get Public IP Address because not conected to network"

#  function to get Windows version details of device
def windows_version():
    windows_version = platform.win32_ver()[0]
    return windows_version


# ===================================== MAIN BLOCK OF CODE ====================================
start = input('Do you want to see details of your PC ? \n Input YES/NO : ').lower()

if start == 'yes':
    # software list 
    software_List = find_installed_software()
    print('='*5, 'Installed software in system', '='*5)
    for i in software_List:
        print(i)

# network speed 
    try:
        network_speed_upload,network_speed_download = check_internet_speed()
        print(f"\n'='*5, 'The speed of network used in system is', '='*5")
        print(f'The upload speed of internet on this device is {network_speed_upload} MB \n and download speed is {network_speed_download} MB')
    except:
        print("Was unable to get Internet speed")


    # screen resolutions
    resolutions = screen_resolution()
    for i, resolution in enumerate(resolutions):
        print(f"\n{'='*5} Screen  {i+1} Resolution {'='*5}")
        print(f"Width: {resolution[0]} pixels")
        print(f"Height: {resolution[1]} pixels")

    # CPU, no. of core and threads
    cpu_info, cpu_cores, cpu_threads = cpu_details()
    print(f"\n{'='*5} CPU Details {'='*5}")
    print(f"Model: {cpu_info}")
    print(f"Cores: {cpu_cores}")
    print(f"Threads: {cpu_threads}")

    # GPU 
    gpu = gpu_details()
    print(f"\n{'='*5} GPU {'='*5}")
    print(gpu)

    # Ram
    ram = ram_size()
    print(f"\n{'='*5} RAM {'='*5}")
    print(f" The Ram Size of Your device is: {ram} GB")

    # screen dimensions
    print('='*5, 'The screen dimensions of your system are ', '='*5)
    print(f"The screen dimensions of your system are  {round(get_screen_dimensions()[0] / 25.4, 2)} x {round(get_screen_dimensions()[1] / 25.4, 2)} inches.")

    # MAC address 
    mac_add = mac_address()
    print(f"\n{'='*5} MAC Address {'='*5}")
    print(f"Mac Address of device is : {mac_add}")

    # Public IP
    ip = public_ip()
    print(f"\n{'='*5} Public IP Address {'='*5}")
    print(f"Public IP Address of device is : {ip}")

    # Windows version
    win_version = windows_version()
    print(f"Version: {win_version}")
