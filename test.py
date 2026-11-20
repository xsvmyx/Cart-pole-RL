from time import sleep
import sys
import gymnasium as gym
import pygame

env = gym.make("CartPole-v1", render_mode="human")

all_episodes_data = []

for episode in range(5):
    observation, info = env.reset()
    terminated = False
    truncated = False

    episode_observations = []

    print(
        f"Episode {episode + 1} in progress... (Press Esc to quit at any time)"
    )

    while not (terminated or truncated):

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                print("\nUser quit the simulation.")
                env.close()
                pygame.quit()
                sys.exit(0)

        episode_observations.append(observation)

        action = env.action_space.sample()

        observation, reward, terminated, truncated, info = env.step(action)

    all_episodes_data.append(episode_observations)

    print(
        f"-> Episode {episode + 1} completed. "
        f"{len(episode_observations)} observations recorded."
    )

    sleep(1)


env.close()
pygame.quit()