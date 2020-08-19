from flask import Flask, render_template, request, redirect
app = Flask(__name__)



import numpy
import pandas
import sklearn
import pickle
import cv2


def classify(text):
	loaded_model= pickle.load( open( "model_nlp.pkl", "rb" ) )
	predict_this=loaded_model.predict([text])

	if predict_this[0]==0:
		return 'Negative Review'
	else:
		return 'Positive Review'

	# return predict_this



# print(classify('Absolutely loved the movie and its character so well directed. Enjoyed it thoroughly. Great work! hope such work continues.'))


@app.route("/")
@app.route("/Home" , methods=["GET","POST"])
def home():
	
	if request.method=="POST":
		try:
			rev=str(request.form["user_review"])
			# a='good'
			return render_template("movie_review_nlp.html", ans=classify(rev))
		except:
			return "Something went wrong."

	return render_template("movie_review_nlp.html", ans='ok')




if __name__ == "__main__":
    app.run(debug=True)





