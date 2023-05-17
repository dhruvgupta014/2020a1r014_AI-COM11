import numpy as np
import pandas as pd

# loading data from a csv file
data = pd.DataFrame(data=pd.read_csv('2020a1r007_1.csv'))
print(data)

# separating concept features from target
concepts = np.array(data.iloc[:,0:-1])
print(concepts)

# isolating target into a separate dataframe 
# copying last column to target array
target = np.array(data.iloc[:,-1])
print(target)

def learn(concepts, target):
    '''
    learn() function implements the learning method of the candidate elimination algorithm.
    Arguments:
        concepts - a data frame with all the features
        target - a data frame with corresponding output values
    '''

# initialise 50 with the first instance from concepts
# .copy() makes sure a new list is created instead of just pointing to the same memory location
    specific_h = concepts[0].copy()
    print("\n initialisation of specific_h and general_h")
    print(specific_h)

    general_h = [["?" for i in range(len(specific_h))] for j in range(len(specific_h))]
    print(general_h)
    # the learning iterations
    for i, h in enumerate(concepts):
        # checking if the hypothesis has a positive target
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                # change values in s & g only if values change
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] ='?'
                    #checking if the hypothesis has a negative target 
        if target[i] == "No":
            for x in range(len(specific_h)):
                            # for negative hypothesis change value only in g
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?' 
        print("\n steps of candidate elimination algorithm",i+1)
        print(specific_h)
        print(general_h)
                    # find indices where we have empty rows, meaning those that are unchanged
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        # remove those rows from general_h
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    # return final values
    return specific_h, general_h

s_final, g_final = learn(concepts, target)
print("\n final specific_h:", s_final, sep="\n")
print("\n final geberal_h:", g_final, sep="\n") 