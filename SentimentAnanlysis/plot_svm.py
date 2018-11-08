import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('NaiveBayes', 'Support Vector Machine')
y_pos = np.arange(len(objects))
performance = [40,38]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Accuracy comparision')
 
plt.show()
