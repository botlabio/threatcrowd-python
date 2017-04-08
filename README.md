# threatcrowd-python
A python wrapper for Thtreatcrowd API that returns all the outputs in pandas dataframes. 

## 1. Getting Started 

### 1.1 Get the module code to your environment

Copy https://raw.githubusercontent.com/botlabio/threatcrowd-python/master/threatcrowd.py to your local working directory (for example the directory you run Jupyter from). 

### 1.2 Receive the data object from Threatcrowd API

    import threatcrowd as tc
    
And then use: 

    o = tc.Threatcrowd('cnn.com')
    
For ip:

    o = tc.Threatcrowd('0.0.0.0','ip')
    
For email: 

    o = tc.Threatcrowd('cnn.com')

For malware: 

    o = tc.Threatcrowd('cnn.com')
    
### 1.3 Access the data in the data object 

