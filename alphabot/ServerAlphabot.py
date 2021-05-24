"" "
Server per Comandare l'Alphabot
"" "

 socket di importazione
importa  sqlite3
importare  thread
 registrazione delle importazioni

my_ip  =  "127.0.0.1"
porta  =  2512

#setto il livello di logging a debug, il più basso. In questo modo riuscirò a stampare tutti i log più in alto
registrazione . basicConfig ( livello  =  registrazione . DEBUG )
logger  =  registrazione . getLogger ()


classe  ClientThread ( threading . Thread ):
    def  __init__ ( self , server , connessione ):
        filettatura . Discussione . __init__ ( auto )
        sé . server = server
        sé . connessione = connessione

    def  run ( self ):
        while ( Vero ):
            #lettura dei dati utilizzati
            dati  =  self . connessione . recv ( 4096 )  
            richiesta  =  dati . decodifica ()
            #comunicazione dei dati del calcolo strumentale
            logger . info ( f "Abbiamo ricevuto quei dati: { data } " )
            percorso  =  elabora_Richiesta ( richiesta )
            invia_dati_alphabot ( self . server , self . connessione , percorso )
            logger . info ( f "ok, dovresti seguire questo percorso: { percorso } " )


def  crea_server ():
    global  my_ip
     porta globale

    #creazione del socket TCP IPv4
    server  =  socket . socket ( socket . AF_INET , socket . SOCK_STREAM )

    #bind del server per esporlo sulla rete
    server . bind (( my_ip , porta ))   

    #comunicazione dei dati del server utilizzato
    logger . info ( f " \ n Il server è online e pronto per funzionare \ t  { my_ip } : { porta } " )

    #attesa di una connessione
    server . ascolta ()

     server di ritorno


def  connetti_alphabot ( server ):
    prova :
        #accettazione delle eventuali connessioni
        connessione , _  =  server . accetta ()
    eccetto :
        connessione  =  Nessuno
        logger . errore ( "4.1, errore nella creazione della connessione" )

    return  connessione 

def  invia_dati_alphabot ( server , connessione , dati ):
    prova :
        dati =  dati . codificare ()
        #restituisco il risultato al client
        connessione . sendall ( data )
    eccetto :
        logger . errore ( "3.1, connessione persa" )

def  chiusura_server ( server ):
    #chiusura del socket
    server . chiudere ()
    logger . info ( f "Il server è chiuso, puoi unirti un'altra volta!" )

def  elabora_Richiesta ( richiesta ):
    prova :
        db  =  sqlite3 . connect ( 'percorsi.db' )
        cursore  =  db . cursore ()
    eccetto :
        logger . errore ( "4.1, database inesistente" )
        ritorno [ 0 ]
    
    prova :
        inizio , fine  =  richiesta . dividere ( ',' )
    eccetto :
        inizio  =  ""
        fine  =  ""
        logger . error ( "2.1, formato messaggi errato" )
    
    prova :
        print ( f'SELECT percorso FROM (inizio_fine INNER JOIN percorsi ON (inizio_fine.id_percorso = percorsi.id) INNER JOIN luoghi s ON (id_start = s.id)) INNER JOIN luoghi f ON (id_end = f.id) WHERE " { inizio } "= s.nome AND" { fine } "= f.nome ' )
        cursore . esegui ( f'SELECT percorso FROM (inizio_fine INNER JOIN percorsi ON (inizio_fine.id_percorso = percorsi.id) INNER JOIN luoghi s ON (id_start = s.id)) INNER JOIN luoghi f ON (id_end = f.id) WHERE " { inizio } "= s.nome AND" { fine } "= f.nome ' )
        percorso  =  cursore . fetchone () #altrimenti fetchall
    eccetto :
        logger . error ( "4.1, errore nell'eseguizione della query" )

    prova :
        percorso  =  f " { percorso [ 0 ] } " #trasformo in stringa il percorso
    eccetto :
        logger . error ( "1.1 - 1.2, percorso non trovato - start e end errati" )
        percorso  =  0
    
    print ( f "Questo il percorso: { percorso } " )
    db . chiudere ()
     percorso di ritorno

def  main ():
    clienti = []
    server  =  crea_server ()
    while ( 1 ):
        connessione  =  connetti_alphabot ( server )
        c  =  ClientThread ( server , connessione )
        clienti . append ( c )
        c . inizio ()

    chiusura_server ( server )

se  __name__  ==  "__main__" :
    principale ()