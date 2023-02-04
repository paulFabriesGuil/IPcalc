#! /usr/bin/python

from network import *
from ipwork import *
def member(network,totest):
    values = description(network)
    br_ad, n_ad, f_host, l_host = values

    nbr = int(ip_to_bin_sanitize(br_ad), 2)
    nn = int(ip_to_bin_sanitize(n_ad), 2)
    nf = int(ip_to_bin_sanitize(f_host), 2)
    nl = int(ip_to_bin_sanitize(l_host), 2)
    nt = int(ip_to_bin_sanitize(totest), 2)

    print('-----------------------------------------------')

    if nt == nbr:
        print("\033[0;33m" +totest + " est une adresse de broadcast\033[0m")
        exit()
    elif nt == nn:
        print("\033[0;33m" +totest + "est une adresse de réseau\033[0m")
        exit()
    elif nt < nbr and nt > nn:
        print("\033[0;32m"+totest +" est une adresse du réseau\033[0m")
        exit()
    elif nt > nbr or nt < nn:
        print("\033[0;31m"+ totest +" est une adresse hors-plage\033[0m")
        exit()

member('192.168.1.1/24', "192.168.10.25")