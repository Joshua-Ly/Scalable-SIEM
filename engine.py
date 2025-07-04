import yaml 
from collections import defaultdict
from datetime import datetime, timedelta

failed_attempts = defaultdict(list)

def load_rules(path="rules.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)["rules"]

def apply_rules(event, rules):
    alerts = []
    for rule in rules:
        if rule['type'] == 'failed_login' and rule['match_phrase'] in event['message']:
            ip = event['message'].split("IP")[-1].strip()
            now = event['timestamp']
            failed_attempts[ip].append(now)

            failed_attempts[ip] = [t for t in failed_attempts[ip] if now - t <= timedelta(seconds=rule['window'])]

            if len(failed_attempts[ip]) >= rule['threshold']:
                alerts.append(f"[ALERT] {rule['name']} triggered for IP {ip}")
    return alerts
