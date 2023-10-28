from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    new_book = {'title': title, 'author': author}
    books.append(new_book)
    return jsonify({'message': 'Book created successfully'}), 201

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify({'books': books})

@app.route('/books/<int:index>', methods=['GET'])
def get_book(index):
    if 0 <= index < len(books):
        return jsonify(books[index])
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    if 0 <= index < len(books):
        data = request.get_json()
        books[index].update(data)
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    if 0 <= index < len(books):
        books.pop(index)
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
