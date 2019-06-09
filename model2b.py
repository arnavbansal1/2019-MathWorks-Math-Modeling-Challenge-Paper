import random
students = 300
l = [[87.961, 90.3688, 100, 100],
     [0, 34, 34, 100, 100],
     [1.6553, 12.6674, 13.3569, 17.4342, 100, 100],
     [49.2, 100, 100],
     [0.067, 100, 100, 100],
     [82.6539, 82.7516, 96, 96, 100, 100],
     [17, 100, 100],
     [0, 0.9, 1.1, 14.8, 91.3, 96.4, 96.4, 100, 100, 100]]
# l stores prefix sums for each of the eight variable demographics (three of them are assumed to be constant for all seniors)
def pickRand(lst): # picks a random demographic (weighted by probability)
    r = random.random() * 100
    for i in range(len(lst)):
        if lst[i] > r:
            return i
studentStat = []
# studentStat is a list of lists storing the demographics of each student
for i in range(students):
    localStat = []
    # localStat is a list storing the demographic of a single student
    for j in range(len(l)):
        if j != 0:
            localStat.append(pickRand(l[j])+1)
        else:
            localStat.append(pickRand(l[j]))
    tempStat = [2] + localStat[0:1] + [5] + localStat[1:5] + [1] + localStat[5:]
    studentStat.append(tempStat)

for lst in studentStat:
    print(lst)
