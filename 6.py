 Hypothetical data: Run rate in an T20 cricket match
overs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
runs_scored = [0,7,12,20,39,49,61,83,86,97,113,116,123,137,145,163,172,192,198,198,203]
# Create a linear plot
plt.plot(overs, runs_scored)
# Add labels and title
plt.xlabel('Overs')
plt.ylabel('Runs scored')
plt.title('Run scoring in an T20 Cricket Match')
# Display the plot
plt.grid(True)
plt.show()
Data Visualization with Python BCS358D
Dr. Azizkhan F Pathan, Dept. of IS&E, JIT, Davangere 6
b) Write a Python program to illustrate liner plotting with line formatting using 
Matplotlib.
import matplotlib.pyplot as plt
# Hypothetical data: Run rate in an T20 cricket match
overs = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
runs_scored = [0,7,12,20,39,49,61,83,86,97,113,116,123,137,145,163,172,192,198,198,203]
# Create a linear plot
plt.plot(overs, runs_scored, marker='X', linestyle='dashed',color='red', linewidth=2, 
markerfacecolor='blue', markersize=8)
# Add labels and title
plt.xlabel('Overs', color = 'green')
plt.ylabel('Runs scored')
plt.title('Run scoring in an T20 Cricket Match')
# Display the plot
plt.grid(True)
plt.show()
7. Write a P
