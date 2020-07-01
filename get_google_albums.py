from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
import json
import os
import glob
import argparse
import logging
import re
from pathlib import Path

def parse_args(arg_input=None):
    parser = argparse.ArgumentParser(description='Get Google Albums')
    parser.add_argument('--auth ', metavar='auth_file', dest='auth_file',
                    help='file for reading/storing user authentication tokens')
    parser.add_argument('--log', metavar='log_file', dest='log_file',
                    help='name of log file for log messages')
    parser.add_argument('--output', metavar='output_file', dest='output_file',
                    help='name of output file for google albums')
    return parser.parse_args(arg_input)



def auth(scopes):
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_id.json',
        scopes=scopes)

    credentials = flow.run_local_server(host='localhost',
                                        port=8080,
                                        authorization_prompt_message="",
                                        success_message='The auth flow is complete; you may close this window.',
                                        open_browser=True)

    return credentials

def get_authorized_session(auth_token_file):

    scopes=['https://www.googleapis.com/auth/photoslibrary',
            'https://www.googleapis.com/auth/photoslibrary.sharing']

    cred = None

    if auth_token_file:
        try:
            cred = Credentials.from_authorized_user_file(auth_token_file, scopes)
        except OSError as err:
            logging.debug("Error opening auth token file - {0}".format(err))
        except ValueError:
            logging.debug("Error loading auth tokens - Incorrect format")


    if not cred:
        cred = auth(scopes)

    session = AuthorizedSession(cred)

    if auth_token_file:
        try:
            save_cred(cred, auth_token_file)
        except OSError as err:
            logging.debug("Could not save auth tokens - {0}".format(err))

    return session


def save_cred(cred, auth_file):

    cred_dict = {
        'token': cred.token,
        'refresh_token': cred.refresh_token,
        'id_token': cred.id_token,
        'scopes': cred.scopes,
        'token_uri': cred.token_uri,
        'client_id': cred.client_id,
        'client_secret': cred.client_secret
    }

    with open(auth_file, 'w') as f:
        print(json.dumps(cred_dict), file=f)
# Generator to loop through all albums


def get_albums(session, appCreatedOnly=False):

    params = {
            'excludeNonAppCreatedData': appCreatedOnly
    }

    while True:

        albums = session.get('https://photoslibrary.googleapis.com/v1/albums', params=params).json()

        logging.debug("Server response: {}".format(albums))

        if 'albums' in albums:

            for a in albums["albums"]:
                yield a

            if 'nextPageToken' in albums:
                params["pageToken"] = albums["nextPageToken"]
            else:
                return

        else:
            return

def main():
    args = parse_args()
    logging.basicConfig(format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I_%M_%S %p',
                    filename=args.log_file,
                    level=logging.INFO)
    # if no auth_file is given, use the directory of the called python file and client_id.json as the auth file name
    if not args.auth_file:
        args.auth_file = os.path.dirname(os.path.realpath(__file__)) + os.sep + "client_id.json"
    session = get_authorized_session(args.auth_file)

    # if no auth_file is given, use the directory of the called python file and client_id.json as the auth file name
    if not args.output_file:
        args.output_file = 'g_albums.txt'
    google_albums = []
    for a in get_albums(session):
        google_albums.append(a.get("title"))
    sorted_uniq_goole_albums = sorted(set(google_albums))
    with open(args.output_file, 'w') as output_f:
        for a in sorted_uniq_goole_albums:
            print(a, file=output_f)
        
if __name__ == '__main__':
  main()