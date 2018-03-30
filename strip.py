#!/usr/bin/python 

'''This python script would be invoked by Pig and the data will be streamed through it.
'''
import sys; 
#This is the test line
print sys.stdin.read().replace('","',',').strip('"')
