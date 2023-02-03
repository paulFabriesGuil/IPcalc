#! /usr/bin/env python3

import sys
import ipaddress
import math

#ip_host = input("entrez votre ip : ")
#mask_adress = input("entrez votre masque : ")

ip_cidr = input("entrez votre ip/cidr : ")
ip_network, separator, cidr = ip_cidr.partition('/')

class conversion:
    ip = ""
    ip_host = ip
    ip_network = ip

    def bin_to_ip(traitement):
        bin_decompo = str(traitement()).split('.')
        ip_masque = []
        str_masque = ""
        occurence = 0

        for terme in bin_decompo:
            valeur_octet=0
            exposant = 7
            for bit in list(terme):
                int_bit=int(bit)
                valeur_bit = int_bit*(2**exposant)
                valeur_octet += valeur_bit
                exposant -= 1
            ip_masque.append(valeur_octet)
        
        for lterme in ip_masque:
            occurence+=1
            for x in str(lterme):
                str_masque+=str(x)
            if occurence < 4:
                str_masque=str_masque+"."
            else:
                str_masque=str_masque      

        return str_masque

    def masque_cidr(mask_adress):
        mask_decompo = mask_adress.split('.')
        mask_bin = []
        str_mask = ""
        occurence = 0

        for terme in mask_decompo:
            iterme=int(terme)
            octet = [0,0,0,0,0,0,0,0]
            index=7

            while iterme != 0:
                modulo = iterme%2
                octet.pop(index)
                octet.insert(index,modulo)
                iterme = iterme//2
                index = index-1
            mask_bin.append(octet)

        for loctet in mask_bin:
            occurence += 1
            for bit in loctet:
                str_mask += str(bit)
            if occurence < 4:
                str_mask = str_mask+'.'
            else:
                strp_mask = str_mask 

        liste_binaire_masque = list(str_mask)
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

    def ip_to_bin(ip):
        ip_decompo = ip.split('.')
        ip_binaire = []
        str_ip=""
        occurence=0

        for terme in ip_decompo:  #Boucle for pour traiter chaque terme à part
            iterme = int(terme) #conversion des termes en integer pour traitement math
            octet = [0,0,0,0,0,0,0,0]
            index=7

            while iterme != 0:
                modulo=iterme%2
                octet.pop(index)
                octet.insert(index,modulo)
                iterme=iterme//2
                index=index-1
            ip_binaire.append(octet)

        for loctet in ip_binaire:
            occurence+=1
            for bit in loctet:
                str_ip+=str(bit)
            if occurence < 4:
                str_ip=str_ip+"."
            else:
                strp_ip=str_ip

        return str_ip

def traitement(): 
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

def nombre_ip_dispo():
    return print('le nombre d\'ip disponible sur la plage est de :', pow(2, 32-int(cidr))-2)

print('l\'ip de votre réseau est :', conversion.bin_to_ip(traitement))
print('l\'ip de votre masque est :', conversion.cidr_masque(cidr))
nombre_ip_dispo()