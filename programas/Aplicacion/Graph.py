import sys
import numpy as np
import matplotlib.pyplot as plt


texto=str(sys.argv[1])
img=str(sys.argv[2])

file = open(texto, "r")
data = file.read()
file.close()

data_list = data.replace('\n', ' ').split(" ")
emotions=[]

for x in data_list:
    if x=="Happy" or x=="Angry" or x=="Neutral" or x =="Sad" \
    or x =="Surprise" or x =="Disgust" or x =="Fear":
        emotions.append(x)

labels, counts = np.unique(emotions,return_counts=True)

ticks = range(len(counts))
plt.bar(ticks,counts, align='center')
plt.xticks(ticks, labels)
plt.savefig(img)
plt.show()
plt.close()
