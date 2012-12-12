#!/usr/bin/env python
import os,string,urllib,urllib2

def main():
    print "Recuperation des IPs en cours"    
    #GetIP
    f=open("IPList.txt","r")
    lIP=f.readlines()
    lIP.sort()
    #print lIP
    f.close()
    #lIP=["212.95.68.69"]
    #Check IP one by one
    # wget --header="accept: application/json" http://arte.tv/artews/services/geolocation?ip=84.154.153.58 to change heaser (json/xml)
    #javascript http://www.arte.tv/artews/js/geolocation.js

    inc=0
    for i in range(10):
        for IP in lIP:
            inc=inc+1
            IP=string.replace(IP,"\n","")
            print string.zfill(inc,0)+"/ "+IP
            opener=urllib2.build_opener()
            opener.addheaders=[('accept','application/json')] # FORMAT JSON
            #opener.addheaders=[('accept','application/xml')] # FORMAT XML 
            #os.system("wget http://degas.preprod.arte.tv/artews/services/geolocation?ip="+IP+" --output-document="+IP+".xml")

            #response=opener.open("http://arte.tv/artews/services/geolocation?ip="+IP).read()
            response=opener.open("http://degas.preprod.arte.tv/artews/services/geolocation?ip="+IP).read()
            #response=opener.open("http://degas.preprod.arte.tv/artews/services/geolocation").read()
            print response+"\n"
            opener.close()    

main()
