import requests

siti = ['http://www.goolge.com', 'http://www.youtube.com', 'http://www.polimi.it', 'http://www.wikipedia.org', 'http://www.amazon.com', 'http://www.twitter.com']
medio = []

for url in siti:
    tempi = []
    for _ in range(10):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds / 1000)
    medio.append(sum(tempi) / len(tempi))
    print('Tempi ', url, ': ', tempi)
    print('Media: ', medio)

print('\nIl sito con tempo di risposta medio minore è: ', siti[medio.index(min(medio))])

