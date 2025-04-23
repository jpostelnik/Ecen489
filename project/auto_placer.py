import numpy as np
import matplotlib.pyplot as plt
import gym

class AnalogDesignEnv:
    def __init__(self, target_gain=20, target_bw=100):
        self.target_gain = target_gain
        self.target_bw = target_bw
        self.param_bounds = [1, 10]  # min/max for W1 and W2
        self.reset()

    def reset(self):
        self.params = np.random.uniform(1, 10, size=2)  # [W1, W2]
        return self.params

    def step(self, action):
        self.params += action
        self.params = np.clip(self.params, *self.param_bounds)

        gain = self._simulate_gain(self.params)
        bw = self._simulate_bw(self.params)
        reward = - (abs(gain - self.target_gain) + abs(bw - self.target_bw))  # lower is better

        done = abs(gain - self.target_gain) < 1 and abs(bw - self.target_bw) < 5
        return self.params, reward, done, {'gain': gain, 'bw': bw}

    def _simulate_gain(self, p):
        return 5 * np.log(p[0] + 1) + 2 * np.sqrt(p[1])  # fake but smooth function

    def _simulate_bw(self, p):
        return 200 / (p[0] * p[1])  # inverse relationship

    def render(self):
        print(f"Params: {self.params}, Gain: {self._simulate_gain(self.params):.2f}, BW: {self._simulate_bw(self.params):.2f}")


def train(env, episodes=100):
    best_params = None
    best_reward = -np.inf
    rewards = []

    for ep in range(episodes):
        state = env.reset()
        for step in range(20):
            action = np.random.uniform(-0.5, 0.5, size=2)
            state, reward, done, info = env.step(action)
            if reward > best_reward:
                best_reward = reward
                best_params = state.copy()
            if done:
                break
        rewards.append(best_reward)

    return best_params, rewards
if __name__ == "__main__":
    env = AnalogDesignEnv(target_gain=20, target_bw=100)
    best_params, rewards = train(env)

    print(f"\nBest found parameters: {best_params}")
    env.params = best_params
    env.render()

    # Plot reward over episodes
    plt.plot(rewards)
    plt.title("Reward vs Episodes")
    plt.xlabel("Episode")
    plt.ylabel("Best Reward")
    plt.grid()
    plt.show()

