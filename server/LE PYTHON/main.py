import network   #import des fonction lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json
from machine import Pin

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

#ssid = 'Pierro-Access-point'
#password = '123456789'
#wlan.connect(ssid, password) # connecte la raspi au réseau
#url = "http://192.168.4.3:3000/"

ssid = 'La Lumière de l\'Empereur'
password = 'photostereoisomerisation'
wlan.connect(ssid, password)
url = "http://192.168.69.133:3000/"

pinNumber = 16
led = Pin(pinNumber, mode=Pin.OUT)

while(True):
    try:
        #print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        #print(r.json()) # traite sa reponse en Json
        
        val=r.json()
        data = val["message"]
        print(data)
        
        r.close() # ferme la demande
        utime.sleep(3)
    except Exception as e:
        print(e)
    
    for i in range(int(data)):
        print(i)
        led.on()
        utime.sleep(0.3)
        led.off()
        utime.sleep(0.3)
    break
