import itertools
import unittest
import functools


class Answers:
    def half(self, matrix, k=1):
        """return the right upper half of the matrix if k=1
        if k=0 return the left down half of the matrix
        Param: k-key, to set which half to return
            matrix-list of lists, can be diffrent length"""
        return [matrix[i][i:] if k == 0 else matrix[i][:i+1] for i in range(len(matrix))]

    def encrypt(self,string="vrorqjdqgwdqnviruwkhilvk",key=3):
        """this function decrypt a string by moving each letter by k moves forward in the alphabet
        String- the string to encrypt
        key- by how many letters move forward in the alphabet
        return the string encrypted"""
        return "".join([chr((ord(ch)-key-ord('a'))%(ord('z')-ord('a')+1)+ord('a')) for ch in string])

    def merge(self,iterable1, iterable2):
        """Genrator function
        the function get 2 iterable objects
        return : generator function that merge the 2 iterable objects"""
        stopItreation=-20000000
        iterator1 = iter(iterable1)
        iterator2 = iter(iterable2)
        object_from_iter1 = next(iterator1, stopItreation)
        object_from_iter2 = next(iterator2, stopItreation)
        obj=stopItreation
        while object_from_iter1 != stopItreation and object_from_iter2 != stopItreation:
            if object_from_iter1 >= object_from_iter2:
                temp = object_from_iter2
                object_from_iter2 = next (iterator2, stopItreation)
            else:
                temp = object_from_iter1
                object_from_iter1 = next (iterator1, stopItreation)
            yield temp

        if object_from_iter1 == stopItreation and object_from_iter2 != stopItreation:
            lastitertor = iterator2
            obj=object_from_iter2
        elif object_from_iter1 !=stopItreation and object_from_iter2 == stopItreation:
            lastitertor = iterator1
            obj=object_from_iter1

        while obj != stopItreation:
            yield obj
            obj = next(lastitertor,stopItreation)

    def rank(self,file_name, how_to_rank='total'):
        """the function get fileName that containing list of countries and num of medals
        :parameter how_to_rank - can be : 'gold' , 'total' , 'weight' and the default is 'total'
        the function return a sorted list by rank so :
        if how to rank is : total- all medals will calculaye, 'gold'- only gold medals  ,
        'weight'- each medal get ran (gold-3,silver-2,bronze-1)
        return : sorted list by how to rank field"""
        rank_dic={'total': lambda x:int(x[1])+int(x[2])+int(x[3]),
                  'gold' : lambda x: int(x[1]),
                  'weight': lambda x:3*int(x[1])+2*int(x[2])+int(x[3])}

        file=open(file_name,'r')
        total_list=[]
        for word in file:
            total_list.append(tuple(w for w in word.split(sep=' ') if w is not '\n'))

        namelist=[name[0] for name in total_list]
        ranks=[rank for rank in list(map(rank_dic[how_to_rank], total_list))]

        newlist = [(namelist[i], ranks[i]) for i in range(len(total_list))]
        newlist.sort(key=lambda x:x[1],reverse=True)
        string_res=""
        for i in range(len(newlist)):
            string_res+=str(newlist[i][0])+": "+str(newlist[i][1])+"\n"

        file.close()
        return string_res

    def createFile(self):
        fh = open('winners.txt','w')
        fh.write("USA 1022 794 705 \n")
        fh.write('ISRAEL 1 1 7 \n')
        fh.write('Great-Britain 263 295 289')
        fh.close()
        return fh.name

class tests(unittest.TestCase):
    def test_half(self):
        self.assertEqual(Answers().half([[1,2,3,4,5],
                                         [6,7,8,9,"spam"],
                                         [11,12,13,14,15],
                                         [16,"stam",18,19,20]],
                                        1),[[1],[6, 7, ],[11, 12, 13],[16, "stam", 18, 19]])

        self.assertEqual(Answers().half([[1, 2, 3, 4, 5],
                                         [6, 7, 8, 9, "spam"],
                                         [11, 12, 13, 14, 15],
                                         [16, "stam", 18, 19, 20]],
                                        0),[[1, 2, 3, 4, 5],[7, 8, 9, "spam"],[13, 14, 15],[19, 20]])

    def test_encrypt(self):
        self.assertEqual(Answers().encrypt("aaa",1),("zzz"))
        self.assertEqual(Answers().encrypt("ccd", 2),("aab"))

    def test_merge(self):
        first = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 24, 35, 40]
        second = [0, 1, 2, 3, 4, 10, 12, 14, 16, 18]
        third = [0, 1, 3, 5, 12, 22, 33, 43]
        for output in Answers().merge(range(0, 10, 1), [1, 15, 24, 35, 40]):  # first test
            self.assertEqual(output, first.pop(0))
        for output in Answers().merge(range(10, 20, 2), range(0, 5, 1)):  # second test
            self.assertEqual(output, second.pop(0))
        for output in Answers().merge([0], [1, 3, 5, 12, 22, 33, 43]):  # third test
            self.assertEqual(output, third.pop(0))

    def test_rank(self):
        self.assertEqual(Answers().rank("Winners.txt","gold"),("USA: 1022\nGreat-Britain: 263\nISRAEL: 1\n"))
        self.assertEqual(Answers().rank("Winners.txt","total"),("USA: 2521\nGreat-Britain: 847\nISRAEL: 9\n"))

