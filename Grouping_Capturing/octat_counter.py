import re

log_entry = "Access denied from 192.168.56.1 at 2025-10-21"

pattern = r'(?P<oct1>\d{1,3})\.(?P<oct2>\d{1,3})\.(?P<oct3>\d{1,3})\.(?P<oct4>\d{1,3})'

match = re.search(pattern,log_entry)

print(f"{match.groupdict()}")