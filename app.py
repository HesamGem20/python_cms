from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_post')
def create_post():
    return render_template('create_post.html')

@app.route('/edit_post/<int:post_id>')
def edit_post(post_id):
    return render_template('edit_post.html', post_id=post_id)

if __name__ == '__main__':
    app.run()
