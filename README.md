# obico-bambu-octoprint

This document & associated files describe a process to allow use of Obico
failure detection to work with any non-Octprint/non-Klipper printer (i.e. your
Bambu printers). Please continue reading for
the requirements to make this work. I am using an [Arducam
USB](https://amzn.to/40smRYU) camera with [this
mount](https://makerworld.com/en/models/59194) on my Bambu A1 Mini.  


# Requirements
1) Working Octoprint installation with Obico plugin. You need a camera that is
designed to work with Octoprint (and Obico) natively (i.e. running on a Pi or other
hardware - not virtualized). For my use case, I'm using a USB-connected Arducam.
2) SSH to your pi and install [bambu-connect](https://github.com/mattcar15/bambu-connect) python
module on your Pi. <pre>pip install bambu-connect</pre>
3) Grab my script <pre> cd ~/
wget https://raw.githubusercontent.com/bdwilson/obico-bambu-octoprint/main/bambuCmds.py
chmod 755 bambuCmds.py
</pre><b>You will also need to know the IP address of your Bambu printer, Serial # and Device Access Code</b> to use this script. In the examples below that call bambuCmds.py, you will need to substitute your IP, Serial and access code.  
4) Obico account that supports streaming (you may be able to use the self-hosted option; I have not tried this). 
5) The .gcode files in the gcode directory. You can also make your own gcode
files using the attached script. These files need to be uploaded to your
Obico-files location within the Obico App (or website).
6) A supported messaging app (via Octoslack). I use Pushover. 

# Setup
1) Install Octoprint and plugins (Obico, OctoSlack, Virtual Printer).  
2) Make sure Webcam works. 
3) Enable Virtual Printer plugin and create a dummy printer; change the port to
Virtual
4) Setup OctoSlack for whatever notification platform you use. 
   * Enable Snapshot hosting
   * Enable Print Started; enable System Command and put <pre>/home/pi/bambuCmds.py -i 192.168.1.XX -s 0309CA392XXXXX -a 34235435 -c light_off</pre> (optional - I prefer the IR lighting on the Arducamand the light from the Bambu seems to wash this out).
   * Enable Print Paused; enable System Command and put <pre>/home/pi/bambuCmds.py -i 192.168.1.XX -s 0309CA392XXXXX -a 34235435 -c pause</pre>
   * Enable Print Resumed; enable System Command and put <pre>/home/pi/bambuCmds.py -i 192.168.1.XX -s 0309CA392XXXXX -a 34235435 -c resume</pre>
   * Enable Print Cancelling (only need to do this if your cancelled prints don't immediately cancel); enable System Command and put <pre>/home/pi/bambuCmds.py -i 192.168.1.XX -s 0309CA392XXXXX -a 34235435 -c stop && sudo service octoprint restart</pre>This restarts octoprint if you cancel your print.  In my initial testing, cancelling took forever and restarting octoprint was the best option I've found to get it cancelled quickly. It seems OK now without this setting using the latest gcodes. 
   * Enable Progress and setup whatever progress % you prefer.
5) Generate or use the pre-generated g-code files from the repository and
upload them to the Obico App or website.
6) Mount your camera somewhere where it can do valid spagetti detection. If you
have a Bambu A1 Mini, I created a camera mount for it
[here](https://makerworld.com/en/models/59194). 

# Usage
1) Start the print on your Bambu
2) Start associated gcode via Obico app which is close as possible to how long
your print will take. 
3) ... Profit.

If you enable detection in Obico, and your printer pauses, it should trigger the Bambu
printer to pause, resume will resume and cancel should cancel! 

<img src="https://bdwilson.github.io/images/IMG_4911.jpeg" width=400px>

# Known Issues
* If you get Serial Timeout errors, you may have to edit this file on your Pi:
<code>/home/pi/oprint/lib/python3.9/site-packages/octoprint/plugins/virtual_printer/virtual.py</code>
and change the following lines. 
<code>
         read_timeout=150.0,
        write_timeout=150.0,
</code>
You will also have to do this upon each Octoprint update unless the issue gets
fixed. (tracked here: [Octoprint issue 4907](https://github.com/OctoPrint/OctoPrint/issues/4907)


# Credits
* Thanks to Pr0Pain on the Obico Discord for the idea and initial g-codes.
