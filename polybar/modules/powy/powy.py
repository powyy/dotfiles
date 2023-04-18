#!/usr/bin/env python3
from src import Spotify
import argparse

def main():
    spotify = Spotify()
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', type=str, default=r'status : % artist % - % title', help='The format to use when displaying the currently playing song information.')
    parser.add_argument('--space', type=str, default=r'%', help='Consider this character to be a space.')
    args = parser.parse_args()

    return spotify.handle_args(args)


if __name__ == '__main__':
    displayed_text = f'\r{main()}'
    print(displayed_text, end='', flush=True)