import re


#Email verifier
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern,email):
        return f"Invalid Format {email}"
    
    domain = email.split('@')[-1].lower()
    
    if domain.endswith('.gov') or '.gov' in domain:
        return f"Rejected (governement domain): {email}"
     
    return f"Valid corporate email: {email}"
    


#Phone number matcher
def phone_number_matcher(text):
    pattern = r"(?:(?:\+\d{1,3}[\s-]?)?  (?:\(?\d{1,4}\)?[\s-]?)? \d{2,4}[\s-]?\d{3,4}[\s-]?\d{3,4})"
    matches = re.findall(pattern, text, re.VERBOSE)
    phones = [m.strip() for m in matches if len(m.strip()) >= 7]
    return phones


#valid ip extractor function
def valid_ip_extractor(logs):

    # Regex pattern to match only valid IPv4 addresses (0–255 in each octet)
    pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?:\.|$)){4}\b'

    # Extract all valid IPs
    valid_ips = re.findall(pattern, logs)

    # Print results
    print("Valid IPs found:")
    for ip in valid_ips:
        print(ip)


#This function will extract the both valid and invalid ip addresses from the givin file
def extract_ips_from_log(file_path):
    """
    Extracts valid and invalid IP addresses from a given log file.
    Returns (valid_ips, invalid_ips)
    """
    with open(file_path, "r") as file:
        log_data = file.read()

    all_ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
    valid_ip_pattern = r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"

    all_ips = re.findall(all_ip_pattern, log_data)
    valid_ips = re.findall(valid_ip_pattern, log_data)
    invalid_ips = [ip for ip in all_ips if ip not in valid_ips]

    return valid_ips, invalid_ips


#Email Hider
def email_hider(report):    
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    redacted_email = re.sub(pattern,'[EMAIL_REDACTED]',report)
    return redacted_email