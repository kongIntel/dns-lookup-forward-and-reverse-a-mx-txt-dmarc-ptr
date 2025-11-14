thonimport json
import logging
from src.extractors.dns_parser import parse_dns_records
from src.outputs.exporter import export_results

def main():
    try:
        with open('data/inputs.sample.json', 'r') as file:
            domains = json.load(file)
        
        results = []
        for domain in domains:
            record = parse_dns_records(domain)
            results.append(record)

        export_results(results)
        logging.info("DNS Lookup complete")
    
    except Exception as e:
        logging.error(f"Error during DNS Lookup: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()