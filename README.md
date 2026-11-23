# CartPole with Deep Q-Learning (DQN)

This is my beginner Reinforcement Learning (RL) project.  
I trained an AI agent to balance a pole on a moving cart using **PyTorch** and **Gymnasium**.

---

## 🎯 Goal

In CartPole-v1, a pole is attached to a cart. The cart moves left or right.  
The goal is to keep the pole upright for as long as possible (up to 500 steps).

---

## 🧠 How It Works

- **Algorithm**: Deep Q-Network (DQN)
- **Observations** (4 inputs):
  1. Cart position
  2. Cart velocity
  3. Pole angle
  4. Pole angular velocity
- **Actions** (2 choices):
  - `0`: Push cart left
  - `1`: Push cart right
- **Reward**: `+1` for every step the pole stays balanced.
- **Experience Replay**: Stores transitions `(state, action, reward, next_state, done)` to break correlations.
- **Target Network**: A copy of the network to make training stable.

---

## 📁 Project Structure

```text
├── model.py           # Neural network architecture (DQN in PyTorch)
├── replay_buffer.py   # Replay memory buffer
├── notebook.ipynb     # Main Jupyter notebook (training & evaluation)
├── test.py            # Quick test script
├── pyproject.toml     # Python dependencies
└── README.md          # Project documentation
```

---

## 🚀 How to Run

### 1. Install dependencies

Using `uv`:
```bash
uv sync
```

Or with standard `pip`:
```bash
pip install gymnasium pygame torch matplotlib numpy
```

### 2. Train the agent

Open and run the notebook:
```bash
jupyter notebook notebook.ipynb
```
Run the cells from top to bottom to train the agent and watch the evaluation with graphics.

---

## 📊 Results

- At the start, the agent fails quickly (rewards ~10 to 20).
- After training, the agent easily reaches the maximum score of **500.0** points!

