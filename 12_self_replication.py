# --------------------------------------------------------------
# Script that self-replicates from one folder to another. It
# deletes its previous self, waits for 20 seconds, copies
# itself to the other folder and starts there with a
# new process id. I guess it's pretty hard to track this process
# as it changes every 20 seconds.
#
# Precondition: Two folders "folder1" and "folder2" where the
# script gets started.
#
# --------------------------------------------------------------

from shutil import copyfile
import os
import subprocess
import time


directory_name = os.path.dirname(__file__)
filename = os.path.basename(__file__)
new_folder = "/folder2/" if "folder1" in directory_name else "/folder1/"
head, tail = os.path.split(directory_name)
destination_file = head + new_folder + filename

try:
    os.remove(destination_file)
except:
    pass

time.sleep(20)
copyfile(__file__, destination_file)
process = subprocess.Popen(['python', destination_file])
