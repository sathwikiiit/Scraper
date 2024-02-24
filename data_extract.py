import requests
from bs4 import BeautifulSoup
import pandas as pd
import tqdm
#creating a fake header to avoid Forbbiden
def sa(url)->str:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    page = url
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.text, 'html.parser')
    n=pageSoup.find("a", attrs={'class': 'next-post'})
    if n != None: 
        lin = n.get("href")
        return lin

#entry = 'https://smnovels.com/novel/the-amazing-son-in-law-novel-cn5/chapter-1-10/'
#txt=[entry]
#next=entry
txt = list(pd.read_csv('ASIL.csv',index_col=0)['0'].values)
next = txt[-1]
t=int(input())

for i in tqdm.tqdm(range(t)):
    try:
        next=sa(next)
        txt.append(next)
    except:
        break
pd.Series(txt).to_csv('ASIL.csv')