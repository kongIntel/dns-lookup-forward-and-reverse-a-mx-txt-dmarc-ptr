thonimport socket
import dns.resolver

def parse_dns_records(domain):
    records = {
        "domain": domain,
        "dnsRecords": [],
        "status": "Failed"
    }
    
    try:
        # Fetching A record
        a_records = dns.resolver.resolve(domain, 'A')
        for a in a_records:
            records["dnsRecords"].append({"type": "A", "ttl": a.ttl, "address": a.to_text()})

        # Fetching MX record
        mx_records = dns.resolver.resolve(domain, 'MX')
        for mx in mx_records:
            records["dnsRecords"].append({"type": "MX", "ttl": mx.ttl, "exchange": mx.exchange.to_text(), "priority": mx.preference})

        # Fetching other record types as needed
        # Add code to fetch CNAME, TXT, NS, SOA, etc.
        
        records["status"] = "Success"
    except Exception as e:
        records["status"] = f"Failed: {str(e)}"
    
    return records