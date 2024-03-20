# Socket

## Soket API
introdotto nella BSD4.1 
Paradigma client server 

## Basi della socket
- il server deve essere in esecuzione prima che il client possa inviare dati
- il server deve avere una socket per ricevere le informazioni (DAEMON)
- Il client deve avere una socket assegnata
- il Client deve conoescere l'indirizzo IP e la Porta del processo del server

### Socket UDP
> Datagramma,  Protocollo Connectionless
- non ha handshaking
- il mittente inserisce esplicitamente l'indizzo ip della destinazione ad ogni segmente
- il OS inserice l'IP e la porta del socket di origine ad ogni segmento
- IL server legge il segmento che riceve che contiene ip e Porta del mittente
