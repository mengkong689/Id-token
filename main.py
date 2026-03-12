import requests
from bs4 import BeautifulSoup

def get_discord_token(user_id):
url = f'https://discord.com/api/v9/users/{user_id}'
headers = {
'Authorization': 'MTA3MzE5MjIyMDUwNjczNDYwMg.G0qybO.D7DXzzik2YyiND-FWi8fnxqbYmXxEUb9FBqus0' # Replace with your bot token
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
data = response.json()
return data['token']
else:
return None

if __name__ == '__main__':
user_id = input('Enter the User ID: ')
token = get_discord_token(user_id)
if token:
print(f'Token for User ID {user_id}: {token}')
else:
print('Failed to retrieve token.')

