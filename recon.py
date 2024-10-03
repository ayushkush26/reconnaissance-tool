import whois
import dns.resolver
import subprocess
import json
import os

# Function to fetch WHOIS information of a domain
def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Error retrieving WHOIS information: {e}"

# Function to fetch DNS records (A, MX, NS, TXT) of a domain
def get_dns_info(domain):
    dns_info = {}
    dns_resolver = dns.resolver.Resolver()
    
    for record_type in ['A', 'MX', 'NS', 'TXT']:
        try:
            dns_info[record_type] = dns_resolver.resolve(domain, record_type)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
            dns_info[record_type] = f"Error: {str(e)}"
    
    return dns_info

# Function to retrieve subdomains using Sublist3r
def get_subdomains(domain):
    try:
        sublist3r_path = "/Users/ayushkush/Sublist3r/sublist3r.py"
        
        if not os.path.exists(sublist3r_path):
            return f"Error: Sublist3r not found at {sublist3r_path}"
        
        result = subprocess.run(['python3', sublist3r_path, '-d', domain, '-o', 'subdomains.txt'], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        
        with open("subdomains.txt", "r") as file:
            subdomains = file.read().splitlines()
        return subdomains
    except Exception as e:
        return f"Error retrieving subdomains: {e}"

# Function to detect web technologies using WhatWeb
def get_website_technologies(domain):
    try:
        result = subprocess.run(['whatweb', domain, '--log-json', 'whatweb_output.json'], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        
        with open('whatweb_output.json', 'r') as file:
            technologies = json.load(file)
        return technologies
    except Exception as e:
        return f"Error retrieving website technologies: {e}"

# Main function to perform reconnaissance
def recon(domain):
    print(f"[*] Starting reconnaissance for domain: {domain}\n")
    
    # WHOIS Information
    print("[*] Fetching WHOIS Information...")
    whois_info = get_whois_info(domain)
    print(whois_info)
    
    # DNS Information
    print("\n[*] Fetching DNS Information...")
    dns_info = get_dns_info(domain)
    for record_type, records in dns_info.items():
        if isinstance(records, str):  # Error message
            print(f"{record_type} Records: {records}")
        else:
            print(f"{record_type} Records:")
            for record in records:
                print(f"  {record}")
    
    # Subdomains
    print("\n[*] Fetching Subdomains...")
    subdomains = get_subdomains(domain)
    print(subdomains)

    # Website Technologies
    print("\n[*] Fetching Website Technologies...")
    website_technologies = get_website_technologies(domain)
    print(website_technologies)
    
if __name__ == "__main__":
    domain = input("Enter the domain for reconnaissance: ")
    recon(domain)
