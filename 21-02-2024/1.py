import requests
from matplotlib import pyplot as plt

siti = ['http://www.gazzetta.it', 'http://www.netflix.com', 'http://www.facebook.com']
stili = [':', '--', '-.']
massimi = []

plt.figure() #inizializza un foglio bianco

for (url, stile) in zip(siti, stili):
    print('Analisi del sito: ', url)
    tempi = []
    for _ in range(10):
        r = requests.get(url)
        # print(r) stampa lo status del GET
        print('Tempo di Risposta: ', r.elapsed.microseconds/ 1000, 'ms')
        tempi.append(r.elapsed.microseconds/1000)
    plt.plot(tempi, label=url, linestyle=stile) #aggiunge una linea al grafico
    print('Tempo di Risposta Minimo: ', min(tempi))
    massimi.append(max(tempi))
    print('Tempo di Risposta Massimo: ', max(tempi))
    print('Tempo di Risposta Medio: ', sum(tempi)/len(tempi))

print('Tempo di Risposta Massimo Assoluto: ', max(massimi))


plt.legend() #aggiunge la legenda
plt.title('Tempo di Risposta google.com')
plt.grid() #aggiunge la griglia
plt.ylim([0, max(tempi)+100]) #imposta i limiti dell'asse y
plt.xlabel('ID Richiesta') #etichetta l'asse x
plt.ylabel('Tempo di Risposta (ms)') #etichetta l'asse y
plt.show() #mostra il grafico

