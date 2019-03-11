import os
import shutil

# Choose the starting directory. This will choose the root directory
# ('/' for linux and 'C:\\' for windows, and also MAC whatever the root is on there)
# NOTE* this will check EVERY image on the computer ex. system image files, so this start directory should be
# able to be changed by the user later.
startDir = os.path.abspath(os.sep)

# Create a list of acceptable image formats.
imageFiles = ['.JPG', '.JPEG', '.TIF', '.PNG', '.RAW']

# Create pictures directory in the current directory of where program is running
# NOTE* this will only run once, as of now it will not over write if there's a pictures directory
pictures = os.path.join(".", "pictures")
os.mkdir(pictures)

# Begin walking Directory
for root, dirs, files, in os.walk(startDir):
    for name in files:
        for fileType in imageFiles:
            if name.endswith(fileType):
                source = os.path.join(root, name)
                shutil.copy(source, pictures)
                print(source)

    # I'm not sure what this loop is for? since we don't need to modify directories but will leave for now
    for name in dirs:
        print(os.path.join(root, name))
