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
        print(totest +" est une adresse de broadcast")
        exit()
    elif nt == nn:
        print(totest +" est une adresse de réseau")
        exit()
    elif nt < nbr and nt > nn:
        print(totest +" est une adresse du réseau")
        exit()
    elif nt > nbr or nt < nn:
        print(totest +" est une adresse hors-plage")
        exit()

member('10.114.96.127/25', "10.114.95.255)