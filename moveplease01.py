#!/usr/bin/enc python3
"""A simple script to move two files cehp_storage/
   Alta3 Research | rzfeeser@alta3.com"""

#import shell utilities
import shutil

#import the operation system module
import os


def main():
    """called at runtime"""
#for python to start in home directory
os.chdir('/home/student/mycode/')

#move the file or folder to the destination
shutil.move('raynor.obj', 'ceph_storage/')

#user input for a new name
xname = input('What is the new name for kerrigan.obj? ')

#rename the current file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)





main() #this calls out main function
