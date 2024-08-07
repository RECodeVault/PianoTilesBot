import numpy as np
import pyautogui
import cv2
import keyboard
import time
import threading


def take_screenshot():
    """
    Takes screenshot and returns image as a numpy array
    :return: Image
    """
    image = pyautogui.screenshot(region=(665, 165, 551, 850))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)


def is_tile(pixel_value):
    """
    Checks if the pixel is black, meaning it is tile
    :param pixel_value:
    :return:
    """
    return pixel_value == 0


def move_and_click(x, y):
    """
    Move and click
    :param x: x position
    :param y: y position
    """
    pyautogui.moveTo(x, y)
    pyautogui.click()


def main():
    print("Ready: ")
    count = 5
    while count > 0:
        print(count)
        count -= 1
        time.sleep(1)

    bar_width = 1
    positions = [44, 187, 326, 472]
    step = 50

    while True:
        if keyboard.is_pressed('s'):
            exit()

        image_array = take_screenshot()
        found_tile = False

        for y in reversed(range(0, len(image_array), step)):
            if found_tile:
                break
            for x_start in positions:
                for x in range(x_start, x_start + bar_width, step):
                    pixel = image_array[y, x]
                    if is_tile(pixel):
                        threading.Thread(target=move_and_click, args=(x + 665, y + 180)).start()
                        found_tile = True
                        break
                if found_tile:
                    break

        if found_tile:
            time.sleep(0.05)


if __name__ == "__main__":
    main()