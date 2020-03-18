#!/usr/bin/env python3
from pynput import keyboard
import osascript
import os, subprocess

class PushToTalk():
    push_to_talk_button = 'alt_r'
    last_volume = 75

    def prompt_sudo(self):
        ret = 0
        if os.geteuid() != 0:
            msg = "[sudo] password for %u:"
            ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
        return ret

    def on_press(self, key):
        try:
            if key and key.name and key.name == self.push_to_talk_button:
                osascript.osascript("set volume input volume " + last_volume)
        except:
            pass

    def on_release(self, key):
        try:
            if key and key.name and key.name == self.push_to_talk_button:
                self.last_volume = osascript.osascript("input volume of (get volume settings)")[1]
                osascript.osascript("set volume input volume 0")
        except:
            pass

ptt = PushToTalk()

if ptt.prompt_sudo() != 0:
    print("Failed to get root privileges. Exiting.")

listener = keyboard.Listener(on_press=ptt.on_press, on_release=ptt.on_release)
print("Press and hold '" + ptt.push_to_talk_button + "' to talk...")
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

