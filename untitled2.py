import urllib2
dwn_link = input("enter video url:\n")

file_name = 'trial_video.mp4' 
rsp = urllib2.urlopen(dwn_link)
with open(file_name,'wb') as f:
    f.write(rsp.read())