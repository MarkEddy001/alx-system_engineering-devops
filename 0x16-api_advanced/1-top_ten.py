#!/usr/bin/python3
"""A module that retrieves the tiltes of hot subreddit."""

import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit."""

    headers = {"User-Agent": "Middle-Chipmunk-3601"}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=headers,
        allow_redirects=False,
    )
    if response.status_code == 200:
        result = response.json()
        for i in range(10):
            print(result['data']['children'][i]['data']['title'])
    else:
        print(None)
