# 🧠 Rock Paper Scissors AI Bot

This project implements an intelligent Rock, Paper, Scissors (RPS) player function that competes against four different bots, aiming to win at least **60% of the games** in each match. This challenge is part of the [freeCodeCamp Machine Learning with Python](https://www.freecodecamp.org/learn/machine-learning-with-python/) curriculum.

## 🎯 Objective

- Develop a `player()` function in `RPS.py` that plays Rock, Paper, Scissors intelligently.
- Defeat the following four bots with at least **60% win rate**:
  - `quincy`
  - `abbey`
  - `kris`
  - `mrugesh`

## 🧩 How It Works

The `player()` function:
- Remembers previous opponent moves using an optional `opponent_history` parameter.
- Predicts the opponent's next move based on their past patterns.
- Uses a **frequency-based strategy** with **sliding window memory** to detect common sequences.
- Counters the predicted move using the classic RPS rules:
  - Rock ➡ Paper
  - Paper ➡ Scissors
  - Scissors ➡ Rock

## 🗃️ File Structure

```

📁 RockPaperScissors/
│
├── RPS.py         # ← Your AI logic goes here (edit only this file)
├── RPS\_game.py    # ← Game engine (do not modify)
├── main.py        # ← Use this to test your bot
└── test\_module.py # ← Unit tests (auto-run from main.py if uncommented)

````

## 🛠️ How to Run

To test the bot against a specific opponent, use the `play()` function in `main.py`:

```python
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

print(play(player, quincy, 1000))
print(play(player, abbey, 1000))
print(play(player, kris, 1000))
print(play(player, mrugesh, 1000))
````

You can also enable verbose mode to see individual moves:

```python
play(player, quincy, 1000, verbose=True)
```

To run all unit tests:

```python
# Uncomment this line in main.py:
# test_module.test(player)
```

## 📈 Strategy Overview

* **Pattern Detection**: Tracks opponent’s last two moves to predict the third.
* **Move Prediction**: Uses a Markov Chain-like frequency table to guess the next move.
* **Adaptive Countering**: Chooses the counter move that beats the predicted play.

## ✅ Success Criteria

To pass the challenge, your player must win **at least 60% of the matches** against each bot across 1000 games.

## 🚀 Deployment

This project runs in the Gitpod IDE or any Python environment.

> Note: Submit the final GitHub repository URL to freeCodeCamp once your bot consistently wins.

## 🧑‍💻 Author

Built as part of the **freeCodeCamp Machine Learning Certification** project by \[Your Name].

---

Feel free to fork, experiment with smarter strategies, or plug in more advanced ML models!
