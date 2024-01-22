'''this code is for checking system details 
'''
import speedtest
import psutil
import ctypes

# function to get list of installed softwares in the device

def find_installed_software():
    software_list = []
    for software in psutil.process_iter(['name']):
        software_list.append(software.info['name'])
    return software_list

# function to get connected internet speed of device
def check_internet_speed():
    speed_test = speedtest.Speedtest()
    download_speed = speed_test.download() // 1000000
    upload_speed = speed_test.upload() // 1000000

    return download_speed,upload_speed


def get_screen_dimensions():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    dpi = user32.GetDpiForSystem()
    screen_size = round(screensize[0] / dpi * 25.4, 2), round(screensize[1] / dpi * 25.4, 2)
    return screen_size








# ===================================== MAIN BLOCK OF CODE ====================================
start = input('y/n : ').lower()

if start == 'y':
    # software list 
    software_List = find_installed_software()
    print('='*5, 'Installed software in system', '='*5)
    for i in software_List:
        print(i)
    print('='*5, 'Above are Installed software in system', '='*5)

# network speed 
network_speed_upload,network_speed_download = check_internet_speed()

print('='*5, 'The speed of network used in system is', '='*5)
print(f'The upload speed of internet on this device is {network_speed_upload} MB \n and download speed is {network_speed_download} MB')

print('='*5, 'The screen dimensions of your system are ', '='*5)
print(f"The screen dimensions of your system are  **{round(get_screen_dimensions()[0] / 25.4, 2)} x {round(get_screen_dimensions()[1] / 25.4, 2)}** inches.")
