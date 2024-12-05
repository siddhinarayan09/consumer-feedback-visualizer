# Customer Feedback Visualizer

This project analyzes and visualizes customer feedback data using natural language processing (NLP) and sentiment analysis techniques. It generates insights by categorizing feedback into sentiment groups and visualizing the results using pie charts.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Output](#output)
- [Acknowledgments](#acknowledgments)

---

## Overview

The **Customer Feedback Visualizer** processes customer feedback data to:
- Preprocess textual data using **spaCy**.
- Perform sentiment analysis using **TextBlob** and **VADER**.
- Categorize feedback into "Satisfactory," "Unsatisfactory," and "Neutral."
- Visualize the results through pie charts.

---

## Features

- **Generate Synthetic Data**: Creates a dataset of 100 customer feedback entries using the Faker library.
- **Preprocessing**: Text preprocessing with stopword removal and tokenization using spaCy.
- **Sentiment Analysis**:
  - TextBlob for polarity scoring.
  - VADER for compound sentiment scoring.
- **Visualization**: Displays sentiment distribution as pie charts for TextBlob and VADER analysis.

---

## Technologies Used

- **Python** (Core Language)
- **pandas** (Data Manipulation)
- **spaCy** (Text Preprocessing)
- **TextBlob** (Sentiment Analysis)
- **VADER Sentiment Analysis** (Sentiment Scoring)
- **Matplotlib** & **Seaborn** (Visualization)
- **Faker** (Synthetic Data Generation)

---

## How It Works

1. **Synthetic Data Generation**:
   - Creates a dataset with `CustomerID`, `Name`, `FeedbackText`, and more using the Faker library.
2. **Text Preprocessing**:
   - Tokenizes text and removes stopwords and punctuation using spaCy.
3. **Sentiment Analysis**:
   - TextBlob analyzes polarity of feedback text.
   - VADER calculates compound sentiment scores.
4. **Categorization**:
   - Scores are categorized into "Satisfactory," "Unsatisfactory," or "Neutral" based on thresholds.
5. **Visualization**:
   - Pie charts are generated to show sentiment distribution.

---

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/customer-feedback-visualizer.git
   cd customer-feedback-visualizer
