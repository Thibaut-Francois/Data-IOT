import network   #import des fonction lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json
from machine import Pin

pinNumber = 17
pinNumber2 = 18 
led_green = Pin(pinNumber, mode=Pin.OUT)
led_blue = Pin(pinNumber2, mode=Pin.OUT)
pinNumber3 = 19 
led_red = Pin(pinNumber3, mode=Pin.OUT)

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

'''
ssid = 'Pierro-Access-point'
password = '123456789'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://192.168.4.3:3000/data"
'''

ssid = 'La Lumière de l\'Empereur'
password = 'photostereoisomerisation'
wlan.connect(ssid, password)
url = "http://192.168.69.133:3000/"

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        #print(r.json()) # traite sa reponse en Json
        
        val=r.json()
        
        blue=val["message"]["blue"]
        red=val["message"]["red"]
        green=val["message"]["green"]
        
        print(blue)
        '''
        blue = 0
        red =0
        green=0
        '''
        
        led_green.on()
        led_blue.on()
        led_red.on()
        utime.sleep(0.1)
        led_blue.off()
        led_green.off()
        led_red.off()
    
        
        
        '''
        print(red)
        print(green)
        '''
        
        r.close()  #ferme la demande
        
    except Exception as e:
        print(e)
