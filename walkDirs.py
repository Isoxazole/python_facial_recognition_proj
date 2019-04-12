import os

# Choose the starting directory. This will choose the root directory
startDir = os.path.abspath(os.sep)

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
