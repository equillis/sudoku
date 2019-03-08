'''
Created on Mar 6, 2019

@author: equillis
'''

import tkinter as tk
import numpy


class appGUI:   
    def __init__(self, master):
        self.master = master
        self.board_frame = tk.Frame(master, height = appGUI.canvas_size,
                                    width = appGUI.canvas_size)
        self.board_frame.place(x = appGUI.grid_position_x, 
                          y = appGUI.grid_position_y, anchor = tk.CENTER)
        self.entry_number = []
        appGUI.main_window(self, master)
        appGUI.buttons(self, master)
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
    canvas_size = board_size + int(line_width_bold/2)
    canvas_step = 50
    button_number = []
    
   
    
    def main_window(self, master):
        master.title("sudoQ")
        master.geometry(appGUI.window_geometry)

    def buttons(self, master):  
        self.button_frame = tk.Frame(master)
        self.button_frame.place(x = appGUI.window_width/2, y = 100,
                                anchor = tk.CENTER)

        for i in range(9):
            b = tk.Button(self.button_frame, text = str(i + 1), 
                          font = ('Helvetica', '14', 'bold'), 
                          pady = 15, padx = 20)
            b.grid(column = i, row = 1)
            appGUI.button_number.append(b)
      
            
    def create_grid(self):

        
        self.canvas = tk.Canvas(self.board_frame, bg = 'white', width = appGUI.canvas_size, 
                                height = appGUI.canvas_size)
        self.canvas.place(x = (appGUI.canvas_size)/2, 
                          y = (appGUI.canvas_size)/2, anchor = tk.CENTER)
        for i in range(2, appGUI.canvas_size + 1, appGUI.canvas_step):
            if (i-2) % 3:
                self.canvas.create_line(i, 0, i, appGUI.canvas_size, 
                                        width = appGUI.line_width)
                self.canvas.create_line(0, i, appGUI.canvas_size, i, 
                                        width = appGUI.line_width)
            else:
                self.canvas.create_line(i, 0, i, appGUI.canvas_size, 
                                        width = appGUI.line_width_bold)
                self.canvas.create_line(0, i, appGUI.canvas_size, i, 
                                        width = appGUI.line_width_bold)
    
    
    def fill_grid(self):
        game.create_board(self)
        
        for i in range(9):
            for j in range(9):
                if game.game_space[i][j] != 0:
                    label = tk.Label(self.board_frame, text = str(game.game_space[i][j]),
                                     bg = 'white', font = ('Helvetica', '14', 'bold'),
                                     padx = 15, pady = 10)
                    label.place(x = (i * appGUI.canvas_step)+(appGUI.line_width_bold), 
                                y = (j * appGUI.canvas_step)+(appGUI.line_width_bold))
                else:
                    entry = tk.Entry(self.board_frame, text = str(game.game_space[i][j]),
                                     bd = 0, highlightthickness = 0, cursor = 'arrow',
                                     insertofftime = 0, width = 1)
                    entry.place(x = (i * appGUI.canvas_step)+(appGUI.line_width_bold)+10, 
                                y = (j * appGUI.canvas_step)+(appGUI.line_width_bold)+10,
                                anchor = tk.NW)
                    self.entry_number.append(entry)
                    #somecomment
                    
 
        
        
        
class game():
    game_space = numpy.zeros((9,9),numpy.dtype(object))
    
    def create_board(self):
    #create a random board
    #exemplary board:
        game.game_space[3][1] = 2
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
        game.game_space[8][8] = 2
        
        
    #def win(self):
        #check if the game is won (only at the end)
               
    
    #def wrong_number(self):
        #check if the written number is correct (during the play)
                
      
                
root = tk.Tk()
app = appGUI(root)
root.mainloop()