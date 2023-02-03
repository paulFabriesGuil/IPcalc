#! /usr/bin/env python3

binai=str(input('entrez votre bin : '))


def compteur(binai):
    lb = list(binai)
    return lb
#print(compteur(binai))

def comparateur_binaire():
    binaire_ip = "11000000.10101000.00000001.00000000"
    lb_ip = list(binaire_ip)
    lb_masque = compteur(binai)
    address_net = []
    incrementeur=0  

    while incrementeur < 35:

        if lb_ip[incrementeur] and lb_ip[incrementeur] == "1":
            address_net.append('1')
        elif lb_ip[incrementeur] and lb_ip[incrementeur] == '.':
            address_net.append('.')
        else:
            address_net.append('0')
        incrementeur += 1

    print('binaire ip : ', lb_ip)
    print('binaire masque : ', lb_masque)
    print('binaire adresse réseau : ', address_net)

comparateur_binaire()
