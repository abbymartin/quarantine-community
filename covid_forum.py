# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:02:03 2021

@author: Abena Laast
"""
def add_to_forum(title, post):
    from datetime import datetime
    #content
    forum_update = post
    #title
    forum_title = title
    
    #date and time of submission
    #https://www.programiz.com/python-programming/datetime/current-datetime
    now = datetime.now()
    #month day, year hour:minute:second
    date_n_time = now.strftime("%B %d, %Y %H:%M:%S")
    
    #the complete forum update
    update = forum_title+"\n"+forum_update+"\n"+date_n_time+"\n\n"
    
    #add title, update, date, and time to top of forum
    return(update)

