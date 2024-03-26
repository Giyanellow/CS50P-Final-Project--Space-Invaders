# Space Invaders

This project is a rendition of the classic arcade game Space Invaders implemented using the Pygame library. The game involves controlling a spaceship at the bottom of the screen, shooting bullets to destroy descending alien invaders while avoiding their attacks. The player earns points for each alien destroyed and progresses through levels as they eliminate more invaders. With customizable features such as speed adjustments and different alien formations, this Space Invaders game offers a nostalgic yet immersive gaming experience.

## Requirements

- Python 3.6 or higher
- Pygame 2.0.1 or higher

## Installation

1. Clone this repository.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt

```
## How to play
Run the `space_invaders.py` script:

``` bash
python space_invaders.py
```
### Controls 
- Move Left: ```A```
- Move Right: ```D```
- Shoot: ```Space```

### Game Rules
- You lose if your health reaches 0 or if all enemies cross the border.
- You win if you defeat all enemies.

### Features
- Player and enemy health bars
- Random enemy attack intervals
- Score Tracking

### Future Improvements
- Add more levels
- Add power-ups
- Improve enemy AI