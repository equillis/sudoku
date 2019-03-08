'''
Created on Mar 6, 2019

@author: equillis
'''

import tkinter as tk
import numpy


class appGUI:   
    def __init__(self, master):
        self.master = master
        self.board_frame = tk.Frame(master, height = self.canvas_size,
                                    width = self.canvas_size)
        self.board_frame.place(x = self.grid_position_x, 
                          y = self.grid_position_y, anchor = tk.CENTER)
        self.entry_number = []
        appGUI.main_window(self, master)
        appGUI.buttons(self, master)
        self.canvas = tk.Canvas(self.board_frame, bg = 'white', width = appGUI.canvas_size, 
                                height = self.canvas_size)
        self.canvas.place(x = (self.canvas_size)/2, 
                          y = (self.canvas_size)/2, anchor = tk.CENTER)
        self.canvas.bind('<Button-1>', self.cell_clicked)
        appGUI.create_grid(self)
        appGUI.fill_grid(self)
    
   
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
    button_number = []
    label_array = numpy.zeros((9,9),numpy.dtype(object))
   
    
    def main_window(self, master):
        master.title("sudoQ")
        master.geometry(self.window_geometry)

    def buttons(self, master):  
        self.button_frame = tk.Frame(master)
        self.button_frame.place(x = self.window_width/2, y = 100,
                                anchor = tk.CENTER)

        for i in range(9):
            b = tk.Button(self.button_frame, text = str(i + 1), 
                          font = ('Helvetica', '14', 'bold'), 
                          pady = 15, padx = 20)
            b.grid(column = i, row = 1)
            self.button_number.append(b)
      
            
    def create_grid(self):      
        for i in range(2, self.canvas_size + 1, self.canvas_step):
            if (i-2) % 3:
                self.canvas.create_line(i, 0, i, self.canvas_size, 
                                        width = self.line_width)
                self.canvas.create_line(0, i, self.canvas_size, i, 
                                        width = self.line_width)
            else:
                self.canvas.create_line(i, 0, i, self.canvas_size, 
                                        width = self.line_width_bold)
                self.canvas.create_line(0, i, self.canvas_size, i, 
                                        width = self.line_width_bold)
    
    
    def fill_grid(self):
        game.create_board(self)

        for i in range(9):
            for j in range(9):
                if game.game_space[i][j] != 0:
                    self.canvas.create_text(i * self.canvas_step + self.margin + self.canvas_step/2, 
                                            j * self.canvas_step + self.margin + self.canvas_step/2,
                                            text = str(game.game_space[i][j]), 
                                            font = ('Helvetica', '16', 'bold'),
                                            anchor = tk.CENTER)
    def cell_clicked(self, event):
        x, y = event.x, event.y
        
        if 0 < x < self.canvas_size and 0 < y < self.canvas_size:
            row = int((y-self.margin)/self.canvas_step)
            col = int((x-self.margin)/self.canvas_step)
            print(row, col)
            self.canvas.focus_set()
            self.canvas.create_rectangle(self.margin + col * self.canvas_step + 2, 
                                         self.margin + row * self.canvas_step + 2, 
                                         self.margin + (col + 1) * self.canvas_step - 2, 
                                         self.margin + (row + 1) * self.canvas_step - 2,
                                         outline = 'red', width = 4)
        
class game():
    game_space = numpy.zeros((9,9),numpy.dtype(object))
    user_game_space = game_space
    def create_board(self):
    #create a random board
    #exemplary board:
        game.game_space[3][1] = '2'
        game.game_space[8][1] = '9'
        game.game_space[0][2] = '5'
        game.game_space[1][2] = '6'
        game.game_space[2][2] = '3'
        game.game_space[3][2] = '7'
        game.game_space[4][2] = '4'
        game.game_space[2][3] = '2'
        game.game_space[4][3] = '9'
        game.game_space[8][3] = '8'
        game.game_space[1][4] = '4'
        game.game_space[7][4] = '1'
        game.game_space[8][4] = '3'
        game.game_space[0][5] = '8'
        game.game_space[4][5] = '6'
        game.game_space[6][5] = '5'
        game.game_space[0][6] = '9'
        game.game_space[1][6] = '2'
        game.game_space[4][6] = '3'
        game.game_space[7][6] = '4'
        game.game_space[8][6] = '7'
        game.game_space[2][7] = '1'
        game.game_space[6][7] = '6'
        game.game_space[7][7] = '9'
        game.game_space[0][8] = '6'
        game.game_space[2][8] = '5'
        game.game_space[3][8] = '9'
        game.game_space[5][8] = '4'
        game.game_space[8][8] = '2'
                
    #def win(self):
        #check if the game is won (only at the end)
               
    
    #def wrong_number(self):
        #check if the written number is correct (during the play)
                
      
                
root = tk.Tk()
app = appGUI(root)
root.mainloop()