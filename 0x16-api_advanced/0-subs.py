#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    custom_user_agent = 'MyCustomApp/1.0'
    headers = {
        'User-Agent': custom_user_agent,
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        dic = response.json()
        return dic["data"]["subscribers"]
    else:
        return 0
