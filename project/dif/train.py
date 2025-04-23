from DifAmp import DiffAmpEnv
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

env = DiffAmpEnv()
check_env(env)  # ✅ Now works

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("ppo_diffamp")
