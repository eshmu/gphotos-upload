# gphotos-upload
Simple but flexible script to upload photos to Google Photos. Useful if you have photos in a directory structure that you want to reflect as Google Photos albums.

## Usage 

```
usage: upload.py [-h] [--auth  auth_file] [--album album_name]
                 [--log log_file]
                 [photo [photo ...]]

Upload photos to Google Photos.

positional arguments:
  photo               filename of a photo to upload

optional arguments:
  -h, --help          show this help message and exit
  --auth  auth_file   file for reading/storing user authentication tokens
  --album album_name  name of photo album to create (if it doesn't exist). Any
                      uploaded photos will be added to this album.
  --log log_file      name of output file for log messages
```


## Setup

### Obtaining a Google Photos API key

1. Obtain a Google Photos API key (Client ID and Client Secret) by following the instructions on [Getting started with Google Photos REST APIs](https://developers.google.com/photos/library/guides/get-started)

**NOTE** When selecting your application type in Step 4 of "Request an OAuth 2.0 client ID", please select "Other". There's also no need to carry out step 5 in that section.

Example:

2. Replace `YOUR_CLIENT_ID` in the client_id.json file with the provided Client ID in provided template.
3. Replace `YOUR_CLIENT_SECRET` in the client_id.json file wiht the provided Client Secret in provided template.

### Installing dependencies and running the script

1. Make sure you have [Python 3.7](https://www.python.org/downloads/) installed on your system
2. If needed, install [pipenv](https://pypi.org/project/pipenv/) via `pip install pipenv`
3. Change to the directory where you installed this script
4. Run `pipenv install` to download and install all the dependencies
5. Run `pipenv shell` to open a shell with all the dependencies available (you'll need to do this every time you want to run the script)
6. Now run the script via `python upload.py` as desired. Use `python upload.py -h` to get help.

 
