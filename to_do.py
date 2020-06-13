from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import backend

root= Tk()
root.title("To Do")

root.geometry("1000x600")
root.configure(background= "black")

#------------------------------------------------Variables ----------------------------------------------

date= StringVar()

Task_Title= StringVar()
Task_Detail= StringVar()


Status= StringVar()



#--------------------------------------------function---------------------------------------

today = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
only_date= datetime.now().strftime("%d-%m-%Y")
date.set(today)

def get_selected_row(event):
    global selected_tuple, New_status
    index= list1.curselection()[0] # It gives list ka index
    selected_tuple= list1.get(index)[0]
    
##    txtdate.delete(0, END)
##    txtdate.insert(END, Selected_date)
    if (list1.get(index)[1]!="Pending" and list1.get(index)[1]!="Done" ):
        date.set(list1.get(index)[1])    
    Task_Title.set(list1.get(index)[2])
    Task_Detail.set(list1.get(index)[3])
    
   
    Status.set(list1.get(index)[4])
    if Status.get() == 'Pending':
        popupMenu.config(font=("arial", 14, "bold"),bg='RED', fg= "White", width=16)
    
    else:
        popupMenu.config(font=("arial", 14, "bold"),bg='GREEN', fg="white", width=16)
    #print(selected_tuple)
    
def to_add_task():    
    backend.insert(only_date,Task_Title.get(), Task_Detail.get(),Status.get())
    print(backend.view())
        
        
def to_exit():
    iExit= tkinter.messagebox.askyesno("ToDo", "Please confirm if you wish to exit")
    if iExit > 0:
        root.destroy()

def to_reset():
    Task_Title.set("")
    Task_Detail.set("")
    
    
    
def to_delete():
##    print(list1.get())
##    messaebox("PLease select show and select any list to get deleted")
##    print(backend.view())
##    print(type(backend.view()))
##    print(backend.view()[0][0])
##    #for 
##    for index in backend.view():
##        print(index[0])
        #Will check what user is selecting
        #backend.delete(serial_num)
    backend.delete(selected_tuple)
    #print(backend.view())

#Show record as per today
def to_show_summary():
    #https://www.w3schools.com/python/python_datetime.asp

    #WED, 3rd JUne, 20202 task lIst
    date_format= datetime.now().strftime("(%a)- %dth %b, %Y")    
    txt_heading.delete("1.0", END)   
    txt_heading.insert(END, "\t" + date_format + " Task List")
    
    list1.delete(0, END)
    try:
        for index in backend.view_With_filter(only_date):
            list1.insert(END, index)
            #print(index[0])
    except IndexError:
        
        messagebox.showinfo(title="Warning: ", message="Today's record is empty, please enter record first ...")
        
        
# Front end modification

    #list1.delete(0, END)
##    for index in backend.view():
##        date_col= index[1]
##        new_date= date_col[:10]
##        if (new_date == only_date):
##            list1.insert(END, index)
            
        
        #list1.insert(END, index)
    
    #print(backend.view())
    

def to_change_status():
    backend.update(selected_tuple,only_date,Task_Title.get(), Task_Detail.get(),Status.get())

def to_show_det():
        #https://www.w3schools.com/python/python_datetime.asp

    #WED, 3rd JUne, 20202 task lIst
    date_format= datetime.now().strftime("(%a)- %dth %b, %Y")    
    txt_heading.delete("1.0", END)   
    txt_heading.insert(END, "\t" + date_format + " Task Details")
    
    list1.delete(0, END)
    try:
        for index in backend.view_With_date_only(only_date):
            list1.insert(END, index)
            #print(index[0])
    except IndexError:
        
        messagebox.showinfo(title="Warning: ", message="Today's record is empty, please enter record first ...")
    
    
def convert_to_excel():
    df= backend.view_for_excel_generation()
    df.to_excel("my_todo.xlsx", index= False)
    messagebox.showinfo(title="Success: ", message="Todo task is conveted into excel succesfully...")



#---------------------------------------For heading and frames---------------------------------------

MainFrame= Frame(root)
MainFrame.grid()

Top= Frame(MainFrame, bd= 15, width= 1000, relief= RIDGE)
Top.pack(side= TOP)

MainTitle= Label(Top, font=("arial", 20, "bold"), text= "To Do")
MainTitle.grid()
MainTitle.configure(bg='light green', fg= "red")

btn_Display_frame = Frame(MainFrame, bd= 10, width= 900, height= 500, relief= RIDGE)
btn_Display_frame.pack(side= BOTTOM)

Task_frame = Frame(btn_Display_frame, bd= 10, width= 400, height= 500, relief= RIDGE)
Task_frame.pack(side= LEFT)
Task_frame.configure(bg='light blue')

