'''
Created on Mar 6, 2019

@author: equillis
'''

import tkinter as tk


class Application:
    window_height = 700
    window_width = 600
    grid_position_x = window_width/2
    grid_position_y = window_height*0.55
    button_frame_positon_x = window_width/2
    button_frame_positon_y = grid_position_y - 50
    window_geometry = "%dx%d" % (window_width, window_height)
    def __init__(self, master):
        self.master = master
        master.title("sudoQ")
        master.geometry(Application.window_geometry)
        
        self.button_frame = tk.Frame(master)
        self.button_frame.place(x = Application.window_width/2, y = 100,
                                anchor = tk.CENTER)
        self.button_number = []
        for i in range(9):
            b = tk.Button(self.button_frame, text = str(i + 1), 
                          font = ('Helvetica', '14', 'bold'), 
                          pady = 15, padx = 20)
            b.grid(column = i, row = 1)
            self.button_number.append(b)
           
        
        Application.create_grid(self, master)
            
    def create_grid(self, master):
        line_width_bold = 4
        line_width = 2
        canvas_size = 450+int(line_width_bold/2)
        canvas_step = 50
        
        self.canvas = tk.Canvas(master, bg = 'white', width = canvas_size, 
                                height = canvas_size)
        self.canvas.place(x = Application.grid_position_x, 
                          y = Application.grid_position_y, anchor = tk.CENTER)
        for i in range(2, canvas_size + 1, canvas_step):
            if (i-2) % 3:
                self.canvas.create_line(i, 0, i, canvas_size, width = line_width)
                self.canvas.create_line(0, i, canvas_size, i, width = line_width)
            else:
                self.canvas.create_line(i, 0, i, canvas_size, width = line_width_bold)
                self.canvas.create_line(0, i, canvas_size, i, width = line_width_bold)
        
        
                
root = tk.Tk()
app = Application(root)
root.mainloop()