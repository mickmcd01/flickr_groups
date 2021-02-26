import argparse
import sys
import flickrapi
import webbrowser
import json
from flickr_utils import authenticate, get_nsid_for_group


parser = argparse.ArgumentParser()
parser.add_argument("--text", help="the group name to search for")
args = parser.parse_args()

if args.text == None:
    sys.exit('Must enter --text')

flickr = authenticate()

item = get_nsid_for_group(flickr, args.text)
if item:
    print(item)
else:
    print('Group not found')
