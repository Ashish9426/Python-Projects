def fun1():
    student  = dict()

    no = int(input('Enter no of student  : '))

    for x in range(no):
        name = input('Name of student : ')
        p = int(input('Marks of physics : '))
        c = int(input('Marks of chemistry : '))
        m = int(input('Marks of math : '))

        marks = {'physics':p,'chemistry':c,'math':m}
        student[name] = marks
        print('Name\tPhy\tChe\tMath\tTotal')
        for name,m in student.items():
            total = 0
            print(name, end='\t')
            print(m['physics'], end='\t')
            print(m['chemistry'], end='\t')
            print(m['math'], end='\t\t')
            total = m['physics'] + m['chemistry'] + m['math']
            print(total)

fun1()