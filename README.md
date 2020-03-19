# macos-push-to-talk
A very simple "push to talk" functionality for microphone on MacOS. An inverted audio "killswitch".

Requires Python 3, osascript and pynput

    pip3 install pynput
    pip3 install osascript

Run with sudo and keep the console open in background. 

    > sudo ./push-to-talk.py
    Your mic is now muted. Press and hold 'alt_r' to talk...

Press right "option" key to talk, release to mute.

### Disclaimer

Tested only on my mac (macbook pro early 2019, mojave 10.14.6), so no guarantees that it'll work on any other device. At the moment, it's built only for my needs. Hopefully that'll improve over time.
