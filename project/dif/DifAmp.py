import gymnasium as gym
import numpy as np
import random

class DiffAmpEnv(gym.Env):  # Make sure it inherits from gymnasium.Env
    def __init__(self):
        super(DiffAmpEnv, self).__init__()

        # Initialize params (ensure it is initialized here)
        self.params = np.zeros(2, dtype=np.float32)  # Example: initializing params as a 2D vector (adjust as needed)
        
        # Define the action and observation space
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(2,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=1.0, high=10.0, shape=(2,), dtype=np.float32)

    def reset(self, seed=None, options=None):
        if seed is not None:
            self.seed(seed)
        
        # Ensure the observation is within the bounds of the observation space
        # You can either sample a valid observation from within the bounds or use a fixed one
        observation = np.random.uniform(low=1.0, high=10.0, size=self.observation_space.shape).astype(np.float32)
        
        info = {}  # Optionally, you can include extra information in this dictionary
        return observation, info
    
    def seed(self, seed=None):
        # Set the random seed for Python, numpy, and any other libraries you use
        random.seed(seed)
        np.random.seed(seed)
        # Optionally, set any other libraries' seed here if needed

    def step(self, action):
        self.params = self.params + action
        self.params = np.clip(self.params, self.observation_space.low, self.observation_space.high)

        # Example metrics (replace with your actual circuit metrics)
        gain = float(self.params[0] * 2)    # dummy calc
        bw = float(self.params[1] * 3)      # dummy calc
        power = float(np.sum(self.params)) # dummy calc

        reward = float(-(gain - 10)**2 - (bw - 1000)**2 - power)  # example reward function
        terminated = False
        truncated = False

        info = {
            "gain": gain,
            "bw": bw,
            "power": power
        }

        return self.params, reward, terminated, truncated, info



