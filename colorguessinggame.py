from tkinter import*
import random
root=Tk()
root.title('color guessing game')
root.geometry('600x500')

colors = ['blue','red','green','yellow','orange','white','black','brown','gray','purple','pink','maroon','cyan','turquoise','teal','lavender','violet']

heading_label = Label(root, text='NAME THE COLOR', font=("Comic",30,"bold"), fg="crimson")
heading_label.place(relx="0.5", rely="0.1", anchor=CENTER)

answer_input = Entry(root)
answer_input.place(relx='0.5',rely='0.6',anchor=CENTER)
answer_input.insert(0,'Enter your answer here')

correct_label = Label(root, font=("Arial",15,"bold"))
correct_label.place(relx='0.5',rely='0.75',anchor=CENTER)

def colorchange():
    colortochangenumber = random.randint(0, 16)
    colortochange = colors[colortochangenumber]
    root['bg']=colortochange
    correct_label['bg']=colortochange
    correct_label['text'] = ''
    if(root['bg']=='black'):
        correct_label['fg'] = 'white'
    elif(root['bg']!='black'):
        correct_label['fg'] = 'black'
     
def checkanswer():
    input_answer = answer_input.get()
    if(input_answer==root['bg']):
        correct_label['text'] = 'Correct answer, good job'
    else:
        correct_label['text'] = 'Not correct, try again or skip'
    
    
btn = Button(root, text='Change Color', command=colorchange, fg='black', font=("Arial",15,"bold"))
btn.place(relx='0.7',rely='0.5',anchor=CENTER)

btn2 = Button(root, text='Check Answer', command=checkanswer, fg='black', font=("Arial",15,"bold"))
btn2.place(relx='0.3',rely='0.5',anchor=CENTER)

root.mainloop()