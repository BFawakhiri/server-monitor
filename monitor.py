import os
import socket
import platform
import datetime
import psutil

def get_system_info():
    hostname = socket.gethostname()
    current_user = os.getlogin() if hasattr(os, 'getlogin') else os.environ.get('USER', 'N/A')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    os_info = f"{platform.system()} {platform.release()}"
    kernel_version = platform.version().split()[0] if platform.system() == "Linux" else platform.release()

    cpu_usage = f"{psutil.cpu_percent(interval=1)}%"

    mem = psutil.virtual_memory()
    total_mem = f"{round(mem.total / (1024**3), 2)} GB"
    used_mem = f"{round(mem.used / (1024**3), 2)} GB"
    free_mem = f"{round(mem.available / (1024**3), 2)} GB"
    mem_usage_pct = f"{mem.percent}%"

    disk = psutil.disk_usage('/')
    disk_used = f"{round(disk.used / (1024**3), 2)} GB"
    disk_free = f"{round(disk.free / (1024**3), 2)} GB"
    disk_usage_pct = f"{disk.percent}%"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        ip_address = "127.0.0.1"

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime_duration = now - boot_time
    days = uptime_duration.days
    hours, remainder = divmod(uptime_duration.seconds, 3600)
    uptime_str = f"{days} Days {hours} Hours"

    return {
        "hostname": hostname,
        "current_user": current_user,
        "current_time": current_time,
        "os_info": os_info,
        "kernel_version": kernel_version,
        "cpu_usage": cpu_usage,
        "total_mem": total_mem,
        "used_mem": used_mem,
        "free_mem": free_mem,
        "mem_usage_pct": mem_usage_pct,
        "disk_used": disk_used,
        "disk_free": disk_free,
        "disk_usage_pct": disk_usage_pct,
        "ip_address": ip_address,
        "uptime_str": uptime_str
    }

def generate_report(info):
    report_content = f"""==============================
SERVER HEALTH REPORT
==============================
Hostname:        {info['hostname']}
Current User:    {info['current_user']}
Date:            {info['current_time']}
Operating System:{info['os_info']}
Kernel:          {info['kernel_version']}
CPU Usage:       {info['cpu_usage']}
------------------------------
Memory Usage:
  Total: {info['total_mem']}
  Used:  {info['used_mem']}
  Free:  {info['free_mem']}
  Usage: {info['mem_usage_pct']}
------------------------------
Disk Usage (/):
  Used:  {info['disk_used']}
  Free:  {info['disk_free']}
  Usage: {info['disk_usage_pct']}
------------------------------
IP Address:      {info['ip_address']}
Uptime:          {info['uptime_str']}
==============================
"""
    print(report_content)
    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "server_report.txt")
    with open(report_path, "w") as file:
        file.write(report_content)
    print(f"[+] Report generated successfully at: {report_path}")

if __name__ == "__main__":
    data = get_system_info()
    generate_report(data)
