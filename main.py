#!/usr/bin/python3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
from sys import stderr,argv
from time import sleep
base_url = 'pastebin.com'
def pBinFetch(times):
    how_many = 0
    links_ = set()
    #starting from zero we avoid the exclusive counting way of range
    for i in range(0,times):
        data = urlopen('http://www.pastebin.com')
        soup = bs4(data)
        top = soup.find('ul',{'class' : 'right_menu'})
        links = top.find_all('a')
        for link in links:
            links_.add(base_url+link.get('href'))
        if i != times-1:#control if it's the last run
            #delay on stderr in case of output redirection
            print('Falling asleep for just 5 seconds', file=stderr)
            sleep(5)
    print("Report for ", len(links_) , file=stderr)
    for link in links_:
        print(link)

if __name__ == '__main__':
    if argv[1:]:
        pBinFetch(int(argv[1]))
    else:
        pBinFetch(2)

