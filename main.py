#!usr/bin/env python3

# Date: 25-1-18, Jan ~ 25th 2018 | Synchronocy
# Project: Discord Scraper
# I don't understand why I haven't been diagnosed with autism yet

import requests
import six
from lxml import html
from threading import Thread
from queue import Queue

class Worker(Thread):
    """
    Pooling
    """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as ex:
                pass
            finally:
                self.tasks.task_done()

class ThreadPool:
    """
    Pooling
    """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """
        Add a task to be completed by the thread pool
        """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """
        Map an array to the thread pool
        """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """
        Await completions
        """
        self.tasks.join()
        
filename = 'proxyscrape.txt'
def removedupes(inputfile, outputfile):
        lines=open(inputfile, 'r').readlines()
        lines_set = set(lines)
        out=open(outputfile, 'w')
        for line in lines_set:
                out.write(line)
        print('\nScan completed.\nRemoved any/all dupes.')
        
def scrapesocks():
    #fyi this can be changed between US, Free, SSL proxies as their site has the same layout.
    src = requests.get('https://www.socks-proxy.net/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",","")
        link = link.replace("Yes","") and link.replace("[","") and link.replace("]","")
        if not ' ' in link:
            print(link)
            with open(filename,'a') as handle:
                handle.write(link + '\n')
                handle.close()    
def scrapeus():    
    src = requests.get('https://www.us-proxy.org/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",","")
        link = link.replace("no","")
        link = link.replace("[","")
        link = link.replace("]","")
        if not ' ' in link:
            print(link)
            with open(filename,'a') as handle:
                handle.write(link + '\n')
                handle.close()                  
def scrapefree():
    src = requests.get('https://free-proxy-list.net/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",","")
        link = link.replace("no","") and link.replace("[","") and link.replace("]","")
        if not ' ' in link:
            print(link)
            with open(filename,'a') as handle:
                handle.write(link + '\n')
                handle.close() 
def scrapeuk():
    src = requests.get('https://free-proxy-list.net/uk-proxy.html')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",","")
        link = link.replace("no","") and link.replace("[","") and link.replace("]","")
        if not ' ' in link:
            print(link)
            with open(filename,'a') as handle:
                handle.write(link + '\n')
                handle.close()

def scrapeanon():
    src = requests.get('https://free-proxy-list.net/anonymous-proxy.html')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",","")
        link = link.replace("yes","") and link.replace("[","") and link.replace("]","") and link.replace("no","")
        if not ' ' in link:
            print(link)
            with open(filename,'a') as handle:
                handle.write(link + '\n')
                handle.close()

def scrapessl():
    src = requests.get('https://www.sslproxies.org/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",","")
        link = link.replace("yes","") and link.replace("[","") and link.replace("]","") and link.replace("no","")
        if not ' ' in link:
            print(link)
            with open(filename,'a') as handle:
                handle.write(link + '\n')
                handle.close()
def poolfunc():
    # Yeah yeah, I get this is bad and not even efficient but this is a learning curve :/
    pool = ThreadPool(200)
    pool.add_task(scrapesocks)
    pool.wait_completion()
    pool.add_task(scrapeus)
    pool.wait_completion()
    pool.add_task(scrapeuk)
    pool.wait_completion()
    pool.add_task(scrapeanon)
    pool.wait_completion()
    pool.add_task(scrapefree)
    pool.wait_completion()
    pool.add_task(scrapessl)
    pool.wait_completion()

def main():
    print("Now Scraping")
    poolfunc()
    print("Done!")
if __name__ == '__main__':
    main()
