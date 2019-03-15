'''
Created on Mar 6, 2019

@author: equillis
'''

import tkinter as tk
import numpy
import copy
import random
import time


class game():
    game_space = numpy.zeros((9,9))
    game_space_solved = numpy.zeros((9, 9))
    user_game_space = numpy.zeros((9, 9))
    #puzzle_array = [9][9] 
    def create_board(self):
    #create a random board
    #exemplary board:
        '''game.game_space[3][1] = 2
        game.game_space[8][1] = 9
        game.game_space[0][2] = 5
        game.game_space[1][2] = 6
        game.game_space[2][2] = 3
        game.game_space[3][2] = 7
        game.game_space[4][2] = 4
        game.game_space[2][3] = 2
        game.game_space[4][3] = 9
        game.game_space[8][3] = 8
        game.game_space[1][4] = 4
        game.game_space[7][4] = 1
        game.game_space[8][4] = 3
        game.game_space[0][5] = 8
        game.game_space[4][5] = 6
        game.game_space[6][5] = 5
        game.game_space[0][6] = 9
        game.game_space[1][6] = 2
        game.game_space[4][6] = 3
        game.game_space[7][6] = 4
        game.game_space[8][6] = 7
        game.game_space[2][7] = 1
        game.game_space[6][7] = 6
        game.game_space[7][7] = 9
        game.game_space[0][8] = 6
        game.game_space[2][8] = 5
        game.game_space[3][8] = 9
        game.game_space[5][8] = 4
        game.game_space[8][8] = 2'''
        
        game.game_space = numpy.array([[2, 9, 7, 1, 8, 3, 4, 5, 6],
                                       [1, 8, 4, 2, 5, 6, 3, 7, 9],
                                       [5, 6, 3, 7, 4, 9, 2, 8, 1],
                                       [3, 0, 2, 4, 9, 1, 7, 6, 8],
                                       [7, 4, 6, 5, 2, 8, 9, 1, 3],
                                       [8, 1, 0, 3, 6, 7, 5, 2, 4],
                                       [9, 2, 8, 6, 3, 5, 1, 4, 7],
                                       [4, 3, 1, 8, 7, 2, 6, 9, 5],
                                       [6, 7, 5, 9, 1, 4, 8, 3, 2]])
        game.user_game_space = copy.deepcopy(game.game_space)
    #exemplary solved board:
        game.game_space_solved = numpy.array([[2, 9, 7, 1, 8, 3, 4, 5, 6],
                                              [1, 8, 4, 2, 5, 6, 3, 7, 9],
                                              [5, 6, 3, 7, 4, 9, 2, 8, 1],
                                              [3, 5, 2, 4, 9, 1, 7, 6, 8],
                                              [7, 4, 6, 5, 2, 8, 9, 1, 3],
                                              [8, 1, 9, 3, 6, 7, 5, 2, 4],
                                              [9, 2, 8, 6, 3, 5, 1, 4, 7],
                                              [4, 3, 1, 8, 7, 2, 6, 9, 5],
                                              [6, 7, 5, 9, 1, 4, 8, 3, 2]])
                
    def check_win(self):
        if numpy.array_equal(game.game_space_solved, game.user_game_space):
            GUI.timer_run = False
            GUI.time_of_round = GUI.counter
            return True
        else:
            return False
    
    def check_mistake(self, row, col):
        for i in range(9):
            if (game.user_game_space[col][row] == game.user_game_space[col][i] and
                    game.user_game_space[col][row] != game.game_space_solved[col][row]):
                col_arg, row_arg = col, i
                GUI.highlight_mistake(self, col, row, col_arg, row_arg)  
            if (game.user_game_space[col][row] == game.user_game_space[i][row] and
                    game.user_game_space[col][row] != game.game_space_solved[col][row]):
                col_arg, row_arg = i, row
                GUI.highlight_mistake(self, col, row, col_arg, row_arg)   
        block_x = int(col/3)
        block_y = int(row/3)
        for i in range(block_x*3, block_x*3 + 3):
            for j in range(block_y*3, block_y*3 + 3):
                if (game.user_game_space[col][row] == game.user_game_space[i][j] and
                    game.user_game_space[col][row] != game.game_space_solved[col][row]):
                    GUI.highlight_mistake(self, col, row, i, j)  
    
    def new_game(self):
        game.create_puzzle(self)
        game.create_board(self)
        GUI.create_grid(self) 
        GUI.fill_grid(self)
        GUI.timer_run = True
        GUI.timer(self)      
    
    def create_puzzle(self):
        print('NEW GAME')
        '''row = random.sample(range(1, 10), 9)
        for i in range(9):
            game.puzzle_array[0][i] = row[i]
        for i in range(1, 9):
            for j in range(9):
                for k in range(i):
                    game.puzzle_array[i][j] = random.randint(1, 9)
                    while game.puzzle_array[i][j] == game.puzzle_array[k][j]:
                        game.puzzle_array[i][j] = random.randint(1, 9)'''                
                 
