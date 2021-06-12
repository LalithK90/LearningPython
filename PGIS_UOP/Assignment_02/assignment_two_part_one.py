import time
from datetime import datetime

problemSizes = [1000, 2000, 3000, 4000, 10000]


def accordingProblemSize(value):
    global total_time
    print("%12s%15s" % ("Problem Size", "Iterations"))
    start_time = time.time()
    problem_size = value
    while problem_size > 0:
        number = 0
        for j in range(problem_size):
            for k in range(problem_size):
                number += 1
                print("%12d%15d" % (problem_size, number))
                problem_size = problem_size // 2
        end_time = time.time()
        total_time = (end_time - start_time)
    return total_time


finalResult = []
for x in problemSizes:
    finalResult.append("Problem Size : " + str(x) + " Total Time : " + str(accordingProblemSize(x)) + "s")

for y in finalResult:
    print(y)
