import pandas as pd
from faker import Faker
from textblob import TextBlob
import nltk
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
from 
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
fake = Faker()
import random

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

spark = SparkSession.builder \
    .appName("Customer Feedback Analysis") \
    .getOrCreate()

file_location = r"C:\Users\TUF GAMING\Desktop\customer-feedback-visualizer\customer_feedback.csv"
filetype = "csv"

df_spark = spark.read.format(filetype).option("header", "true").option("sep", ",").load(file_location)
df_filtered = df.filter(col("CustomerId").rlike("^[0-9]+$"))
df.createOrReplaceTempView("customer_feedback")

df_filtered.show()
