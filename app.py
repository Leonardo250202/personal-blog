from flask import Flask, render_template, request

app = Flask(__name__)

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        posts.append({'title': title, 'content': content})
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
