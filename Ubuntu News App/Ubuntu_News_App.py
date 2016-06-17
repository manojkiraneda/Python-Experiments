# My News App -- Created to push the top News articles onto your ubuntu Notification
# Author   : ManojKiran Eda
# Version  : 1.0
# Date     : June 04-2016
# **********************************************************************************

import gi
gi.require_version('Notify','0.7')
from gi.repository import Notify,GdkPixbuf
import os
import feedparser
import time
import sys

Notify.init("News App")

Notify.init("NewsApp")
notification = Notify.Notification.new("NewsApp Created By ManojKiran !!")

image = GdkPixbuf.Pixbuf.new_from_file("/home/whoami/Pictures/final.png")

notification.set_icon_from_pixbuf(image)
notification.set_image_from_pixbuf(image)
notification.show()


types_articles = int(raw_input("Enter Which types of News Articles You Want : \n 1.Top Stories \n 2.Technology \n 3.Entertainment \n 4.Exit\n Enter Choice : "))

if types_articles == 1:
    news = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
elif types_articles == 2:
    news = feedparser.parse('http://rss.cnn.com/rss/edition_technology.rss')
elif types_articles == 3:
    news = feedparser.parse('http://rss.cnn.com/rss/edition_entertainment.rss')
else:
    sys.exit(0)


for post in news.entries:
    notification = Notify.Notification.new(post.title)
    time.sleep(5)
    notification.show()

