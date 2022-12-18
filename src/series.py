import requests
from bs4 import BeautifulSoup
from requests.api import head

class Series:
    
    def series(self, id):
        series={}
        
        series['id'] = id
        URL = "https://www.vlr.gg/series/" + id
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        header = soup.find_all('div', class_='event-header')[0]
        series['title'] = header.find_all('div', class_='wf-title')[0].get_text().strip()
        series['subtitle'] = header.find_all('div', class_='wf-title')[0].find_next_siblings('div')[0].get_text().strip()
        
        events = []
        completedEvents = soup.find_all('div', class_='events-container-col')[1].find_all('a', class_='event-item')
        
        for card in completedEvents:
            event = {}
            event['id'] = card['href'].split('/')[2]
            #event['title'] = card.find_all('div', class_='event-item-title')[0].get_text().strip()
            #event['status'] = card.find_all('span', class_='event-item-desc-item-status')[0].get_text().strip()
            #event['prize'] = card.find_all('div', class_='mod-prize')[0].get_text().strip().replace('\t','').split('\n')[0]
            #event['dates'] = card.find_all('div', class_='mod-dates')[0].get_text().strip().replace('\t','').split('\n')[0]
            #event['location'] = card.find_all('div', class_='mod-location')[0].find_all('i', class_='flag')[0].get('class')[1].replace('mod-', '')
            #img = card.find_all('div', class_='event-item-thumb')[0].find('img')['src']
            #if img == '/img/vlr/tmp/vlr.png':
            #    img = "https://vlr.gg" + img
            #else:
            #    img = "https:" + img
            #event['img'] = img
            events.append(event)
        
        series["numEvents"] = len(events)
        series["events"] = events
        
        return series;