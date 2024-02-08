#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Push files around using shutil and os from the standard library"""

#import additional code to complete out task
import shutil
import os

def main():
    """code to move files around"""
    #start the program in the home user directory
    os.chdir("/home/student/mycode/")

    #copy the file to the folder
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy the entire folder and every folder contained in it
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")


if __name__ == "__main__":
    main()
