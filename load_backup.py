import shutil

#call this script if you accidentally delete the default data and dont want to take the time to rescrape it.

shutil.copyfile('backup.txt', 'sample_data.csv')