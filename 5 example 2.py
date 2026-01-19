#5a
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
student_scores = np.random.normal(loc=70, scale=15, size=100)
plt.hist(student_scores, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Student Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Student Scores')
plt.show()

#5b
import matplotlib.pyplot as plt
countries = ['Brazil', 'Germany', 'Italy', 'Argentina', 'Uruguay', 'France', 'England', 'Spain']
wins = [5, 4, 4, 3, 2, 2, 1, 1]
colors = ['yellow', 'magenta', 'green', 'blue', 'lightblue', 'blue', 'red', 'cyan']
plt.pie(wins, labels=countries, autopct='%1.1f%%', colors=colors, startangle=90,explode=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], shadow=True)
plt.title('FIFA World Cup Wins by Country')
plt.axis('equal')
plt.show()
