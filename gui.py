#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# on commence toujours par importer le module tkinter
# ici on lui donne le surnom (alias) de tk

from tkinter import *
from tkinter import ttk
from ipwork import ip_to_bin
from network import host

def cipbin(*args):
    value = ip.get()
    bina.set(ip_to_bin(value))

def cbinip(*args):
    test1 = binar.get()
    ipa.set(bin_to_ip(test1))

def chost(*args):    
    test2 = acab.get()
    nhost.set(host(test2))

root = Tk()
root.title("ip calculator")

#definition du cadre
mainframe = ttk.Frame(root, padding="4 4 14 14")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

n = ttk.Notebook(mainframe)
n.pack(pady=10, expand=True)
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
f3 = ttk.Frame(n)
f1.pack(fill='both', expand=True)
f2.pack(fill='both', expand=True)
f3.pack(fill='both', expand=True)
n.add(f1, text='ip')
n.add(f2, text='binaire')
n.add(f3, text='hotes')

# definition du calcul de l'ip 
ip = StringVar()
ip_entry = ttk.Entry(f1, width=7, textvariable=ip)
ip_entry.grid(column=2, row=1, sticky=(W, E))
bina = StringVar()
ttk.Label(f1, textvariable=bina).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f1, text="Calculate", command=cipbin).grid(column=3, row=3, sticky=W)
ttk.Label(f1, text="ip").grid(column=3, row=1, sticky=W)
ttk.Label(f1, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(f1, text="in bin").grid(column=3, row=2, sticky=W)
for child in f1.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
ip_entry.focus()
root.bind("<Return>", cipbin)

# definition du calcul de l'ip 
binar = StringVar()
binar_entry = ttk.Entry(f2, width=7, textvariable=binar)
binar_entry.grid(column=2, row=1, sticky=(W, E))
ipa = StringVar()
ttk.Label(f2, textvariable=ipa).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f2, text="Calculate", command=cbinip).grid(column=3, row=3, sticky=W)
ttk.Label(f2, text="bin").grid(column=3, row=1, sticky=W)
ttk.Label(f2, text="is equal to").grid(column=1, row=2, sticky=E)
ttk.Label(f2, text="in 4-dotted").grid(column=3, row=2, sticky=W)
for child in f2.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
binar_entry.focus()
root.bind("<Return>", cbinip)

# definition du calcul de l'ip 
acab = StringVar()
acab_entry = ttk.Entry(f3, width=7, textvariable=acab)
acab_entry.grid(column=2, row=1, sticky=(W, E))
nhost = StringVar()
ttk.Label(f3, textvariable=nhost).grid(column=2, row=2, sticky=(W, E))
ttk.Button(f3, text="Calculate", command=chost).grid(column=3, row=3, sticky=W)
ttk.Label(f3, text="this net").grid(column=3, row=1, sticky=W)
ttk.Label(f3, text="gives you").grid(column=1, row=2, sticky=E)
ttk.Label(f3, text="hosts").grid(column=3, row=2, sticky=W)
for child in f3.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
acab_entry.focus()
root.bind("<Return>", chost)

root.mainloop()