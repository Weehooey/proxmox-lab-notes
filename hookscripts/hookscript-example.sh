#!/bin/bash

# A Bash version of 'guest-example-hookscript.pl' hookscript from Proxmox VE.

VMID=$1
PHASE=$2

echo "GUEST HOOK: VMID=$VMID PHASE=$PHASE"

case "$PHASE" in
  pre-start)

    echo "$VMID is starting, doing preparations."

    # Uncomment the following two lines to simulate a failure:
    # echo "Preparations failed, aborting."
    # exit 1
    ;;

  post-start)
    echo "$VMID started successfully."
    ;;

  pre-stop)
    echo "$VMID will be stopped."
    ;;

  post-stop)
    echo "$VMID stopped. Doing cleanup."
    ;;

  *)
    echo "Unknown phase: $PHASE"
    exit 1
    ;;
esac

exit 0
