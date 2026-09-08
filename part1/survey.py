class AnonymousSurvey:
    def __init__(self,question):
        self.question=question
        self.reponses=[]

    def show_quesion(self):
        print(self.question)

    def stored_response(self, new_response):
        self.reponses.append(new_response)

    def show_response(self):
        for response in self.reponses:
            print(response)
