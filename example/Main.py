import Menu as menu
from assigment2 import Answers
from assigment2 import tests
import tkinter as tk

def return_Details(index):
    """determime details for the quesion window: title,description,instructions,numberOf_param"""
    string_dic = {
        1: ("Q1","welcome to Q1", " clean half of the matrix \n", "Paramaters:\nmatrix- list of lists \n key(=1)- if 0 "
                                                             "clean the left side \nelse the upper right\n"
                                                                  "Instructions:\nplace space beetween objects \n new line beetween rows\n "
                                                                  "of the matrix(no brackets)\n",2),
        2: ("Q2","welcome to Q2", " decrypt the string \nby moving each charachter \n'key' times back \n",
            "Paramaters:\nString- to encrypt\n key(=1)- key encryption an integer\n",2),
        3: ("Q3","welcome to Q3", "merger two sorted iterables \n"
            , "Paramaters:\niterable1,iterable2- 2 iterables objects\n"
              "Instructions:\nplace space beetween objects (no brackets)",2),
        4: ("Q4","welcome to Q4", "sort list of countries by num of medals \n"
            , "Paramaters:\nfile name- file to read the information,\n how_to_rank-key to rank the countries\n"
              "can be 'total'-to sum all medals,\n 'gold'-to sum by gold medal\n'weighted'-"
              "gives a weight for each medal",2)
        }
    return string_dic[index]

"""each method build her question window: """
def q1_window(menu):
    details=return_Details(1)
    menu.addQuestion(details[0],details[1],details[2],details[3],details[4],question_adapter,'250x650')
    menu.getWindow(0).set_parameters_lbl(Matrix=0,Key=1)
    menu.getWindow(0).set_size_text(0,'large')
    menu.getWindow(0).set_size_text(1,'small')

def q2_window(menu):
    details=return_Details(2)
    menu.addQuestion(details[0],details[1],details[2],details[3],details[4],question_adapter,'250x300')
    menu.getWindow(1).set_parameters_lbl(String=0,Key=1)
    menu.getWindow(1).set_size_text(0, 'normal')
    menu.getWindow(1).set_size_text(1, 'small')

def q3_window(menu):
    details = return_Details (3)
    menu.addQuestion (details[0], details[1], details[2], details[3], details[4],question_adapter)
    menu.getWindow (2).set_parameters_lbl (Iterable1=0, Iterable2=1)
    menu.getWindow (2).set_size_text (0, 'normal')
    menu.getWindow (2).set_size_text (1, 'normal')

def q4_window(menu):
    details = return_Details (4)
    menu.addQuestion (details[0], details[1], details[2], details[3], details[4], question_adapter,'300x350')
    menu.getWindow (3).set_parameters_lbl (Filename=0, How_to_rank=1)
    menu.getWindow (3).set_size_text (0, 'normal')
    menu.getWindow (3).set_size_text (1, 'normal')

def question_adapter(q_num,parameters):
    """question adapter for the the gui conditions and rules
    each top level window get this method as the action command
    the index(q_num) determines which command the window do"""
    submit_dic = {0: lambda:Answers ().half (q1_convert(parameters[0]),
                                             int(parameters[1]) if parameters[1]  is not "" else None ),
                  1: lambda: Answers ().encrypt(parameters[0],int(parameters[1]) if parameters[1]  is not "" else None ),
                  2: lambda: Answers ().merge (q3_convert(parameters[0]), q3_convert(parameters[1])),
                  3: lambda: Answers ().rank(parameters[0], parameters[1])}

    """convert from list to str"""
    if q_num ==0 or q_num==2:
        return list_to_str(submit_dic[q_num]())

    return str(submit_dic[q_num]())

def list_to_str(list):
    """convert from list to string"""
    res=""
    for obj in list:
        res+=str(obj)+("\n" if isinstance(obj,type(list)) else ",")
    return  res

def q3_convert(string_toconv):
    """convert from str to list"""
    return [int(columm) for columm in string_toconv.split(sep=" ")]

def q1_convert(string_toconv):
    """convert from str to list"""
    return [[columm  for columm in row.split(sep=" ") if columm is not ""] for row in string_toconv.split(sep='\n')]


if __name__ == '__main__':

    """call to the test unit"""
    tests().test_half()
    tests().test_encrypt()
    tests().test_merge()
    tests().test_rank()

    root=tk.Tk()
    root.title("Assigment2")
    program_menu=menu.menu(root)
    q1_window(program_menu)
    q2_window(program_menu)
    q3_window(program_menu)
    q4_window(program_menu)
    root.mainloop()







