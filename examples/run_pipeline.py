"""Example: load an action and run it on an image."""
from PIL import Image

from photocraft.core import load_action, run_action


if __name__ == "__main__":
    img = Image.open("input.jpg")  # replace with your own image
    action = load_action("actions/grayscale.json")
    out = run_action(img, action)
    out.save("output.png")
    print("Done -> output.png")
