#!/usr/bin/python3
"""returns a list containing the titles of all hot articles for a given
subreddit"""
import requests


def recurse(subreddit, hot_list=[]):
    """function that returns a list containing the titles of all hot
    articles for a given subreddit"""
    after = None
    while True:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        if after:
            url += '&after={}'.format(after)
        headers = {'User-Agent': 'user-agent/1.0'}
        params = {"limit": 100}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after is None:
                break
        else:
            return None
    return hot_list
