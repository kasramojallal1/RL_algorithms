import numpy as np
from numpy.core.fromnumeric import argmax

NUM_TRIALS = 10000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class Bandit:
    def __init__(self, p):
        self.p = p
        self.p_estimate = 0
        self.N = 0
        
    def pull(self):
        return np.random.random() < self.p
    
    def update(self, x):
        self.N = self.N + 1
        self.p_estimate = (self.p_estimate * (self.N - 1) + x) / self.N
        
        
def experiment():
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]
    rewards = np.zeros(NUM_TRIALS)
    
    num_times_explored = 0
    num_times_exploited = 0
    num_optimal = 0
    
    optimal_j = np.argmax([b.p for b in bandits])
    print('optimal j:', optimal_j)
    
    for i in range(NUM_TRIALS):
        
        if np.random.random() < EPS:
            num_times_explored += 1
            j = np.random.randint(len(bandits))
        else:
            num_times_exploited += 1
            j = argmax(b.p_estimate for b in bandits)
            
        if j == optimal_j:
            num_optimal += 1
            
        x = bandits[j].pull()
        rewards[i] = x
        bandits[j].update(x)
    

if __name__ == '__main__':
    experiment()