import whois

domain = input("Enter a domain to lookup (e.g. example.com): ")

try:
    w = whois.whois(domain)

    print(f"\n WHOIS Lookup for: {domain}\n")
    print(f"Registrar      : {w.registrar}")
    print(f"Creation Date  : {w.creation_date}")
    print(f"Expiration Date: {w.expiration_date}")
    print(f"Name Servers   : {w.name_servers}")
    print(f"Emails         : {w.emails}")

except Exception as e:
    print(f"Error: Could not fetch WHOIS for {domain}")
    print(f"Details: {e}")
