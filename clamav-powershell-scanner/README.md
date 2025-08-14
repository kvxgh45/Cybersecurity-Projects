# ClamAV PowerShell Scanner

## 📌 Overview
This project is a PowerShell script that automates ClamAV antivirus scanning on Windows.  
It updates virus definitions, scans local or network paths, quarantines infected files, and logs the results.  
Designed for quick deployment in enterprise or lab environments.

---

## 🛠 Features
- Automatic virus signature updates with `freshclam`
- Recursive scans of local or network directories
- Quarantines infected files safely
- Detailed scan logs with timestamps
- Works in Task Scheduler for scheduled scans

---

## 📂 Project Structure
```
src/         # Main PowerShell script
docs/        # Architecture diagrams & usage examples
samples/     # Example scan logs & test files
```

---

## 🚀 Installation
1. Download and install ClamAV for Windows: [https://www.clamav.net/downloads](https://www.clamav.net/downloads)
2. Clone this repository:
```powershell
git clone https://github.com/yourusername/clamav-powershell-scanner.git
cd clamav-powershell-scanner
```
3. Edit `clamav_scan.ps1` to set your ClamAV install path and scan targets.

---

## 📖 Usage
Run a scan:
```powershell
.\src\clamav_scan.ps1 -TargetPath "C:\Users\Public" -QuarantinePath "C:\ClamAV\quarantine"
```

Output:
```
[INFO] Updating virus definitions...
[INFO] Starting scan on C:\Users\Public
C:\Users\Public\infected_file.exe: Win.Test.EICAR_HDB-1 FOUND
[INFO] Scan complete. Log saved to C:\ClamAV\logs\scan_20250813_2130.log
```

---

## 🖼 Architecture
![Architecture Diagram](docs/architecture.png)

---

## 📅 Roadmap
- [ ] Add email alerts when threats are found
- [ ] Add multiple target path scanning
- [ ] Add CSV log export for SIEM ingestion

---

## ⚠ Legal Disclaimer
This project is for educational and authorized use only.  
Do not scan systems without permission.

---

## 📜 License
MIT License
