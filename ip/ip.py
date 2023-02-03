#! /usr/bin/python3

import math

ip = "10.114.96.25"
ip_split = ip.split(".")
ip_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip_split[0]),int(ip_split[1]),int(ip_split[2]),int(ip_split[3])))
print(ip_bin)

op_ipbin = (ip_bin.replace('.',''))
#print(op_ipbin) 

bina = ip_bin
bin_split = bina.split(".")
bin_ip = ('{0}.{1}.{2}.{3}'.format(int(bin_split[0],2),int(bin_split[1],2),int(bin_split[2],2),int(bin_split[3],2)))
#print(bin_ip)

mask = "255.255.128.0"
mask_split = mask.split(".")
mask_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(mask_split[0]),int(mask_split[1]),int(mask_split[2]),int(mask_split[3])))
print(mask_bin)

op_maskbin = (mask_bin.replace('.',''))
#print(op_maskbin) 

CIDR = mask_bin.count("1")
#print(CIDR)

Host_Count = pow(2, mask_bin.count("0")) - 2
#print(Host_Count)

a = int(op_ipbin, 2)
#print(a)
b = int(op_maskbin, 2)
#print(b)
c = b & a
#print(c)
d = c.to_bytes(4,'big')
#print(d)
e = bytearray(d)
#print(e)

net_addr=""
for by in e:
    str_by= str(by)
    net_addr += str_by + "." 
    
net_addr = net_addr[:-1]
#print(net_addr)

ip_inverse = '11111111111111111111111111111111'
f = int(ip_inverse, 2)
g = b ^ f
h = g.to_bytes(4, 'big')
i = bytearray(h)

broad_addr=""
for by in i:
    str_by= str(by)
    broad_addr += str_by + "." 
    
broad_addr = broad_addr[:-1]
#print(broad_addr)
print('------------------------------------------------')

ip = str(net_addr)
print(ip)
ip_split = ip.split(".")
print(ip_split)
ip_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip_split[0]),int(ip_split[1]),int(ip_split[2]),int(ip_split[3])))
print(ip_bin)
op_ipbin = (ip_bin.replace('.',''))
a = int(op_ipbin, 2)
print(a)
print('------------------------------------------------')
ip = str(broad_addr)
print(ip)
ip_split = ip.split(".")
print(ip_split)
ip_bin = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip_split[0]),int(ip_split[1]),int(ip_split[2]),int(ip_split[3])))
print(ip_bin)
op_ipbin = (ip_bin.replace('.',''))
j = int(op_ipbin, 2)
print(j)
k = a | j
print(k)
l = k.to_bytes(4, 'big')
m = bytearray(l)
print(m)

print('------------------------------------------------')

broad_addr=""
for by in m:
    str_by= str(by)
    broad_addr += str_by + "." 
    
broad_addr = broad_addr[:-1]
print(broad_addr)