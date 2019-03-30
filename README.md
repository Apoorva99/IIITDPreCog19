# Movie Recommendation System (IIITD PreCog'19)

The project explores three different algorithms to recommend K movies provided that user has already rated some movies.
  The dataset used has been downloaded from (http://files.grouplens.org/datasets/movielens/ml-latest-small.zip) which contained movies along with ratings according to different users. 
  A web scraping script has been used to scrape about 780 movies from IMDB containing particulars about title, year of release, thumbnail, IMDB rating and Synopsis.
## Getting Started

Install all the requirements using 
```
pip install requirements.txt

```
Run the application using
```
python app.py

```

### File Structure

* Web based application using Heroku by **User Based collaborative filtering** (https://movierecomm388.herokuapp.com/?fbclid=IwAR2V_f2cSfglqHSVNx3-pM9yrdVEju64SJ-AgyOml0WD1p2Q3x0uYrN0CFM).
* The ipynb notebooks for **Matrix Factorization Method** and **Item based collaborative filtering** algorithms has been uploaded in Notebooks directory.
* **The web application was only deployed for the standout performing technique of **User Based collaborative filtering.**

## Execution

The data was scraped from IMDB website and uploaded on [mLab](https://mlab.com/) and the whole execution was carried out using [Heroku](https://www.heroku.com/).

## Dataset
The dataset used is a subsample of original Movielens dataset containing data of about 780 movies.
The datafiles include-
* **IIITDPreCog_movies** - Title of movies mapped with movieId.
* **IIITDPreCog_ratings** - movieId mapped with user ratings.
* **IIITDPreCog_IMDB_scraped** - Scraped data from IMDB website containing Title,year of release, IMDB rating, thumbnail and Synopsis.


