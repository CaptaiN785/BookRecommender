# Book Recommender
![Screenshot (6)](https://user-images.githubusercontent.com/83746932/229270172-3796326b-411b-4994-9537-c791b90390fc.png)

**Simulation link: https://captain785-bookrecommender-streamlit-app-nwwk6d.streamlit.app/**

## Overview
The method used to create a recommendation system is collaborative filtering and will use centered cosine  similarity. It uses the matrix of books isbn as row and userid in columns and rating as values.
<pre>
ISBN\USERID | user_1 | user_2 | .....
1223334487  |    3   |   8    | .....
8873122330  |    0   |   1    | .....
..
..
</pre>

## Use
<pre>

git clone https://github.com/CaptaiN785/BookRecommender.git

cd BookRecommender

python flask_app.py

</pre>

