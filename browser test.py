import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

TOOLS = {
    "Virustotal": "https://www.virustotal.com/gui/ip-address/{ip}/detection",
    "AbuseIPDB": "https://www.abuseipdb.com/check/{ip}",
    "IP Analyzer": "https://www.ipalyzer.com/{ip}",
    "IPVoid": "https://www.ipvoid.com/ip-blacklist-check/",
    "Shodan": "https://www.shodan.io/host/{ip}",
    "Whois": "https://who.is/dns/{ip}",
    "PulseDive": "https://pulsedive.com/indicator/?ioc={ip}",
    "IP Lookup": "https://www.iplocation.net/ip-lookup",
    "DNSlytics": "https://dnslytics.com/ip/{ip}",
    "Talos Intelligence": "https://talosintelligence.com/reputation_center/lookup?search={ip}"
}

def scan_ip(target_ip):
    # Configure Firefox to open new tabs
    options = Options()
    options.set_preference("browser.link.open_newwindow", 3)  # Open in new tab
    options.set_preference("browser.link.open_newwindow.restriction", 0)
    
    # Initialize Firefox
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    
    try:
        # Open first tool in initial tab
        first_tool, first_url = next(iter(TOOLS.items()))
        url = first_url.format(ip=target_ip)
        driver.get(url)
        print(f"Scanning with {first_tool}...")
        time.sleep(3)
        
        # Open remaining tools in new tabs
        for tool_name, url_template in list(TOOLS.items())[1:]:
            url = url_template.format(ip=target_ip)
            driver.execute_script(f"window.open('{url}', '_blank');")
            print(f"Opened {tool_name} in new tab")
            time.sleep(1)  # Brief pause between tabs
            
        # Keep browser open for viewing
        input("Press Enter to close all tabs...")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    target_ip = sys.argv[1] if len(sys.argv) > 1 else input("Enter target IP: ").strip()
    
    if not all(part.isdigit() for part in target_ip.split('.') if part.isdigit()):
        print("Invalid IP format")
    else:
        print(f"\nStarting scan for {target_ip}")
        scan_ip(target_ip)
        print("\nScan complete!")