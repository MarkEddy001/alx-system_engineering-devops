#!/usr/bin/python3
"""A module that retrieves the number of subscribers of a subreddit."""


import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers (total subscribers)
        for a given subreddit. If an invalid subreddit is given,
        the function will return 0"""

    headers = {"User-Agent": "Middle-Chipmunk-3601"}
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        result = response.json().get("data")
        return result.get("subscribers")
    else:
        return 0
