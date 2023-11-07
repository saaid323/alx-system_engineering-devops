#!/usr/bin/python3
"""prints a sorted count of given keywords """
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """function that prints a sorted count of given keywords """
    if counts is None:
        counts = {}

    if not subreddit:
        print_results(counts)
        return

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after={}'.format(after)

    headers = {'User-Agent': 'user-agent/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word] = counts.get(word, 0) + 1

        after = data['data']['after']
        count_words(subreddit, word_list, after, counts)
    elif word_list:
        print_results(counts)


def print_results(counts):
    """sort the counts by value in descending order"""
    if counts:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print('{}: {}').format(keyword, count)
