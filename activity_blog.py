# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 01:20:28 2021

@author: Abena Laast
"""
#code similar to forum code
def add_to_activities(title, text):
    from datetime import datetime

    #take in input
    #post
    blog_update = text
    #title
    post_title = title
        
    #date and time of submission
    #https://www.programiz.com/python-programming/datetime/current-datetime
    now = datetime.now()
    #month day, year hour:minute:second
    date_n_time = now.strftime("%B %d, %Y %H:%M:%S")
        
    #the complete forum update
    update = post_title+"\n"+blog_update+"\n"+date_n_time+"\n\n"

    #add title, update, date, and time to top of forum
    return(update)

