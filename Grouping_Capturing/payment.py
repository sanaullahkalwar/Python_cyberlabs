import re
report = "Payment: **** **** **** 1234 (full: 4111-1111-1111-1234)"
pattern = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
redacted = re.sub(pattern, 'XXXX-XXXX-XXXX-XXXX', report)
print(redacted) # Expected: Payment: **** **** **** 1234(full: XXXX-XXXX-XXXX-XXXX)