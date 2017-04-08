# threatcrowd-python
A python wrapper for Thtreatcrowd API that returns all the outputs in pandas dataframes. 

## 1. Getting Started 

### 1.1 Get the module code to your environment

Copy https://raw.githubusercontent.com/botlabio/threatcrowd-python/master/threatcrowd.py to your local working directory (for example the directory you run Jupyter from). 

    import threatcrowd as tc

### 1.2 Receive the data object from Threatcrowd API
    
There are four different modes; domain, ip, email, antivirus. The domain mode is on by default.
    
#### 1.2.1 domain: 

    o = tc.Threatcrowd('cnn.com')
    
#### 1.2.1 ip: 

    o = tc.Threatcrowd('0.0.0.0','ip')
    
#### 1.2.1 email: 

    o = tc.Threatcrowd('john@doe.com','email)

#### 1.2.1 antivirus: 

    o = tc.Threatcrowd('some hash or antivirus name','antivirus')
    
    
### 1.3 Access the data in the data object 

