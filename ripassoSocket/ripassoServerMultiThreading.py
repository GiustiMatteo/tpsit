socket di importazione
importare   thread

ip = "192.168.88.88"
porta = 8000

def  main ():
   s = presa . socket ( socket . AF_INET , socket . SOCK_STREAM )
   s . bind (( ip , porta ))
   listathread = []
   s . ascolta ()
   mentre  True :
    conn , addr =  s . accetta ()
    clientThread ( addr [ 0 ], addr [ 1 ], conn )
    listathread . append ( conn )


classe  clientThread ( threading . Thread ):
    def  __init__ ( self , ip , p , conn ):
        filettatura . Discussione . __init__ ( auto )
        sé . ip_address =  ip
        sé . porta = p
        sé . connessione = conn
        def  run ( self ):
            mentre  True :
                clientThread . inizio ()
                data  =  clientThread . recv ( 4096 )
                print ( data . decode ())
                clientThread . sendall ( data )
            for  i  in  clientThread :
                clientThread [ i ]. join ()



if  __name__  ==  '__main__' :
    principale ()