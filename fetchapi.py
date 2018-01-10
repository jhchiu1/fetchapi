import requests

key = '  '

# URL where API is called
base_url = 'http://www.omdb.com'

# Ask user what movie rating they want to search for
movie = input('What movie do you want to search a rating for?')

# Get key data pair
params = { 'apikey' : key, 't' : movie}
data = requests.get(base_url, params ).json()

# Print moving rating
print(data)

print ('Rating for movie: ')
print(data['ratings'][0]['value'])

