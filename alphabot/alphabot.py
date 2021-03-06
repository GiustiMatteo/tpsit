""" 
Comandi Alphabot 
"""
import RPi.GPIO as GPIO
import time

#configurazione per comandare i motori delle ruote 
class AlphaBot(object):

    def __init__(self,in1=12,in2=13,ena=6,in3=20,in4=21,enb=26):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4
        self.ENA = ena
        self.ENB = enb

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)
        GPIO.setup(self.ENA,GPIO.OUT)
        GPIO.setup(self.ENB,GPIO.OUT)
        self.forward()
        self.PWMA = GPIO.PWM(self.ENA,500)
        self.PWMB = GPIO.PWM(self.ENB,500)
        self.PWMA.start(40) #50
        self.PWMB.start(40) #50
        print("initializing Alphabot")

    def forward(self):
        
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
        print("L'alphabot sta andando avanti")

    def stop(self):
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.LOW)
        print("L'alphabot si è fermato")

    def backward(self):
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
        print("L'alphabot sta andando indietro")

    def left(self):
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
        print("L'alphabot sta girando a sinistra")

    def right(self):
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.LOW)
        print("L'alphabot sta girando a destra")
    
    #velocita' dei motori 
    def setPWMA(self,value):
        self.PWMA.ChangeDutyCycle(value)
    
    #velocita' dei motori
    def setPWMB(self,value):
        self.PWMB.ChangeDutyCycle(value)
  
        
    def setMotor(self, left, right):

        if(left is not 0):
            print("L'alphabot sta ruotando a sinistra")
        elif(right is not 0):
            print("L'alphabot sta ruotando a destra")
           
        if((right >= 0) and (right <= 100)):
            GPIO.output(self.IN1,GPIO.HIGH)
            GPIO.output(self.IN2,GPIO.LOW)
            self.PWMA.ChangeDutyCycle(right)
        elif((right < 0) and (right >= -100)):
            GPIO.output(self.IN1,GPIO.LOW)
            GPIO.output(self.IN2,GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(0 - right)

        if((left >= 0) and (left <= 100)):
            GPIO.output(self.IN3,GPIO.HIGH)
            GPIO.output(self.IN4,GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif((left < 0) and (left >= -100)):
            GPIO.output(self.IN3,GPIO.LOW)
            GPIO.output(self.IN4,GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(0 - left)