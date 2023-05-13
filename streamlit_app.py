import streamlit as st
from filters import BookRecommender
from LoadImage import getImage

## Page configuration
st.set_page_config(
    page_title="Book Recommender",
    page_icon="📚",
    layout="wide",
)

st.title("Book Recommender")
st.write("Visit [repo](https://github.com/CaptaiN785/BookRecommender) to get more")
## Instantiate the book recommender and get book list
br = BookRecommender()
book_dict = br.get_book_list()


def show_name(isbn):
    return book_dict[isbn]

isbn = st.selectbox("Select a book", list(book_dict.keys()), format_func=show_name)

if isbn is not None:
    rm_books, book_name = br.recommend(isbn)

    books = iter(rm_books)

    for col in st.columns(5, gap="medium"):
        book = next(books)
        
        img_url = str(book[5])
        col.image(getImage(img_url))
        col.markdown("##### " + str(book[1]))

    st.divider()

    for col in st.columns(5, gap="medium"):
        book = next(books)
        
        img_url = str(book[5])
        col.image(getImage(img_url))
        col.markdown("##### " + str(book[1]))
    st.divider()




