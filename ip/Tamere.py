#! /usr/bin/python3
import socket
import math
import struct

ip = "179.158.225.110"
mask = "255.255.240.0"
ip_inverse = '11111111111111111111111111111111'


def ip_to_bin (ip) :
    
    ip_split = ip.split(".")
    ip_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip_split[0]),int(ip_split[1]),int(ip_split[2]),int(ip_split[3])))
    print(ip_bin)
    return ip_bin

def bin_to_ip (binar) :

    bin_split = binar.split(".")
    bin_ip = ('{0}.{1}.{2}.{3}'.format(int(bin_split[0],2),int(bin_split[1],2),int(bin_split[2],2),int(bin_split[3],2)))
    return bin_ip

def mask_to_bin (mask) :
    
    mask_split = mask.split(".")
    mask_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(mask_split[0]),int(mask_split[1]),int(mask_split[2]),int(mask_split[3])))
    return mask_bin

def cidr () :

    CIDR = mask_to_bin(mask).count("1")
    return CIDR

def hosts_quant() :

    Host_Count = pow(2, mask_to_bin(mask).count("0")) - 2
    return Host_Count

def bin_and (a, b):
    a = int(a, 2)
    b = int(b, 2)
    c = b & a
    d = c.to_bytes(4,'big')
    e = bytearray(d)

    net_addr=""
    for by in e:
        str_by= str(by)
        net_addr += str_by + "." 

    net_addr = net_addr[:-1]
    return net_addr

op_maskbin = (mask_to_bin(mask).replace('.',''))
op_ipbin = (ip_to_bin(ip).replace('.',''))

def bin_or (b , f):    
    f = int(f, 2)
    b = int(b, 2)
    g = b ^ f
    h = g.to_bytes(4, 'big')
    i = bytearray(h)

    broad_addr=""
    for by in i:
        str_by= str(by)
        broad_addr += str_by + "." 

    broad_addr = broad_addr[:-1]
    return broad_addr

def cidr_to_mask (cidr) :
    cidr = 32 - int(cidr)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << cidr)))
    return netmask

print(bin_and(op_ipbin, op_maskbin) + '/' + str(cidr()))

netad = ip_to_bin(bin_and(op_ipbin, op_maskbin)).replace('.', '')
broadad = ip_to_bin(bin_or(op_maskbin, ip_inverse)).replace('.', '')
print(bin_or(broadad, netad))

print(socket.inet_ntoa(socket.inet_aton("179.158.225.110")))
print(cidr_to_mask("20"))