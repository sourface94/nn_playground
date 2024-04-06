import numpy as np


def create_dataset():
    X = np.array([0, 0], [0, 1], [1, 0], [1, 1])
    y = np.array([[0], [0], [1], [1]])
    return X, y


class NN():

    def __init__(self, input_size, hidden_size, output_siz):
        params = init_params(input_size, hidden_size, output_size)

    def init_params(self, input_size, hidden_size, output_size):


    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    def forward(self, X)
        W1, b1, W2, b2 = self.params
