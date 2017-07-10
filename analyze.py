# Import necessary packages and methods
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

# Initialize credentials to access Twitter API
twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''

# Create instance of Twitter API
twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

# Specify user handle
user_handle = ""

# Gather and analyze tweets
def analyze(handle):
    # Get user's last 200 tweets
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

    # Convert tweet from Unicode to UTF-8
    # Append UTF-8 encoded tweets to the text variable
    text = ""
    for status in statuses:
        if (status.lang == 'en'):
            text += status.text.encode('utf-8')

    # Initialize IBM Bluemix credentials for Personality Insights
    pi_username = ''
    pi_password = ''

    # Initialize PersonalityInsights
    personality_insights = PersonalityInsights(username=pi_username, password=pi_password)

    # Analyze tweets
    pi_result = personality_insights.profile(text)

    # Return results
    return pi_result

# Flatten JSON structure produced by analyze() function
def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data

# Gather and analyze specified user's tweets
user_result = analyze(user_handle)

# Format results
user = flatten(user_result)

# Sort results
sorted_user = sorted(user.items(), key=operator.itemgetter(1), reverse=True)

# Print results
print(sorted_user)
