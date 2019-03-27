from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def welcome():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'templates')
    app.template_folder = template_dir
    return render_template('index.html')


@app.route('/json-parse', methods=['POST', 'GET'])
def json_parse():
    if request.method == 'POST':
        req_data = request.get_json()
        file_name = req_data['file']
        file_format = req_data['format']
        file_path = req_data['path']

        return '''<h1>Value received to launch spark</h1>
        <h2>File Name is {file}</h2>
        <h2>File Format is {format}</h2>
        <h2>File Path is {path}</h2>'''.format(file=file_name, format=file_format, path=file_path)

    else:
        return '''<h1>This is JsonParse Get Method</h1>'''


if __name__ == '__main__':
    app.run(debug=True)
