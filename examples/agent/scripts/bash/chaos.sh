#!/bin/bash

############################################################
# Chaos Injection Script for Systemd Services
#
# Description:
#     This script introduces chaos into a specified systemd service by either:
#     1. Introducing network latency for the traffic originating from the service's process.
#     2. Manipulating the service process using signals or restart commands (e.g., SIGSTOP, SIGKILL).
#
# Usage:
#     1. Modify the `AVIS_SERVICE_NAME` variable to the name of your systemd service.
#     2. Modify the `MODBUS_SERVER_SERVICE_NAME` variable to the name of your modbus server service.
#     2. Modify the `AVIS_HOST` variable to the hostname of your AVIS server.
#     3. Run the script: `sudo ./chaos.sh`.
#     4. The script will keep running, introducing chaos at random intervals until stopped.
#
# Prerequisites:
#     - Root privileges for manipulating network configurations and sending signals to the systemd service.
#
############################################################


AVIS_SERVICE_NAME="avis_agent.service"
MODBUS_SERVER_SERVICE_NAME="modbus_server.service"
AVIS_HOST="avis.vu.engineering"

SERVICES=( "$AVIS_SERVICE_NAME" "$MODBUS_SERVER_SERVICE_NAME" )


network_chaos() {
    # max 2 minute
    SLEEP_DURATION=$(( ( RANDOM % 120 )  + 1 ))
    echo "Blocking network traffic to $AVIS_HOST for $SLEEP_DURATION seconds..."

    # Resolve the domain to IP
    IPs=$(dig +short $AVIS_HOST)

    for ip in $IPs; do
        # Add a rule to block OUTPUT (outgoing) traffic to the specific IP
        iptables -A OUTPUT -d "$ip" -j DROP
    done

    sleep $SLEEP_DURATION

    # Remove the blocking rule
    for ip in $IPs; do
        iptables -D OUTPUT -d "$ip" -j DROP
    done
}

process_chaos() {
    # randomly select a chaos action
    CHAOS_ACTION=$(( RANDOM % 3 ))  # 0: SIGSTOP, 1: SIGKILL, 2: Restart

    # decide if chaos is applied to one or both services
    TARGET_CHOICE=$(( RANDOM % 3 ))  # 0: AVIS, 1: Modbus, 2: Both

    TARGETS=()  # Services to be affected
    if [[ $TARGET_CHOICE -eq 0 ]]; then
        TARGETS=("$AVIS_SERVICE_NAME")
    elif [[ $TARGET_CHOICE -eq 1 ]]; then
        TARGETS=("$MODBUS_SERVER_SERVICE_NAME")
    else
        TARGETS=("$AVIS_SERVICE_NAME" "$MODBUS_SERVER_SERVICE_NAME")
    fi

    for SERVICE in "${TARGETS[@]}"; do
        case $CHAOS_ACTION in
            0)
                echo "Sending SIGSTOP to $SERVICE..."
                sudo systemctl kill --signal=SIGSTOP "$SERVICE"
                ;;
            1)
                echo "Sending SIGKILL to $SERVICE..."
                sudo systemctl kill --signal=SIGKILL "$SERVICE"
                ;;
            2)
                echo "Restarting $SERVICE..."
                sudo systemctl restart "$SERVICE"
                ;;
        esac
    done

    # if the action was SIGSTOP, we need to send a SIGCONT after a delay
    if [[ $CHAOS_ACTION -eq 0 ]]; then
        sleep $(( ( RANDOM % 10 ) + 1 ))
        for SERVICE in "${TARGETS[@]}"; do
            echo "Sending SIGCONT to $SERVICE..."
            sudo systemctl kill --signal=SIGCONT "$SERVICE"
        done
    fi
}


for service in "${SERVICES[@]}"; do
    # Check if the service exists
    if ! [ "$(systemctl list-unit-files "$service" | wc -l)" -gt 3 ];then
      echo "$service service does not exist. Exiting..."
      exit 1
    fi
done

# Main loop for chaos
while true; do
        case $(( RANDOM % 3 )) in
        0)
            network_chaos
            ;;
        1)
            process_chaos
            ;;
        2)
            echo "Introducing both network and process chaos..."
            network_chaos &  # run in background
            process_chaos
            wait   # we wait for the background process (network_chaos) to complete before moving to the sleep section
            ;;
    esac

    # Sleep for a random interval before introducing the next chaos. Max 20 minutes.
    SLEEP_DURATION=$(( ( RANDOM % 1200 )  + 1 ))
    echo "Sleeping for $SLEEP_DURATION seconds before next chaos..."
    sleep $SLEEP_DURATION
done
