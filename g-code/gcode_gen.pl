#!/usr/bin/perl
# Generate some fake gcode to last a certain amount of time 
# in order to trick obico into doing spagetti detection on
# a non-Octoprint/non-Klipper printer. 
#
# run this script with a single argument as # of minutes 
# ./gcode_gen.pl 60 > 1hr.gcode
# 
$mins = $ARGV[0];
$secs = $mins * 60;
$period = $secs / 100;
$elapsed = 0;
#print ";Virtual Gcode for $i minutes\n";
print ";FLAVOR:Marlin\n";
print ";TIME $secs\n";
print ";LAYER_COUNT:100\n";
print ";LAYER:0\n";
print "M117 INDICATOR-Layer0\n";
$count = 0;
for ($j=1;$j<=$secs;$j++) {
	if (($j % $period)==0) {
		$elapsed=$period + $elapsed;
		$count++;
		print "G4 S" . $period . "\n";
		#print "; $j $period\n";
		print ";TIME_ELAPSED:$elapsed\n";
		print ";LAYER:$count\n";
		print "M117 INDICATOR-Layer" . $count . "\n";
	}
}
print "; BEGIN DISPLAYLAYERPROGRESS SETTINGS\n;DisplayLayerProgress_layerIndicatorProcessed = true\n ;END DISPLAYLAYERPROGRESS SETTINGS\n";
		
