import joblib

# Unpacking our model
model = joblib.load(r'C:\Users\Akars\Desktop\Wipro\Movie Review System\react-flask\backend\tools\review_model')


def predict_review(reviews):
    y_pred = model.predict(reviews['new_review'])
    reviews['prediction'] = y_pred

    # Getting the count of the reviews
    positiveReview = int(reviews['prediction'].value_counts()['positive'])
    negativeReview = int(reviews['prediction'].value_counts()['negative'])

    # Now let us put the movies in 5 categories
    perCentReview = (positiveReview/(positiveReview + negativeReview)) * 100
    print(perCentReview) 

    if (perCentReview <= 20.0):
        return "Hard Pass"
    elif(20.0 < perCentReview and perCentReview <= 30.0):
        return "Bearable"
    elif(30.0 < perCentReview and perCentReview <= 45.0):
        return "Could Watch"
    elif(45.0 < perCentReview and perCentReview <= 70.0):
        return "Worth a Flix"
    elif(70.0 < perCentReview and perCentReview <= 100.0):
        return "How have you not watched it yet??"