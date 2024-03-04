import requests 
from bs4 import BeautifulSoup 
    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://www.flipkart.com/canon-eos-r10-mirrorless-camera-body-rf-s-18-150-mm-f-3-5-6-3-stm-lens-kit/p/itmd3e8ee6e3f328") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.select_one('.CXW8mj _3nMexc'):
    print(item['src'])
