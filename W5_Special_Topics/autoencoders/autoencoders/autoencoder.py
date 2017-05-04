'''
An autoencoder is a type of "unsupervised" or self-supervised neural network.  Autoencoders allow us to take an input vector and embed it into a lower dimensional space.

Base code attained from Keras, check it out for more information on autoencoders --> https://blog.keras.io/building-autoencoders-in-keras.html
'''

from keras.layers import Input, Dense
from keras.models import Model
import keras

import numpy as np
import pandas as pd


def encode(vecs):
    '''Use autoencoder to embed data into a lower dimension
    INPUT: Matrix where each row vector represents you X-variables for a specific observation (documents, images, etc.)
    OUTPUT: Encoded matrix where each row vector represents your X-variables embedded into lower dimensional space
    '''
    # split train and test
    train = vecs[5000:,:]
    test = vecs[:5000,:]
    input_cols = vecs.shape[1]
    input_vec = Input(shape=(input_cols,))
    encoded = Dense(32, activation='relu')(input_vec)
    decoded = Dense(input_cols, activation='sigmoid')(encoded)
    # take in vector and reconstruct it
    autoencoder = Model(input=input_vec, output=decoded)
    # create encoder
    encoder = Model(input=input_vec, output=encoded)
    # final layer encoder input shape
    encoded_input = Input(shape=(32,))
    decoder_layer = autoencoder.layers[-1]
    # create the decoder model
    decoder = Model(input=encoded_input, output=decoder_layer(encoded_input))
    # compile the model
    autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
    # fit the model
    autoencoder.fit(train, train,
                epochs=10,
                batch_size=100,
                shuffle=True,
                validation_data=(test, test))
    # get encoded representations
    encoded_vecs = encoder.predict(np.array(vecs))
    return encoded_vecs



if __name__ == '__main__':
    plt.close('all')
    digits = pd.read_csv('data/digits.csv')
    y = digits.pop('label').values
    X = digits.values
    encoded_repr = encode(X)
