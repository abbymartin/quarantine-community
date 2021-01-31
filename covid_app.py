import tkinter as tk
from tkinter import *
from tkinter import ttk
import abc_news_scraper
import webbrowser
import covid_forum
import activity_blog

#open article link in browser tab
def open_link(url):
    webbrowser.open_new(url)

#add forum/blog ui and functionality to page
def add_post(tab_num, command):
    page_text = StringVar()
    page_text.set("")

    ttk.Label(tab_num, text="New Post").grid(column=0, row=1, padx=0, pady=2)
    #post titles
    title = ttk.Entry(tab_num)
    title.grid(column=0, row=2, padx=0, pady=5)
    #post body
    desc = tk.Text(tab_num, width=60, height=10)
    desc.grid(column=0, row=3, padx=0, pady=2)

    #submit button
    ttk.Button(tab_num, text ="Submit", command=lambda : submit_post(title, desc, command, page_text)).grid(column=0, row=4, padx=0, pady=5)

    #display all posts
    post = tk.Label(tab_num, textvariable=page_text)
    post.grid(column=0, row=5, padx=0, pady=30)

#handles submit button press on forum/blog
def submit_post(title, body, command, page_text):
    #get text from input boxes
    entry = command(title.get(), body.get("1.0",'end-1c'))
    #clear text boxes
    body.delete('1.0', END)
    title.delete(0, 'end')
    #update forum posts on app
    page_text.set(entry + "\n" + page_text.get())

# intializing the window
window = tk.Tk()
window.title("Quarantine Community")
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
ttk.Label(TAB1, text="Top ABC News Articles on Covid-19", justify='center', font='Helvetica 18 bold').grid(column=0, row=0, padx=300, pady=30)
article_names = abc_news_scraper.get_names()
article_urls = abc_news_scraper.get_URLS()

#loop through articles and display them
for i in range(0, len(article_names), 2):
    ttk.Label(TAB1, text=article_names[i]).grid(column=0, row=i+1, padx=10, pady=5)
    ttk.Button(TAB1, text ="Link", command=lambda aurl=article_urls[i]:open_link(aurl)).grid(column=0, row=i+2, padx=20, pady=5)

#tab 2 (forum)
ttk.Label(TAB2, text="Forum", justify='center', font='Helvetica 18 bold').grid(column=0, row=0, padx=466, pady=30)
add_post(TAB2, covid_forum.add_to_forum)

#tab 3 (activities)
ttk.Label(TAB3, text="Activity Blog", justify='center', font='Helvetica 18 bold').grid(column=0, row=0, padx=430, pady=30)
add_post(TAB3, activity_blog.add_to_activities)


#Calling Main()
window.mainloop()