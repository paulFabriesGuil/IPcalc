#! /usr/bin/python

from ipwork import *
from main import *
import math

#if verbose == True:
#    print("verbose")

def description(ip_cidr):

    cidr = ip_cidr.split("/",1)[1]
    
    WILDCARD = str(wildcard(ip_cidr))
    NETAD = str(netad(ip_cidr))
    BROADAD = str(broadad(NETAD, WILDCARD))
    MASK = cidr_to_mask(cidr)
    FHOST = str(firsthost(NETAD))
    LHOST = str(lasthost(BROADAD))

    bin_netad = ip_to_bin(NETAD).replace('.', ' ')
    bin_broadad = ip_to_bin(BROADAD).replace('.', ' ')
    bin_mask = ip_to_bin(MASK).replace('.', ' ')
    bin_fhost = ip_to_bin(FHOST).replace('.', ' ')
    bin_lhost = ip_to_bin(LHOST).replace('.', ' ')
    bin_wild = ip_to_bin(WILDCARD).replace('.', ' ')

    typeA = ["Adresse Réseau : ","Adresse Broadcast : ","Masque : ","Premier Hote : ", "Dernier Hote : ", "Wildcard : "]
    quaddot = [NETAD, BROADAD, MASK, FHOST, LHOST, WILDCARD]
    quadbin = [bin_netad, bin_broadad, bin_mask, bin_fhost, bin_lhost, bin_wild]
    print("-"*75)
    print(f"{'Rapport pour Adresse Réseau : ' +ip_cidr : ^75}")
    print("-"*75)
    
    for i in range(0, 4):
        print(f"{typeA[i] : >20}{quaddot[i] : ^20}{quadbin[i] : >35}")
        print('-'*75)
    print(f"{'Nombre Hotes : ' : >20} {str(host(ip_cidr)) : ^20}")
    print('-'*75)

    return BROADAD, NETAD, FHOST, LHOST

def byteconverter(ip):
    test2=ip.to_bytes(4, 'big')
    m = bytearray(test2)
    broad_addr=""
    for by in m:
        str_by= str(by)
        broad_addr += str_by + "."
    broad_addr = broad_addr[:-1]
    return broad_addr

# todo accepter plusieurs type d'input...
def host(ip_cidr):
    if len(ip_cidr) <= 18 and '/' in ip_cidr:
        ip_cidr = ip_cidr.split("/",1)[1]
    if len(ip_cidr) <= 15 and '.' in ip_cidr:
        ip_cidr = mask_to_cidr(ip_cidr)
    if int(ip_cidr) > 32:
        print("entrez un cidr valide : - 32")
    Host_Count = pow(2, 32- int(ip_cidr)) - 2
    return Host_Count

def netad(ip_cidr):
    ip = ip_cidr.split("/",1)[0]
    if len(ip) > 18:
        print("entrez une ip valide")
        exit()
    ip_as_a_bin_number = int(ip_to_bin_sanitize(ip), 2)
    cidr = ip_cidr.split("/",1)[1]
    cidr=(cidr_to_mask(cidr))
    mask_as_a_bin_number = int(ip_to_bin_sanitize(cidr), 2)
    #Et logique pour determiner l'adresse de réseau
    logical_and = mask_as_a_bin_number & ip_as_a_bin_number
    #conversion en octet
    net_addr = byteconverter(logical_and)
    return net_addr

def wildcard(ip_cidr):
    if len(ip_cidr) > 18:
        print("entrez une valeur valide type 192.168.1.1/18")
        exit()
    if '/' in ip_cidr:
        cidr = ip_cidr.split("/",1)[1]
    else:
        cidr = cidr
    cidr=(cidr_to_mask(cidr))
    mask_as_a_bin_number = int(ip_to_bin_sanitize(cidr), 2)
    ip_inverse = '11111111111111111111111111111111'
    f = int(ip_inverse, 2)
    g = mask_as_a_bin_number ^ f
    wilcard_addr = byteconverter(g)
    return wilcard_addr

def broadad(a, j):
    a = int(ip_to_bin_sanitize(a), 2)
    j = int(ip_to_bin_sanitize(j), 2)
    #a est net_ad / j est wildcard
    k = a | j
    broad_addr = byteconverter(k)
    return broad_addr

def firsthost(netadd):
    netadd=int(ip_to_bin_sanitize(netadd), 2)
    first_add = netadd + 1
    firsthosts = byteconverter(first_add)
    return firsthosts

def lasthost(netadd):
    netadd=int(ip_to_bin_sanitize(netadd), 2)
    last_add = netadd -1
    lasthosts =byteconverter(last_add)
    return lasthosts