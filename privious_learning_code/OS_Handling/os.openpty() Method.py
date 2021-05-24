
# Description
#
# The method openpty() opens a pseudo-terminal pair and returns a pair of file descriptors(master,slave) for the pty & the tty respectively.
# Syntax
#
# Following is the syntax for openpty() method −
#
# os.openpty()
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns a pair of file descriptors i.e., master and slave.
# Example
import os

# master for pty, slave for tty
m, s = os.openpty()

print(m)
print(s)

# showing terminal name
s = os.ttyname(s)
print(m)
print(s)