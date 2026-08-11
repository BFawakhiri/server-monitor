import os
import platform
import socket
import datetime
import psutil

def get_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = now - boot_time
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{days} Days {hours} Hours {minutes} Minutes"

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def collect_info():
    hostname = socket.gethostname()
    username = os.getlogin() if hasattr(os, 'getlogin') else os.environ.get('USER', 'N/A')
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    os_info = f"{platform.system()} {platform.release()}"
    kernel = platform.version().split()[0]
    
    cpu_usage = f"{psutil.cpu_percent(interval=1)}%"
    
    mem = psutil.virtual_memory()
    mem_total = f"{round(mem.total / (1024**3), 2)} GB"
    mem_used = f"{round(mem.used / (1024**3), 2)} GB"
    mem_free = f"{round(mem.available / (1024**3), 2)} GB"
    mem_percent = f"{mem.percent}%"
    
    disk = psutil.disk_usage('/')
    disk_total = f"{round(disk.total / (1024**3), 2)} GB"
    disk_used = f"{round(disk.used / (1024**3), 2)} GB"
    disk_free = f"{round(disk.free / (1024**3), 2)} GB"
    disk_percent = f"{disk.percent}%"
    
    ip_addr = get_ip_address()
    uptime_str = get_uptime()

    report_content = f"""==============================
SERVER HEALTH REPORT
==============================
Hostname       : {hostname}
Current User   : {username}
Date           : {date_str}
Operating System: {os_info}
Kernel         : {kernel}
CPU Usage      : {cpu_usage}

Memory Usage   :
  Total        : {mem_total}
  Used         : {mem_used}
  Free         : {mem_free}
  Usage        : {mem_percent}

Disk Usage (/) :
  Total        : {disk_total}
  Used         : {disk_used}
  Available    : {disk_free}
  Usage        : {disk_percent}

IP Address     : {ip_addr}
Uptime         : {uptime_str}
==============================
"""
    return report_content

def main():
    report = collect_info()
    print(report)
    
    os.makedirs("reports", exist_ok=True)
    with open("reports/server_report.txt", "w") as f:
        f.write(report)
    print("Report generated successfully at 'reports/server_report.txt'")

if __name__ == "__main__":
    main()
