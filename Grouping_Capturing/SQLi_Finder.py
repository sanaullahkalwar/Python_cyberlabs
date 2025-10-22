import re
log_file = """
GET /login?user=admin' OR '1'='1 HTTP/1.1
GET /search?q=normal HTTP/1.1
GET /login?user=admin'; DROP TABLE users-- HTTP/1.1
"""
pattern = r"(?i)\b(union|select|drop|insert|delete|update|or|and)\b"


suspicious = re.findall(pattern, log_file, re.MULTILINE)

for match in suspicious:
    print(f"Potential SQLi: {match}")