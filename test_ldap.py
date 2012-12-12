#!/usr/bin/python
# -*- coding: utf-8 -*-
#tentative de programmation avec les classes selon le modèle de Frederic Roth.

import string
import re
import ldap


class aReport:  #La classe globale
	#Les attributs globaux de la classe.
	host=""
	login=""
	password=""

	
	def __init__ (self,host,login,password):				
		self.host=host
		self.login=login
		self.password=password
		
	def GetParams(self,debut,fin):		
		#On fait une regexp afin de pallier à tous les cas possibles (enfin je crois).
		#return re.findall ( debut+"([^"+fin+"]*)"+fin,self.data)				
		return re.findall ( debut+"(.*?)"+fin,self.data)
        		

	def GetParam(self,debut,fin):		
		#On fait une regexp afin de pallier à tous les cas possibles (enfin je crois).
		exp = re.compile ( debut+"(.*?)"+fin)
		mat = exp.search ( self.data ) 
		if (mat):
			return  mat.group(1)
		else:
			return ""
		
	def PrintData(self):
		print self.host,self.login,self.password

	def Connect(self):
		try:
			l = ldap.open(self.host)	
			l.protocol_version = ldap.VERSION3	
			# Pass in a valid username and password to get 
			# privileged directory access.
			# If you leave them as empty strings or pass an invalid value
			# you will still bind to the server but with limited privileges.	
			username = self.login
			password  = self.password
			# Any errors will throw an ldap.LDAPError exception 
			# or related exception so you can ignore the result
			l.simple_bind(username, password)
			return l
		except ldap.LDAPError, e:
			print e,"aaa"
			
	def Chercher(self,baseDN,retrieveAttributes,searchFilter):		
		## The next lines will also need to be changed to support your search requirements and directory
		#baseDN = "cn=users,dc=mail,dc=strg,dc=arte"
		searchScope = ldap.SCOPE_SUBTREE
		## retrieve all attributes - again adjust to your needs - see documentation for more options
		#retrieveAttributes = ['name'] # If None alors tous les attributs
		#searchFilter = "mDBUseDefaults=FALSE"
		#try:
		ldap_result_id = self.l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
		#print ldap_result_id
		Resultat = []
		while 1:
			result_type, result_data = self.l.result(ldap_result_id, 0)
			#print result_type,result_data
			if (result_data == []):
				break
			else:					
				if result_type == ldap.RES_SEARCH_ENTRY:
					Resultat.append(result_data)			
		#except ldap.LDAPError, e:
		#	print e,
		return Resultat
	
	
	def PrettyPrint(self):		
		#Recherche des clés
		i=1		
		for result in self.Resultat:
			print result
			print i
			result=result[0]
			titre=result[0]
			data=result[1]
			liste_cle=data.keys()
			for cle in liste_cle:
				e=data[cle][0]
				try:					
					e=e.decode('utf-8')
					e=e.encode('iso-8859-1')
				except:
					e=e				
				print cle,"=",e,"\t"
			print ""
			i=i+1
			
			
	def PrettyPrint2(self):
		llmail=[]
		i=1		
		for result in self.Resultat:
			print i,"/"
			result=result[0]			
			lmail=result[1]["memberUid"]
			print lmail
			for mail in lmail:
				llmail.append(string.strip(mail))
			"""
			
			titre=result[0]
			data=result[1]
			"""
			print ""
			i=i+1
		llmail=list(set(llmail))
		llmail.sort()
		print llmail

		
def main():
	a=[]	
	#R=aReport("rufus","CN=Administrator,CN=users,DC=mail,dc=strg,dc=arte","P¦óÇ")
	#chakra
	#R=aReport("chakra","cn=admin,dc=linux,dc=strg,dc=arte","S>Ë6ö\\")
	#R=aReport("thor","cn=Admin Exchange,cn=Users,DC=test,DC=ad2003","P¦óÇ")
	#R=aReport("badiane","cn=Admin Exchange,cn=Users,DC=mail,DC=strg,DC=arte","tera")
	R=aReport("ldap.newtech.arte.tv","cn=Manager,dc=arte,dc=tv","pan49ldapsearch") #ldapsearch -v -D "cn=Manager,dc=arte,dc=tv" -W -h ldap.newtech.arte.tv -b "ou=people,dc=arte,dc=tv " "objectclass=*"

	R.l=R.Connect()	
	#R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",['name'],"(&(mDBUseDefaults=FALSE)(name=FAX))")
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",['name','mDBUseDefaults'],"(mDBUseDefaults=FALSE)")
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",a,"(name=#Service Multimedia)")
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",['name'],'(name=*)') #Tout le monde
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",a,'(name=user test)') #Tout le monde
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",a,'(name=*)') #Tout le monde
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",a,'(&(member=*)(CN=#Présidence - Comité de Gérance))') #Tout le monde
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",['name','mailNickName'],"(memberOf=CN=\""+"\#Presidence - Comite de Gerance"+"\",CN=Users,DC=mail,DC=strg,DC=arte)") #Nom des gens du service
	#R.Resultat=R.Chercher("dc=linux,dc=strg,dc=arte",['cn'],'(&(objectClass=PosixGroup)(objectClass=sambaGroupMapping))') #Tous les groupes
	#R.Resultat=R.Chercher("dc=linux,dc=strg,dc=arte",['memberUid'],'(cn=Service informatique)') #Tous les users du groupes
	#R.Resultat=R.Chercher("dc=linux,dc=strg,dc=arte",a,'(cn=Files)') #Tous les users du groupes
	#R.Resultat=R.Chercher("ou=ArteSecurityGroup,dc=test,dc=ad2003",['name'],'(name=*)') #Tout le monde de l'ou artesecuritygroup
	#R.Resultat=R.Chercher("ou=ArteSecurityGroup,dc=test,dc=ad2003",['name','arteServiceId'],'(arteServiceId=16)') #artenumber id et cn pour le groupe arteserviceid 21
	
	R.Resultat=R.Chercher("ou=groups,dc=arte,dc=tv",['memberUid'],'(cn=confluence*)') #les mails des gens du groupe confluence*
	R.PrettyPrint2()
	
	
	#R.Resultat=R.Chercher("cn=users,dc=mail,dc=strg,dc=arte",['cn'],'(objectclass=group)') #Tout le monde
	#R.PrettyPrint()
	
main ()
