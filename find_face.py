'''
Script to call both scripts that find images, and finds faces.

'''

import walkDirs
import faceRec
import os
import sys

# Get the first argument from command line to be the starting directory
try:
    print('before')
    startDir = sys.argv[1]
    print('after')
    if os.path.exists(startDir) != True:    # Check if the given path exists
        startDir = os.path.abspath(os.sep)  # If given path DNE set to root directory
        print("Given path doesn't exists, using root")  
except:
    print('Failed input arg')
    startDir = os.path.abspath(os.sep)      # If no argument is given default to root directory
  

# Run method to collect images full path.
walkDirs.walk_dirs(startDir)
# Use OpenFace to recognize faces in image.
known_face_file, count = faceRec.face_rec()

print("There were %s recognized faces" % count)
print("The full path of the images with the recognized face is here: \n %s" % known_face_file)