status_frame = Frame(btn_Display_frame, bd= 10, width= 450, height= 500, relief= RIDGE)
status_frame.pack(side= RIGHT)
status_frame.configure(bg='LIGHT green')

Task_frame1 = Frame(Task_frame, bd= 10, width= 300, height= 200, relief= RIDGE)
Task_frame1.pack(side= TOP)

status_frame1 = Frame(Task_frame, bd= 10, width= 300, height= 120, relief= RIDGE)
status_frame1.pack(side= BOTTOM)

Task_frame2 = Frame(status_frame, bd= 10, width= 300, height= 500, relief= RIDGE)
Task_frame2.pack(side= TOP)

status_frame2 = Frame(status_frame, relief= RIDGE)
status_frame2.pack(side= BOTTOM)


#---------------------------------------For Labels and text filelds ---------------------------------------


lbldate= Label(Task_frame1, font=("arial", 14, "bold"), text= "Date", bd=7)
lbldate.grid(row=0, column=0, sticky=W)


txtdate= Entry(Task_frame1, font=("arial", 14, "bold"), textvariable= date, bd=7, insertwidth= 2, justify= RIGHT)
txtdate.grid(row=0, column=1)

lbltask_title= Label(Task_frame1, font=("arial", 14, "bold"), text= "Task Title", bd=7)
lbltask_title.grid(row=1, column=0, sticky=W)

txttask_title= Entry(Task_frame1, font=("arial", 14, "bold"), textvariable= Task_Title, bd=7, insertwidth= 2, justify= RIGHT)
txttask_title.grid(row=1, column=1)

lbltask_detail= Label(Task_frame1, font=("arial", 14, "bold"), text= "Task Detail", bd=7)
lbltask_detail.grid(row=2, column=0, sticky=W)

txttask_detail= Entry(Task_frame1, font=("arial", 14, "bold"), textvariable= Task_Detail, bd=7, insertwidth= 2, justify= RIGHT)
txttask_detail.grid(row=2, column=1)






lblstatus= Label(Task_frame1, font=("arial", 14, "bold"), text= "Status", bd=7)
lblstatus.grid(row=3, column=0, sticky=W)

#------------------------------------------------------------Display widow------------------------------------------------------

list1=Listbox(Task_frame2, height= 14,width=50)
list1.grid(row=1,column=0)
list1.configure(font= ("arial", 10, "bold"), bd=10, relief= SUNKEN)

list1.bind('<<ListboxSelect>>',get_selected_row)

txt_heading= Text(Task_frame2, width=45, height= 2, font= ("arial", 14, "bold"))
txt_heading.grid(row=0, column=0)
#--------------------------------------for buttons-------------------------------------------------------------------------------




btnadd_task= Button(status_frame1, padx=18, bd=7, font= ("arial", 14, "bold"), width= 10, text= "Add Task", command= to_add_task)
btnadd_task.grid(row=0, column=0)

btnchange_status= Button(status_frame1, padx=18, bd=7, font= ("arial", 14, "bold"), width= 10, text= "Task Update", command= to_change_status)
btnchange_status.grid(row=0, column=1)

btnshow= Button(status_frame2, padx=18, bd=7, font= ("arial", 16, "bold"), width= 10, text= "Show Tasks", command= to_show_summary)
btnshow.grid(row=0, column=1)

btnshow= Button(status_frame2, padx=18, bd=7, font= ("arial", 16, "bold"), width= 10, text= "Show details", command= to_show_det)
btnshow.grid(row=1, column=1)

btndelete= Button(status_frame2, padx=18, bd=7, font= ("arial", 16, "bold"), width= 5, text= "DELETE", command= to_delete)
btndelete.grid(row=1, column=0)

btnreset= Button(status_frame2, padx=18, bd=7, font= ("arial", 16, "bold"), width= 5, text= "RESET", command= to_reset)
btnreset.grid(row=0, column=0)

btnexit= Button(status_frame2, padx=18, bd=7, font= ("arial", 16, "bold"), width= 3, text= "EXCEL", command= convert_to_excel)
btnexit.grid(row=0, column=2)

btnexit= Button(status_frame2, padx=18, bd=7, font= ("arial", 16, "bold"), width= 3, text= "EXIT", command= to_exit)
btnexit.grid(row=1, column=2)




# Dictionary with options
choices = { 'Pending','Done'}
Status.set('Pending')
popupMenu = OptionMenu(Task_frame1 ,Status, *choices)
popupMenu.config(font=("arial", 14, "bold"), bg="red", fg="white", width=16)

popupMenu.grid(row = 3, column =1, columnspan=2)
    



root.mainloop() 
