
# Description
#
# The method clock() returns the current processor time as a floating point number expressed in seconds on Unix. The precision depends on that of the C function of the same name, but in any case, this is the function to use for benchmarking Python or timing algorithms.
#
# On Windows, this function returns wall-clock seconds elapsed since the first call to this function, as a floating point number, based on the Win32 function QueryPerformanceCounter.
# Syntax
#
# Following is the syntax for clock() method −
#
# time.clock()
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns the current processor time as a floating point number expressed in seconds on Unix and in Windows it returns wall-clock seconds elapsed since the first call to this function, as a floating point number.
# Example
import time

def procedure():
   time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print(time.clock(), "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print(time.time() - t0, "seconds wall time")
