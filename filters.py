import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

class BookRecommender:
    def __init__(self):
        self.filter = dict(pickle.load(open('data/final_filter.pkl', 'rb')))
        self.books_df = pd.read_csv('data/book_data.csv')
        print("Every file is loaded successfully...")

    def recommend(self, isbn:str):
        if isbn not in self.filter:
            raise KeyError("Book not Found")
        isbns = self.filter[isbn]
        return self.books_df[self.books_df['ISBN'].isin(isbns)].values,\
             self.books_df[self.books_df['ISBN'] == isbn]['TITLE'].values[0]
    
    def get_book_list(self):
        return dict(self.books_df[['ISBN', 'TITLE']].values)