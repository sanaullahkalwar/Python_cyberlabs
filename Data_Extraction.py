import re

log_line = '127.0.0.1 - - [11/Sep/2025:10:00:00 +0000] "GET/admin HTTP/1.1" 200 1234 "http://evil.com" "Mozilla/5.0"'

pattern = r'(\S+) \S+ \S+ \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'

match = re.match(pattern, log_line)

if match:
    ip, timestamp, request, status, size, referer, user_agent= match.groups()
    data = {
        'IP': ip, 
        'Timestamp': timestamp, 
        'Request':request, 
        'Status': status, 
        'Size': size, 
        'Referer': referer,
        'User-Agent': user_agent}
    print(data)
