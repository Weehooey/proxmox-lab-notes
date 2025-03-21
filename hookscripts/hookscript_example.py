#!/usr/bin/env python3

"""
A Python version of 'guest-example-hookscript.pl' hookscript from Proxmox VE.

"""

import sys

def main(vmid, phase):
    """ Main entry point. """
    
    print(f"GUEST HOOK: VMID={vmid} PHASE={phase}")

    if phase == "pre-start":
        print(f"{vmid} is starting, doing preparations.")

        # Uncomment the following two lines to simulate a failure:
        # print("Preparations failed, aborting.")
        # sys.exit(1)

    elif phase == "post-start":
        print(f"{vmid} started successfully.")

    elif phase == "pre-stop":
        print(f"{vmid} will be stopped.")

    elif phase == "post-stop":
        print(f"{vmid} stopped. Doing cleanup.")

    else:
        print(f"Unknown phase: {phase}")
        sys.exit(1)

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Usage: hookscript_example.py <vmid> <phase>")
        sys.exit(1)

    vmid = sys.argv[1]
    phase = sys.argv[2]

    main(vmid=vmid, phase=phase)
