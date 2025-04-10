import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from gymnasium.wrappers import RecordVideo
import os
from IPython.display import HTML, display
from base64 import b64encode

# ==== 1. Przygotowanie środowiska ====
env_id = "Swimmer-v5"
env = make_vec_env(env_id, n_envs=1, seed=0)

# ==== 2. Trening agenta ====
model = PPO(
    "MlpPolicy",
    env,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    gae_lambda=0.95,
    clip_range=0.2,
    ent_coef=0.0,
    verbose=1,
    tensorboard_log="./ppo_swimmer_tensorboard/"
)

rewards = []
episodes = 50
steps_per_episode = 10000

for i in range(episodes):
    model.learn(total_timesteps=steps_per_episode, reset_num_timesteps=False)
    mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=5, render=False)
    rewards.append(mean_reward)
    print(f"Episode {i+1}/{episodes}, Mean reward: {mean_reward}")

model.save("ppo_swimmer_model")
np.save("rewards.npy", rewards)

# ==== 3. Wykres krzywej uczenia ====
plt.figure(figsize=(10, 5))
plt.plot(rewards, marker='o', linestyle='-', color='royalblue')
plt.xlabel("Epizod")
plt.ylabel("Średnia nagroda")
plt.title("📈 Krzywa uczenia dla Swimmer-v5 (PPO)", fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig("learning_curve.png")
plt.show()

# ==== 4. Testowanie i nagrywanie wideo oraz osadzanie ====
video_folder = "videos"
os.makedirs(video_folder, exist_ok=True)

env_test = gym.make(env_id, render_mode="rgb_array")
env_test = RecordVideo(env_test, video_folder=video_folder, episode_trigger=lambda e: True)

model = PPO.load("ppo_swimmer_model")
obs, _ = env_test.reset()

max_steps = 1000
for step in range(max_steps):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env_test.step(action)
    if done or truncated:
        break

env_test.close()

# Znajdź najnowsze wideo
video_files = sorted(
    [f for f in os.listdir(video_folder) if f.endswith(".mp4")],
    key=lambda x: os.path.getmtime(os.path.join(video_folder, x)),
    reverse=True
)
video_path = os.path.join(video_folder, video_files[0])
print(f"Wideo zapisane: {video_path}")

# Wyświetlenie wideo inline
mp4 = open(video_path, "rb").read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
display(HTML(f"<h4>🎬 Działanie agenta PPO w środowisku Swimmer-v5</h4><video width=600 controls><source src='{data_url}' type='video/mp4'></video>"))
