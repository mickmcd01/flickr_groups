# flickr_groups
python scripts to help manage flickr groups

Open a browser tab and display the pictures in a group for a particular user (note that the group name is as it appears in a typical flickr url):

    python show_user_photos.py --group='group-name' --user='user-name'
    python show_user_photos.py --group='winterlandscapes' --user='mick mcd'

Count the photos in a group for a user:

    python count_user_photos.py --group='group name' --user='user-name'
    python count_user_photos.py --group='winter landscapes' --user='mick mcd'

Find the NSID for a group:

    python find_group_nsid.py --text='winter landscapes'

These scripts use flickrapi. To install it:

    pip install flickrapi



