#basic flask app i hope

from flask import Flask, render_template
import abc_news_scraper;

app = Flask(__name__)



@app.route('/')
def index():
    return(abc_news_scraper.getHTML())
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)