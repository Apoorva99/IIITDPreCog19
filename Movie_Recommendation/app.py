#Import Dependancies
from flask import Flask, render_template,request,url_for
from math import sqrt
import pandas as pd
import random
import numpy as np
from scipy.sparse.linalg import svds
from pymongo import MongoClient
import csv
app = Flask(__name__)


client = MongoClient("mongodb+srv://apoorva:Run15jhun@cluster0-tlbtp.mongodb.net/test?retryWrites=true")
db = client.recomm
Collection_IMDB_ScrapedData = db.IMDB_ScrapedData
Collection_Movies = db.Movies

@app.route('/')
def home():	
	def Generate_Random_movies():
		count = Collection_IMDB_ScrapedData.count()
		return Collection_IMDB_ScrapedData.find()[random.randrange(count)]

	info = []
	for i in range(1,50):
		movie = Generate_Random_movies()
		info.append(movie)
		
	return render_template('index1.html' , info = info)


@app.route('/prediction', methods=['POST'])
def prediction():
	
	userId = 1000
	if request.method == 'POST':
		result = request.form.to_dict()
		movieId = []
		ratings = []
		for x in result:
			movieId.append(int(x))
			ratings.append(result[x])
		num=0;
		for x in ratings:
			if x == '':
				ratings[num]=0
			else:
				ratings[num] = int(x)

			num=num+1
		
		Movies = pd.read_csv("ml-latest-small/IIITDPreCog_movies.csv")
		Movies = Movies.drop(Movies.columns[0], axis=1)
		Ratings = pd.read_csv("ml-latest-small/IIITDPreCog_ratings.csv")
		Ratings = Ratings.drop(Ratings.columns[0], axis=1)

		for i in range(len(movieId)):
			l = [userId,movieId[i],ratings[i],0]
			temp_dataframe = pd.DataFrame([l],columns=['userId','movieId','rating','timestamp'])
			
			Ratings= pd.concat([Ratings,temp_dataframe])
			Ratings = Ratings.reset_index(drop=True)
		
					

		def Similarity_score(user1,user2):

		    # Items rated by person1 as well as person2
			viewed = {}

			for item in user_movie[user1]:
				if item in user_movie[user2]:
					viewed[item] = 1
				 #Length of items viewed by both users
				if len(viewed) == 0:
					return 0
				number_of_ratings = 3
				# Checking for number of ratings in common
				if number_of_ratings == 0:
					return 0
		    	 	

		    #Calculate Euclidean distance
			eclidean_distance_sum = []
			for item in user_movie[user1]:
				if item in user_movie[user2]:
					eclidean_distance_sum.append(pow(user_movie[user1][item] - user_movie[user2][item],2))
				sums = 0
				for i in eclidean_distance_sum:
					sums = sums + i

			return 1/(1+sqrt(sums))   


	
	    
		def user_recommed(user):

		    # Gets recommendations for a user by using a weighted average of every other user's Standing_movie
		    totals = {}
		    Sum_similarity = {}
		    Standing_movie_list =[]
		    for other in user_movie:
		        if other == user:
		            continue
		        similarity = Similarity_score(user,other)
		        

		        # ignore scores of zero or lower
		        if similarity <=0: 
		            continue
		        for movie in user_movie[other]:

		            # only score movies i haven't seen yet
		            if movie not in user_movie[user] or user_movie[user][movie] == 0:

		            # Similrity * score
		                totals.setdefault(movie,0)
		                totals[movie] += user_movie[other][movie]* similarity
		                # sum of similarities
		                Sum_similarity.setdefault(movie,0)
		                Sum_similarity[movie]+= similarity

		        # Create the normalized list

		    Standing_movie = [(total/Sum_similarity[movie],movie) for movie,total in totals.items()]
		    Standing_movie.sort()
		    Standing_movie.reverse()
		    # returns the recommended movies
		    recommendataions_list = [recommend_movie for score,recommend_movie in Standing_movie]
		    return recommendataions_list[:15] 
		df = pd.merge(Ratings, Movies, on='movieId')
		df1 = df[['userId','title','rating']]
		Dictionary_1 =df1.groupby('userId')[['title','rating']].apply(lambda g: g.values.tolist()).to_dict()
		for key in Dictionary_1:
			Dictionary_1[key]=dict(Dictionary_1[key])
		user_movie = Dictionary_1
		result = predictions = user_recommed(userId)

		info = []
		def Info_doc(pymong):
			for y in pymong:
				return dict(y)
		for x in result:
			myquery = { "Title": x }
			mydoc = Collection_IMDB_ScrapedData.find(myquery)
			info.append(Info_doc(mydoc))


		return render_template("result1.html",info = info )


if __name__ == '__main__':
	app.debug = True

	app.run()
