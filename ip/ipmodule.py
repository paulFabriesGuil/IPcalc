#! /usr/bin/python3

import ipaddress

monip = input('entrez votre ip : ')
ipa = ipaddress.ip_address(monip)

print(type(ipa))
print(ipa.is_global)
print(ipa.is_private)