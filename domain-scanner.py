import time
import logging
import whois
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

log_file = Path("./scan.log")
log_format = "%(asctime)s - %(levelname)s - %(message)s"

logging.basicConfig(level=logging.INFO, format=log_format, filename=log_file)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(log_format))

logger = logging.getLogger()
logger.addHandler(console_handler)

# Check
def check_domain_availability(domain_name):
    try:
        w = whois.whois(domain_name)
        if w.status:
            logging.info(f"The domain '{domain_name}' is already registered.")
        else:
            logging.info(f"The domain '{domain_name}' is available for registration.")
            return domain_name
    except Exception as e:
        logging.error(f"An error occurred while checking the availability of the domain '{domain_name}'.")
        logging.error(e)

# Read Dict
def read_domain_dict(domain_type):
    domain_dict = []
    try:
        domain_file = Path(f"./dict/{domain_type}.txt")
        with domain_file.open("r") as file:
            domain_dict = [line.strip() for line in file]
    except FileNotFoundError:
        logging.error(f"File '{domain_file}' not found.")
        exit()
    except Exception as e:
        logging.error(f"An error occurred while reading the domain dict '{domain_type}'.")
        logging.error(e)
        exit()
    return domain_dict


# Save File
def save_available_domain(available_domains, result_file):
    if available_domains:
        result_file.parent.mkdir(parents=True, exist_ok=True)
        with result_file.open("w") as file:
            file.write("\n".join(available_domains))
            logging.info(f"Available domains are saved to '{result_file}'.")
    else:
        logging.warning("No available domain found.")

# Scan
def scan_domains(domain_list, thread_num):
    with ThreadPoolExecutor(max_workers=thread_num) as executor:
        results = executor.map(check_domain_availability, domain_list)
        available_domains = [domain for domain in results if domain]
    return available_domains

if __name__ == "__main__":
    domain_suffix = input("Input the domain suffix to scan (default com): ") or "com"
    domain_type = input("Input the domain type to scan (default abc): ") or "abc"
    thread_num = int(input("Input the number of threads (default 2): ") or 2)
    
    start_time = time.time()
    result_file = Path(f"./result/{domain_type}_{domain_suffix}.txt")
    domain_dict = read_domain_dict(domain_type)
    domain_list = [f"{domain}.{domain_suffix}" for domain in domain_dict]
    
    logging.info(f"Start scanning {len(domain_list)} domains.")
    available_domains = scan_domains(domain_list, thread_num)
    save_available_domain(available_domains, result_file)
    
    end_time = time.time()
    logging.info(f"Finished scanning {len(domain_list)} domains in {end_time - start_time} seconds.")
