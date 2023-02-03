#! /usr/bin/python3

ip = input('entrez votre ip : ')
masque = input('entrez votre masque : ')

def binaire(ip):
    # Décomposition de l'ip en termes séparés par un point, Output est une liste comprenant chaque terme
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

def bin(masque):
     # Décomposition de l'ip en termes séparés par un point, Output est une liste comprenant chaque terme
    masque_decompo = masque.split('.')
    masque_binaire = []
    str_masque=""
    occurence=0
    
    for terme in masque_decompo:  #Boucle for pour traiter chaque terme à part
        iterme = int(terme) #conversion des termes en integer pour traitement math
        octet = [0,0,0,0,0,0,0,0]
        index=7
        
        while iterme != 0:
            modulo=iterme%2
            octet.pop(index)
            octet.insert(index,modulo)
            iterme=iterme//2
            index=index-1
        masque_binaire.append(octet)
        
    for loctet in masque_binaire:
        occurence+=1
        for bit in loctet:
            str_masque+=str(bit)
        if occurence < 4:
            str_masque=str_masque+"."
        else:
            str_masque=str_masque

    return str_masque

           
print(binaire(ip))
print(bin(masque))
print('votre ip est : ', ip)
print('votre masque est : ', masque)