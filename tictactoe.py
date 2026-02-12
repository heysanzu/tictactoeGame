import turtle
import time
import tkinter as tk

# Game setup
current_player = "X"
board = [""] * 9
game_over = False
turn_time = 10  # seconds per turn
time_remaining = turn_time
timer_running = False
