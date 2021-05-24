
# Description
#
# The method isatty() returns True if the file is connected (is associated with a terminal device) to a tty(-like)
# device, else False. Syntax
#
# Following is the syntax for isatty() method −
#
# fileObject.isatty();
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns true if the file is connected (is associated with a terminal device) to a tty(-like) device,
# else false. Example Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

ret = fo.isatty()
print("Return value : ", ret)

# Close opend file
fo.close()