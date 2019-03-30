import nltk
from nltk.corpus import stopwords
import string
import random
from nltk.stem import PorterStemmer
from allennlp.predictors.predictor import Predictor
from chatbotscraper import newsapi
def preprocess(input):
    token = nltk.word_tokenize(input)
    remove_tokens = set(stopwords.words('english')+list(string.punctuation))
    ps = PorterStemmer()
    filtered_tokens = []
    for w in token:
        if w not in remove_tokens:
            filtered_tokens.append(ps.stem(w))
    return filtered_tokens

def reply(input,user):
    greeting_inputs = ["hello", "hi", "greetings", "sup", "what's up","hey"]
    greeting_response = ["hi!", "hey!", "hi there!", "hello!"]
    thanking_inputs = ["thank","thankyou"]
    thanking_response = ["You are welcome.","Always a pleasure."]
    leaving_inputs = ["bye"]
    leaving_response = ["Bye! Take care!","GoodBye! See you later!"]
    no_response = ["Sorry! I can't answer this question.", "Sorry! Maybe try asking something else?"]
    for word in input:
        if word in greeting_inputs:
            return random.choice(greeting_response)
        if word in leaving_inputs:
            return random.choice(leaving_response)
        if word in thanking_inputs:
            return random.choice(thanking_response)
        else:
            try:
                query = ""
                phrase = ""
                answers = []
                for i in input:
                    query=query + " " + i
                apiresponseinit=newsapi(query)
                apiresponse=apiresponseinit.getcontent()
                for i in range(3):
                    predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")
                    x1 = predictor.predict(
                        passage=apiresponse[i].text,
                        question=user
                    )
                    answers.append(x1['best_span_str'])
                return answers
            except:
                return random.choice(no_response)
def userinput(input_text):
    user=input_text
    tokens = preprocess(user)
    return(reply(tokens,user))
"""
user = ""
flag = True
while(flag==True):
    user = str(input())
    user = user.lower()
    tokens = preprocess(user)
    print(reply(tokens))
"""
