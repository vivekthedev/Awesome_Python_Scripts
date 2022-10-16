import pyshorteners

# creating shortener object
s = pyshorteners.Shortener()

# get user original link
link = input("enter link ")

# use tinyurl api to shorten
print(s.tinyurl.short(link))
