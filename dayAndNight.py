from tkinter import *
from time import *

class MyPicture(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=800, height=500, bg="sky blue")
        self.myCanvas.grid()



        #Grass
        self.myCanvas.create_rectangle(0, 400, 800, 600, fill = "olive drab", outline="dark green")
    

        #Rainbow
        self.myCanvas.create_arc(200, 200, 700, 600, style="arc", start=0, extent=180, fill="red", outline="red", width=20)
        self.myCanvas.create_arc(220, 220, 680, 580, style="arc", start=    0, extent=180, fill="dark orange", outline="dark orange", width=20)
        self.myCanvas.create_arc(240, 240, 660, 560, style="arc", start=0, extent=180, fill="gold", outline="gold", width=20)
        self.myCanvas.create_arc(260, 260, 640, 540, style="arc", start=0, extent=180, fill="lime green", outline="lime green", width=20)
        self.myCanvas.create_arc(280, 280, 620, 520, style="arc", start=0, extent=180, fill="dodger blue", outline="dodger blue", width=20)
        self.myCanvas.create_arc(300, 295, 600, 505, style="arc", start=0, extent=180, fill="medium purple", outline="medium purple", width=20)

        #Clouds
        self.myCanvas.create_oval(40+200, 120, 130+200, 170, fill="white", outline="white")
        self.myCanvas.create_oval(90+200, 100, 150+200, 140, fill="white", outline="white")
        self.myCanvas.create_oval(100+200, 120, 190+200, 170, fill="white", outline="white")
        self.myCanvas.create_oval(60+200, 140, 130+200, 190, fill="white", outline="white")
        

        #Sun
        sun = self.myCanvas.create_oval(10, 250, 60, 300, fill="yellow", outline="gold")

        for x in range(0,10):
            text = self.myCanvas.create_text(50, 50, text="Day "+str(x+1), font=("Verdana", 18))
            self.myCanvas.update()
            sleep(0.5)
              
            for i in range(1,30):
                self.myCanvas.coords(sun, 10+i**2, 250-8*i, 60+i**2, 300-8*i)
                self.myCanvas.update()
                sleep(0.1)


            self.myCanvas.delete(text)
            if x != 0:
                self.myCanvas.delete(branches)

            #Night
            night = self.myCanvas.create_rectangle(0, 0, 800, 800, fill="midnight blue", outline="midnight blue")
            moon = self.myCanvas.create_oval(600, 50, 700, 150, fill="lemon chiffon", outline="lemon chiffon")


            crescent = self.myCanvas.create_oval(580-9*x, 70, 680-9*x, 170, fill="midnight blue", outline="midnight blue")
            night_grass = self.myCanvas.create_rectangle(0, 400, 800, 600, fill = "black", outline="black")
            night_text = self.myCanvas.create_text(50, 50, text="Night", font=("Verdana", 18), fill="lemon chiffon")
            
            if x > 0:
                night_tree = self.myCanvas.create_rectangle(100-2*(x-1), 380-20*(x-1), 110+2*(x-1), 400, fill="gray11", outline="gray11")
                night_branches = self.myCanvas.create_oval(98-5*(x-1), 375-25*(x-1), 112+5*(x-1),390-20*(x-1), fill="gray10", outline="gray10")
            self.myCanvas.update()
            sleep(2)
            
            self.myCanvas.delete(night)
            self.myCanvas.delete(moon)
            self.myCanvas.delete(crescent)
            self.myCanvas.delete(night_grass)
            self.myCanvas.delete(night_text)

            if x > 0:
                self.myCanvas.delete(night_tree)
                self.myCanvas.delete(night_branches)

            #Tree
            tree = self.myCanvas.create_rectangle(100-2*x, 390-20*x, 110+2*x, 400, fill="saddle brown", outline="saddle brown")
            if x < 1:
                branches = self.myCanvas.create_rectangle(100-2*x, 390-20*x, 110+2*x, 400, fill="saddle brown", outline="saddle brown")
            else:
                branches = self.myCanvas.create_oval(98-5*x, 385-25*x, 112+5*x,400-20*x, fill="forest green", outline="forest green")


pic01 = MyPicture()
pic01.mainloop()
