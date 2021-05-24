socket di importazione

#server
def  main ():
    ipPros = "192.168.0.119"
    portaPros = 7000
    mioip = "192.168.0.117"
    mioPorta = 7000
    mentre  True :
        server = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
        server . bind (( mioip , mioPorta ))
        dati , indirizzo =  server . recvfrom ( 4096 )
        print ( data . decode ())
        server . chiudere ()
        #cliente
        client = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
        cliente . sendto ( data , ( ipPros , portaPros ))
        print ( "mandato" )
        cliente . chiudere ()


if  __name__  ==  '__main__' :
    principale ()