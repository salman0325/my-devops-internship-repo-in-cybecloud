import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse

# List of domains to check
DOMAINS = ["example.com", "github.com"]

def get_ssl_expiry(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            return expiry_date

def main():
    for domain in DOMAINS:
        try:
            expiry = get_ssl_expiry(domain)
            days_left = (expiry - datetime.utcnow()).days
            print(f"{domain} expires on {expiry} ({days_left} days left)")
        except Exception as e:
            print(f"Error checking {domain}: {e}")

if __name__ == "__main__":
    main()
