#!/usr/bin/python
# -*- coding: latin-1 -*-
#BUT : 
#    rapidement créer une base des règles du FW sous MySQL
#Auteur :
#    <guillaume.renard@arte.tv>
#
"""
		INSERT into utlrs VALUES ('SAPPROD','SAPPROD',' ',' ','172.25.4.47','00:02:a5:c8:9e:5f','sapprod',' ',TO_DATE('2005-11-24 15:55:47','YYYY-MM-DD HH24:MI:SS'),'Compaq Computer Corporation')
		select sysdate from dual  # Pour voir le format que donne Oracle
"""


import  os,pprint, sys, socket, string, MySQLdb, re

#MySQL



def getparam (data,deb,fin):
    """
        renvoie la 1ere sous chaine de data comprise entre deb et fin (deb et fin exclus)
        si data ne contient pas deb, renvoie ''
        si data ne contient pas fin, renvoie ''
    """
    import string

    start=string.find(data,deb)
    if start==-1:
        return ""
    start+=len(deb)
    end=string.find(data,fin,start)
    if end==-1:
        return""
    return data[start:end]

def getparams (data,deb,fin):
    """
        renvoie la liste des sous chaine
        de data comprise entre deb et fin (deb et fin exclus)
    """
    import string
    res=[]
    a=getparam(data,deb,fin)
    while a!="":
        res.append(a)
        data=data[string.find(data,deb)+1:]
        a=getparam(data,deb,fin)
    return res
    

def TestOracle():
	req="select * from toto"
	o.execute(req)	
	res=o.fetchall()
	for elt in res:	
		print elt

def RecupBaseMysql():
	listeBase=[]
	print "## Liste des différentes bases"
	req="show databases"
	m.execute(req)
	res=m.fetchall()
	for elt in res:		
		listeBase.append(elt[0])			
	return listeBase
	
def RecupTableMysql(base):
	listeTable=[]
	print "---- Liste des différentes tables de "+base
	req="use "+base
	m.execute(req)
	req="show tables"
	m.execute(req)
	res=m.fetchall()
	for elt in res:		
		listeTable.append(elt[0])			
	return listeTable

def RecupChampsMysql(base,table):
	listeChamps=[]
	print "-------- Liste des différents champs de "+base+"."+table
	req="use "+base
	m.execute(req)
	req="desc "+table
	m.execute(req)
	res=m.fetchall()
	for elt in res:
		listeChamps.append(elt)
	return listeChamps
	
		
def main():
	connectionObject = MySQLdb.connect(host='localhost', user='guillaume', passwd='guillaume',db='test') 
	c = connectionObject.cursor() 
	os.system("clear") # Pas très propre mais affichage plus lisible
	print c
	for source in (2,24,28,14,16,8):
	    source=string.zfill(source,0)
	    req="INSERT INTO rule (id, rule_id, source, destination, service) VALUES (NULL, 48, "+source+", 40, 2)"
	    print req
	    a=c.execute(req)
	    print a
	connectionObject.commit()

	"""
	# print all the first cell of all the rows
	req="select * from object"
	c.execute(req)
	for row in c.fetchall() :
	    print row[0],row[1]
	"""
	c.close()	
main()

