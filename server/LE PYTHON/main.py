import network   #import des fonction lier au wifi
import urequests    #import des fonction lier au requetes http
import utime    #import des fonction lier au temps
import ujson    #import des fonction lier aà la convertion en Json
from machine import Pin
from neopixel import Neopixel

pix = 64
strip = Neopixel(pix, 0, 1, "RGB")
delay= 0.5
strip.brightness(5)
blue=(0,0,255)
white=(255,255,255)
red=(0,255,0)
green=(255,0,0)
black=(0,0,0)
yellow=(255,255,0)


def France():
    strip.set_pixel(0+8*i, blue)
    strip.set_pixel(1+8*i, blue)
    strip.set_pixel(2+8*i, white)
    strip.set_pixel(3+8*i, white)
    strip.set_pixel(4+8*i, white)
    strip.set_pixel(5+8*i, white)
    strip.set_pixel(6+8*i, red)
    strip.set_pixel(7+8*i, red)
    
def Italie():
    strip.set_pixel(0+8*i, green)
    strip.set_pixel(1+8*i, green)
    strip.set_pixel(2+8*i, white)
    strip.set_pixel(3+8*i, white)
    strip.set_pixel(4+8*i, white)
    strip.set_pixel(5+8*i, white)
    strip.set_pixel(6+8*i, red)
    strip.set_pixel(7+8*i, red)

def Espagne():
    strip.set_pixel(0+8*i, red)
    strip.set_pixel(1+8*i, red)
    strip.set_pixel(2+8*i, yellow)
    strip.set_pixel(3+8*i, yellow)
    strip.set_pixel(4+8*i, yellow)
    strip.set_pixel(5+8*i, yellow)
    strip.set_pixel(6+8*i, red)
    strip.set_pixel(7+8*i, red)

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
url2 = "http://192.168.69.133:3000/flag"

pinNumber = 15
led = Pin(pinNumber, mode=Pin.OUT)

i=0
while(True):
    try:
        #print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        #print(r.json()) # traite sa reponse en Json
        
        val=r.json()
        data = val["message"]["number"]
        print(data)
        
        r.close() # ferme la demande
        utime.sleep(3)
        
        for i in range(int(data)):
            print(i)
            led.on()
            utime.sleep(0.3)
            led.off()
            utime.sleep(0.3)
    except Exception as e:
        print(e)
    
    print('suivant')
    
    try:
        
        for i in range(8):
            France()
        
        strip.show()
        utime.sleep(1)
        '''
        r = urequests.get(url2)
        val=r.json()
        data = val["message"]
        print(data["pays"])
        
        r.close() # ferme la demande
        utime.sleep(0.1)
        '''
    except Exception as e:
        print(e)