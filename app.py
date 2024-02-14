from flask import Flask, render_template
import markdown

app = Flask(__name__)
def read_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return markdown.markdown(content, extensions=['extra', 'sane_lists', 'meta'])

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def site(u_path):
    data = read_markdown_file('DATA.md')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)