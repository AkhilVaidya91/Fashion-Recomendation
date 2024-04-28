import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

df = pd.read_csv('styles.csv')

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')

def extract_keywords(sentence):
    words = word_tokenize(sentence)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    return lemmatized_words

user_input = "white dress that is worn by not men"

tokens = extract_keywords(user_input)
print(tokens)

def search_keywords(tokens, df):
    matching_ids = []
    
    for i in range(0, len(df)):
        text = str(str(df.iloc[i, 1]) + str(df.iloc[i, 2]) + str(df.iloc[i, 3]) + str(df.iloc[i, 4]) + str(df.iloc[i, 5]) + str(df.iloc[i, 6]) + str(df.iloc[i, 7]) + str(df.iloc[i, 9])).lower()
        count = 0
        for token in tokens:
            if text.find(token) != -1:
                count += 1
            if count >= 3:
                filename = str(df.iloc[i, 0]) + ".jpg"
                matching_ids.append(filename)
        if len(matching_ids) == 50:
            break
    matching_ids = list(set(matching_ids))

    return matching_ids

# matching_ids = search_keywords(tokens, df)
# print(matching_ids)
