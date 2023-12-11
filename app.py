from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [
    {
        "id": 0,
        "author": "J. R. R. Tolkien",
        "language": "English",
        "title": "The Lord of the rings"
    }
]

@app.route('/')
def index():
    return 'Hello World'

@app.route('/<name>')
def print_name(name):
    return f"Hello {name}"

@app.route('/books', methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if len(book_list) > 0:
            return jsonify(book_list), 201
        else:
            'Error - Nothing Found', 404

    if request.method == 'POST':
        new_author = request.form['author']        
        new_language = request.form['language']
        new_title = request.form['title']
        new_id = book_list[-1]['id'] + 1

        new_obj = {
            "id": new_id,
            "author": new_author,
            "language": new_language,
            "title": new_title
        }

        book_list.append(new_obj)

        return jsonify(book_list), 201

if __name__ == '__main__':
    app.run(debug=True)