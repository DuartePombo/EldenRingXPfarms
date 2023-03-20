import time
# from helpers.autopy_helpers import AutopyHelpers
from helpers.win32_helpers import Win32Helpers

class Bot():
    def __init__(self):
        self.elden_ring_window = Win32Helpers.get_window('ELDEN RING™')


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

    def teleport_back(self):
        if not self.check_window():
            return False
        time.sleep(0.5)
        Win32Helpers.press("g")
        time.sleep(0.5)
        Win32Helpers.press("f")
        time.sleep(0.5)
        Win32Helpers.press("e")
        time.sleep(0.5)
        Win32Helpers.press("e")
        time.sleep(6)
        return True

    def start_session(self):
        Win32Helpers.click_mouse(1000, 500)

    def do_routine(self):
        if not self.teleport_back(): return False
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
        while self.check_window():
            i += 1
            print("Starting iteration " + str(i))
            if not self.do_routine(): break
            time.sleep(5.5)
        print("Stopped session because we're no longer in the right window")
        return

if __name__ == '__main__':
    bot = Bot()
    bot.main()