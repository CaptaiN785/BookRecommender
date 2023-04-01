from flask import Flask, render_template, request, redirect
from filters import BookRecommender

app = Flask(__name__)

br = BookRecommender()
book_list = br.get_book_list()

@app.route("/", methods=["post", "get"])
def home():
    rm_books = []
    isError = False
    if request.method == "POST":
        isbn = request.form["isbn"]
        try:
            rm_books, book_name = br.recommend(isbn)
        except KeyError as e:
            isError = True

    return render_template('index.html', book_list = book_list, 
        rm_books=rm_books, isError = isError, book_name=book_name)

if __name__ == '__main__':
    app.run(debug=True)