from numpy import *
import numpy as np
from scipy import stats as st
from ItemBasedRecommendation import get_training_data

#   Initializing the matrix to all zeros for No of users = 49290 items = 139739
s = (49290,139739)
num_users=49290
num_items=139739
# rating_matrix = [[0 for col in range(139737)] for row in range(49289)]
rating_matrix = np.zeros((num_users,num_items))
pearson_correlation_matrix =np.zeros((num_items,num_items))
user_avg_rating_matrix=np.zeros(num_users)

#Building training data samples
# Converted the training input data from file to an integer matrix
def get_user_input_matrix():
    global rating_matrix
    size = (581720,3)
    data = np.zeros(size)
    data = (get_training_data())
    size =(49290,139739)
    user_item_matrix= np.zeros(size)
    for j in range(581720):
        rating_matrix[data[j][0]][data[j][1]]=data[j][2]
    return rating_matrix

#Generating the rating matrix
get_user_input_matrix()

#calculates average rating for each user and stores in the user_avg_rating_matrix
def user_averages():
    global rating_matrix
    global user_avg_rating_matrix
    for i in range(num_users):
        nne=np.count_nonzero(rating_matrix[i])
        if(nne!=0):
            user_avg_rating_matrix[i]=np.sum(rating_matrix[i])*1.0/nne
    print user_avg_rating_matrix

# Takes as input i,j which are the indices for users and returns the pearson coefficient for item i and j
def pearson_corr(i,j):
    global rating_matrix
    global user_avg_rating_matrix
    col1 = rating_matrix[:,i]
    col2 = rating_matrix[:,j]
    subset = (col1>0)&(col2>0) ## returing the boolean values
    rate_i = rating_matrix[subset,i]
    rate_j = rating_matrix[subset,j]
    user_avg=user_avg_rating_matrix[subset]
    rate_i=rate_i-user_avg
    rate_j=rate_j-user_avg
    num=np.dot(rate_i,rate_j)
    deno1=np.sqrt(np.dot(rate_i,rate_i))
    deno2=np.sqrt(np.dot(rate_j,rate_j))
    deno = deno1*deno2
    if (deno !=0):
        print num/deno

# ideal suppose to calculate the pearson coefficient matrix

def get_Pearson_Correlation_Matrix():
    for item in range(100): ## calculating for 100 users
        for item1 in range(item+1,100):
            pearson_corr(item,item1)

user_averages()
get_Pearson_Correlation_Matrix()


