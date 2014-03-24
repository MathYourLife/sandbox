#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

OUTFILE="out.ogv"
STARTDELAY=2  # Seconds before start recording

WID=$(wmctrl -l | grep -i $1 | cut -f 1 -d ' ')
OUTPATH=$DIR/screen_capture/$OUTFILE
echo "************************************************************************"
echo " Screen capture of $1 to commence in $STARTDELAY seconds"
echo " File: $OUTPATH"
echo "************************************************************************"

recordmydesktop -o $OUTPATH --no-sound --delay $STARTDELAY --overwrite --windowid $WID
