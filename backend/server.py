# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

import tools.webScraper as sc
import tools.cleaner as cl
import tools.model as model

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app)

# Creating a demo method
@app.route('/hi', methods=['GET'])
def hi():
	return jsonify({'hello':'World'})


# Creating the search method
@app.route('/search', methods=['POST'])
def search():
	movie_name = request.json['content']

	# Data processing part
	# Let's get the reviews of the movie using our webscraper
	[img_url, url, director_name, description, stars, Actors, reviews, movie_name] = sc.getting_reviews(movie_name)
	print([[img_url, url, movie_name, director_name, description, stars, Actors, reviews]])
	print("Done Getting the Reviews")
	# Let us now clean our data using our clearner.py
	reviews['new_review'] = reviews['review'].apply(lambda text: cl.updated_cleaner(text))
	print("Done Cleaning the Reviews")

	# Predicting the reviews and adding it to the final dataset
	review = model.predict_review(reviews)
	print(review)

	# For now, Let's just return the query as it is
	return jsonify({'result': review, "poster": img_url, "url": url, "movie_name": movie_name, "director_name": director_name, "description": description, "stars": stars, "Actors": Actors})

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)
