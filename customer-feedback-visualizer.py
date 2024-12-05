import pandas as pd
from faker import Faker
from textblob import TextBlob
#import nltk
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
fake = Faker()
import random

#nltk.download('punkt')
#nltk.download('stopwords')

nlp = spacy.load('en_core_web_sm')
analyzer = SentimentIntensityAnalyzer()

data = {
    'CustomerID': [i for i in range(1, 101)],
    'Name': [fake.name() for _ in range(100)],
    'FeedbackDate': [fake.date_this_decade() for _ in range(100)],
    'FeedbackText': [fake.text() for _ in range (100)],
    'FeedbackScore': [random.randint(1,5) for _ in range(100)]

}

df = pd.DataFrame(data)

df.to_csv('customer_feedback.csv', index = False)
#print("csv file created successfully.")

#def preprocess_text(text):
   # tokens = nltk.word_tokenize(text.lower())
   # stop_words = set(nltk.corpus.stopwords.words('english'))
   # filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
   # return ' '.join(filtered_tokens)

#df['ProcessedFeedback'] = df['FeedbackText'].apply(preprocess_text)*//

def preprocess_text_spacy(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if not token.is_stop and not token.is_punct]

df['ProcessedFeedback'] = df['FeedbackText'].apply(preprocess_text_spacy)


#sentiment analysis using textblob
def get_sentiment_textblob(tokens):
    text = " ".join(tokens)
    blob = TextBlob(text)
    return blob.sentiment.polarity

df['SentimentTextBlob'] = df['ProcessedFeedback'].apply(get_sentiment_textblob)


#sentiment analysis using VADER
def get_sentiment_vader(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']

df['SentimentVader'] = df['FeedbackText'].apply(get_sentiment_vader)

#categorising the sentiments into unsatisfactory, satisfactory and neutral
def categorize_sentiment_custom(score):
    if score > 0.1:
        return 'Satisfactory'
    elif score < -0.1:
        return 'Unsatisfactory'
    else:
        return 'Neutral'

#categorisation fro textblob and vader
df['SentimentCategoryTextBlob'] = df['SentimentTextBlob'].apply(categorize_sentiment_custom)
df['SentimentCategoryVader'] = df['SentimentVader'].apply(categorize_sentiment_custom)

#counting th number of occurences of each sentiment category
sentiment_counts_textblob = df['SentimentCategoryTextBlob'].value_counts()
sentiment_counts_vader = df['SentimentCategoryVader'].value_counts() 

#pie chart for textblob sentiment distribution
plt.figure(figsize=(8, 6))
plt.pie(sentiment_counts_textblob, labels = sentiment_counts_textblob.index, autopct = '%1.1f%%', startangle = 140)
plt.title('Sentiment distribution by Textblob')
plt.axis('equal') #to ensure that the pie chart is circular.
plt.show()
#thank you beyonce

#pie chart for Vader Sentiment Distribution
plt.figure(figsize=(8, 6))
plt.pie(sentiment_counts_vader, labels = sentiment_counts_vader.index, autopct = '%1.1f%%', startangle = 140)
plt.title('Sentiment Distribution by VADER')
plt.axis('equal')
plt.show()
#thankyou beyonce yet again