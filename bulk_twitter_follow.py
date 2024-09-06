# Author: Cab00s3
# Twitter @Cab00s3Mustache
#
# /usr/bin/python3
#
# Use: Simple script that takes a list of Twitter user accounts and follows
# Requires twitter-api-client

import time
import random
import argparse

from twitter.account import Account
from twitter.scraper import Scraper


def startup():
  print('')
  print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣷⣶⣦⣄⡀⣀⣤⣶⣶⣿⣿⣿⣿⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
  print('⠀⠀⢀⣤⣶⣶⣶⣶⣄⡀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣶⣤⡀⠀⠀')
  print('⠀⣴⣿⣿⣿⣿⠿⢿⣿⣿⡄⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⣰⣿⣿⡿⢿⣿⣿⣿⣿⣄⠀')
  print('⢸⣿⣿⣿⡟⠀⠀⠀⠈⢿⡿⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⣿⡟⠁⠀⠀⠈⢿⣿⣿⣿⡄')
  print('⢸⣿⣿⣿⣇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡇')
  print('⠘⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⡿⠀')
  print('⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀')
  print('⠀⠀⠀⠈⠙⠻⠿⠿⣿⣿⣿⡿⠿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⠿⣿⣿⣿⣿⡿⠿⠟⠋⠁⠀⠀⠀')
  print('')


def generate_random_number():
  return random.randint(4, 9)


def random_sleep_time():
  time.sleep(generate_random_number())
  pass

# Cookies from Twitter Session are required
def gather_twitter_cookies(ct0, auth_token):
  cookies={}
  cookies["ct0"] = ct0
  cookies["auth_token"] = auth_token
  return cookies


# Creating the necessary handlers for communications with twitter's api
def twitter_handlers(cookies):
  scraper = Scraper(cookies=cookies)
  account = Account(cookies=cookies)
  return scraper, account


def user_list(user_file_path):
  print(f'Parsing {user_file_path} for users...')
  with open(user_file_path, 'r') as file:
    users = [line.strip() for line in file]
    return users
  

def twitter_user_lookup(scraper, user):
  print(f'Searching for {user} id#...')
  userData = scraper.users([user])
  # UserId is required for the Follow Action
  userId = userData[0]["data"]['user']['result']['rest_id']
  return userId


def process_users_list(scraper, account, users):
  print('Bulk following the supplied list of users...')
  for user in users:
    random_sleep_time()
    try:
      result = account.follow(twitter_user_lookup(scraper, user))
      print(f'Now Following...{user}')
      time.sleep(generate_random_number())
    except Exception as error:
      print(f"Error at {user}")
      print(error)


def main():
  startup()
  # Create the argument parser
  parser = argparse.ArgumentParser(description="This script follows a list of Twitter user account names.")

  parser.add_argument('-c', '--ct0', type=str, required=True, help="Twitter ct0 cookie value from a valid logged in session.")
  parser.add_argument('-a', '--auth_token', type=str, required=True, help="Twitter auth_token cookie value from a valid logged in session.")
  parser.add_argument('-f', '--user_file_path', type=str, required=True, help="Path/to/file of Twitter usersnames ie: Cab00s3Mustache")

  # Parse arguments
  args = parser.parse_args()
  
  # Main working function calls
  scraper, account = twitter_handlers(gather_twitter_cookies(args.ct0, args.auth_token))
  process_users_list(scraper, account, user_list(args.user_file_path))


if __name__ == "__main__":
  main()
