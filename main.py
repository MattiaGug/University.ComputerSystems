
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Define the structured type The tasks that include:
class Homework:
    def __init__(self, name, surname):
        # a Stud type St field representing a student
        self.st = Student(name, surname)
        # 2. a hw list of 5 integer elements which represents the evaluation in 
        # thirtieths (30/30) of eachof 5 tasks acquired during the semester; 
        # if an assignment has not been delivered, therating indicated is -1
        self.hw = [0, 0, 0, 0, 0]
        # 3. an entire grade field which is the final grade assigned
        self.grade = 0

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

def setVoto(valhw):
    # from a homework list, set the grade of each student
    # the grade is the average of the evaluations of the 5 tasks

    for i in range(0, len(valhw)):
        # get the average of the 5 tasks, if some values is -1 add to the average +12
        sum = 0
        for j in range(0, len(valhw[i].hw)):
            if valhw[i].hw[j] == -1:
                sum += 12
            else:
                sum += valhw[i].hw[j]

        valhw[i].grade = proper_round(sum/len(valhw[i].hw))
    
def ordStud(valhw):
    # from a homework list, sort the students by the name in ascending order
    # use key with concatenation of the name and surname
    # return a list of students

    return sorted(valhw, key=lambda x: x.st.surname + x.st.name )

def ordVoto(valhw):
    # from a homework list, sort the students by the average grade in descending order
    # return a list of students
    return sorted(valhw, key=lambda x: x.grade, reverse=True)

def findName(homeworks, prefix):
    # from a homework list, find the student with the prefix in the name
    # return the index of the student in the list, othrewise return -1
    for i in range(0, len(homeworks)):
        if prefix in (homeworks[i].st.surname + homeworks[i].st.name):
            return i
    return -1

def findVoto(homeworks, voto):
    # from a homework list, find the student with the voto
    # return a list with indexes of the students with the same voto, othrewise return -1
    # if there is more than one student with the same voto, return a list with all the indexes
    # of the students with the same voto

    list_index = []

    for i in range(0, len(homeworks)):
        if homeworks[i].grade == voto:
            list_index.append(i)

    if len(list_index) == 0:
        return -1
    return list_index


def main():
    # initialize the homework list with input from the user
    valhw = []
    
    # ask for the quantity of students
    n = int(input("Insert the quantity of students: "))

    # create a list of Homework type with the quantity of students
    for i in range(0, n):
        # ask for the name and surname of the student
        name = input("Insert the name of the student: ")
        surname = input("Insert the surname of the student: ")
        # create a new Homework type
        homework = Homework(name, surname)
        # ask for the evaluations of the 5 tasks
        for j in range(0, 5):
            homework.hw[j] = int(input("Insert the evaluation of the task " + str(j+1) + ": "))
        # add the new Homework type to the list
        valhw.append(homework)

    # call the setVoto function
    setVoto(valhw)
    # print all the students with the average grade
    print("The students with the average grade are:")
    for i in range(0, len(valhw)):
        print(valhw[i].st.surname + " " + valhw[i].st.name + ": " + str(valhw[i].grade))

    # call ordStud function
    valhw = ordStud(valhw)
    # print all the students with the name in ascending order
    print("The students with the name in ascending order are:")
    for i in range(0, len(valhw)):
        print(valhw[i].st.surname + " " + valhw[i].st.name + ": " + str(valhw[i].grade))

    for i in range(0, 3): # for test purposes
        name2search = input("Insert the name of the student to search: ")
        # call findName function
        index = findName(valhw, name2search)
        # print the student with the name John
        if index != -1:
            print("The student with the name " + name2search + " is: " + valhw[index].st.surname + " " + valhw[index].st.name)
        else:
            print("There is no student with the name " + name2search)

    # call ordVoto function
    valhw = ordVoto(valhw)
    # print all the students with the average grade in descending order
    print("The students with the average grade in descending order are:")
    for i in range(0, len(valhw)):
        print(valhw[i].st.surname + " " + valhw[i].st.name + ": " + str(valhw[i].grade))

    # ask for the voto to search
    voto = int(input("Insert the voto to search: "))
    # call findVoto function
    list_index = findVoto(valhw, voto)
    # print the students with the voto
    if list_index != -1:
        print("The students with the voto " + str(voto) + " are:")
        for i in range(0, len(list_index)):
            print(valhw[list_index[i]].st.surname + " " + valhw[list_index[i]].st.name + ": " + str(valhw[list_index[i]].grade))
    else:
        print("There is no student with the voto " + str(voto))

# call the main function
if __name__ == '__main__':
    main()