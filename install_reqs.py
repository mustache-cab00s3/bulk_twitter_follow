# Author: Cab00s3
# Twitter @Cab00s3Mustache
#
# /usr/bin/python3


import subprocess
import sys

def install_and_check_package(package_name):
    try:
        # Try to import the package to check if it's installed
        __import__(package_name)
        print(f"'{package_name}' is already installed.")
    except ImportError:
        print(f"'{package_name}' is not installed. Installing now...")
        # If the package is not installed, install it using pip
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"'{package_name}' has been installed successfully.")

def main():
    package_name = "twitter-api-client"
    
    # The Python package name used in pip might not match the import name, so we check both.
    install_and_check_package("twitter_api_client")  # Import name for twitter-api-client

if __name__ == "__main__":
    main()
