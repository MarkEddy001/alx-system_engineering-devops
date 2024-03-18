#!/usr/bin/python3
"""
Queries the Reddit API

"""
import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers of a subreddit.

    """
    try:
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={"User-Agent": "GetSubscriberCount"},
            allow_redirects=False
        )
        response.raise_for_status()

        data = response.json().get('data')

        if data and 'subscribers' in data:
            return data['subscribers']
        else:
            return 0

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
