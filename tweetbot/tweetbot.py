import tweepy  # pip3 install tweepy
import time

consumer_key = 0
consumer_secret = 0
access_token = 0
access_token_secret = 0

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()

print(user.name)
print(user.screen_name)
print(user.followers_count)


# api 제한 있어서 sleep 함수
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# generous bot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)

    # 100명 이상인 사람만 following
    # if follower.followers_count > 100:
    #     follower.follow()

    # 특정인만 following
    # if follower.name == 'something':
    #     follower.follow()
    #     break


search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        # 좋아요함
        # tweet.favorite()
        print('I like that tweet')

        # 리트윗
        # tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break