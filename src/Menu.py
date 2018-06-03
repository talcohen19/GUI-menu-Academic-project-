import tkinter as tk


class menu(tk.Frame):

    def __init__(self,root):
        root.geometry('200x100')
        self.root=root
        self.root.winfo_screenwidth()
        tk.Frame.__init__(self,root)
        self.pack()
        self.buttons=[]
        self.quesionWindows=[]
        self.counter = -1
        self.placment_row=0
        label=tk.Label(self)
        label.grid(row=1,column=0)

    def addQuestion(self,button_text,title,description,instructions,numberOf_param,command_act,size='300x300'):
        """add details to a new question and,
         design the window,
         finally conceal/withdraw the question window"""
        self.counter += 1
        if self.counter % 2 == 0:
            self.placment_row += 1
        num=self.counter
        self.buttons.append(tk.Button(self,text=button_text,command=lambda :self.open(num)))
        self.buttons[len(self.buttons)-1].grid(row=2+ self.placment_row ,column=self.counter%2)
        self.quesionWindows.append(questionWindow(
            self.root,self.counter,title,description,instructions,numberOf_param,command_act,size))
        self.quesionWindows[self.counter].withdraw()

    def open(self,numOf_q):
        """reveal the question window"""
        self.quesionWindows[numOf_q].deiconify()

    def getWindow(self,index):
        """return specific top level window"""
        return self.quesionWindows[index]


class questionWindow(tk.Toplevel):
    def __init__(self,parent,q_num,title,description,instructions,numberOf_param,command_act,size):
        tk.Toplevel.__init__(self,parent)
        self.geometry(size)
        self.q_num=q_num
        self.resizable(False,False)
        self._title_lbl=tk.Label(self,text=title)
        self._title_lbl.grid(row=0,column=0)
        self._description_lbl=tk.Label(self,text=description)
        self._description_lbl.grid(row=1,column=0)
        self._instructions_lbl=tk.Label(self,text=instructions)
        self._instructions_lbl.grid(row=2,column=0)
        self.numberOfParam=numberOf_param

        """text box list"""
        self.paramText=[]
        """labels list"""
        self.paramLabels=[]

        for i in range(self.numberOfParam):
            self.paramLabels.append(tk.Label(self))
            self.paramLabels[i].grid(row=3+i,column=0,sticky='w',padx=32)
            self.paramText.append(tk.Text(self,bg='darkgrey'))
            self.paramText[i].grid(row=3+i,column=0,sticky='e')
        self.submit_bt=tk.Button(self,text="Sumbit",command=lambda :self.submitMethod())
        self.submit_bt.grid(row=3+self.numberOfParam,column=0)
        self._res_lbl=tk.Label(self)
        self._res_lbl.grid(row=4+self.numberOfParam,column=0,sticky='w')

        """diversity size window in accordance with the size of the input"""
        self.dic_size = {'small':[2,1],
                         'normal':[18,1],
                         'large':[12,7]}

        """which method the button supposed to start"""
        self.command_act = command_act
        self.protocol("WM_DELETE_WINDOW", self.withdraw)

    @property
    def title_lbl(self):
        return self._title_lbl

    @property
    def instruction_lbl(self):
        return self._instructions_lbl

    @property
    def description_lbl(self):
        return self._description_lbl

    @property
    def res_lbl(self):
        return self._res_lbl

    @title_lbl.setter
    def title_lbl(self,title):
        self._title_lbl.configure(text=title)

    @instruction_lbl.setter
    def instruction_lbl(self,instruction):
        self._instructions_lbl.configure(text=instruction)

    @description_lbl.setter
    def description_lbl(self,description):
        self._description_lbl.configure(text=description)

    @res_lbl.setter
    def res_lbl(self,resualt):
        self._res_lbl.configure(text=resualt)

    def set_parameters_lbl(self,**texts):
        """set text labels respectively"""
        for text,index in texts.items():
            self.paramLabels[index].configure(text=text)

    def set_size_text(self,index_text,size):
        """set size textbox respectively"""
        self.paramText[index_text].configure(width = self.dic_size[size][0],
                                        height=self.dic_size[size][1])

    def submitMethod(self):
        """get the input from the textbox & set the result on the result label"""
        parameters=[]
        for i in range(self.numberOfParam):
            parameters.append(self.paramText[i].get('1.0','end-1c'))
        self.res_lbl=self.command_act(self.q_num,parameters)

