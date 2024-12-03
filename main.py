#!/usr/bin/env python3
from chess_game import ChessGame
import os
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_title():
    title = """
╔═══════════════════════════════════════╗
║             Chess Game                ║
║      Player vs AI or AI vs AI        ║
╚═══════════════════════════════════════╝
"""
    print(title)

def get_game_mode():
    while True:
        try:
            print("Game Modes:")
            print("1. Player vs AI")
            print("2. AI vs AI")
            choice = input("\nSelect game mode (1 or 2): ").strip()
            
            if choice == "1":
                return "player_vs_ai"
            elif choice == "2":
                return "ai_vs_ai"
            else:
                print("Please enter 1 or 2")
        except (EOFError, KeyboardInterrupt):
            print("\nGame terminated by user")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again")

def main():
    try:
        clear_screen()
        print_title()
        
        mode = get_game_mode()
        clear_screen()
        
        game = ChessGame(mode)
        print_title()
        print(f"Starting {mode.replace('_', ' ').title()} game...\n")
        game.play()
        
        try:
            input("\nPress Enter to exit...")
        except (EOFError, KeyboardInterrupt):
            pass
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()