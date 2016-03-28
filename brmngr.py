#/usr/bin/python

from os import listdir, path
import sys, getopt

__version__ = "0.0.1"

"""the location where backlight exposures are stored"""
BACKLIGHT_DIR = "/sys/class/backlight/"

"""the name of the file that exposes the brightness of a backlight"""
BRIGHTNESS_FILE = "brightness"

""" the name of the file that exposes the maximum brightness of a backlight """
MAX_BRIGHTNESS_FILE = "max_brightness"

""" holder of the -b argument """
backlight = ""

""" returns a list of all available backlights """
def list_backlights():
    return listdir(BACKLIGHT_DIR)

""" returns true if the backlight is valid, false if otherwise """
def is_valid_backlight(backlight):
    return path.exists(path.join(BACKLIGHT_DIR, backlight))

""" returns and int defining the current brightness for the specified backlight """
def get_brightness(backlight):
    with open(path.join(BACKLIGHT_DIR, backlight, BRIGHTNESS_FILE), "r") as brfile:
        return int(brfile.readlines()[0]) # the first line in the brightness file.

""" returns an int defining maximum brightness of the backlight """
def get_max_brightness(backlight):
     with open(path.join(BACKLIGHT_DIR, backlight, MAX_BRIGHTNESS_FILE), "r") as brfile:
        return int(brfile.readlines()[0]) # the first line in the brightness file.

""" sets the brightness of the specified backlight. Returns true if set successfully, false if not. """
def set_brightness(backlight, value):
    if value > get_max_brightness(backlight) or value < 0:
        return False
    
    try:
        with open(path.join(BACKLIGHT_DIR, backlight, BRIGHTNESS_FILE), "w") as brfile:
            brfile.truncate()
            brfile.write(str(value))
    except PermissionError as e:
        print("Permission error. Make sure you're running the script as root! (sudo). " + str(e))

    return True

""" prints the help message """
def print_help():
    print ("brmng v%s help message:" % __version__)
    print_cmd_help("-b <backlight>", "Sets the backlight. This arg must be set before manipulating or reading a backlight.")
    print_cmd_help("-l", "Lists available backlights.")
    print_cmd_help("-s <value>", "Sets the backlight brightness to the given value.")
    print_cmd_help("-m", "Returns the maximum brightness of the backlight.")
    print_cmd_help("-g", "Returns the current brightness of the backlight.") 
    print_cmd_help("-h", "Prints this message.")

def print_cmd_help(cmd, desc):
    print("%-14s %s" % (cmd, desc))

if __name__ == "__main__":
    # handle args
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlb:s:mg")
    except getopt.GetoptError as  e:
        print("Invalid input: " + str(e))
        sys.exit(1)

    for opt, arg in opts:
        if opt == "-h":
            print_help();

        elif opt == "-l":
            print("Available backlights:")
            for backlight in list_backlights():
                print(backlight)
            
        elif opt == "-b":
             if is_valid_backlight(arg):
                 backlight = arg
             else:
                 print("Backlight doesn't exist.")
        elif backlight != "":
            if opt == "-s":
                if not set_brightness(backlight, int(arg)):
                    print("Failed setting brightness.")

            elif opt == "-g":
                print(get_brightness(backlight))
        
            elif opt == "-m":
                print(get_max_brightness(backlight))
