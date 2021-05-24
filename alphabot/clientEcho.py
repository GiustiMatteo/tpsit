"" "
Client ECHO TCP
"" "
 socket di importazione

ip_server  =  "127.0.0.1"
porta_server  =  4000

#creazione del socket TCP IPv4
client  =  socket . socket ( socket . AF_INET , socket . SOCK_STREAM )

#connessione al server
cliente . connetti (( ip_server , porta_server ))

while ( Vero ):
    #richiesta del messaggio
    messaggio  =  input ( "messaggio:" )

    #invio dei dati al server
    cliente . sendall ( messaggio . encode ())
    
    #controllo del comando di chiusura
    se ( messaggio  ==  "close ()" ):
        rompere

    #leggo il risultato
    risultato  =  client . recv ( 4096 )

    #comunicazione risultato
    print ( "risultato:"  +  risultato . decode ())

#chiusura del socket
cliente . chiudere ()