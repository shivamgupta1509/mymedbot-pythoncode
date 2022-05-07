import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.stem.porter import PorterStemmer
from apyori import apriori



dataset = pd.read_csv("Copy Disease_Dataset - Disease_Dataset.csv")
x = dataset.iloc[:, 1:16].values
y = dataset.iloc[:, -2].values
remedies = dataset.iloc[:, -1].values

for row in range(len(x)):
    column = 0
    ps = PorterStemmer()
    for word in x[row]:
        if(type(x[row, column]) == str):
            x[row, column] = ps.stem(x[row, column])

transactions = x.astype(str).tolist()

rules = apriori(transactions = transactions, min_support = 0.02, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 5)

results = list(rules)


def diseaseDetection(list_of_inputs):
    print(list_of_inputs)
    max_count = 0
    index = 0
    disease_index = 0
    print(x)
    for diseases in x:
        count = 0
        for symptoms in diseases:
            if(symptoms in list_of_inputs):
                count += 1
        if(count > max_count):
            disease_index = index
            max_count = count
        index += 1
    
    # print("Disease: " + y[disease_index] + "\n")
    # print("Remedy: " + remedies[disease_index])

    return (y[disease_index], remedies[disease_index])

def symptomRecommendation(list_of_inputs):
    count = 0
    list_of_recommendation = []
    copy_of_list_of_inputs = list_of_inputs
    for arm in results:
        if(copy_of_list_of_inputs[-1] in arm[0]):
            for symptoms in arm[0]:
                if(not symptoms in copy_of_list_of_inputs and not symptoms in list_of_recommendation and not symptoms == 'None'):
                    list_of_recommendation.append(symptoms)
                    count += 1
        if(count == 5):
            break 
    # print(list_of_recommendation)
    return(list_of_recommendation)

# # diseaseDetection(['running nose', 'eye irritation',])
# sym = ["headache", "muscle pain"]
# print(symptomRecommendation(sym))


