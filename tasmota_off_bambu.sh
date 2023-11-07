#!/bin/sh
# replace the IP address with the IP of your tasmota 
# outlet that your printer is plugged into.
curl -s http://192.168.1.61/cm?cmnd=Power%200
echo "Printer stopped"
