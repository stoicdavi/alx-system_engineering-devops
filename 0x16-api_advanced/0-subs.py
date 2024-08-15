#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""

def number_of_subscribers(subreddit):
    """ return total number of subscriber"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.9"}
    response = requests.get(url, headers=headers, allow=redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers =data['data']['subscribers']
        return subscribers
    else:
        return 0
