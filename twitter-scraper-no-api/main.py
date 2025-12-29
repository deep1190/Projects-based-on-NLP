# Scraping Twitter with Python without API

import twint
import pandas as pd
from collections import Counter

# List of users to analyze
users = [
    'shakira',
    'KimKardashian',
    'rihanna',
    'jtimberlake',
    'KingJames',
    'neymarjr',
]

# Function to get followings of a user
def get_followings(username):
    c = twint.Config()
    c.Username = username
    c.Pandas = True
    twint.run.Following(c)
    list_of_followings = twint.storage.panda.Follow_df
    return list_of_followings['following'][username]

# Scrape followings and create combined list
followings = {}
following_list = []

for person in users:
    print('#####\nStarting: ' + person + '\n#####')
    try:
        followings[person] = get_followings(person)
        following_list += followings[person]
    except KeyError:
        print('IndexError')

# Most followed accounts among the users
print(Counter(following_list).most_common(10))

# Follow relationships among the user group
follow_relations = {}
for following_user in followings.keys():
    follow_relation_list = []
    for followed_user in followings.keys():
        follow_relation_list.append(followed_user in followings[following_user])
    follow_relations[following_user] = follow_relation_list

# Convert to DataFrame for better visualization
following_df = pd.DataFrame.from_dict(follow_relations, 
                                     orient='index', columns=followings.keys())
print(following_df)
