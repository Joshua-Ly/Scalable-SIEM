from collector import tail_log_file
from parser import parse_log
from engine import load_rules, apply_rules
from alerts import send

LOG_PATH = "syslog.log"

def main():
    rules = load_rules()
    print("Monitoring logs...")

    for line in tail_log_file(LOG_PATH):
        parsed = parse_log(line)
        if parsed:
            alerts = apply_rules(parsed, rules)
        send(alerts)

if __name__ == "__main__":
    main()
