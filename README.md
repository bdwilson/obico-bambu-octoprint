# obico-bambu-octoprint

This document & associated files describe a process to allow use of Obico
failure detection to work with any non-Octprint/non-Klipper printer (i.e. your
Bambu printers). Please continue reading for
the requirements to make this work.


# Requirements
1) Working Octoprint installation with Obico plugin. You need a camera that is
designed to work with Octoprint (and Obico) natively (i.e. running on a Pi or other
hardware - not virtualized). For my use case, I'm using a USB-connected
Arducam. 
2) If you want the ability to "pause" the printer if there are issues, then you
need an outlet that supports Tasmota (or can be turned on/off via a URL or
command issued from Octoprint). Pause is accomplished by turning the printer
off and back on (resume) and exploits Bambu's ability to do power outage
recovery. You should test this. 
3) Obico account that supports streaming. 
4) The .gcode files in the gcode directory. You can also make your own gcode
files using the attached script. These files need to be uploaded to your
Obico-files location within the Obico App (or website).
5) A supported messaging app (via Octoslack). I use Pushover. 

# Setup
1) Install Octoprint and plugins (Obico, OctoSlack, Virtual Printer,
PrintTimeGenius).  
2) Make sure Webcam works. 
3) Enable Virtual Printer plugin and create a dummy printer; change the port to
Virtual
4) Setup OctoSlack for whatever notification platform you use. 
   * Enable Snapshot hosting
   * Enable Print Paused (if you have a tasmota outlet); enable System Command and put <pre>sh /home/pi/scripts/tasmota_off_bambu.sh</pre>. You will need to create this file using info below.
   * Enable Print Resumed (if you have a tasmota outlet); enable System Command and put <pre>sh /home/pi/scripts/tasmota_on_bambu.sh</pre>. You will need to create this file using info below.
   * Enable Progress and setup whatever progress % you prefer.
5) Create the on and off scripts if you have a tasmota plug. 
   * Contents should mimic the examples in this repo, but you should replace the IP address with the IP address of your outlet. 
6) Generate or use the pre-generated g-code files from the repository and
upload them to the Obico App or website.
7) Mount your camera somewhere where it can do valid spagetti detection. 

# Usage
1) Start the print on your Bambu
2) Start associated gcode via Obico app which is close as possible to how long
your print will take. 
3) ... Profit.

If you enable detection, and your printer pauses, it should trigger the power
to turn off on your printer.  You will have to fix the issue then hit resume
and it *should* come back. 

<img src="https://bdwilson.github.io/images/IMG_4911.jpeg" width=400px>

# Credits
* Thanks to Pr0Pain on the Obico Discord for the idea and initial g-codes.
