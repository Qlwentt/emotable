# figure out how to save and load the model so you don't have to keep building it
from keras.models import load_model
import numpy
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

tk=Tokenizer(num_words=5,split=" ")
model = load_model('sentiment_analysis_model.h5')
x_new = "This is a sad sentence"
x_new=numpy.array([x_new])
# print(text.shape)
tk.fit_on_texts(x_new)
x_new = tk.texts_to_sequences(x_new)
x_new = pad_sequences(x_new, maxlen=31)
x_new = numpy.array([x_new.flatten()])
prediction=model.predict(x_new)

#Preprocess this new sentence.
#Convert the text to vector using word_index
#Pad the vector's with same length as you specified during training
#Flatten the array and pass it as an input to your model


# word_index = imdb.get_word_index()
#
# tokenizer = Tokenizer(num_words=10,split=' ')
# x_new =tokenizer.fit_on_texts(x_new)
# X_new = tokenizer.texts_to_sequences(x_new)
#
# x_test = [[self.word_index[w] for w in sentences if w in self.word_index]]
#
# x_test = pad_sequences(x_test, maxlen=maxlen) # Should be same which you used for training data
#
# vector = np.array([x_test.flatten()])
#
# model.predict_classes(vector)

print(prediction)
print(numpy.argmax(prediction))
