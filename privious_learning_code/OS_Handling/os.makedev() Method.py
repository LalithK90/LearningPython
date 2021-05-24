
# Description
#
# The method makedev() composes a raw device number from the major and minor device numbers.
# Syntax
#
# Following is the syntax for makedev() method −
#
# os.makedev(major, minor)
#
# Parameters
#
# major − This is Major device number.
#
# minor − This is Minor device number.
#
# Return Value
#
# This method returns the device number.
# Example
import os, sys

path = "/var/www/html/foo.txt"

# Now get  the touple
info = os.lstat(path)

# Get major and minor device number
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print("Major Device Number :", major_dnum)
print("Minor Device Number :", minor_dnum)

# Make a device number
dev_num = os.makedev(major_dnum, minor_dnum)
print("Device Number :", dev_num)