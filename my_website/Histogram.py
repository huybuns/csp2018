import numpy as np
import matplotlib.pyplot as plt

N = 5
totalMeans = (1.4, 10.3, 29.9, 34.7, 23.7)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, totalMeans, width, color='#6d6dff')

standardMeans = (2.5, 14.6, 34.6, 31.8, 16.5)
rects2 = ax.bar(ind+width, standardMeans, width, color='#3a3a59')

ax.set_ylabel('Results of Students (%)')
ax.set_xlabel('AP Spanish Exam Scores')
ax.set_title('The Overall Percentage of AP Spanish Exam Scores')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1', '2', '3', '4', '5') )

ax.legend( (rects1[0], rects2[0]), ('Total Group', 'Standard Group**') )

plt.show()