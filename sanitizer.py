#! /usr/bin/python

import ipaddress

def isCIDR(cidr):

    try: 
        int(cidr)
        return True
    except ValueError:
        print("Entrez un CIDR valide")
        return False

    if int(cidr) > 32:
        print("Entrez un CIDR valide")
        return False
    return 


def isIP(addr):
    try :
        ipaddress.IPv4Address(addr)
        return True
    except ipaddress.AddressValueError:
        print("Entrez une IPv4 valide")
        return False
    return 

def isMask(mask):

    try :
        ipaddress.IPv4Address(mask)
    except ipaddress.AddressValueError:
        print("Entrez un masque IPv4 valide")
        return False
    
    mask_list = ['128.0.0.0', '192.0.0.0', '224.0.0.0', '240.0.0.0', '248.0.0.0', '252.0.0.0', '254.0.0.0', '255.0.0.0', '255.128.0.0', '255.192.0.0', '255.224.0.0', '255.240.0.0', '255.248.0.0', '255.252.0.0', '255.254.0.0', '255.255.0.0', '255.255.128.0', '255.255.192.0', '255.255.224.0', '255.255.240.0', '255.255.248.0', '255.255.252.0', '255.255.254.0', '255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240', '255.255.255.248', '255.255.255.252', '255.255.255.254', '255.255.255.255']

    if mask not in mask_list:
        print("Entrez un masque valide")
        return False
    else:
        return True
    return 
    
def isNet(net):
    if '/' not in net:
        print("entrez une adresse de réseau valide : 192.168.1.0/24")
        return False
    
    ip_block = net.split("/",1)[0]
    cidr_block = net.split("/",1)[1]

    if isIP(ip_block) is True and isCIDR(cidr_block) is True:
        return True
    else:
        print("entrez une adresse de réseau valide : 192.168.1.0/24")
        return False