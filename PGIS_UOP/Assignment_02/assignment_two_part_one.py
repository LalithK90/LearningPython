import time
from datetime import datetime

problemSizes = [1000, 2000, 3000, 4000, 10000]


def accordingProblemSize(value):
    print("%12s%15s" % ("Problem Size", "Iterations"))
    start_time = time.time()
    problemSize = value
    while problemSize > 0:
        number = 0
        for j in range(problemSize):
            for k in range(problemSize):
                number += 1
        print("%12d%15d" % (problemSize, number))
        problemSize = problemSize // 2
    end_time = time.time()
    total_time = (end_time - start_time)
    return total_time


finalResult = []
for x in problemSizes:
    finalResult.append("Problem Size : " + str(x) + " Total Time : " + str(accordingProblemSize(x))+"s")

for y in finalResult:
    print(y)
