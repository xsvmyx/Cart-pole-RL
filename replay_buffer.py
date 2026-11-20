from collections import deque
import random


class ReplayBuffer:

  def __init__(self, capacity):
    self.buffer = deque(maxlen=capacity)

  def push(self, state, action, reward, next_state, done):
    """Enregistre une transition (s, a, r, s', done)"""
    self.buffer.append((state, action, reward, next_state, done))

  def sample(self, batch_size):
    """Pioche un mini-batch aléatoire d'expériences"""
    return random.sample(self.buffer, batch_size)

  def __len__(self):
    return len(self.buffer)