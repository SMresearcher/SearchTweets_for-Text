import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'Your CONSUMER_KEY'
credentials['CONSUMER_SECRET'] = 'Your CONSUMER_SECRET'
credentials['ACCESS_TOKEN'] = 'Your ACCESS_TOKEN'
credentials['ACCESS_SECRET'] = 'Your ACCESS_SECRET'


# Save the credentials object to file
with open("mytwitter_credentials.json", "w") as file:
    json.dump(credentials, file)