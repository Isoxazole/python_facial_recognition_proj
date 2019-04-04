"""
Program Description: Checks the OS for all the required dependencies to run openCV
    and other modules needed to compete the final project. Feel free to change the logging
    from WARN to DEBUG to view all of the logs come across the consol.
    
Required Modules:
    Python 3 or greater
    Numpy
    OpenCV

Possible Modules:
    Matplotlib
"""

# Main imports
import logging
import sys
import datetime
# END imports

# Set up Logging to print lineno, the name and the message, To see all debugging messages change WARN to DEBUG
logging.basicConfig(level=logging.WARN, format= ' %(lineno)d - %(levelname)s - %(message)s')

# Print out the OS platform and time
logging.debug('Checking system platform')
print("Current System: " + sys.platform)
logging.debug('Checking system time')
print("Date and time: " + str(datetime.datetime.now()))

# Check Python Version
logging.debug('Checking Python Version')
print('Python Version: ', sys.version)

### IMPORT NUMPY AND OPENCV ###

print("\nPrimary Modules:")

# First numpy, import the module and print version to terminal
logging.debug('Checking for numpy modules') #Logging that numpy modules are being loaded
try:
    import numpy                            #import the module
    logging.debug('numpy modules found')    #Logging information for debugging

    # Check numpy Version
    logging.debug('Checking numpy Version') #Logging that the version is being checked

    if (numpy.__version__ < '1.16.2'):      #If the version is less than the one found when run 3/6/2019, warn the user
        print("\tnumpy: " + numpy.__version__)
        logging.warning('numpy version is less than 1.16.2, Consider upgrading to the newest version.')
    else:
        logging.debug('numpy is up to date')#If version is equal too or greater than the version continue on
        print("\tnumpy: " + numpy.__version__ +": Numpy is up-to-date")
    #End check numpy
    
except:                                                                     #Exception case if the module cannot be loaded
    raise Exception('\tUnable to locate numpy modules or not installed.')   #Raise and display exeption
# End numpy import

# import openCV and print version to screen
logging.debug('Checking for OpenCV modules')

try:
    import cv2
    logging.debug('openCV modules found')
    
    # Check openCV
    logging.debug('Checking openCV Version')

    if (cv2.__version__ < '4.0.0'):
        print("\tOpenCV: " + cv2.__version__)
        logging.warning('openCV version is less than 4.0.0, Consider upgrading to the newest version.')
    else:
        logging.debug('OpenCV is upto date')
        print("\tOpenCV: " + cv2.__version__ + ": OpenCV is up-to-date")
    # End check openCV

except:
    raise Exception('\tUnable to locate openCV modules or not installed.')
# End openCV import
#End Main import dependences

### IMPORT POSSIBLE NEEDED MODULES ###

print("\nExtra Modules:")

# import matplotlib and print version to terminal
logging.debug('Checking for Matplotlib modules')
try:
    import matplotlib
    logging.debug('matplotlib modules found')

    # Check Matplotlib version
    logging.debug('Checking Matplotlib Version')

    if (matplotlib.__version__ < '3.0..3'):
        print('\tmatplotlib: ' + matplotlib.__version__)
        logging.warning('Matplotlib version is less than 3.0.3, Consider upgrading to the newest version.')
    else:
        logging.debug('Matplotlib is upto date')
        print('\tmatplotlib: ' + matplotlib.__version__ + ": Matplotlib is up-to-date")
    # End check Matplotlib

except:
    raise Exception('\tUnable to locate Matplotlib modules')
# End matplotlib import
#End possible modules needed imports

logging.debug('End of program')
### END dependCheck.py ###
