from tkinter import*
import speech_recognition as sr
root = Tk()
root.geometry("500x500")
root.config(bg = '#F2CCC3')

label = Label(root, text = "LANGUAGE TRANCELATER", font = 'areal 20')
label.place(relx = 0.5, rely = 0.1, anchor =CENTER)

input_label = Label(root, text = "Enter Text", font = 'areal 15')
input_label.place(relx = 0.03, rely = 0.3, anchor =W)

my_text = Text(root,width = 60, height = 15, wrap = WORD, pady=5, padx = 5)
my_text.place(relx = 0.02, rely = 0.5, anchor = W)







root.mainloop()