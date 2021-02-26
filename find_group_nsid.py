import argparse
import sys
import flickrapi
import webbrowser
import json
from auth import authenticate


parser = argparse.ArgumentParser()
parser.add_argument("--text", help="the group name to search for")
args = parser.parse_args()

if args.text == None:
    sys.exit('Must enter --text')

flickr = authenticate()

more = True
page = 1
while more is True:
    info = flickr.groups.search(text=args.text, per_page=100, page=page, format='json')
    info = json.loads(info.decode('utf-8'))
    count = len(info['groups']['group'])
    print('Page number %d, number of items %d' % (page, count))
    if count < 100:
        more = False
    else:
        page += 1
    for item in info['groups']['group']:
        if item['name'] == args.text:
            print(item)
            more = False
            break



