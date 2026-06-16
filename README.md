# Custom Snake Game

> Made this game to surprise my friends. Originally put photos of them with sounds affects from our whatsapp voice notes. Was a lot of fun. Thought it would be nice to make it public and generic.
An elegant, highly customizable, and robust Python Snake game built with Pygame. It dynamically loads custom assets and features classic arcade gameplay screens, automatic difficulty progression, and high score persistence!

---

## Features

- **Dynamic Asset Loading and Custom Themes**: Put any of your favorite .png or .jpg images in the resources/ directory and they will automatically become the snake's food options! Place a background.jpg in the folder to set your customized wallpaper.
- **Robust Fallbacks (Zero-Configuration Required)**: Out of the box, if no resources or images are present, the game dynamically falls back to classic vector drawing (rendering a beautiful retro apple and solid dark slate-gray background) so it never crashes!
- **High Score Tracking**: Compete with yourself! High scores are saved locally in highscore.txt and displayed live on-screen during gameplay.
- **Classic Arcade Game States**:
  - **Start Screen**: Press SPACE to play, ESC to quit.
  - **Live Game Screen**: Real-time score and high score.
  - **Game Over Screen**: Play again instantly by pressing R or exit with ESC without ever getting booted back to the desktop!
- **Speed Progression**: The snake moves faster as it eats more food, creating an engaging, challenging difficulty curve.

---

## Requirements and Installation

Make sure you have Python 3.8+ installed.

1. Clone this repository:
   ```bash
   git clone https://github.com/Chaiky3/CustomSnakeGame.git
   cd CustomSnakeGame
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

Simply run:
```bash
python source_code/main.py
```

---

## Asset Customization Guide

You can easily customize the look and sound of the game by editing the resources/ folder.

| Asset Type | Target Filename | Description | Fallback Behavior |
| :--- | :--- | :--- | :--- |
| **Background Wallpaper** | resources/background.jpg | Window size scales automatically to match this image's dimensions. | Classic 800x600 dark slate-gray screen. |
| **Food Stickers** | resources/your_image.png (or .jpg) | Place any number of transparent images here; they are chosen at random. | A beautiful vector-drawn red apple with green leaf. |
| **Eat Sound** | resources/eat.wav | Sound effect played when eating food. | Silent (no crash). |
| **Food Appearance Sound** | resources/mew.wav | Sound effect played when food appears. | Silent (no crash). |

---

## Controls

- **Arrow Keys** (Up, Down, Left, Right) to steer.
- **SPACE** to start playing from the main menu.
- **R** to restart instantly on the Game Over screen.
- **ESC** to quit the game at any point.

---

## License

Distributed under the MIT License (LICENSE).
