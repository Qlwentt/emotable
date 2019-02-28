## Setup
use pipenv for mangaging packages

**install pipenv with homebrew**
```
brew install pipenv
```

If you don't have homebrew [see documentation](https://pipenv.readthedocs.io/en/latest/install/) for installation instructions.


**install dependencies**
```
pipenv install
```

**activate virtual env**
```
pipenv shell
```

## Usage
```
python3 create_model.py
```

## Output
Trains and validates a model on tweet data stored in data directory

```
Epoch 1/10
2019-02-27 17:36:26.288721: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
 - 8s - loss: 0.6093 - acc: 0.6718
Epoch 2/10
 - 8s - loss: 0.2397 - acc: 0.9091
Epoch 3/10
 - 7s - loss: 0.1288 - acc: 0.9502
Epoch 4/10
 - 7s - loss: 0.0960 - acc: 0.9646
Epoch 5/10
 - 7s - loss: 0.0800 - acc: 0.9687
Epoch 6/10
 - 7s - loss: 0.0618 - acc: 0.9718
Epoch 7/10
 - 9s - loss: 0.0547 - acc: 0.9759
Epoch 8/10
 - 7s - loss: 0.0644 - acc: 0.9697
Epoch 9/10
 - 7s - loss: 0.0500 - acc: 0.9789
Epoch 10/10
 - 6s - loss: 0.0439 - acc: 0.9774
487/487 [==============================] - 1s 2ms/step
0.8952772075145886
```
