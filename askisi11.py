#Ασκηση 11
from urllib.request import Request, urlopen
from scipy.stats import entropy
import pandas as pd

#Βρισκω τον γύρο
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
round = urlopen(req).read()
round=str(round)
round=round.split(",")
round=round[0]
round=round.replace('''b'{"round":''','''''')
round=int(round)

values=[]
for i in range(20):
    which= round-i #i γυροι πριν τον τελευταιο γυρο
    which=str(which)
    req2 = Request('https://drand.cloudflare.com/public/'+which, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    value = urlopen(req2).read()
    value=str(value)
    value=value.split(",")
    value=value[1]
    value=value.replace('''"randomness":"''','''''')
    value=value.replace('"','')
    value=int(value, 16)
    hexvalue=hex(value)#μετετρεψα την τιμή σε δεκαεξαδικό
    values.append(hexvalue)
#υπολογίζω την εντροπία
pd_series = pd.Series(values)
counts = pd_series.value_counts()
entropy = entropy(counts)

print(entropy)
