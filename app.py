#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import pandas as pd


# ### Matching combinations
# 
# 1. g_men -> g_men + b_men
# 2. g_women -> g_women + b_women
# 
# 3. h_men -> h_women + b_women
# 4. h_women -> h_men + b_men 
# 
# 5. b_men -> b_men + g_men + b_women + h_women -- only category they can't date is h_men (who only want women)
# 6. b_women -> b_women + b_men + g_women +  h_men  -- only category they can't date is h_women (who only want men) 
# 
# h = heterosexual 
# g = gay
# b = bisexual 
# 
# loading below some users and matching preferences of these users.
# 

# In[2]:


data = {'name': ['Christine', 'Susan', 'Margaret', 'Judith', 'Jennifer', 'Mary', 'Elizabeth', 'Patricia', 'Linda', 
'Barbara', 'Lynette', 'Anne', 'Karen', 'Helen', 'Diane', 'Sandra', 'Wendy', 'Janet', 'Heather', 
'Pamela', 'Carol', 'Janice', 'Julie', 'Suzanne', 'Lorraine', 'Dianne', 'Marilyn', 'Rosemary', 'Sheryl', 
'Kathleen', 'John', 'David', 'Peter', 'Michael', 'Robert', 'Paul', 'Stephen', 'Kevin', 'Christopher', 
'Brian', 'William', 'Ian', 'Mark', 'Richard', 'Alan', 'Bruce', 'Geoffrey', 'Raymond', 'Gary', 'Anthony', 
'Graham', 'Philip', 'Barry', 'Colin', 'Trevor', 'Kenneth', 'Ross', 'Grant', 'Keith', 'Allan'], 
        'gender': ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 
'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 
'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm'], 
        'likes_women': ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 
'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 
'y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'y'], 
        'likes_men': ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 
'n', 'n', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 
'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'], 
        'preference': ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'g', 'g', 'g', 'g', 'g', 
'g', 'g', 'g', 'g', 'g', 'b', 'b', 'b', 'b', 'b', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 
'h', 'h', 'h', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'b', 'b', 'b', 'b', 'b']}


# In[3]:


df = pd.DataFrame(data, columns = ['name', 'gender', 'likes_women', 'likes_men', 'preference'])
df['match_type'] = df['gender'] + '-' + df['preference']


# In[4]:


df.head()


# the `match_type` variable combines the gender and the user's sexual orientation. eg. w-h is a heterosexual woman. 

# In[5]:


def preference_selection(gender, likes_women, likes_men):
    if gender == 'w':
        if likes_women == 'n':
            if likes_men == 'y':
                return 'w-h'
            else:
                pass
        elif likes_women == 'y':
            if likes_men == 'n':
                return 'w-g'
            elif likes_men == 'y':
                return 'w-b'
            else:
                pass
        else:
            pass
    elif gender == 'm':
        if likes_men == 'n':
            if likes_women == 'y':
                return 'm-h'
            else:
                pass
        elif likes_men == 'y':
            if likes_women == 'n':
                return 'm-g'
            elif likes_women == 'y':
                return 'm-b'
            else:
                pass
        else:
            pass
    else:
        pass
        


# In[6]:


def data_selection(match_type):
    match_for_df = []
    match_with_df = []
    
    if match_type == 'w-h':
        match_for_df = df[df['match_type'] == 'w-h']
        match_with_df = df[df['match_type'].isin(['m-h', 'm-b'])]
        return match_for_df, match_with_df
    elif match_type == 'm-h':
        match_for_df = df[df['match_type'] == 'm-h']
        match_with_df = df[df['match_type'].isin(['w-h', 'w-b'])]
        return match_for_df, match_with_df
    elif match_type == 'm-g':
        match_for_df = df[df['match_type'] == 'm-g']
        match_with_df = df[df['match_type'].isin(['m-g', 'm-b'])]
        return match_for_df, match_with_df
    elif match_type == 'w-g':
        match_for_df = df[df['match_type'] == 'w-g']
        match_with_df = df[df['match_type'].isin(['w-g', 'w-b'])]
        return match_for_df, match_with_df
    elif match_type == 'm-b':
        match_for_df = df[df['match_type'] == 'm-b']
        match_with_df = df[df['match_type'].isin(['m-b', 'm-g', 'w-b', 'w-h'])]
        return match_for_df, match_with_df
    elif match_type == 'w-b':
        match_for_df = df[df['match_type'] == 'w-b']
        match_with_df = df[df['match_type'].isin(['w-b', 'm-b', 'w-g', 'm-h'])]
        return match_for_df, match_with_df
    else:
        pass


# In[7]:


def user_matching(match_for_df, match_with_df):
    n = 5
    matched = []
    match_for = match_for_df['name'].tolist()
    match_with = match_with_df['name'].tolist()
    
    while len(match_for) >= n and len(match_with) >= n:
        batch_1 = match_for[:n]
        batch_2 = [user for user in match_with if user not in batch_1]
        batch_2 = random.sample(batch_2, n)
        for i in range(n):
            matched.append(batch_1[i])
            matched.append(batch_2)
        for i in range(n):
            matched.append(batch_2[i])
            matched.append(batch_1)
        remove_batches = batch_1 + batch_2
        match_for = [user for user in match_for if user not in remove_batches]
        match_with = [user for user in match_with if user not in remove_batches]
    return matched


# provide inputs as instructed, otherwise program will not work. :p 

# In[8]:


def main():
    gender = input('What is your gender? m/w: ')
    likes_women = input('Do you like women? y/n: ')
    likes_men = input('Do you like men? y/n: ')
    
    match_type = preference_selection(gender, likes_women, likes_men)
    match_for_df, match_with_df = data_selection(match_type)
    matched = user_matching(match_for_df, match_with_df)
    print("\n\nUsers who have a", match_type, "match type: \n\n", match_for_df, 
          "\n\nUsers available to match with", match_type, "match type:\n\n", match_with_df, "\n")
    print("Note: In situations where the same user shows up in both lists, they will be removed from the second list before matching starts, so that they are not matched with him/herself.\n")
    print("Matched Users:\n")
    for i in matched:
        print(i)
    


# In[9]:


main()

