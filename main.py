import os
import time
import numpy as np
import tensorflow as tf
import pygetwindow as gw
from PIL import ImageGrab
from win32_helpers import Win32Helpers
from tensorflow.keras.models import load_model


class Bot():

    def __init__(self):
        window_title = 'ELDEN RING™'
        self.elden_ring_window = Win32Helpers.get_window(window_title)


    def take_screenshot_in_memory(area_percentage=(0.88, 0.25), window_title='ELDEN RING™'):
        # Find the window by title (window_title)
        window = gw.getWindowsWithTitle(window_title)[0]

        if window:
            # Get the window's position and size
            left, top, right, bottom = window.left, window.top, window.right, window.bottom

            # Determine the area coordinates within the window based on percentages
            if area_percentage:
                width = right - left
                height = bottom - top

                x1 = int(area_percentage[0] * width)
                y1 = int(0.02 * width)
                x2 = int(width*(1-0.02))
                y2 = int(area_percentage[1] * height)

                left, top, right, bottom = x1, y1, x2, y2

            # Capture the screenshot for the specified area
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

            # Resize the screenshot to a lower resolution
            screenshot_resized = tf.image.resize(screenshot,(256,256))

            return screenshot_resized
        else:
            return None



    def img_prob(reloaded_model):
        # Take a screenshot with 50% of the original resolution and store it in memory
        resize = Bot.take_screenshot_in_memory(area_percentage=(0.88, 0.25), window_title='ELDEN RING™')
        y_hat_prob = reloaded_model.predict(np.expand_dims(resize/255,0),verbose=0)
        return y_hat_prob

    def isMap(self,model):
        inside_prob = Bot.img_prob(model)
        if inside_prob > 0.5:
            return True
        elif inside_prob <=0.5:
            return False


    def run_to_point(self):
        if not self.check_window():
            return False

        Win32Helpers.pressAndHold("spacebar", "w")
        time.sleep(1.7)
        Win32Helpers.pressAndHold("h")
        time.sleep(0.28)
        Win32Helpers.release("h")
        time.sleep(2)
        Win32Helpers.release("spacebar", "w")
        time.sleep(0.3)
        return True

    def run_up_further(self):
        if not self.check_window():
            return False
        Win32Helpers.pressAndHold("spacebar", "w")
        time.sleep(6)
        Win32Helpers.release("spacebar", "w")
        time.sleep(0.5)
        return True

    def use_ability(self):
        if not self.check_window():
            return False
        Win32Helpers.press("alt")
        return True

    def teleport_back(self,model):
        if not self.check_window():
            return False
        time.sleep(0.5)
        Win32Helpers.press("g")
        time.sleep(3)
        while not self.isMap(model):
            Win32Helpers.press("q")
            time.sleep(0.5)
            Win32Helpers.press("q")
            time.sleep(0.5)
            Win32Helpers.press("g")
            time.sleep(0.5)
        if not self.isMap(model):
            return self.teleport_back(model)
        Win32Helpers.press("f")
        time.sleep(0.5)
        if not self.isMap(model):
            return self.teleport_back(model)
        Win32Helpers.press("e")
        time.sleep(0.5)
        if not self.isMap(model):
            return self.teleport_back(model)
        Win32Helpers.press("e")
        time.sleep(6)
        return True

    def start_session(self):
        Win32Helpers.click_mouse(1000, 500)

    def do_routine(self,model):
        if not self.teleport_back(model): return False
        if not self.run_to_point(): return False
        if not self.use_ability(): return False
        return True

    def check_window(self):
        activeWindow = Win32Helpers.get_active_window()
        return activeWindow == self.elden_ring_window

    def main(self):
        i = 0
        print("Starting session by clicking in the window")
        self.start_session()
        print("Loading CV model...")
        reloaded_model = load_model(os.path.join('EldenRingXPfarms','models','insideMap.h5'))
        print("Model Loaded")
        while self.check_window():
            i += 1
            print("Starting iteration " + str(i))
            if not self.do_routine(reloaded_model): break
            time.sleep(5.5)
        print("Stopped session because we're no longer in the right window")
        return

if __name__ == '__main__':

    bot = Bot()
    bot.main()