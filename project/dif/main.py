import matplotlib.pyplot as plt
from train import *

from draw import *

obs, _ = env.reset()
rewards = []
gains, bws, powers = [], [], []

for _ in range(50):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

    rewards.append(reward)
    gains.append(info["gain"])
    bws.append(info["bw"])
    powers.append(info["power"])
    
    if done:
        break

print(f"Final Params: {obs}")
print(f"Gain: {info['gain']:.2f}, BW: {info['bw']:.2f}, Power: {info['power']:.2f}")

# Plot
plt.figure(figsize=(10, 4))
plt.plot(rewards, label="Reward")
plt.title("Reward during Evaluation")
plt.xlabel("Step")
plt.grid()
plt.legend()
plt.show()


draw_diff_amp(obs)
draw_layout()