#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright as problem provider
#  Resolution performed by cmi_kamalos 
# --------------------------------------------------------------------------

prev_word          = ""                #initialize previous word  to blank string
curr_show          = ""
abc_found=False
dico= {}
# see https://docs.python.org/2/tutorial/datastructures.html for list details

list_curr_show     = []
total=0

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list   

    #note: for simple debugging use print statements, ie:  
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
#-----------------------------------------------------
    # Check if its a new word and not the first line 
    #   (b/c for the first line the previous word is not applicable)
    #----------------------------------------------------
   
    if curr_word != prev_word:
       # -----------------------     
	#now write out the join result, but not for the first line input
        # -----------------------
        if prev_word:
	    dico[prev_word]=total
	    total=0  #now reset our total count while curr can change
       	prev_word         =curr_word
    else:
	    if value_in == "ABC":
	  
            #print("{0}\t{1}".format(value_in, running_total))
	      abc_found = True
	      curr_show = curr_word #if abc is tested then save elt as a current_show
	    
	    #print("{0}\t{1}".format(value_in,curr_word))
	    if value_in.isdigit():
                abc_found= False
		value=int(value_in)
		total += value
   	      #set up previous word for the next set of input lines
    # ---------------------------------------------------------------
    #whether or not the join result was written out, 
    #   now process the curr word    
  
    # ---------------------------------------------------------------
 
    if abc_found: #test if abc is found then insert to list of shows
 	if any(x == curr_show for x in list_curr_show):
	  pass
	else:
	  list_curr_show.append(curr_show)
    
# ---------------------------------------------------------------
#now write out the LAST join result
# ---------------------------------------------------------------

for item in list_curr_show:  #loop through the list of shows in <show, abc > 
        print('{} {}'.format(item,dico[item])) #get result from the dictionary
	
