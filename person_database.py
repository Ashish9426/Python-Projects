def fun1():
    ans = 'y'
    student = []
    while ans == 'y':
        print('1. Add Name')
        print('2. Show All')
        print('3. Search Name')
        print('4. Delete Name')
        print('5. Modidy Name')
        print('6. Exit')
        print('Enter Choice 1 .. 6')

        ch = int(input())
        if ch == 1:
            name = input('Enter Student Name')
            student.append(name)
            print('Record Saved')
        elif ch == 2:
            print('Name of Student')
            for x in student:
                print(x)
        elif ch == 3:
            sname = input('Search Name')
            if sname in student:
                print('Name found', sname)
            else:
                print('Name not Found', sname)
        elif ch == 4:
            dname = input('Name to Delete')
            if dname in student:
                student.remove(dname)
                print('Record Deleted')
            else:
                print('Record not Found')
        elif ch == 5:
            oname  = input('Old Name')
            newname = input('New Name')
            i = student.index(oname)
            student[i] = newname
            print('Record Updated')
        else:
            exit()
        ans = input('Continue y/n')

fun1()