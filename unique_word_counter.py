# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:21:31 2017

@author: David Holdaway

find words that are only used once in a text file
ignore list of common words in "ignore_list.txt"
"""

from collections import Counter
from string import punctuation

try:
    with open('ignore_list.txt') as f:
        delete_list = f.readlines()
# remove whitespace characters like `\n` at the end of each line
        delete_list = [x.strip() for x in delete_list] 
        #print(delete_list)         
except:   #if ignore list is not found then just use a default set
    print('file:ignore_list.txt not found, using default list')
    delete_list = ["The","And","He","She","It","Is","A","By","This","With","Was","Have","We","that","had"]        

print "please enter the filename of the text file you wish to analyse"
file_to_read = raw_input("> ")

# use counter to count words
with open(file_to_read) as input_file:
    word_counts = Counter(word.strip(punctuation) for line in input_file for word in line.split())
    
    print("enter 'full' to see full word count or anything else to see words used once")
    lg_val = raw_input("> ")
    
    if lg_val == 'full':
        full_list = word_counts
        #print(type(full_list))
    else:
        full_list = [word for (word, count) in word_counts.iteritems() if count==1]      
                     # remove banned words from the list
        def string_set(string_list):
            return set(i for i in string_list 
                   if not any(i in s for s in delete_list))
        full_list = string_set(full_list)   
                
    print("enter the name of the file to output the information to")
    print("or enter 'print' to simply print out the value in the console")
    in_val = raw_input("> ")        

    if in_val == 'print':
        print(full_list)
    else:    
        target = open(in_val,'w+') 
        if lg_val == 'full':
            print >> target, full_list, in_val  
            #I haven't figured out a good other way besides redirecting print
        else:
            target.write('\n'.join(full_list))

        target.close()
#for x in delete_list: