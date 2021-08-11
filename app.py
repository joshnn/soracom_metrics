from dotenv import load_dotenv

load_dotenv() 

class SoracomMeasure:
    TARGET_WEBSITE = os.getenv('TARGET_WEBSITE')
    TARGET_DOWNLOAD = os.getenv('TARGET_DOWNLOAD')
    
    def __init__(self, host):
        self.host = host
    
    def measure_ping(self):
        """
        calculate settings
        """
        