class GUI:   
    
    text_id = numpy.empty((9, 9))
    window_height = 700
    window_width = 600
    grid_position_x = window_width/2
    grid_position_y = window_height*0.55
    button_frame_positon_x = window_width/2
    button_frame_positon_y = grid_position_y - 50
    board_size = 450
    window_geometry = "%dx%d" % (window_width, window_height)
    line_width_bold = 4
    line_width = 2
    margin = int(line_width_bold/2)
    canvas_size = board_size + margin
    canvas_step = 50
    counter = 0
    timer_run = False
    time_of_round = 0
    minutes = 0
    seconds = 0
    row, col = -1, -1
    
    def __init__(self, master):
        self.master = master
        self.board_frame = tk.Frame(master, height = self.canvas_size,
                                    width = self.canvas_size)
        self.board_frame.place(x = self.grid_position_x, 
                          y = self.grid_position_y, anchor = tk.CENTER)
        self.entry_number = []
        GUI.main_window(self, master)
        GUI.play_buttons(self, master)
        GUI.control_buttons(self, master)
        GUI.function_buttons(self, master)
        self.canvas = tk.Canvas(self.board_frame, bg = 'white', width = self.canvas_size, 
                                height = self.canvas_size)
        self.canvas.place(x = (self.canvas_size)/2, 
                          y = (self.canvas_size)/2, anchor = tk.CENTER)
        self.canvas.bind('<Button-1>', self.cell_clicked)
        self.canvas.bind("<Key>", self.command_key)
        GUI.create_grid(self)
        self.timer = tk.Label(master)
        self.timer.place(x = (self.window_width + self.canvas_size)/2, 
                         y = 20, anchor = tk.NE)
        GUI.timer(self)
    
    

   
    
    def main_window(self, master):
        master.title("sudoQ")
        master.geometry(self.window_geometry)

    def play_buttons(self, master):  
        self.play_buttons_frame = tk.Frame(master)
        self.play_buttons_frame.place(x = self.window_width/2, y = 100,
                                anchor = tk.CENTER)
        button_number = []
        for i in range(9):
            play_button = tk.Button(self.play_buttons_frame, text = str(i + 1), 
                          font = ('Helvetica', '14', 'bold'), 
                          pady = 15, padx = 20, command = lambda i=i: GUI.command_button(self, i+1))
            play_button.grid(column = i, row = 1)
            button_number.append(play_button)
    
    def control_buttons(self, master):
        control_buttons_frame = tk.Frame(master)
        control_buttons_frame.place(x = (self.window_width+self.board_size)/2, 
                                         y = self.grid_position_y - (self.board_size/2))
        erase_button = tk.Button(control_buttons_frame, text = "ERASE",
                                 command = lambda: GUI.command_erase(self))
        erase_button.grid()
        hint_button = tk.Button(control_buttons_frame, text = "HINT",
                                command = lambda: GUI.command_hint(self))
        hint_button.grid()
    
    def function_buttons(self, master):   
        function_buttons_frame = tk.Frame(master)
        function_buttons_frame.place(x = self.window_width/2, 
                                     y = self.grid_position_y + self.canvas_size/2 + 50,
                                     anchor = tk.CENTER)
        new_game_button = tk.Button(function_buttons_frame, text = "NEW GAME",
                                    wraplength = 50, width = 15,
                                 command = lambda: game.new_game(self))
        new_game_button.grid(row = 0, column = 0, padx = 5)
        reset_board_button = tk.Button(function_buttons_frame, text = "RESET BOARD",
                                       wraplength = 50, width = 15,
                                command = lambda: GUI.reset_board(self))
        reset_board_button.grid(row = 0, column = 1, padx = 5)
      
    def create_grid(self):      
        for i in range(2, self.canvas_size + 1, self.canvas_step):
            if (i-2) % 3:
                self.canvas.create_line(i, 0, i, self.canvas_size, 
                                        width = self.line_width,
                                        tags = 'grid')
                self.canvas.create_line(0, i, self.canvas_size, i, 
                                        width = self.line_width,
                                        tags = 'grid')
            else:
                self.canvas.create_line(i, 0, i, self.canvas_size, 
                                        width = self.line_width_bold,
                                        tags = 'grid')
                self.canvas.create_line(0, i, self.canvas_size, i, 
                                        width = self.line_width_bold,
                                        tags = 'grid')
       
    def fill_grid(self):
        game.create_board(self)
        for i in range(9):
            for j in range(9):
                self.canvas.delete(int(self.text_id[i][j]))
        for i in range(9):
            for j in range(9):
                if game.game_space[i][j] != 0:
                    self.text_id[i][j] = self.canvas.create_text(i * self.canvas_step + self.margin + self.canvas_step/2, 
                                            j * self.canvas_step + self.margin + self.canvas_step/2,
                                            text = str(game.game_space[i][j]), 
                                            font = ('Helvetica', '16', 'bold'), tags = "board",
                                            anchor = tk.CENTER)

    def fill_user_grid(self):
        for i in range(9):
            for j in range(9):
                if game.user_game_space[i][j] != 0:
                    self.canvas.delete(int(self.text_id[i][j]))
                    self.text_id[i][j] = self.canvas.create_text(i * self.canvas_step + self.margin + self.canvas_step/2, 
                                            j * self.canvas_step + self.margin + self.canvas_step/2,
                                            text = str(int(game.user_game_space[i][j])), 
                                            font = ('Helvetica', '16', 'bold'),
                                            anchor = tk.CENTER)
                elif game.user_game_space[i][j] == 0:
                    self.canvas.delete(int(self.text_id[i][j]))
        self.canvas.delete('highlight')
        if game.check_win(self) == False:
            game.check_mistake(self, self.row, self.col)
            self.col, self.row = -1, -1
        else:
            GUI.win_animation(self)
                    
    def cell_clicked(self, event):
        x, y = event.x, event.y
        self.canvas.focus_set()
        if 0 < x < self.canvas_size and 0 < y < self.canvas_size:
            row = int((y-self.margin)/self.canvas_step)
            col = int((x-self.margin)/self.canvas_step)
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
                self.canvas.delete('highlight')
            elif game.game_space[col][row] == 0:
                self.row, self.col = row, col
                self.canvas.delete('highlight')
                if self.row >= 0 and self.col >= 0:
                    self.canvas.create_rectangle(self.margin + col * self.canvas_step + 2, 
                                             self.margin + row * self.canvas_step + 2, 
                                             self.margin + (col + 1) * self.canvas_step - 2, 
                                             self.margin + (row + 1) * self.canvas_step - 2,
                                             outline = 'red', width = 4, tags = 'highlight')
                    
    def highlight_mistake(self, row, col, i, j):
        self.canvas.delete(int(self.text_id[i][j]))
        self.text_id[i][j] = self.canvas.create_text(i * self.canvas_step + self.margin + self.canvas_step/2, 
                                                     j * self.canvas_step + self.margin + self.canvas_step/2,
                                                     text = str(int(game.user_game_space[i][j])), 
                                                     font = ('Helvetica', '16', 'bold'), fill = 'red',
                                                     anchor = tk.CENTER)        
    
    def reset_board(self):
        for i in range(9):
            for j in range(9):
                self.canvas.delete(int(self.text_id[i][j]))
        GUI.fill_grid(self)
          
    def command_key(self, event):
        if self.row >= 0 and self.col >= 0:
            if event.char in "1234567890":
                game.user_game_space[self.col][self.row] = int(event.char)
                GUI.fill_user_grid(self)

        
    def command_button(self, button):
        if self.row >= 0 and self.col >= 0:
            game.user_game_space[self.col][self.row] = button
            GUI.fill_user_grid(self)
            
    def command_erase(self):
        if game.check_win(self) == False:
            if self.row >= 0 and self.col >= 0:
                game.user_game_space[self.col][self.row] = 0
                GUI.fill_user_grid(self)
            
    def command_hint(self):
        if game.check_win(self) == False:
            if self.row >= 0 and self.col >= 0:
                game.user_game_space[self.col][self.row] = game.game_space_solved[self.col][self.row]
            else:
                zero_elements_array = numpy.where(game.user_game_space == 0)
                if len(zero_elements_array[0]) > 1:
                    zero_element = random.randint(1, len(zero_elements_array[0])-1)
                    zero_x = zero_elements_array[0][zero_element]
                    zero_y = zero_elements_array[1][zero_element]
                else:
                    zero_x = zero_elements_array[0][0]
                    zero_y = zero_elements_array[1][0]
            game.user_game_space[zero_x][zero_y] = game.game_space_solved[zero_x][zero_y] 
            GUI.fill_user_grid(self)  
    
    def win_animation(self):
        for i in range(9):
            for j in range(9):
                self.canvas.delete(int(self.text_id[i][j]))
        self.canvas.delete('grid')
        self.canvas.create_text(self.canvas_size/2, self.canvas_size/2,
                                text = 'YOU WON!', fill = 'blue',
                                font = ('Helvetica', '62', 'bold'),
                                anchor = tk.CENTER)
        self.canvas.create_text(self.canvas_size/2, self.canvas_size/2 + 62,
                                text = 'Your time: ' + GUI.time_format(self), fill = 'blue',
                                font = ('Helvetica', '18', 'bold'),
                                anchor = tk.CENTER)
    def timer(self):
        if GUI.timer_run:
            seconds = int(GUI.counter%60)
            minutes = int(GUI.counter/60)
            self.timer.config(text = GUI.time_format(self))
            self.timer.after(1000, GUI.timer, self)
            GUI.counter += 1
            
    def time_format(self):
        seconds = int(GUI.counter%60)
        minutes = int(GUI.counter/60)
        if seconds < 10:
            text = '%d:0%d' % (minutes, seconds)
        else:
            text = '%d:%d' % (minutes, seconds)
        return text

           
root = tk.Tk()
app = GUI(root)
root.mainloop()
