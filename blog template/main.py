from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

URL = 'https://api.npoint.io/c790b4d5cab58020d391'

response = requests.get(URL)

posts = response.json()



@app.route('/blog')
def home():
    return render_template("index.html", post = posts)



@app.route('/post/<id>')
def blog(id):
    index = int(id) - 1  # Adjusting index to match list index (starting from 0)
    
    if 0 <= index < len(posts):
        post = posts[index]
        return render_template('post.html', title=post['title'], subtitle=post['subtitle'], body=post['body'])
    else:
        return render_template('post_not_found.html')


if __name__ == "__main__":
    app.run(debug=True)


