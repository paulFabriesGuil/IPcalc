#! /usr/bin/pyhton

from ipwork import *
from network import *
from sanitizer import *
import getopt, sys

def main(argv):
    # Define the possible options and arguments
    short_options = "hi:b:c:m:d:"
    long_options = ["help", "ip-to-bin", "bin-to-ip"]

    try:
        # Get the options and arguments from the command line
        opts, args = getopt.getopt(argv, short_options, long_options)
    except getopt.GetoptError:
        # If the options are not correctly formatted, print an error message and exit
        print(help())
        sys.exit(2)

    # Define default values for the options
    #global verbose == False

    # Process the options and arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit()
        elif opt in ("-i", "--ip-to-bin"):
            if isIP(arg) is True:
                print(ip_to_bin(arg))
        elif opt in ("-b", "--bin-to-ip"):
            print(bin_to_ip(arg))
        elif opt in ("-c"):
            if isMask(arg) is True:
                print(mask_to_cidr(arg))
        elif opt in ("-m"):
            if isCIDR(arg) is True:
                print(cidr_to_mask(arg))
        elif opt in ("-d"):
            if isNet(arg) is True:
                description(arg)

def help():
    help = "help"
    return help

if __name__ == "__main__":
    main(sys.argv[1:])