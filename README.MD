# Server Health Monitor

A lightweight DevOps automation script written in Python to inspect and generate automated server health reports for Linux systems.

## Features
- **System Identifiers**: Hostname, Current User, System Date & Time.
- **OS Details**: Operating System name and Kernel version.
- **Resource Usage**: CPU Usage, RAM Usage (Total, Used, Free, Usage %), Disk Space Usage.
- **Network & Status**: Primary IPv4 address and System Uptime.
- **Automated Reporting**: Automatically saves formatted logs into `reports/server_report.txt`.

## Requirements
- Python 3.x
- `psutil` library

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd server-monitor
