import numpy as np 
from PIL import Image
import re
from tensorflow import keras
import pandas as pd 
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
import nltk 
from nltk.stem import WordNetLemmatizer
from keras.utils import pad_sequences
import requests 

category = {
    'home furnishing': 0,
    'baby care': 1,
    'watches': 2,
    'home decor & festive needs': 3,
    'kitchen & dining': 4,
    'beauty and personal care': 5,
    'computers': 6
    }

def category_mapping(idx):
  for key, val in category.items():
    if idx == val:
      return key 

def preprocessing(description, image):
    nltk.download("wordnet")
    nltk.download('omw-1.4')
    df = pd.read_csv('models/flipkart.csv')
    X_train, X_test = train_test_split(df['description'], test_size=0.2, shuffle=True, random_state=2)
    X_test, X_val = train_test_split(X_test, test_size=0.15, shuffle=True, random_state=2)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X_train)
    description_regex = re.sub(r'[^a-zA-Z0-9]', ' ', description)
    X_description_tokens = tokenizer.texts_to_sequences(description_regex)
    lemmatizer = WordNetLemmatizer()
    X_description_lemmatized = [[lemmatizer.lemmatize(str(token)) for token in sequence] for sequence in list(X_description_tokens)]
    description_process = pad_sequences(X_description_lemmatized, maxlen=582)   
    image_process = np.array(Image.open(image).resize((224, 224))).reshape(1, 224, 224, 3) / 255
    return description_process, image_process

def prediction(description, image):
    model = keras.models.load_model('models/model_file/multi_input_2.h5')
    description_process, image_process = preprocessing(description, image)
    softmax_result = np.argmax(model.predict([description_process[0:1], image_process])[0])
    category = category_mapping(softmax_result)
    return category

def post_api(description, image):
    data = {"description": description.tostring(), "img": image.tostring()}
    prediction = requests.post('http://127.0.0.1:5000/predict/', json=data)
    return prediction