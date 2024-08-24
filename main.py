# Python music player -- requires pygame dependency
from pygame import mixer
mixer.init()

def main():
    mixer.music.load("songs/secret_song.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()

def displayMenuStrings():
    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' set volume")
    print("Press 'e' to exit")

def musicController():
    play = True
    while (play):
        prompt = input("Enter command here: ")
        if prompt == "p":
            mixer.music.pause()
        elif prompt == "r":
            mixer.music.unpause()
        elif prompt == "v":
            v = float(input("Enter a decimal value between 0 to 1 to set the volume volume(i.e. 0.5): "))
            mixer.music.set_volume(v)
        elif prompt == "e":
            mixer.music.stop()
            play = False
            print("Music player has stopped. Thanks for playing!")

if __name__ == "__main__":
    main()
    displayMenuStrings()
    musicController()