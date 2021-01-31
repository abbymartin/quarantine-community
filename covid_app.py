import tkinter as tk
from tkinter import *
from tkinter import ttk
import abc_news_scraper
import webbrowser
import covid_forum
import activity_blog

# intializing the window
window = tk.Tk()
window.title("Hackathon Project")
# configuring size of the window 
window.geometry('1000x1000')
#Create Tab Control
TAB_CONTROL = ttk.Notebook(window)
#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='News')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Forum')
#Tab3
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Activities')

TAB_CONTROL.pack(expand=1, fill="both")


#tab 1 (articles)
def open_link(url):
    webbrowser.open_new(url)

ttk.Label(TAB1, text="Top ABC News Articles on Covid-19", justify='center', font='Helvetica 18 bold').grid(column=0, row=0, padx=300, pady=30)
article_names = abc_news_scraper.get_names()
article_urls = abc_news_scraper.get_URLS()

#loop through articles and display them
for i in range(0, len(article_names), 2):
    ttk.Label(TAB1, text=article_names[i]).grid(column=0, row=i+1, padx=10, pady=5)
    ttk.Button(TAB1, text ="Link", command=lambda aurl=article_urls[i]:open_link(aurl)).grid(column=0, row=i+2, padx=20, pady=5)


#tab 2 (forum)
forumtext = StringVar()
forumtext.set("")

def submit(): 
    entry = covid_forum.add_to_forum(title.get(), text.get("1.0",'end-1c'))
    text.delete('1.0', END)
    title.delete(0, 'end')
    forumtext.set(entry + "\n" + forumtext.get())

ttk.Label(TAB2, text="Forum", justify='center', font='Helvetica 18 bold').grid(column=0, row=0, padx=480, pady=30)
ttk.Label(TAB2, text="New Post").grid(column=0, row=1, padx=0, pady=2)
#post titles
title = ttk.Entry(TAB2)
title.grid(column=0, row=2, padx=0, pady=5)
#post body
text = tk.Text(TAB2, width=60, height=10)
text.grid(column=0, row=3, padx=0, pady=2)

#submit button
ttk.Button(TAB2, text ="Submit", command=submit).grid(column=0, row=4, padx=20, pady=5)

#posts
post = tk.Label(TAB2, textvariable=forumtext)
post.grid(column=0, row=5, padx=0, pady=30)


#tab 3 (activities)
activitytext = StringVar()
activitytext.set("")

def add_activity(): 
    entry = activity_blog.add_to_activities(activity.get(), desc.get("1.0",'end-1c'))
    desc.delete('1.0', END)
    activity.delete(0, 'end')
    activitytext.set(entry + "\n" + activitytext.get())

ttk.Label(TAB3, text="Activity Blog", justify='center', font='Helvetica 18 bold').grid(column=0, row=0, padx=480, pady=30)
ttk.Label(TAB3, text="New Post").grid(column=0, row=1, padx=0, pady=2)
#post titles
activity = ttk.Entry(TAB3)
activity.grid(column=0, row=2, padx=0, pady=5)
#post body
desc = tk.Text(TAB3, width=60, height=10)
desc.grid(column=0, row=3, padx=0, pady=2)

#submit button
ttk.Button(TAB3, text ="Submit", command=add_activity).grid(column=0, row=4, padx=20, pady=5)

#posts
blog = tk.Label(TAB3, textvariable=activitytext)
blog.grid(column=0, row=5, padx=0, pady=30)



#Calling Main()
window.mainloop()