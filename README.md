# bulk_twitter_follow
A quick script to follow a list of twitter usernames

## Setup

```bash
[~/github/bulk_twitter_follow] [main] ❱❱❱ python3 install_reqs.p

'twitter_api_client' is not installed. Installing now...
...
'twitter_api_client' has been installed successfully.
```


## Usage

```bash
[~] ❱❱❱ python3 bulk_twitter_follow.py -h

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣷⣶⣦⣄⡀⣀⣤⣶⣶⣿⣿⣿⣿⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣶⣶⣶⣶⣄⡀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣶⣤⡀⠀⠀
⠀⣴⣿⣿⣿⣿⠿⢿⣿⣿⡄⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⣰⣿⣿⡿⢿⣿⣿⣿⣿⣄⠀
⢸⣿⣿⣿⡟⠀⠀⠀⠈⢿⡿⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⣿⡟⠁⠀⠀⠈⢿⣿⣿⣿⡄
⢸⣿⣿⣿⣇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⡿⠀
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀
⠀⠀⠀⠈⠙⠻⠿⠿⣿⣿⣿⡿⠿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⠿⣿⣿⣿⣿⡿⠿⠟⠋⠁⠀⠀⠀

usage: bulk_twitter_follow.py [-h] -c CT0 -a AUTH_TOKEN -f USER_FILE_PATH

This script follows a list of Twitter user account names.

options:
  -h, --help            show this help message and exit
  -c CT0, --ct0 CT0     Twitter ct0 cookie value from a valid logged in session.
  -a AUTH_TOKEN, --auth_token AUTH_TOKEN
                        Twitter auth_token cookie value from a valid logged in session.
  -f USER_FILE_PATH, --user_file_path USER_FILE_PATH
                        Path/to/file of Twitter usersnames ie: Cab00s3Mustache

```
