# Domain Scanner

This is a Python script that scans a list of domain names for availability.

## Requirements

- Python 3.x
- `whois` library (`pip install python-whois`)

## Usage

```bash
~/Domain-Scanner ᐅ python3 domain-scanner.py
Input the domain suffix to scan (default com): com
Input the domain type to scan (default abc): aaaa
Input the number of threads (default 2): 2
2023-08-20 06:05:08,959 - INFO - Start scanning 26 domains.
2023-08-20 06:05:09,501 - INFO - The domain 'aaaa.com' is already registered.
2023-08-20 06:05:09,501 - INFO - The domain 'bbbb.com' is already registered.
2023-08-20 06:05:09,913 - INFO - The domain 'cccc.com' is already registered.
2023-08-20 06:05:09,943 - INFO - The domain 'eeee.com' is already registered.
2023-08-20 06:05:10,029 - INFO - The domain 'dddd.com' is already registered.
2023-08-20 06:05:10,162 - INFO - The domain 'ffff.com' is already registered.
2023-08-20 06:05:10,594 - INFO - The domain 'gggg.com' is already registered.
2023-08-20 06:05:10,966 - INFO - The domain 'iiii.com' is already registered.
2023-08-20 06:05:10,993 - INFO - The domain 'jjjj.com' is already registered
```
