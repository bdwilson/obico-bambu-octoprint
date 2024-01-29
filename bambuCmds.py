#!/usr/bin/python3
#
#
# 1/28/2024 - initial release - https://github.com/bdwilson/obico-bambu-octoprint
#
# * Requires bambu_connect: https://github.com/mattcar15/bambu-connect
#   pip install bambu-connect
#
# Warning: there is no verification that your commands were sent. 
#
import time
from bambu_connect import BambuClient, PrinterStatus
import pprint
import os
import argparse

parser = argparse.ArgumentParser(description='Bambu Execute Client')
parser.add_argument('-c','--cmd', help='Command could be: pause, resume, stop, speed_slient, speed_normal, speed_sport, speed_ludacris, light_on, light_off', required=True)
parser.add_argument('-i','--ip', help='IP Address of Bambu Printer', required=True)
parser.add_argument('-s','--serial', help='Serial # of Bambu Printer', required=True)
parser.add_argument('-a','--access', help='Access code from your Printer menu', required=True)
args = vars(parser.parse_args())

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

# info came from: https://community.home-assistant.io/t/bambu-lab-x1-x1c-mqtt/489510/29
# https://github.com/greghesp/ha-bambulab/blob/main/custom_components/bambu_lab/pybambu/commands.py

pause = f'{{"print": {{ "sequence_id": 0, "command": "pause"}}, "user_id":"1234567890"}}'
resume = f'{{"print": {{ "sequence_id": 0, "command": "resume"}}, "user_id":"1234567890"}}'
stop = f'{{"print": {{ "sequence_id": 0, "command": "stop"}}, "user_id":"1234567890"}}'

speed_silent = f'{{"print":{{"sequence_id":"2004","command":"print_speed","param":"1"}},"user_id":"1234567890"}}'
speed_normal = f'{{"print":{{"sequence_id":"2004","command":"print_speed","param":"2"}},"user_id":"1234567890"}}'
speed_sport = f'{{"print":{{"sequence_id":"2004","command":"print_speed","param":"3"}},"user_id":"1234567890"}}'
speed_ludacris = f'{{"print": {{"sequence_id":"2004","command":"print_speed","param":"4"}},"user_id":"1234567890"}}'

# P1 and X1 the led_node = chamber_light, A1 and A1 mini led_node = # camera_light
light_on = f'{{"system": {{"sequence_id": "0", "command": "ledctrl", "led_node": "camera_light", "led_mode": "on", "led_on_time": 500, "led_off_time": 500, "loop_times": 0, "interval_time": 0}}, "user_id":"1234567890"}}'
light_off = f'{{"system": {{"sequence_id": "0", "command": "ledctrl", "led_node": "camera_light", "led_mode": "off", "led_on_time": 500, "led_off_time": 500, "loop_times": 0, "interval_time": 0}}, "user_id":"1234567890"}}'

def main():
	
	if (args['cmd'] == "pause"):
		cmd = pause
	elif (args['cmd'] == "resume"):
		cmd = resume
	elif (args['cmd'] == "stop"):
		cmd = stop
	elif (args['cmd'] == "light_on"):
		cmd = light_on
	elif (args['cmd'] == "light_off"):
		cmd = light_off
	elif (args['cmd'] == "speed_silent"):
		cmd = speed_silent
	elif (args['cmd'] == "speed_normal"):
		cmd = speed_normal
	elif (args['cmd'] == "speed_sport"):
		cmd = speed_sport
	elif (args['cmd'] == "speed_ludacris"):
		cmd = speed_ludacris
	else:
		print("Invalid argument: %s", args['cmd'])
		cmd = None

	try:
		bambu_client = BambuClient(args['ip'], args['access'], args['serial'])
	except Exception as e:
   		print("Failed to connect %s", e)
	try: 
		if (cmd is not None) and (bambu_client is not None):
			bambu_client.executeClient.send_command(cmd)
			print("Command successfully executed")
	except Exception as e:
		print("Failed to execute command: %s", e)

	bambu_client.executeClient.disconnect()

if __name__ == "__main__":
    main()

