# twi-world

This repository contains a simple TCP port scanner implemented in Python.

**File:** `Port_scanner.py`

**Description:**
- Scans TCP ports 1–1024 on a target host (default: localhost `127.0.0.1`).
- Prints each open port and the total scan time.

**Requirements:**
- Python 3.x (no external packages required)

**Usage:**
1. (Optional) Create and activate a virtual environment named `myenv`:

```powershell
python -m venv myenv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\myenv\Scripts\Activate.ps1
```

2. Run the scanner:

PowerShell / CMD:

```powershell
python Port_scanner.py
```

**Notes & customization:**
- The script sets `target = "127.0.0.1"` by default. Change this to scan another IP or hostname.
- The scanned port range is `range(1, 1025)`; adjust the range in the file to scan other ports.
- Socket timeout is set to 1 second (`sock.settimeout(1)`) — increase for slower networks.

**Example output:**

```
Starting scan on host: 127.0.0.1
Port 22: Open
Port 80: Open
Scanning completed in 0.85 seconds
```

**License & Safety:**
- Use this scanner only on systems you own or are authorized to test. Unauthorized scanning may be illegal.

---
If you'd like, I can add command-line arguments (target, port range, timeout) to `Port_scanner.py` next.
# twi-world
