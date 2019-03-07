import os

# Choose the starting directory. For this project it will probably be '/'.
startDir = '/home/'

# Create a list of acceptable image formats.
imageFiles = [ '.JPG', '.JPEG', '.TIF', '.PNG', '.RAW']

# Begin walking Directory
for root, dirs, files, in os.walk(startDir):
    for name in files:
        for fileType in imageFiles:
            if name.endswith(fileType):
                print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
