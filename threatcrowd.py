import json
import requests
import pandas as pd

class Threatcrowd:
    
    '''
    EXAMPLE USE: o = Threatcrowd('cnn.com')
                 dfs = o.run()
                 dfs[1]
    
    MODES:       email, antivirus, ip, domain
    '''
    
    def __init__(self,value,mode='domain'):
        
        self.url = 'http://www.threatcrowd.org/searchApi/v2/' + mode +'/report/'
        self.value = value
        self.mode = mode
        self.result = self._request()
        self.json = json.loads(self.result.text)
        
    def _request(self):

        out = requests.get(self.url,{self.mode : self.value})
        
        return out
    
    def _ip(self):
        
        self.resolutions = pd.DataFrame(self.json['resolutions']).sort_values('last_resolved',ascending=False)
        self.hashes = pd.DataFrame(self.json['hashes'])
        self.hashes.columns = ['hash']
        
        return self.resolutions,self.hashes
        
    def _domain(self):
        
        self.resolutions = pd.DataFrame(self.json['resolutions']).sort_values('last_resolved',ascending=False)
        self.hashes = pd.DataFrame(self.json['hashes'])
        self.hashes.columns = ['hash']
        self.subdomains = pd.DataFrame(self.json['subdomains'])
        self.subdomains.columns = ['subdomain']
        
        return self.resolutions,self.hashes,self.subdomains
        
    def _email(self):
        
        self.domains = pd.DataFrame(self.json['domains'])
        self.domains.columns = ['domain']
        
        return self.domains
        
    def _hash(self):
        
        self.hashes = pd.DataFrame(self.json['hashes'])
        self.hashes.columns = ['hash']
        
        return self.hashes
        
    def run(self):
        
        '''
        NOTE:     This may yield more than one pandas dataframe object
                  and in many cases that's exactly what happens.
              
        EXAMPLE:  If you search for domain or IP you'll get more than one
                  dataframe in out so use:
                  
                  o = Threatcrowd('cnn.com')
                  a,b = o.run()
                  
                  ...and get the result in two dataframes. 
        '''
        
        if self.mode == 'ip':
            out = self._ip()
            print "you get 2 dataframes"
        if self.mode == 'domain':
            out = self._domain()
            print "you get 3 dataframes"
        if self.mode == 'email':
            out = self._email()
            print "you get 1 dataframe"
        if self.mode == 'antivirus':
            out = self._hash()
            print "you get 1 dataframe"
            
        return out
