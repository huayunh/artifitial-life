# the GUI part

# RGB
# R = life (population, birth rate, etc)
# G = natural resources
# B = civilization

import eventBasedAnimation

class Struct(object):
    pass

class GUI(eventBasedAnimation.Animation):
    def onDraw(self,canvas):
        canvas.create_rectangle(0,0,self.width,self.height,
            fill = "white",width = 0)
        n = 60
        w = 10
        left = 0
        top = left
        for i in xrange(n):
            for j in xrange(n):
                canvas.create_rectangle(left + i * w, top + j * w,
                    left + (i+1)*w, top + (j+1)*w, width = 2,
                    outline = "grey",fill = "yellow")

GUI(width = 600, height = 600, 
    timerDelay = 1000,
    fullscr = False).run()