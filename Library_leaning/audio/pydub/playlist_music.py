from glob import glob
from pydub import AudioSegment
from pydub.playback import play
from tkinter import *

def ring():

    def on_lick (e):
        sound_alarm = True
        sound = AudioSegment.from_mp3(f'{e.widget["text"]}')
        # print(f'{e.widget["value"]}')
        while True:
            try:
                if sound_alarm == False:
                    return
                play(sound)
            except KeyboardInterrupt:
                sound_alarm = False
                
                print ("Stopping playing")
                break #to exit out of loop, back to main program
    
        



    playlist_songs = [mp3_file  for mp3_file in glob("*.mp3")]

    root = Tk()
    root.option_add("*font" , "consolas 25")
    f1 = Frame(root , bg = "blue")
    f1.grid(row = 0 , columnspan = 2 ,sticky = "news")

    chks = StringVar()
    chks.set("gintama01.mp3")
    for i,v in enumerate(playlist_songs):
        lb = Radiobutton(f1, text = v ,value = v, variable = chks ,indicatoron = False ,width = 30 , bg = "gold")
        lb.pack(anchor = W , ipady= 5 , fill = X)
        lb.bind("<Button-1>" , on_lick)



    root.mainloop()

if __name__ == "__main__":
    import sys
    ring()
