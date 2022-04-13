import urllib
dwn_link = input("enter video link.\n")

file_name = 'trial_video.mp4' 
urllib.retrieve(dwn_link, file_name)
