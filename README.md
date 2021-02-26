# flickr_groups
python scripts to help manage flickr groups

Open a browser tab and display the pictures in a group for a particular user:

python show_user_photos.py --group='group-name' --user='user-name'

Count the photos in the group for a user. This requires the NSID for the group:

python count_user_photos.py --group='group-nsid' --user='user-name'

Find the NSID for a group:

python find_group_nsid.py --text='winter landscapes'

These scripts use flickrapi. To install it:

pip install flickrapi



