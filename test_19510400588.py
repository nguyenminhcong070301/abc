import math
import random

#Cau 1, 2, 3
class HUMAN(object):

    def __init__(self, age=None , gender=None):
        if age is not None:
            self._age = age
        else: 
            self._age = random.randint(1, 160)
        if gender is not None:
            self._gender = gender
        else:
            self._gender = random.choice(['male', 'female'])

    @property
    def eat(self):
        pass
    
    @property
    def sleep(self):
        pass
    
    @property
    def run(self):
        pass

class STUDENT(HUMAN):

    def __init__(self, age=None , gender=None , id=None , score=None , credit=None):
        super().__init__(age, gender)
        if score is not None:
            self._score = score
        else:
            self._score = round((random.uniform(0, 4)),1)
        if credit is not None:
            self._credit = credit
        else:
            self._credit = random.randint(0, 250)
        if id is not None:
            self._id = id
        else:
            self._id = "SV_{}".format(random.randint(0, 9999))
        if age is not None:
            self._age = age
        else:
            self._age = (random.randint(18, 28))
        if gender is not None:
            self._gender = gender
        else:
            self._gender = (random.choice(['male', 'female']))

    def result(self):
        if self._score >= 3.8 and self._score <= 4:
            return "A+"
        elif self._score >= 3.3 and self._score <= 3.7:
            return "A"
        elif self._score >= 3 and self._score <= 3.2:
            return "B+"
        elif self._score >= 2.6 and self._score <= 2.9:
            return "B"
        elif self._score >= 1.8 and self._score <= 2.5:
            return "C"
        elif self._score < 1.8:
            return "D"
    
    def graduate(self):
        if self.result != 'D' and self._credit == 250 and self._score >= 1.8:
            return True
        else: return False

# Cau 4 va cau 5
def sort(x: STUDENT):
    return x._score

def test_19510400588():
    n = input("Nhap so sinh vien: ")
    list_graduate = []
    list_student = []
    for i in range(int(n)):
        s = STUDENT()
        list_student.append(s)
        if s.graduate():
            list_graduate.append(s)
    list_student.sort(key=sort, reverse=True)
    print(f'MSSV co diem cao nhat: {list_student[0]._id}')
    for student in list_student:
        print(f'{student._id}: {student._score}, result: {student.result()}, credit: {student._credit}, graduate: {student.graduate()}')

test_19510400588()