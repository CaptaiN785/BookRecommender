import streamlit as st
from filters import BookRecommender
from PIL import Image
import requests
from io import BytesIO




## Creating the objects of BookRecommender
br = BookRecommender()
book_list = br.get_book_list()
IS_SELECTED = False

## Title
st.title("Book Recommendation System")


def __show_label(option):
    return book_list[option]

## Select box
header = st.container()
option = header.selectbox(
    "Select a book",
    options=list(book_list.keys()),
    format_func=__show_label,
)

st.header("Recommended books...")

## Columns are:
## ISBN,TITLE,AUTHOR,YEAR,PUBLISHER,IMAGE

books = iter(br.recommend(option))

## First layer
results1 = st.container()
for col in results1.columns(5):
    data = next(books)
    img_link = str(data[-1]).replace('http', 'https')
    print(img_link)
    response = requests.get(img_link)
    img = Image.open(BytesIO(response.content))
    col.image(img)
    
## Second layer
results2 = st.container()










if __name__ =='__main__':
    print("App is running...")