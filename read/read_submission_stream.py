#!/usr/bin/python
import praw
from samplekeys import key1

k_user_agent = key1['user_agent']
k_client_id = key1['client_id']
k_client_secret = key1['client_secret']
k_username = key1['username']
k_password = key1['password']



def run():
    print('Logging Into Reddit...')
    #Create Reddit Bot
    redditbot = praw.Reddit(user_agent=k_user_agent,
        client_id=k_client_id, client_secret=k_client_secret,
        username=k_username, password=k_password)
    print('Logged in')

    subreddit = redditbot.subreddit('travel')                          #Subreddit

    #Read submissios stream forever
    for submission in subreddit.stream.submissions():
        print(submission.title.upper())
        print(submission.selftext)
        for comment in submission.comments.list():
            print(comment.body)


if __name__ == '__main__':
    run()
