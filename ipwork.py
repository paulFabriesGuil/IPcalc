#! /usr/bin/python

import math

def ip_to_bin(zer):

    ip_split = zer.split(".")
    ip_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip_split[0]),int(ip_split[1]),int(ip_split[2]),int(ip_split[3])))
    return ip_bin

def ip_to_bin_sanitize(ip):

    ip_bin = str(ip_to_bin(ip))
    op_ipbin = ip_bin.replace('.','')
    return op_ipbin

def bin_to_ip(bina):
    bin_split = bina.split(".")
    bin_ip = ('{0}.{1}.{2}.{3}'.format(int(bin_split[0],2),int(bin_split[1],2),int(bin_split[2],2),int(bin_split[3],2)))
    return bin_ip

def mask_to_cidr(mask):
    if len(mask) <= 15 : #is_ipformat
        mask = ip_to_bin(mask)
    CIDR = mask.count("1")
    return CIDR

def cidr_to_mask(cidr):
    cidr=int(cidr)
    #right=32-cidr
    if cidr > 32:
        print("Entrez un CIDR valide")
        exit()
    first_part='1'*cidr
    second_part='0'*(32-cidr) #right
    mask_bin = first_part+second_part
    mask_bin = '.'.join([str(mask_bin)[i:i+8] for i in range(0, len(str(mask_bin)), 8)])
    mask = bin_to_ip(mask_bin)
    return mask
