import requests
import time
import random
from datetime import datetime

# Configuration
MALICIOUS_IP = "194.0.234.35"
INTERVAL_SECONDS = 5  # Time between requests
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def send_beacon():
    try:
        # Randomize URL parameters to avoid caching
        url = f"http://{MALICIOUS_IP}/beacon?data={random.randint(1000,9999)}"
        
        # Custom headers to mimic browser traffic
        headers = {
            "User-Agent": USER_AGENT,
            "X-Test": "StellarCyberDemo"
        }
        
        response = requests.get(url, headers=headers, timeout=3)
        print(f"[{datetime.now()}] Beacon sent to {MALICIOUS_IP} - Status: {response.status_code}")
        
    except Exception as e:
        print(f"[{datetime.now()}] Error: {str(e)}")

if __name__ == "__main__":
    print(f"Starting beacon to {MALICIOUS_IP} every {INTERVAL_SECONDS} seconds...")
    print("Press Ctrl+C to stop")
    
    while True:
        send_beacon()
        time.sleep(INTERVAL_SECONDS)