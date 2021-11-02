import torch
import numpy as np

class BahdanauAttention(torch.nn.Module):
    def __init__(self, encoder_dim, decoder_dim):
        super().__init__()
        self.encoder_dim = encoder_dim
        self.decoder_dim = decoder_dim
        self.V = torch.nn.Parameter(torch.rand(self.decoder_dim))
        self.W1 = torch.nn.Linear(self.decoder_dim, self.decoder_dim)
        self.W2 = torch.nn.Linear(self.encoder_dim, self.decoder_dim)

    def forward(self, query, values):
        weights = self._get_weights(query,values)
        weights = torch.nn.functional.softmax(weights, dim = 0)
        return weights @ values

    def _get_weights(self, query, values):
        query = query.repeat(values.size(0), 1)
        weights = self.W1(query) + self.W2(values)
        return torch.tanh(weights) @ self.V 

class LuongAttention(torch.nn.Module):
    def __init__(self, encoder_dim: int, decoder_dim: int):
        super().__init__(encoder_dim, decoder_dim)
        self.W = torch.nn.Parameter(torch.FloatTensor(self.decoder_dim, self.encoder_dim).uniform_(-0.1, 0.1))

    def forward(self, query, values):
        weights = self._get_weights(query,values)
        weights = torch.nn.functional.softmax(weights, dim = 0)
        return weights @ values
        
    def _get_weights(self, query, values):
        weights = query @ self.W @ values.T
        return weights/np.sqrt(self.decoder_dim)