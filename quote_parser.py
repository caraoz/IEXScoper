import os
import config
from IEXTools import Parser, messages

'''
Processes raw TOPS PCAP files and prints QuoteUpdate messages.
'''

def get_pcap_filepath(filename: str) -> str:
    """Returns the full path of a PCAP file by appending the filename to PCAP_FOLDER."""
    return os.path.abspath(os.path.join(config.PCAP_FOLDER, filename))

def iter_quote_updates(parser):
    """Iterates over QuoteUpdate messages in the PCAP file."""
    allowed = [messages.QuoteUpdate]
    while True:
        msg = parser.get_next_message(allowed)
        if msg is None:
            break
        yield msg

if __name__ == "__main__":
    pcap_file_name = get_pcap_filepath("20241231_IEXTP1_TOPS1.6.pcap.gz")
    print(f"Processing PCAP file: {pcap_file_name}")
    
    p = Parser(pcap_file_name)
    
    for quote in iter_quote_updates(p):
        print(quote)
