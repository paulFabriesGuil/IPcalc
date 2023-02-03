#! /bin/python

import getopt
import sys

class bin_to_ip:
    
    def process(binaire):
        decompo_bin = binaire.split('.')
        ip = []
        str_ip = ""
        occurence = 0

        for terme in decompo_bin:
            valeur_octet = 0
            exposant = 7
            for bit in list(terme):
                int_bit = int(bit)
                valeur_bit = int_bit*(2**exposant)
                valeur_octet += valeur_bit
                exposant -= 1
            ip.append(valeur_octet)
        
        for lterme in ip:
            occurence += 1
            for x in str(lterme):
                str_ip +=str(x)
            if occurence < 4:
                str_ip = str_ip+"."
            else:
                str_ip = str_ip
        
        return str_ip

class cidr:

    def masque_cidr(binaire_masque):

        liste_binaire_masque = list(binaire_masque)
        lbmc = liste_binaire_masque.count("1")

        return lbmc
    
    def cidr_masque(cidr):
        cidr=int(cidr)
        str_bin_cidr = ""
        compteur=32
        str_binaire_masque = ""

        while cidr != 0:
            str_bin_cidr += "1"
            cidr -= 1

        while len(str_bin_cidr) < 32:
            str_bin_cidr += "0"

        for bit in str_bin_cidr:
            str_binaire_masque += bit
            compteur-=1
            if compteur == 24:
                str_binaire_masque += '.'
            elif compteur == 16:
                str_binaire_masque += '.'
            elif compteur == 8:
                str_binaire_masque += '.'

        return str_binaire_masque

class ip_to_bin: 

    def process(ip):
        decompo_ip = ip.split('.')
        ip_bin = []
        str_ip = ""
        occurence = 0

        for terme in decompo_ip: 
            iterme = int(terme)
            octet = [0,0,0,0,0,0,0,0]
            index=7

            while iterme != 0:
                modulo=iterme%2
                octet.pop(index)
                octet.insert(index,modulo)
                iterme=iterme//2
                index=index-1
            ip_bin.append(octet)

        for loctet in ip_bin:
            occurence+=1
            for bit in loctet:
                str_ip+=str(bit)
            if occurence < 4:
                str_ip=str_ip+"."
            else:
                strp_ip=str_ip

        return str_ip


def adresse_reseau():
    binaire_ip = list(conversion.ip_to_bin(ip_network))
    binaire_masque = list(conversion.cidr_masque(cidr))
    adresse_reseau = []
    compteur = 0

    while compteur < 35:
        if binaire_ip[compteur]=='1' and binaire_masque[compteur] == "1":
            adresse_reseau.append("1")
        elif binaire_ip[compteur]=='.' and binaire_masque[compteur] == ".":
            adresse_reseau.append('.')
        else:
            adresse_reseau.append('0')
        compteur += 1

    str_adresse_resal = "" 
    for bit in adresse_reseau:
        str_adresse_resal = str_adresse_resal+bit         
    return str_adresse_resal



version = '1.0'
verbose = False
output_filename = 'default.out'

print('ARGV      :', sys.argv[1:]) 
options, remainder = getopt.getopt(sys.argv[1:], 'o:v', ['output=', 'verbose','version=',])
print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print('VERSION   :', version)
print('VERBOSE   :', verbose)
print('OUTPUT    :', output_filename)
print('REMAINING :', remainder)

#rand_bin = input('place ton binaire ici : ')
#print(bin_to_ip.process(rand_bin))
#
#fix_bin = '11111111.11111111.11111111.11111111'
#print(bin_to_ip.process(fix_bin))
#
#print(cidr.masque_cidr(rand_bin))
#print(cidr.masque_cidr(fix_bin))
#
#rand_ip = input('entrez votre ip ici : ')
#print(ip_to_bin.process(rand_ip))
#
#fix_ip = '255.255.255.255'
#print(cidr.masque_cidr(ip_to_bin.process(fix_ip)))