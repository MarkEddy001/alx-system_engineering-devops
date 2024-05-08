#!/usr/bin/python3
"""Function to query subscribers on a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            if 'data' in data:
                return data['data']['subscribers']
            else:
                print("Invalid JSON response - 'data' key not found")
                return 0
        except ValueError:
            print("Invalid JSON response")
            return 0
    else:
        print("Request failed with status code: {}".format(response.status_code))
        return 0
