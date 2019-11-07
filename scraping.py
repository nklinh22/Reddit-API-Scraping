# API Structure Reference:
# https://old.reddit.com/dev/api#listings
# https://old.reddit.com/dev/api#GET_comments_{article}


# define Authorization token for accessing Reddit
headers={"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
# retrieve only the top posts for the past day, t is time parameter
params={'t':'day'}
response=requests.get('https://oauth.reddit.com/r/python/top', headers=headers, params=params)
# result containing all the individual posts from Reddit
python_top=response.json()


#dictionary of Reddit post
{'data': {'approved_by': None,
     'archived': False,
     'author': 'ingvij',
     ...
     'ups': 43,
     'url': 'http://hkupty.github.io/2016/Functional-Programming-Concepts-Idioms-and-Philosophy/',
     'user_reports': [],
     'visited': False},
     'kind': 't3'}


python_top_articles=python_top['data']['children']
most_upvoted='' #id
most_upvotes=0  #number of upvotes

#for loop in the Reddit post list
for article in python_top_articles:
ar=article['data']
if ar['ups'] > most_upvotes:
    most_upvotes=ar['ups']
    most_upvoted=ar['id']

# Result retrieved: '4b7w9u' (id of the most upvoted post)


# get all comments of the top post from the past day
comments=requests.get('https://www.oauth.reddit.com/r/Python/comments/4b7w9u', headers=headers).json()


# find the most upvoted top-level comment in comments
comments_list=comments[1]['data']['children']

most_upvoted_comment='' #id
most_upvotes_comment=0  #number of upvotes
for c in comments_list:
    co=c['data']
    if co['ups'] > most_upvotes_comment:
        most_upvoted_comment=co['id']
        most_upvotes_comment=co['ups']

# Result returned: 'd16y4ry' (id of the most upvoted comment)

# Using API POST to upvote the top comment
# dir: 1/0/-1 (-1 is downvote)
payload={'dir':'1', 'id':'d16y4ry'}

#Upvote the comment using id above
response=requests.post('https://oauth.reddit.com/api/vote', json=payload, headers=headers)

#check status of the above command
status=response.status_code
