# Proxmox Virtual Environment Hookscript Examples

In Proxmox Virtual Environment, you can call a script at specific phases of a VM's or LXC's lifecycle. 

## Proxmox VE Guest Operating Cycle Phases

hookscripts are executed at each of the four phases of the guest life cycle. 

## Hookscript Execution

When a guest has a hookscript set, the target hookscript will be called at each of the four phases. When the script is called, it is passed two arguments: the guest's VMID and the phase's name. 

For example: `hookscript.py <VMID> <PHASE>`

Values passed as a arguments indicating the phase:

- `pre-start`
- `post-start`
- `pre-stop`
- `post-stop`

Any output from the script (e.g. `echo` or `print()`) will be recorded in the systemd journal (`journalctl`).

Proxmox VE can run a variety of scripts. An example script written in Perl is provided with each installation and is located at `/usr/share/pve-docs/examples/guest-example-hookscript.pl`. There is no requirement for this script to be written in Perl.

### Pre-start Phase

When a guest is given the command to start, it is the pre-start phase, and the hookscript is called. If the script exits with a code other than zero, the start of the guest will be aborted. 

You could use this script to check whether a required service is running or another condition is met and abort the guest's start if this check fails.

### Post-start Phase

The hookscript will be called again after the Proxmox VE host determines the guest has successfully started. 

### Pre-stop Phase

If the guest is stopped with the API, the hookscript will be executed before stopping the guest. If the guest is powered off within the guest, the Proxmox VE host will not know it has received the power off command and cannot execute the hookscript. 

### Post-stop Phase

The fourth phase is after the guest has stopped, and the hookscript will be executed no matter how the guest comes to be stopped. 

## Usage

To use a hookscript:

1. Save the hookscript to any Proxmox VE storage location configured for snippets (e.g., file storage and the `snippets` folder).  
2. Mark the file as executable (e.g. `chmod +x hookscript.sh`).  
3. Configure the guest to use the hookscript using qm, pct, pvesh or API call.

Configuration example:

`qm set <vmid> --hookscript <volume-id>:snippets/<script-name>`

## Reference

[Proxmox VE Admin Guide - Hookscripts](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#_hookscripts)
