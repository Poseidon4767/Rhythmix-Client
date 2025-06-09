import os
import pygame
import random
import glob
import sys
import pickle

class Rhythmix_Client:
    def __init__(self):
        self.folder_path = os.path.join(os.path.dirname(__file__), "music")
        self.music_path = glob.glob(os.path.join(self.folder_path, "*.mp3"))
        self.last_played = ''
        self.playlist = {}
        self.song_name = ''

    def save_playlist(self):
        with open('playlist.bin', 'wb') as file:
            pickle.dump(self.playlist, file)
            print("\nPlaylist saved! :)\n")

    def load_playlist(self):
        try:
            with open('playlist.bin', 'rb') as file:
                self.playlist = pickle.load(file)
            i = 1
            print("\nYour playlist:")
            for song_name, path in self.playlist.items():
                print(f"{i}. {song_name}")
                i += 1
            print()
        except EOFError:
            print("\nEmpty playlist! :(\n")
        except FileNotFoundError:
            print("\nNo playlist found! :(\n")
    
    def delete_playlist(self):
        try:
            os.remove('playlist.bin')
            print("\nPlaylist deleted! :)\n")
        except FileNotFoundError:
            print("\nNo playlist found! :(\n")

    def user_playlist(self):
        os.system('cls')
        print("[1] Add music to playlist.\n[2] View playlist.\n[3] Delete playlist.\n[0] Go back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            os.system('cls')
            song_name = input("Enter song name (avoid song names that already exist in your playlist!):\n")
            song_path = input("Enter song path: ")
            self.playlist[song_name] = song_path
            self.save_playlist()
        elif choice == 2:
            self.load_playlist()
        elif choice == 3:
            self.delete_playlist()
        elif choice == 0:
            os.system('cls')
            self.main()
        else:
            print("\nInvalid choice! :(\n")

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


    def search(self, song_name):
        os.system('cls')
        if song_name in self.playlist:
            pygame.init()
            pygame.mixer.init()
            print(f"Now playing: {song_name} :)\n")
            pygame.mixer.music.load(self.playlist[song_name])
            pygame.mixer.music.play()
        else:
            print("\nNo such song found :(\n")
        
    def main(self):
        pygame.init()
        pygame.mixer.init()
        while True:
            print("[1] Play random.\n[2] Search in your playlist.\n[3] Your playlist.\n[0] Quit")
            main_choice  = int(input("\nEnter your choice: "))
            if main_choice == 1:
                self.play_random_music()
            elif main_choice == 2:
                os.system('cls')
                song_name = input("Enter song name: ")
                self.search(song_name)
            elif main_choice == 3:
                self.user_playlist()
            elif main_choice == 0:
                sys.exit("\nGoodbye! :)\n")
            else:
                print("\nInvalid choice! :(\n")

if __name__ == '__main__':
    print("\n\n********** Music Player **********\n\n")
    print("Credits: Poseidon4767 for making the ENTIRE code.")
    print("Github Profile: https://github.com/Poseidon4767")
    print("Publishing license: GNU License")
    print("Only MP3 files are supported for now!\n\n")
    player = Rhythmix_Client()
    player.main()