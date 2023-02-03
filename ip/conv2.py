#! /usr/bin/python3

binaire_masque = input('entrez votre binaire ici : ')
cidr = int(input('entrez votre cidr ici : '))

def conv_bin_ip(binaire_masque):
    bin_decompo = binaire_masque.split('.')
    ip_masque = []
    str_masque = ""
    occurence = 0

    for terme in bin_decompo:
        liste_terme=list(terme)
        valeur_octet=0
        exposant = 7
        
        for bit in terme:
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
            strp_masque=str_masque

    return str_masque

def cidr_masque(cidr):
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

print(conv_bin_ip(binaire_masque))
print(type(cidr_masque(cidr)))