from survey import AnonymousSurvey
def test_fruit_survey():
    question = "Which fruit do you like?"
    fruit_survey = AnonymousSurvey(question)
    fruits = ['apple','strewbarry','banana','peach']
    for fruit in fruits:
        fruit_survey.stored_response(fruit)
    for i in fruits:
        assert i in fruit_survey.reponses