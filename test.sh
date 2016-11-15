#!/bin/bash
date
pwd
ls
echo $bamboo_password_1
ftp -i -n transfert.artepro.com << END_SCRIPT
quote USER aaa
quote PASS $bamboo_password_aaa
pwd
ls
quit
END_SCRIPT

