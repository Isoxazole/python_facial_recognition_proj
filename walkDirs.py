import os
import sys

# Get the first argument from command line to be the starting directory
try:
    startDir = sys.argv[1]
    if os.path.exists(startDir) != True:    # Check if the given path exists
        startDir = os.path.abspath(os.sep)  # If given path DNE set to root directory
        print("Given path doesn't exists")  
except:
    startDir = os.path.abspath(os.sep)      # If no argument is given default to root directory
    
print("Starting directory: " + startDir)

# Create a list of acceptable image formats.
imageFiles = ['.JPG', '.JPEG', '.TIF', '.PNG', '.RAW']

# Create file to list all paths to images.
f = open("img_paths.txt", "w+")

# Begin walking Directory
for root, dirs, files, in os.walk(startDir):
    for name in files:
        for fileType in imageFiles:
            if name.endswith(fileType.lower()):
                source = os.path.join(root, name)
                print(source)
                f.write(source + "\n") # Write image path to the file on separate lines
f.close() # Close file
