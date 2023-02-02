#! /usr/bin/python

from ipwork import *
import math

def description(ip_cidr):
    NETAD = str(netad(ip_cidr))
    WILDCARD = str(wildcard(ip_cidr))
    BROADAD = str(broadad(NETAD, WILDCARD))
    FHOST = str(firsthost(NETAD))
    LHOST = str(lasthost(BROADAD))
    print("Le nombre d'hotes du sous réseau est : "+ str(host(ip_cidr)))
    print ("l'adresse de réseau est : " + NETAD)
    print ("la Wildcard est : " + WILDCARD)
    print ("l'adresse de Broadcast est : " + BROADAD)
    print ("la première adresse est : " + FHOST)
    print ("la dernière adresse est : " + LHOST)
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

def host(ip_cidr):
    if len(ip_cidr) > 18:
        print("entrez une valeur valide type 192.168.1.1/18")
        exit()
    ip_cidr = int(ip_cidr.split("/",1)[1])
    if ip_cidr > 32:
        print("entrez un cidr valide : - 32")
    Host_Count = pow(2, 32- ip_cidr) - 2
    return Host_Count

def netad(ip_cidr):
    ip = ip_cidr.split("/",1)[0]
    if len(ip) > 18:
        print("entrez une ip valide")
        exit()
    ip_as_a_bin_number = int(ip_to_bin_sanitize(ip), 2)
    cidr = ip_cidr.split("/",1)[1]
    mask_as_a_bin_number = int(cidr_to_mask(cidr), 2)
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
    mask_as_a_bin_number = int(cidr_to_mask(cidr), 2)

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