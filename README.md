"Scalable SIEM" is a python-based tool that performs log moitoring, parsing, rule-based detection, and alerting. 

# Features
- Monitors logs in real-time (tailing)
- YAML-based detection rules
- Brute-force detection
- Scalable

# How To Implement Testcases
After running main.py, open up a new concurrent terminal. Add in custom testcases, to parse custom logs to 'syslog.log', and example format includes: 

echo "[2025-07-04 10:01:00] [auth] [WARNING] Failed login for user 'admin' from IP 192.168.1.5" >> syslog.log 

# How to Run Scalable SIEM
```bash
pip install -r requirements.txt
python main.py

