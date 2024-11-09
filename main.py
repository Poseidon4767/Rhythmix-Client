import os
import pygame
import random
import glob
import sys

class Rhythmix_Client:
    def __init__(self):
        self.folder_path = os.path.join(os.path.dirname(__file__), "music")
        self.music_path = glob.glob(os.path.join(self.folder_path, "*.mp3"))
        self.last_played = ''

    def play_random_music(self):
        if not self.music_path:
            os.system('cls')
            print("\nNo music files found! Download some MP3 files, put them in the 'music' folder and restart the program.\n")
            return
        while True:
            os.system('cls')
            while True:
                random_choice = random.choice(self.music_path)
                if random_choice != self.last_played:
                    break
            file_name = os.path.basename(random_choice)
            print(f"Now playing {file_name} :)")
            print("Ctrl + C to quit.\n")
            self.last_played = random_choice
            pygame.mixer.music.load(random_choice)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(500)

    def select_music(self, path):
        os.system('cls')
        if path in self.music_path:
            os.system('cls')
            file_name = os.path.basename(path)
            print(f"Now playing {file_name} :)\n")
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        else:
            os.system('cls')
            print("\nNo such music found :(\n")

    def main(self):
        pygame.init()
        pygame.mixer.init()
        while True:
            print("[1] Play random.\n[2] Select music to play.\n[0] Quit")
            main_choice  = int(input("Enter your choice: "))
            if main_choice == 1:
                self.play_random_music()
            elif main_choice == 2:
                os.system('cls')
                path = input("Enter path: ")
                self.select_music(path)
            elif main_choice == 0:
                sys.exit("Goodbye! :)")

if __name__ == '__main__':
    print("\n\n********** Rhythmix Client **********\n\n")
    print("Credits: Poseidon4767 for making the ENTIRE code.")
    print("Github Profile: https://github.com/Poseidon4767")
    print("Publishing license: GNU License")
    print("Only MP3 files are supported for now!\n\n")
    player = Rhythmix_Client()
    player.main()
