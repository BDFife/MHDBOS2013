# Collector

"Collector" project for Music Hack Day Boston 2013

## Goals

Collector reads in an iTunes XML file and extracts out the albums in a
user's library. 

The album titles (strings from the XML) are matched against a range of
filters that identify albums missing from your collection of favorite
artists, and helps identify other interesting characteristics of your
collection and guide your next purchases. 

iTunes file parsing seems to run quite slow (~5-10s) for large iTunes
files... but this seems to be a limitation of the plist parser and as 
such, not easily addressable. 

## Out Of Scope

For this weekend hack, we are not attempting to match the albums
identfied in the iTunes XML to unique IDs from MusicBrainz, EchoNest
or Rovi.

Matching like this would make the system more robust in general and
make automated creation of the filters easier.

## Reminder Notes

To restart the server, remember to use the command:
   'sudo reload collector'
