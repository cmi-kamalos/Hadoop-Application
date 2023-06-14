#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <date key, value> input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..

#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
# San Diego Supercomputer Center copyright as problem provider
# Solved by cmi_kamalos
# --------------------------------------------------------------------------

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    #print key_in
    if  value_in.isdigit():           #check if data is a valid entry

        print( '%s\t%s' % (key_in,value_in))  #print a key, value pair
    else:   #key is only <word> so just pass it through
	if value_in == "ABC": #check if abc channel
        	print( '%s\t%s' % (key_in,value_in))  #print a string < show, chan >

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
