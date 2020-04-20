#!/usr/bin/python
import datetime
import time
import random
import praw
import os
from samplekeys import key1

k_user_agent = key1['user_agent']
k_client_id = key1['client_id']
k_client_secret = key1['client_secret']
k_username = key1['username']
k_password = key1['password']

debug = True

#Create reddit bot
bot = praw.Reddit(user_agent=k_user_agent,
    client_id=k_client_id, client_secret=k_client_secret,
    username=k_username, password=k_password)

def run():
    #Collect Recent Thread, Collect Comments, Format Comment, Save to .txt file
    print("I am Reddit Bot \n")
    time.sleep(5)
    subreddit = 'travel'      #Subreddit
    num_threads = 10        #Number of Threads
    comment_list = []

    for submission in bot.subreddit(subreddit).top(limit=num_threads):
        if debug:
            print("Submission Title:    ", submission.title)
        file_name = str(submission.title.replace(" ", "_"))+".txt"

        if not os.path.isfile(file_name):

            if debug:
                print("File name: " +file_name)
                print("Date: " +
                    datetime.datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'))
            comment_list.append([str(submission.author), str(submission.created_utc),
                submission.selftext.replace("\n", " "), str(submission.score)])
            submission.comments.replace_more(limit=None)

            for comment in submission.comments.list():
                if debug:
                    print("Author:      ", comment.author)
                    print("Created Date:",
                        datetime.datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'))
                    print("Comment:     ", comment.body)
                    print("Score:       ", comment.score)
                comment_list.append([str(comment.author),
                    str(datetime.datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')),
                    comment.body.replace("\n", " "),str(comment.score)])
                if debug:
                    print(comment_list)

            write_file(comment_list, file_name)
        else:
            print("Submission already saved to file")
        time.sleep(10)

def write_file(list, filename):
    #Format: ['Author', 'Created Date', 'Comment', 'Score']
    with open(filename, 'w') as file:
        for msg in list:
            try:
                file.write("\n"+msg[0] +", " + msg[1] +", " + msg[2] +", " + msg[3])
            except UnicodeError:
                print("Unicode Error");

if __name__=="__main__":
    run()
