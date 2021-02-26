import flickrapi
import webbrowser
import json
from settings import flickr_key, flickr_secret


def authenticate():
    flickr = flickrapi.FlickrAPI(flickr_key, flickr_secret)

    print('Authenticate...')

    # Only do this if we don't have a valid token already
    if not flickr.token_valid(perms='read'):

        # Get a request token
        flickr.get_request_token(oauth_callback='oob')

        # Open a browser at the authentication URL. Do this however
        # you want, as long as the user visits that URL.
        authorize_url = flickr.auth_url(perms='read')
        webbrowser.open_new_tab(authorize_url)

        # Get the verifier code from the user. Do this however you
        # want, as long as the user gives the application the code.
        verifier = str(input('Verifier code: '))

        # Trade the request token for an access token
        flickr.get_access_token(verifier)

    return flickr

def get_nsid_for_group(flickr, group_name):
    more = True
    page = 1
    while more is True:
        info = flickr.groups.search(text=group_name, per_page=100, page=page, format='json')
        info = json.loads(info.decode('utf-8'))
        count = len(info['groups']['group'])
        if count < 100:
            more = False
        else:
            page += 1
        for item in info['groups']['group']:
            if item['name'] == group_name:
                return item
    return None


