import argparse
import sys
import flickrapi
import webbrowser
import json
from flickr_utils import authenticate


def display_user_photos(group, user):
    print('Get user info and display photos')

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

flickr = authenticate()

display_user_photos(args.group, args.user)


