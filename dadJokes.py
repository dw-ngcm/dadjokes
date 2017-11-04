import praw

reddit = praw.Reddit(client_id='hwrJ2ATYZfBZyQ',
                     client_secret='A0ejth4nkSJ1nQylr4BU9AWkCJQ',
                     user_agent='getdadjokes by /u/danielwallace42')

reddit.read_only = True

subreddit = reddit.subreddit('dadjokes')

hooks = [];
punch = [];

while True:
    submission = subreddit.random();
    print(submission.title)
    input("What's the answerrrr?")
    print(submission.selftext)
    input("Press Enter for another Joke! ")

#
#for i, submission in enumerate(subreddit.hot(limit=10)):
#    hooks.append(submission.title)
#    punch.append(submission.selftext)
#
#for joke in zip(hooks,punch):
#    print(joke)
