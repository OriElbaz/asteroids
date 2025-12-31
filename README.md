# Asteroids

A Python implementation of the classic arcade game "Asteroids," built using [Pygame](https://www.pygame.org/).

## Overview

This project recreates the core mechanics of Asteroids, featuring ship movement, shooting mechanics, and asteroid collisions. The game loop handles entity updates, drawing, and collision detection (both ship-to-asteroid and bullet-to-asteroid).

## Features

* **Player Control:** Piloting mechanics (movement and rotation).
* **Combat:** Shooting mechanism with collision detection.
* **Asteroid Mechanics:** Asteroids spawn via an `AsteroidField` and split into smaller chunks when hit.
* **Event Logging:** Custom logging for game states and specific events (e.g., `player_hit`, `asteroid_shot`).

## Prerequisites

To run this project, you will need:

* **Python 3.13**
* **[uv](https://github.com/astral-sh/uv)** (An extremely fast Python package installer and runner).

## How to Run

This project uses `uv` for dependency management and execution.

1.  **Clone the repository** (or navigate to your project folder).
2.  **Run the game** using the following command:

```bash
uv run ./main.py

```

*Note: `uv` will automatically handle the installation of `pygame` and any other dependencies defined in your project environment.*

## Controls

* **Rotate:** Keys or A/D
* **Thrust:** W Key
* **Reverse:** S Key
* **Shoot:** Spacebar
* **Quit:** Close window

