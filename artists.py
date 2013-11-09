#!/usr/bin/python

# python test of reading iTunes xml file on OS X or Windows
# Glenn Axelrod 2013-11-05

# Usage: 
#  If executed with no arguments, reads the local system's iTunes file.
#  If there is an argument, it should contain the path to an iTunes 
#  file on the current system.

import plistlib # read xml formatted plist file (iTunes)
import re       # for regular expressions
import sys      # for error info
import json

# Substitution for user environment variable for /Users/<name>
from os.path import expanduser
home = expanduser("~")

debug = True

# Need to determine current system to build path to iTunes Library file # (only runs on Mac OS and Windows) (Not tested on Windows yet.)
import platform
os = platform.system() 

if len(sys.argv) < 2:
    if re.search("Darwin", os):
        # if debug: print "os is Darwin. Home is " + home
        # No need for shell-type escape for spaces in path or name
        xml_file = home + '/Music/iTunes/iTunes Music Library.xml'
    elif re.search("Windows", os):
        release = platform.release()
        if re.search('XP', release):
            xml_file = home + '\My Documents\My Music\iTunes\iTunes Library.xml'
        else:
            # Windows Vista, 7, & 8
            xml_file = home + '\Music\iTunes\iTunes Library.xml'
    else:
        if debug: print "Sorry, but this program uses iTunes data which we don't think is available on this " + os + " system"
else:
    xml_file = sys.argv[1]

# Protection from undecodable utf-8 in plists is from
# http://stackoverflow.com/questions/18275020/
#   python-2-7-2-plistlib-with-itunes-xml
# More than that, an ASCII conversion / cleanup is needed because titles 
# from the web may contain strange 
# characters. My own iTunes library includes a couple that cause 
# trouble, for example a solid arrow symbol here (faked 
# with '>'.
# > Boston Python October 29 - Helper Languages - YouTube
# http://stackoverflow.com/questions/4299675/
#   python-script-to-convert-from-utf-8-to-ascii

def safe_unicode(s):
    if isinstance(s, unicode):
        udata=s.decode("utf-8", errors='ignore')
        asciidata=udata.encode('ascii','xmlcharrefreplace')
        return asciidata
    else:
        return s

#def set_up_dict ():


try:
   xml = plistlib.readPlist(xml_file)    
except IOError:
   if debug: print 'Problem opening ' + os + ' iTunes file ' + xml_file

try:
   artists_file = open('artists_data.json', 'w')
except IOError:
   if debug: print 'Problem opening artists_data.json'

source_data = {}
#source_names = ['track_artist', 'track_name', 'track_album']

unicode_errors = 0

# For each entry in the iTunes library, extract the artist-> album-> 
# track data, and build a dictionary "music" with cascading dicts.


music = {}

# The try loop catches unconvertable char problems such as multibyte 
# languages and symbols.
 
for track in xml['Tracks']:
    try:
		info = xml['Tracks'][track]
		# if debug: print "Info = " + info['Name']

		track_artist = safe_unicode(info['Album Artist'])
		if debug: print "Artist = " + track_artist

		track_name = safe_unicode(info['Name'])
		if debug: print "Track = " + track_name

		track_album = safe_unicode(info['Album'])
		if debug: print "Album = " + track_album

		if track_artist in music: 
			if track_album in music[track_artist]:
				music[track_artist][track_album].append(track_name)
			else:
				# this case should never get exercised
				music[track_artist][track_album] = [track_name]
		else:
			music[track_artist] = { track_album:[track_name] }
    except UnicodeError:
        if debug: print "Couldn't convert a character in a track name " + info['Name']
        unicode_errors += 1

    except KeyError:
        if debug: print "Couldn't find data for track " + source_data['track_name'] if 'track_name' in source_data else ''

print music 

json.dump(music, artists_file, indent=4)
 
artists_file.close()
 
if debug: print "Unicode conversion failures: ", unicode_errors

