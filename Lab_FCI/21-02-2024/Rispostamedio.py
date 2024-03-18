import requests

url = ['http://www.goolge.com', 'http://www.youtube.com']
medio = []

for url in url:
    tempi = []
    for _ in range(5):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds/1000)
    medio.append(sum(tempi)/len(tempi))
    print('Tempi ', url, ': ', tempi)
    print('Media: ', medio)
    
if medio.index(0) > medio.index(1):
    print('Il sito con tempo di risposta medio minore è: ', url[1])


