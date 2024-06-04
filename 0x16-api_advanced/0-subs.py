#!/usr/bin/python3
"""A module that retrieves the number of subscribers of a subreddit."""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers (total subscribers)
        for a given subreddit. If an invalid subreddit is given,
        the function will return 0"""

    headers = {"User-Agent": "Middle-Chipmunk-3601"}
    try:
        response = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers=headers,
            allow_redirects=False
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return 0

    try:
        result = response.json().get("data")
        subscribers = result.get("subscribers")
        if subscribers is not None:
            print("OK")
        return subscribers
    except ValueError:
        print("Error: Unable to parse JSON response")
        return 0
