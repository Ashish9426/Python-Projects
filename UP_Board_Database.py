def fun1():
    ans = 'y'
    student = {}
    while ans == 'y':
        print('1. Add Name and Marks of Student: ')
        print('2. Show All Record')
        print('3. Search Record by Name: ')
        print('4. Delete Record: ')
        print('5. Modify Name: ')
        print('6. Get Record by Name:')
        print('7. Exit')
        print('Enter Choice 1 .. 7')

        ch = int(input())
        if ch == 1:
            #name = input('Enter Student Name')
            #student.append(name)
            #print('Record Saved')

            name = input('Name of student : ')
            p = int(input('Marks of physics : '))
            c = int(input('Marks of chemistry : '))
            m = int(input('Marks of math : '))
            e = int(input('Marks of english : '))
            h = int(input('Marks of hindi : '))

            marks = {'physics': p, 'chemistry': c, 'math': m, 'english': e, 'hindi': h}
            student[name] = marks
            print('Record Saved')


        elif ch == 2:
            #print('Name of Student')
            #for x in student:
            #    print(x)
            print('Name\tPhy\tChe\tMath\tEng\tHin\tTotal')
            for name, m in student.items():
                total = 0
                print(name, end='\t')
                print(m['physics'], end='\t')
                print(m['chemistry'], end='\t')
                print(m['math'], end='\t')
                print(m['english'], end='\t')
                print(m['hindi'], end='\t\t')
                total = m['physics'] + m['chemistry'] + m['math'] + m['english'] + m['hindi']
                print(total)

        elif ch == 3:
            sname = input('Search Name : ')
            if sname in student:
                print('Name found : ', sname)
            else:
                print('Name not Found : ', sname)
        elif ch == 4:
            dname = input('Name to Delete : ')
            if dname in student:
                student.pop(dname)
                print('Record Deleted')
            else:
                print('Record not Found')
        elif ch == 5:
            oname  = input('Old Name : ')
            #newname = input('New Name : ')
            #i = student.index(oname)
            #student[i] = newname
            if oname in student:
                print('Name Found...')
                newname = input('Enter New Name : ')
                student[newname] = student[oname]
                del student[oname]
                print('Record Updated')
            else:
                print('Sorry... Record Not Found')
        elif ch == 6:
            sname = input('Search Name: ')
            if sname in student:
                print('*' * 50)
                print('Student Name : ',sname)
                #print('Entered Name Exist in Database', sname)
                #print('Show Record of', sname)
                t = 0
                for k, v in student[sname].items():
                    print('_'*20)
                    print(k, ':', v)
                    t = t + v
                print('*' * 50)
                print('\t\t\t\tTotal marks:', t)
                per = (t * 100) / 500
                print('*' * 50)
                print('\t\t\t\tpercentage: ',per)
                if per>=75:
                    print('\t\t\t\tCongratulations...!!!\n\t\t\t\tFirst Division with Dictintion')
                elif per>=60 and per<75:
                    print('\t\t\t\tFirst Division')
                elif per<60 and per>=45:
                    print('\t\t\t\tSecond Divsion')
                elif per<45 and per>=33:
                    print('\t\t\t\tThird Division')
                else:
                    print('\t\t\t\tFailed')
                print('*' * 50)
            else:
                print('Name not Found', sname)
        else:
            exit()
        ans = input('Continue y/n')

fun1()