# macos-push-to-talk
A very simple "push to talk" functionality for microphone on MacOS. An inverted audio "killswitch".

Requires Python 3, osascript and pynput

    pip3 install pynput
    pip3 install osascript

Run with sudo and keep the console open in background. 

    > sudo ./push-to-talk.py
    Press and hold 'alt_r' to talk...

Press right "option" key to talk, release to mute.
