import tkinter
from random import choice
class Simon() :
    def __init__(self, master) :
        
        self.master = master
        self.master.minsize(640, 480)
        self.master.resizable(False, False)
        self.master.title("Simon Memory Game")
        self.master.update() 

        
        self.game_canvas = tkinter.Canvas(self.master, width = self.master.winfo_width(), height = self.master.winfo_height(), highlightthickness = 0)
        self.game_canvas.pack()

       
        self.couleur_visible  = ("red", "blue", "green", "yellow")
        self.teinte_couleurs = ("#000000", "#000000", "#000000", "#000000")
        self.couleurs_actuel  = [color for color in self.couleur_visible]

        self.rectangle_ids = []

        
        self.sequence = [choice(self.couleur_visible)]
        self.sequence_position = 0

        self.draw_canvas()

        self.show_sequence()

        self.master.mainloop()

        
    def show_sequence(self) :
        
        self.flash(self.sequence[self.sequence_position])
        
        if(self.sequence_position < len(self.sequence) - 1) :
           
            self.sequence_position += 1
            self.master.after(1250, self.show_sequence)
        else :
            self.sequence_position = 0 

        
    def flash(self, color) :
        index = self.couleur_visible.index(color) 
        if self.couleurs_actuel [index] == self.couleur_visible[index] : 
            
            self.couleurs_actuel [index] = self.teinte_couleurs[index]
            self.master.after(1000, self.flash, color) 
        else :
            self.couleurs_actuel [index] = self.couleur_visible[index] 
        self.draw_canvas() 

    def check_choice(self) :
        color = self.couleur_visible[self.rectangle_ids.index(self.game_canvas.find_withtag("current")[0])]
        if(color == self.sequence[self.sequence_position]) :
            if(self.sequence_position < len(self.sequence) - 1) :
                self.sequence_position += 1
            else :
                self.master.title("Simon Jeu de mémoire - Score: {}".format(len(self.sequence)))
                
                self.sequence.append(choice(self.couleur_visible))
                self.sequence_position = 0
                self.show_sequence()
        else :
           
            self.master.title("Simon Jeu de mémoire - Game Over! | Final Score: {}".format(len(self.sequence)))
            self.sequence[:] = [] 
            self.sequence.append(choice(self.couleur_visible)) 
            self.sequence_position = 0
            self.show_sequence()

    def draw_canvas(self) :
        self.rectangle_ids[:] = [] 
        self.game_canvas.delete("all") 
        for index, color in enumerate(self.couleurs_actuel ) : 
            if index <= 1 :
                self.rectangle_ids.append(self.game_canvas.create_rectangle(index * self.master.winfo_width(), 0, self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
            else :
                self.rectangle_ids.append(self.game_canvas.create_rectangle((index - 2) * self.master.winfo_width(), self.master.winfo_height(), self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
        for id in self.rectangle_ids :
            self.game_canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.check_choice())

def main() :
    root = tkinter.Tk()
    gui = Simon(root)

if __name__ == "__main__" : main()