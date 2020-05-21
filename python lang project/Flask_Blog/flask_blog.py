from flask import Flask, render_template, url_for
app = Flask(__name__)


my_posts = [
    {
        'author': 'Joelly Ekofo Awina Malet',
        'title' : 'Blog post',
        'content' : 'first post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author': 'joel Malet',
        'title' : 'Blog post 2',
        'content' : 'second post content',
        'date_posted' : 'April 21, 2018'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=my_posts)


@app.route('/about')
@app.route('/visit_us')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)  