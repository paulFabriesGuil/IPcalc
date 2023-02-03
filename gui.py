#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from ipwork import *
from network import host

def cipbin(*args):
    value = ip.get()
    bina.set(ip_to_bin(value))

def cbinip(*args):
    test1 = binar.get()
    ipa.set(bin_to_ip(test1))

def chost(*args):    
    test2 = netadr.get()
    nhost.set(host(test2))

def ccidr(*args):
    value = incidr.get()
    maskout.set(cidr_to_mask(value))

def cmask(*args):
    value = inmask.get()
    cidrout.set(mask_to_cidr(value))

root = Tk()
root.title("ip calculator")

#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

n = ttk.Notebook(root, width=600, height=150)
n.pack(pady=10, expand=1)
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
f3 = ttk.Frame(n)
f4 = ttk.Frame(n)
f5 = ttk.Frame(n)
f1.pack(fill='both', expand=1)
f2.pack(fill='both', expand=1)
f3.pack(fill='both', expand=1)
f4.pack(fill='both', expand=1)
f5.pack(fill='both', expand=1)
n.add(f1, text='ip')
n.add(f2, text='binaire')
n.add(f3, text='hotes')
n.add(f4, text='Cidr')
n.add(f5, text='masques')

# definition du calcul de l'ip 
ip = StringVar()
ip_entry = ttk.Entry(f1, width=15, textvariable=ip)
ip_entry.grid(column=2, row=1, sticky=(W, E))
bina = StringVar()
ttk.Label(f1, textvariable=bina).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f1, text="convert", command=cipbin).grid(column=2, row=3, sticky=W)
ttk.Label(f1, text="Entrez votre ip").grid(column=1, row=1, sticky=W)
ttk.Label(f1, text="Résultat").grid(column=1, row=2, sticky=E)
root.bind("<Return>", cipbin)

# definition du calcul de l'ip 
binar = StringVar()
binar_entry = ttk.Entry(f2, width=35, textvariable=binar)
binar_entry.grid(column=2, row=1, sticky=(W, E))
ipa = StringVar()
ttk.Label(f2, textvariable=ipa).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f2, text="Convert", command=cbinip).grid(column=2, row=3, sticky=W)
ttk.Label(f2, text="Entrez votre binaire").grid(column=1, row=1, sticky=W)
ttk.Label(f2, text="Résultat").grid(column=1, row=2, sticky=E)
root.bind("<Return>", cbinip)

# definition du calcul de l'ip 
netadr = StringVar()
netadr_entry = ttk.Entry(f3, width=18, textvariable=netadr)
netadr_entry.grid(column=2, row=1, sticky=(W, E))
nhost = StringVar()
ttk.Label(f3, textvariable=nhost).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f3, text="Calculate", command=chost).grid(column=2, row=3, sticky=W)
ttk.Label(f3, text="entrez votre adresse réseau: ").grid(column=1, row=1, sticky=W)
ttk.Label(f3, text="gives you").grid(column=1, row=2, sticky=E)
root.bind("<Return>", chost)

incidr = StringVar()
incidr_entry = ttk.Entry(f4, width=18, textvariable=incidr)
incidr_entry.grid(column=2, row=1, sticky=(W, E))
maskout = StringVar()
ttk.Label(f4, textvariable=maskout).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f4, text="Calculate", command=ccidr).grid(column=2, row=3, sticky=W)
ttk.Label(f4, text="entrez votre cidr: ").grid(column=1, row=1, sticky=W)
ttk.Label(f4, text="gives you").grid(column=1, row=2, sticky=E)
root.bind("<Return>", ccidr)

inmask = StringVar()
inmask_entry = ttk.Entry(f5, width=18, textvariable=inmask)
inmask_entry.grid(column=2, row=1, sticky=(W, E))
cidrout = StringVar()
ttk.Label(f5, textvariable=cidrout).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f5, text="Calculate", command=cmask).grid(column=2, row=3, sticky=W)
ttk.Label(f5, text="entrez votre masque réseau: ").grid(column=1, row=1, sticky=W)
ttk.Label(f5, text="gives you").grid(column=1, row=2, sticky=E)
root.bind("<Return>", cmask)

root.mainloop()