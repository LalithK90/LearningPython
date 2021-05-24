# Description
#
# The method pipe() creates a pipe and returns a pair of file descriptors (r, w) usable for reading and writing, respectively
# Syntax
#
# Following is the syntax for pipe() method −
#
# os.pipe()
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns a pair of file descriptors.
# Example
import os, sys

print("The child will write text to a pipe and ")
print("the parent will read the text written by child...")

# file descriptors r, w for reading and writing
r, w = os.pipe()

processid = os.fork()
if processid:
# This is the parent process
# Closes file descriptor w
os.close(w)
r = os.fdopen(r)
print("Parent reading")
str = r.read()
print("text =", str)
sys.exit(0)
else:
# This is the child process
os.close(r)
w = os.fdopen(w, 'w')
print("Child writing")
w.write("Text written by child...")
w.close()
print("Child closing")
sys.exit(0)
