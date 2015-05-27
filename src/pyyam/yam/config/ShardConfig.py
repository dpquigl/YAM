from ConfigParser import SafeConfigParser
from yam.exceptions import ShardConfigException

class ShardConfig(object):
    '''
    Tool configuration file format. The format uses the SafeConfigParser ini format. 
    
    Definition:
    
    [General]
    '''

    def reload(self):
        '''Do any cleanup needed and just call load again'''
        self.load(self.configFileName)
        pass
    
    def load(self, filename):
        config = SafeConfigParser()
        config.read(filename)
                    
        if config.has_section("General") is False:
            raise ShardConfigException("Configuration must contain a General section")
        self.type = config.get("General", "TransportType")
        self.address = config.get("General", "Address")
        self.port = config.get("General", "Port")
        self.resource = config.get("General", "Resource")
            
        self.configFileName = filename
        pass
    def __init__(self, filename=None):
        '''
        Constructor
        '''
        if filename:
            self.load(filename)
        pass