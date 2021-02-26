import argparse
import sys
import flickrapi
import json
from flickr_utils import authenticate, get_nsid_for_group


def count_user_photos(group, user):
    print('Get user info...')

    info = flickr.people.findByUsername(username=user, format='json')
    info = json.loads(info.decode('utf-8'))

    if info['stat'] == 'ok':
        user_id = info['user']['nsid']
        print('User name %s, User ID %s' % (user, user_id))
        print('Count photos...')

        info = flickr.groups.pools.getPhotos(group_id=group, user_id=user_id, per_page=500, format='json')
        info = json.loads(info.decode('utf-8'))

        count = len(info['photos']['photo'])
        if count < 500:
            print('User has %d photos in the group' % count)
        else:
            print('User has at least 500 photos in the group')
    else:
        print('User not found')

parser = argparse.ArgumentParser()
parser.add_argument("--group", help="the group name")
parser.add_argument("--user", help="the user name")
args = parser.parse_args()

if args.group == None or args.user == None:
    sys.exit('Must enter --group and --user')

flickr = authenticate()

item = get_nsid_for_group(flickr, args.group)
if item:
    count_user_photos(item['nsid'], args.user)
else:
    print('Group not found')


