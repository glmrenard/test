#!/usr/bin/python
# -*- coding: utf-8 -*-


import ldap

LDAP_ADDR = 'devinci.arte.tv'
LDAP_CONFIG = 'uid=%s,ou=people,dc=arte,dc=tv'

def checkPassword(username, password):
   server = LDAP_ADDR
   l = ldap.open(server)   
   if password == "":
       password = "wrong"
   try:
       l.simple_bind_s(LDAP_CONFIG % username, password)
   except:
       return False
   return True

def main():
    res=checkPassword("chef2@arte.tv","chef2")
    print "==>", res
    
main()

  
