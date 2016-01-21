import numpy as np
import matplotlib.pyplot as plt

year = []
runtime = []
with open("olympicsData.csv") as data:
    for line in data.readlines():
        line = line.rstrip().split(",")
        year.append(float(line[0]))
        runtime.append(float(line[1]))

def avg(lista):
    return sum(lista)/len(lista)


avg_y_t = avg([obs[0]*obs[1] for obs in zip(year, runtime)])
avg_y = avg(year)
avg_t = avg(runtime)
avg_y2 = avg([y * y for y in year])

print(avg_y_t, avg_y, avg_t, avg_y2)

w1 = (avg_y_t - avg_y * avg_t) / (avg_y2 - avg_y * avg_y)

w0 = avg_t - w1*avg_y

def linearFunc(w0, w1, x):
    return x*w1 + w0
lineRange = [1880, 2012]
runningTime = [linearFunc(w0, w1, lineRange[0]), linearFunc(w0, w1, lineRange[1])]
print(runningTime)
plt.plot(lineRange, runningTime)
plt.scatter(year, runtime)

print(w1, w0)
plt.show()
