
from tkinter import *


root =Tk()
root.title("Currency converter - Ahmed")
root.configure(background="white")

def output():
    one_dollar = 168
    user_dollor = int(box_entry.get())
    result = one_dollar * user_dollor
    lbl = Label(output_frame,text = f" {user_dollor} dollor is equals to  {result} dollors.", bg="powder blue",
    fg="#021c13", font="Decorative 14")
    lbl.pack()
    box_entry.delete(0,END)
#FRAME
heading_frame = Frame(root, borderwidth=1, relief=SUNKEN, padx=10, pady=10, bg="powder blue")
heading_frame.grid(ipadx=50, pady=10, padx=10, row=0, column=0)

content_frame = Frame(root, borderwidth=1, relief=SUNKEN, padx=10, pady=10, bg="powder blue")
content_frame.grid(row=1, column=0, pady=20)

output_frame = Frame(root, borderwidth=1, relief=SUNKEN, padx=10, pady=10, bg="powder blue")
output_frame.grid(row=3, column=0, pady=20)

#---------------------------------heading----------------------------------
heading_label = Label(heading_frame, text="Dollor to Rupees", font=("courier", "20", "bold"), bg="black", fg="#2b7a68")
heading_label.grid(row=0, column=0, padx=(100, 0))

#----------------------------------content----------------------------------
text_label = Label(content_frame, text="Dollor: ", bg="powder blue", fg="#021c13", font="courier 14 bold")
text_label.grid(row=0, column=0)

box_entry = Entry(content_frame, bg="powder blue", fg="#021c13", font="courier 14")
box_entry.grid(row=0, column=1)

btn = Button(content_frame, text="Calculate", command=output, bg="powder blue", fg="orange", font="courier 14 bold")
btn.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
