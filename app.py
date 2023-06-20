"""
This is a Flask web application that allows users to create and edit blog posts.
"""
#lib
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the homepage template.
    """
    return render_template('index.html')

@app.route('/create_post')
def create_post():
    """
    Renders the create post template.
    """
    return render_template('create_post.html')

@app.route('/edit_post/<int:post_id>')
def edit_post(post_id):
    """
    Renders the edit post template with the specified post ID.
    """
    return render_template('edit_post.html', post_id=post_id)

if __name__ == '__main__':
    app.run()
