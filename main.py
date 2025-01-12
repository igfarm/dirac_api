from dirac import DiracLiveProcessor

base_url = "http://192.168.86.42:5006/api"  # Replace with the actual base URL of your Dirac Live Processor API

processor = DiracLiveProcessor(base_url)
print(processor.get_slots())