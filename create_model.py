import os, sys
import pandas
import numpy
import keras
import json
from definitions import ROOT_DIR
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.layers import Embedding, LSTM, Dense
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


data_path = "{0}/data/tweets".format(ROOT_DIR)
tweet_files = os.listdir(data_path)
tweet_dfs = []

for file in tweet_files:
    tweet_df = pandas.read_csv(data_path + '/' + file)
    tweet_dfs.append(tweet_df)

all_tweets_df = pandas.concat(tweet_dfs)

x_var_tweets = all_tweets_df['tweet_text'].tolist()
y_var_labels = all_tweets_df['sentiment'].tolist()

print(x_var_tweets[2])
print(y_var_labels[2])

x = x_var_tweets
y = y_var_labels

tokenizer = Tokenizer(num_words=3000,split=' ')
tokenizer.fit_on_texts(x)
X = tokenizer.texts_to_sequences(x)
X = pad_sequences(X, maxlen=31)

Y = []
for val in y:
    if(val == 0):
        Y.append([1,0])
    else:
        Y.append([0,1])
Y = numpy.array(Y)

x_train, x_test, y_train, y_test = train_test_split(X,Y,train_size=0.8)


model = Sequential()
model.add(Embedding(3000,128,input_length=X.shape[1],dropout=0.2))
model.add(LSTM(300, dropout_U=0.2,dropout_W=0.2))
model.add(Dense(2,activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,optimizer='adam',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10,verbose=2,batch_size=32)

print(model.evaluate(x_test,y_test)[1])

model.save('sentiment_analysis_model.h5')
