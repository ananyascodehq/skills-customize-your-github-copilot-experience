# 📘 Assignment: Reaction Timer Game

## 🎯 Objective

Build a simple reaction timer game that measures how quickly a player responds to a prompt. Students will practice event-driven input, timing, and simple state tracking.

## 📝 Tasks

### 🛠️ Build the Reaction Timer

#### Description
Create a program that waits a random short delay, prompts the player to respond, and measures the time between the prompt and the player's response. Allow multiple rounds and show per-round and summary statistics.

#### Requirements
Completed program should:

- Prompt the player to start a round and wait a random delay before signaling "GO!".
- Measure and display the reaction time (in milliseconds) for each round.
- Allow the player to play a configurable number of rounds (minimum 3).
- After all rounds, display the best, worst, and average reaction times.
- Include a brief usage example.

#### Example

Run the program and follow on-screen prompts. Example output:

```
Round 1: Get ready...
GO!
Your reaction: 312 ms

Round 2: Get ready...
GO!
Your reaction: 278 ms

Summary: Best=278 ms, Worst=312 ms, Avg=295 ms
```

Use the provided `starter-code.py` to get started and modify or extend it as desired.
