import numpy as np


NUM_TRIALS = 10000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class Bandit:
    def __init__(self, p):
        self.p = p
        self.p_estimate = np.random.randint(100, 1000)
        self.N = 0
        
    def pull(self):
        return np.random.random() < self.p
    
    def update(self, x):
        self.N = self.N + 1
        self.p_estimate = (self.p_estimate * (self.N - 1) + x) / self.N
        
def experiment():
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]
    
    