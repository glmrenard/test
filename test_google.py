#!/usr/bin/python
# -*- coding: utf-8 -*-
# test gdata

import string
import gdata.docs.service
import gdata.spreadsheet.service
import getpass
import csv
import tempfile
import os

#Download a spreadsheet from Google Docs using Python

def get_spreadsheet(key, gid=0):
  gd_client = gdata.docs.service.DocsService()
  gd_client.email = 'guillaume.renard@gmail.com'
  gd_client.password = 'atled1gma2' #getpass.getpass()
  gd_client.ssl = True
  gd_client.source = "My Fancy Spreadsheet Downloader"
  gd_client.ProgrammaticLogin()
  
  spreadsheets_client = gdata.spreadsheet.service.SpreadsheetsService()
  spreadsheets_client.email = gd_client.email
  spreadsheets_client.password = gd_client.password
  spreadsheets_client.source = "My Fancy Spreadsheet Downloader"
  spreadsheets_client.ProgrammaticLogin()

  file_path = tempfile.mktemp(suffix='.csv')
  #uri = 'http://docs.google.com/feeds/documents/private/full/%s' % key
  uri = 'https://docs.google.com/spreadsheet/ccc?key=0AlFiwrTtlZQDdDVGQmZIbm5jU0xzWlRBRGFjZXJaUmc#gid=0'
  try:
    entry = gd_client.GetDocumentListEntry(uri)

    # XXXX - The following dies with RequestError "Unauthorized"
    gd_client.Download(entry, file_path)

    return get_csv(file_path)
  finally:
    try:
      os.remove(file_path)
    except OSError:
      pass

		
def main():
	print "Hey google guy"
	a=get_spreadsheet('0AlFiwrTtlZQDdDVGQmZIbm5jU0xzWlRBRGFjZXJaUmc')
	print a
	
	
main ()


