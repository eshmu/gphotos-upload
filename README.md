# gphotos-upload
Simple but flexible script to upload photos to Google Photos. Useful if you have photos in a directory structure that you want to reflect as Google Photos albums.
## Setup
1. Obtain a Google Photos API key (Client ID and Client Secret) by following the instructions on [Getting started with Google Photos REST APIs](https://developers.google.com/photos/library/guides/get-started)
..* *NOTE* When selecting your application type in Step 4 of "Request an OAuth 2.0 client ID", please select "Other". There's also no need to carry out step 5. 
2. Replace `YOUR_CLIENT_ID` in the client_id.json file with the provided Client ID. 
3. Replace `YOUR_CLIENT_SECRET` in the client_id.json file wiht the provided Client Secret.
4. Make sure you have [Python 3.7](https://www.python.org/downloads/) installed on your system
5. If needed, install [pipenv](https://pypi.org/project/pipenv/) via `pip install pipenv`
6. Change to the directory where you installed this script
7. Run `pipenv install` to download and install all the dependencies
8. Run `pipenv shell` to open a shell with all the dependencies available (you'll need to do this every time you want to run the script)
9. Now run the script via `python upload.py` as desired. Use `python upload.py -h` to get help.

 