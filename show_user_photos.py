import argparse
import sys
import flickrapi
import webbrowser
import json
from settings import flickr_key, flickr_secret


def authenticate():
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

def display_user_photos(group, user):
    print('Get user info and display photos')
    #info = flickr.photos.getInfo(photo_id='7658567128',  format='json')
    #info = json.loads(info.decode('utf-8'))
    #print(info)

    #info = flickr.groups.members.getList(group_id='74496825@N00', format='json')
    #info = json.loads(info.decode('utf-8'))
    #print(info)

    #info = flickr.groups.pools.getPhotos(group_id='74496825@N00', user_id='22695810@N04', format='json')
    #info = json.loads(info.decode('utf-8'))
    #print(info)

    info = flickr.people.findByUsername(username=user, format='json')
    info = json.loads(info.decode('utf-8'))

    if info['stat'] == 'ok':
        print('User name %s, User ID %s' % (user, info['user']['nsid']))
        user_photos_url = 'https://www.flickr.com/groups/%s/pool/%s' % (group, info['user']['nsid'])
        webbrowser.open_new_tab(user_photos_url)
    else:
        print('User not found')

parser = argparse.ArgumentParser()
parser.add_argument("--group", help="the group name")
parser.add_argument("--user", help="the user name")
args = parser.parse_args()

if args.group == None or args.user == None:
    sys.exit('Must enter --group and --user')

flickr = flickrapi.FlickrAPI(flickr_key, flickr_secret)

authenticate()

display_user_photos(args.group, args.user)


