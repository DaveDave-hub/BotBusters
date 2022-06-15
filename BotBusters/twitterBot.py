import os

import tweepy

from datetime import datetime

twitter_keys = {
    'consumer_key': os.environ.get('api_key', 'wID1lvpoGvyRHCurdwCxuwSYD'),
    'consumer_secret': os.environ.get('api_secret', 'rjhYAd4HkxCY3ZVNR2CL9qSDDgUAYuBWBSDLMlOjcBd2T4vOso'),
    'access_token_key': os.environ.get('access_token_key', 'AAAAAAAAAAAAAAAAAAAAAOPKbgEAAAAAXBC63C72IHZ9v1TZHeEvSz5e0Mc%3DMO2wMFHNMwwjVDQKwQaUJIN8hQrF4N24CwL0bkoPXKoW3qjlCB'),
    'access_token_secret': os.environ.get('access_token_secret', None)
}

#setting connection for Twitter API - usk for tokens
auth = tweepy.OAuthHandler(twitter_keys['consumer_key', twitter_keys['consumer_secret']])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

#creates tweepy API instance
api = tweepy.API(auth)

#getting factors for account after providing username
def get_factors(screen_name):
    try:
        #here we get username (for checking numbers in the name)
        user = api.get_user(screen_name)
        print(user)

        #factors used for verification
        verified_acocunt = user.verified
        account_age =(datetime.now() - user.created_at).days #provided in days
        followers_number = user.follower_count
        friend_number = user.friends.count
        #number of tweets posted on this account (from joining day)
        tweets_number = user.statuses_count
        #tweets per day - average
        tweets_per_day = round(tweets_number / account_age, 2)
        #language, posting time, retweets
        posting_time = int(user.created_at.strftime("%H")) #strftime means date to string, we need hour only

        # list of factors
        account_factors =[verified_acocunt, account_age, followers_number, friend_number, tweets_per_day, posting_time]

        #if else statements to check conditions

        true_conditions = 0
        if verified_acocunt == True
            return 'Not a bot'

        if verified_acocunt == False:
            if tweets_per_day > 100:
                true_conditions += 1

            if account_age <= 365:
                true_conditions += 1

            if friend_number <= 10 and followers_number >= 10000:
                true_conditions += 1

    except:
        return 'User not found'

def bot_prediction(twitter_username):

    user_factors = get_factors(twitter_username)
    true_conditions = 0

    if user_factors =='User not found':
        return 'User not found'

    else:
        factors =['verfied-account', 'account age', 'followers number', 'friends number', 'tweets per day', 'posting time']

