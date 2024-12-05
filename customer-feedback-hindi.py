import random
import pandas as pd
from faker import Faker

fake = Faker('hi_IN')  #hindi locale in faker
feedback_data = []

#providing wiht the sample feedback
feedback_samples = [
    "यह उत्पाद बहुत अच्छा है!",
    "मुझे इसकी गुणवत्ता पसंद नहीं आई।",
    "सेवा बहुत अच्छी थी।",
    "कृपया सुधारें।",
    "बहुत अच्छा अनुभव!",
    "संतुष्ट नहीं हूँ।"
]

#generating random feedback
for _ in range(100):
    feedback_data.append({
        'CustomerID': fake.random_int(min=1, max=100),
        'Name': fake.name(),
        'FeedbackDate': fake.date_this_decade(),
        'FeedbackText': random.choice(feedback_samples),
        'FeedbackScore': random.randint(1, 5)
    })

#creating the pandas DataFrame
df = pd.DataFrame(feedback_data)

# Save to CSV
df.to_csv('customer_feedback_hindi.csv', index=False)
