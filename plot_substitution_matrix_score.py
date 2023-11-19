import matplotlib as mp 


import matplotlib.pyplot as plt


BLOSUM = [45,55,62,75,90]
PAM = [50, 80, 100, 120, 150, 200, 250, 300]

#
##These scores were obtained from the emboss_needle tool available at https://www.ebi.ac.uk/Tools/psa/emboss_needle/
#
# For sequence pair 1 and 2, 1 and 3, and 2 and 3, respectively
Bscore12 = [218, 226, 155, 126, 131] 
Bscore13 = [220, 230, 161, 130, 130]
Bscore23 = [766, 865, 638, 643, 723] 

Pscore12 = [22,100,119,125,131,209,190,216]
Pscore13 = [6,83,110,123,129,205,187,211]
Pscore23 = [806,749,696,647,577,758,631,704]

# #plotting the scores with PAM
plt.plot(BLOSUM, Bscore12,color="blue")
plt.plot(BLOSUM, Bscore13,color="green")
plt.plot(BLOSUM, Bscore23,color="red")

# # Add labels and title
plt.xlabel('BLOSUM Value')
plt.ylabel('Score')
plt.title('BLOSUM vs Score')

# # Show the plot
plt.show()

#plotting the scores with PAM
plt.plot(PAM, Pscore12)
plt.plot(PAM, Pscore13)
plt.plot(PAM, Pscore23)

# Add labels and title
plt.xlabel('PAM Value')
plt.ylabel('Score')
plt.title('PAM vs Score')

# Show the plot
plt.show()