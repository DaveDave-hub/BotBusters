import os
from datetime import datetime, timezone

import tweepy

from datetime import datetime

twitter_keys = {
    'consumer_key': os.environ.get('consumer_key', 'wID1lvpoGvyRHCurdwCxuwSYD'),
    'consumer_secret': os.environ.get('consumer_secret', 'rjhYAd4HkxCY3ZVNR2CL9qSDDgUAYuBWBSDLMlOjcBd2T4vOso'),
    'access_token_key': os.environ.get('access_token_key', '1516738608627171330-lW2tgAZ7vwHiawraKBNqNbvtITlV0X'),
    'access_token_secret': os.environ.get('access_token_secret', 'UDNJfAtVJT9s9ttXBcyHKBgE0Dh9JKKu9ctxi5Jef8ONn')
}

#setting connection for Twitter API - usk for tokens
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

#creates tweepy API instance
api = tweepy.API(auth)

#getting factors for account after providing username
def get_factors(screen_name):
    user = api.get_user(screen_name=screen_name)
    print(user)

    # factors used for verification
    username = user.screen_name
    verified_account = user.verified
    account_age = (datetime.now() - user.created_at.replace(tzinfo=None)).days  # provided in days
    followers_number = user.followers_count
    friend_number = user.friends_count
    # number of tweets posted on this account (from joining day)
    tweets_number = user.statuses_count
    # tweets per day - average
    tweets_per_day = round(tweets_number / account_age, 2)
    # language, posting time, retweets
    posting_time = int(user.created_at.strftime("%H"))  # strftime means date to string, we need hour only

    # list of factors
    account_factors = [verified_account, account_age, followers_number, friend_number, tweets_per_day, posting_time, username]
    return account_factors if len(account_factors) == 7 else f'User not found'




def account_verification(twitter_handle):
    user_factors = get_factors(twitter_handle)

    if user_factors == 'User not found':
        return 'User not found'

    else:
       # factors = ['verified account', 'account age', 'followers number', 'friend number', 'tweets per day', 'posting time', 'username']
        true_conditions = 0
        number_of_factors = 4
        percentage = 0
        letters = 0
        numbers = 0
        #verified account
        if user_factors[0] == True:
            percentage = 0
            return percentage

        elif user_factors[0] == False:
            #tweets per day
            if user_factors[4] > 100:
                print('tweets per day > 100')
                true_conditions += 1

            #account age
            if user_factors[1] <= 365:
                print('account age less than a year')
                true_conditions += 1

            #friends number - following - users that this user follows
            if user_factors[3] >= 10000:
                print('following more than 10000')
                true_conditions += 1

            #followers number
            if user_factors[2] <= 10:
                print('followers less than 10')
                true_conditions += 1
            #cheking numbers and letters in username
            for x in user_factors[6]:
                if x.isnumeric():
                    numbers += 1
                elif x.isalpha():
                    letters += 1

            if numbers > 4:
                print('more than 4 numbers in username')
                true_conditions += 1

            if letters < 3:
                print('less than 3 letters in username')
                true_conditions += 1
        percentage = (true_conditions * 100) / number_of_factors
        return percentage



