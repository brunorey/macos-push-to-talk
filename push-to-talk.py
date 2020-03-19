#!/usr/bin/env python3
from pynput import keyboard
import osascript
import os, subprocess
from signal import signal, SIGINT
from sys import exit


class PushToTalk():
    push_to_talk_button = 'alt_r'
    last_volume = 75

    def handler(self, signal_received, frame):
        print('SIGINT or CTRL-C detected. Terminating...')
        print('Setting volume to normal level (mic open)...')
        self.open_mic()
        print('Done. Bye!')
        exit(0)

    def prompt_sudo(self):
        ret = 0
        if os.geteuid() != 0:
            msg = "[sudo] password for %u:"
            ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
        return ret

    def on_press(self, key):
        try:
            if key and key.name and key.name == self.push_to_talk_button:
                self.open_mic()
        except:
            pass

    def on_release(self, key):
        try:
            if key and key.name and key.name == self.push_to_talk_button:
                self.last_volume = osascript.osascript("input volume of (get volume settings)")[1]
                self.hush_mic()
        except:
            pass

    def open_mic(self):
        try:
            osascript.osascript("set volume input volume " + str(self.last_volume))
        except:
            pass

    def hush_mic(self):
        try:
            osascript.osascript("set volume input volume 0")
        except:
            pass


ptt = PushToTalk()

signal(SIGINT, ptt.handler)

if ptt.prompt_sudo() != 0:
    print("Failed to get root privileges. Exiting.")

ptt.hush_mic()

listener = keyboard.Listener(on_press=ptt.on_press, on_release=ptt.on_release)
print("Your mic is now muted. Press and hold '" + ptt.push_to_talk_button + "' to talk...")
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

