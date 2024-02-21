from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
app = Flask(__name__)

books = [{'title': 'Software Engineering', 'id': '1'}, \
		 {'title': 'Algorithm Design', 'id':'2'}, \
		 {'title': 'Python', 'id':'3'}]

@app.route('/book/JSON')
def bookJSON():
	r = json.dumps(books)
	return r


@app.route('/')
@app.route('/book/')
def showBook():
	return render_template('showBook.html', books = books)


@app.route('/book/new/', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        new_entry = request.form['name']
        books.append({'title': new_entry, 'id': len(books)+1})
        return render_template('showBook.html', books = books)
    return render_template('newBook.html', books = books)


@app.route('/book/<int:book_id>/edit/', methods=['GET','POST'])
def editBook(book_id):
    if request.method == 'POST':
        search_key = request.form['name']
        for oneBook in books:
            if int(oneBook['id']) == book_id :
                if len(str(search_key)) != 0:
                    oneBook['title'] = str(search_key)
            return render_template('showBook.html', books = books)  
    else:
        return render_template('editBook.html', book_id = book_id)  


@app.route('/book/<int:book_id>/delete/', methods = ['GET', 'POST'])
def deleteBook(book_id):
    if request.method == 'POST':
        bookIndex = next((index for (index, oneBook) in enumerate(books) if int(oneBook['id']) == book_id), None)
        del books[bookIndex]
        return render_template('showBook.html', books = books)
    else:
        for oneBook in books:
            if int(oneBook['id']) == book_id :
                book_title = oneBook['title']
                return render_template('deleteBook.html', book_id = book_id, book_title = book_title, books = books)
  

if __name__ == '__main__':
	# app.debug = True
	# app.run(host = '0.0.0.0', port = 5000)
 	app.run(debug=True)