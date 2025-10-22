import re

inputs = ["<script>alert('xss')</script>", "Normal text","<img src='javascript:alert(1)'>"]

xss_pattern = r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>'
for inp in inputs:
    if re.search(xss_pattern, inp):
        print(f"XSS detected in: {inp}")