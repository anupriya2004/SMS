import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="pass1234",database="schoolmanagement")
cur=con.cursor()
#ADDING A NEW STUDENT'S INFO#
def add_student():
    adno=int(input("enter admission number="))
    sname=input("enter student name=")
    dob=input("enter dob=")
    c=int(input("enter class="))
    sec=input("enter section=")
    q1="insert into studentsinfo values({},'{}','{}',{},'{}')".format(adno,sname,dob,c,sec)
    cur.execute(q1)
    print("RECORD OF THE NEW STUDENT ADDED SUCCESSFULLY!!!")
    con.commit()
    main_menu()

#SEARCHING STUDENT'S RECORD#
def search_stu_record():
    adno=int(input("enter admission number="))
    q1="select*from studentsinfo where admission_no={}".format(adno)
    cur.execute(q1)
    row=cur.fetchone()
    print("DETAILS OF THE STUDENT WITH ADMISSION NO.",adno,"ARE")
    print("ADMISSION NUMBER=",row[0])
    print("NAME OF THE STUDENT IS",row[1])
    print("DATE OF BIRTH=",row[2])
    print("CLASS=",row[3])
    print("SECTION=",row[4])
    print("RECORD DISPLAYED SUCCESSFULLY!!!")
    main_menu()


#COUNTING THE NUMBER OF NEW STUDENTS IN EACH SECTION#
def counting():
    c=input("TOTAL NUMBER OF NEW STUDENTS OF WHICH SECTION DO YOU WANT TO KNOW?")
    print("1.SECTION-A")
    print("2.SECTION-B")
    print("3.SECTION-C")
    print("4.ALL THREE ALTOGETHER")
    ch=int(input("enter choice="))
    if ch==1:
        q1="select section,count(*) from studentsinfo where section='A'"
        cur.execute(q1)
        t=cur.fetchone()
        print("SECTION" , "TOTAL NUMBER OF NEW STUDENTS", sep="   ")
        print(t[0],t[1],sep="              ")
    elif ch==2:
        q1="select section,count(*) from studentsinfo where section='B'"
        cur.execute(q1)
        t=cur.fetchone()
        print("SECTION" , "TOTAL NUMBER OF NEW STUDENTS", sep="   ")
        print(t[0],t[1],sep="              ")
    elif ch==3:
        q1="select section,count(*) from studentsinfo where section='C'"
        cur.execute(q1)
        t=cur.fetchone()
        print("SECTION" , "TOTAL NUMBER OF NEW STUDENTS", sep="   ")
        print(t[0],t[1],sep="              ")
    elif ch==4:
        q1="select section,count(*) from studentsinfo group by section"
        cur.execute(q1)
        t=cur.fetchall()
        for i in t:
             print("SECTION" , "TOTAL NUMBER OF NEW STUDENTS", sep="   ")
             print(i[0],i[1],sep="              ")
    else:
        pass
    main_menu()


#FOR REMOVING STUDENT'S RECORD#
def remove_sturecord():
    adno=int(input("enter admission number="))
    q1="delete from studentsinfo where admission_no={}".format(adno)
    cur.execute(q1)
    q2="delete from marks where admission_no={}".format(adno)
    cur.execute(q2)
    print("RECORD DELETED SUCCESSFULLY!!!")
    con.commit()
    main_menu()


#DISPLAY ALL THE RECORDS OF THE STUDENTSINFO TABLE#
def display():
    q1="select*from studentsinfo order by section"
    cur.execute(q1)
    data=cur.fetchall()
    for i in data:
        print(i)
    main_menu()

#ADDING THE RECORD OF A NEW TEACHER#
def add_teacher_record():
    empid=int(input("enter id="))
    empname=input("enter name=")
    dob=input("enter dob=")
    depa=input("enter department=")
    desig=input("enter designation=")
    sal=int(input("enter salary="))
    q1="insert into teachersinfo values({},'{}','{}','{}','{}',{})".format(empid,empname,dob,depa,desig,sal)
    cur.execute(q1)
    print("RECORD OF THE NEW TEACHER ADDED SUCCESSFULLY!!!")
    con.commit()
    main_menu()


#DISPLAYING THE RECORDS OF THE TEACHERSINFO TABLE#
def display_teacherstable():
    q1="select*from teachersinfo"
    cur.execute(q1)
    data=cur.fetchall()
    for i in data:
        print(i)
    main_menu()


#SEARCHING A RECORD IN TEACHERSINFO TABLE#
def search_trecord():
    empid=int(input("enter employee id="))
    q1="select*from teachersinfo where empid={}".format(empid)
    cur.execute(q1)
    row=cur.fetchone()
    print("===========================================================================")
    print("===========================================================================")
    print("DETAILS OF THE TEACHER WITH EMPID",empid,"ARE:")
    print("===========================================================================")
    print("===========================================================================")
    print("EMPLOYEE ID=",row[0])
    print("EMPLOYEE NAME=",row[1])
    print("DOB=",row[2])
    print("DEPARTMENT=",row[3])
    print("DESIGNATION=",row[4])
    print("SALARY=",row[5])
    main_menu()


#DELETING A RECORD IN TEACHERSINFO TABLE#
def delete_trecord():
    empid=int(input("enter employee id="))
    q1="delete from teachersinfo where empid={}".format(empid)
    cur.execute(q1)
    print("RECORD DELETED SUCCESSFULLY!!!")
    con.commit()
    main_menu()


#UPDATING THE RECORDS IN TEACHERSINFO TABLE#
def update_trecord():
    empid=int(input("enter employee id="))
    print("===========================================================================")
    print("WHAT DO WANT TO UPDATE?")
    print("===========================================================================")
    print("1.DESIGNATION")
    print("2.SALARY")
    print("3.BOTH")
    a=int(input("enter your choice="))
    if a==1:
        d=input("enter designation=")
        q1="update teachersinfo set designation='{}' where empid={}".format(d,empid)
    elif a==2:
        s=int(input("enter salary="))
        q1="update teachersinfo set salary={} where empid={}".format(s,empid)
    elif a==3:
        d=input("enter designation=")
        s=int(input("enter salary="))
        q1="update teachersinfo set designation='{}',salary={} where empid={}".format(d,s,empid)
    else:
        print("INVALID CHOICE!!!!")
    cur.execute(q1)
    print("RECORD UPDATED SUCCESSFULLY!!!!")
    con.commit()
    main_menu()

    
def schoolrules():
    print("=============================================================================")
    print("=============================================================================")
    print("SCHOOL RULES ARE:")
    print("=============================================================================")
    print("=============================================================================")
    print("1.BE PUNCTUAL AND COME TO SCHOOL IN NEAT AND CLEAN UNIFORM WITH POLISHED SHOES")
    print("2.FOLLOW THE INSTRUCTIONS GIVEN BY YOUR RESPECTIVE TEACHERS")
    print("3.RESPECT ALL THE STAFF MEMBERS")
    print("4.75% OF ATTENDANCE IS MANDATORY SO BE REGULAR")
    print("5.FEES SHOULD BE SUBMITTED ON TIME IN ORDER TO AVOID ANY INCONVENIENCE")
    print("6.ANY KIND OF MISBEHAVIOUR BY THE STUDENT WILL NOT BE TOLERATED AND STRICT ACTIONS WILL BE TAKEN")
    main_menu()


#ADDING THE HY MARKS OF THE NEW STUDENT IN THE MARKS TABLE#
def marks():
    s="select admission_no from marks"
    L=[]
    cur.execute(s)
    t=cur.fetchall()
    for i in t:
        p=i[0]
        k=str(p)
        L.append(k)
    m="select admission_no from studentsinfo"
    L1=[]
    cur.execute(m)
    q=cur.fetchall()
    for j in q:
        o=j[0]
        z=str(o)
        L1.append(z)
    adno=int(input("enter the admission number="))
    if str(adno) in L and str(adno) in L1:
        print("MARKS FOR THIS ADMISSION NUMBER ALREADY EXISTS")
    elif str(adno) not in L and str(adno) not in L1:
        print("WRONG ADMISSION NUMBER ENTERED")
    elif str(adno) in L1 and str(adno) not in L:
        w="select section from studentsinfo where admission_no={}".format(adno)
        cur.execute(w)
        v=cur.fetchone()
        print(v)
        a=input("HAS THE STUDENT GIVEN THE HY EXAMS?YES/NO = ")
        if a=='NO' or a=='no':
            r=input("enter the reason for not giving the half yearly examinations=")
        elif a=='YES' or a=='yes':
            i="NULL"
            g="insert into marks(admission_no,phy_marks,chem_marks,eng_marks,maths_marks,bio_marks,bst_marks,acc_marks,eco_marks,ped_marks,cs_marks,hin_marks,ip_marks) values({},{},{},{},{},{},{},{},{},{},{},{},{})".format(adno,i,i,i,i,i,i,i,i,i,i,i,i)
            cur.execute(g)
            if v[0]=="A":
                p=int(input("enter phy marks="))
                c=int(input("enter chem marks="))
                m=int(input("enter maths marks="))
                e=int(input("enter eng marks="))
                print("OPTIONAL SUBJECTS:")
                print("1.COMPUTER SCIENCE")
                print("2.PHYSICAL EDUCATION")
                o=input("enter the optional subject the student chose=")
                if o=="1":
                    cs=int(input("enter cs marks="))
                    q1="update marks set phy_marks={},chem_marks={},maths_marks={},eng_marks={},cs_marks={} where admission_no={}".format(p,c,m,e,cs,adno)
                    cur.execute(q1)
                elif o=="2":
                    ped=int(input("enter ped marks="))
                    q1="update marks set phy_marks={},chem_marks={},maths_marks={},eng_marks={},ped_marks={} where admission_no={}".format(p,c,m,e,ped,adno)
                    cur.execute(q1)
                else:
                    print("THIS OPTIONAL SUBJECT IS NOT ALLOTTED FOR A PCM STUDENT")
            elif v[0]=="B":
                p=int(input("enter phy marks="))
                c=int(input("enter chem marks="))
                b=int(input("enter bio marks="))
                e=int(input("enter eng marks="))
                print("OPTIONAL SUBJECTS:")
                print("1.HINDI")
                print("2.PHYSICAL EDUCATION")
                o=input("enter the optional subject the student chose=")
                if o=="1":
                    h=int(input("enter hindi marks="))
                    q1="update marks set phy_marks={},chem_marks={},bio_marks={},eng_marks={},hin_marks={} where admission_no={}".format(p,c,b,e,h,adno)
                    cur.execute(q1)
                elif o=="2":
                    ped=int(input("enter ped marks="))
                    q1="update marks set phy_marks={},chem_marks={},bio_marks={},eng_marks={},ped_marks={} where admission_no={}".format(p,c,b,e,ped,adno)
                    cur.execute(q1)
                else:
                    print("THIS OPTIONAL SUBJECT IS NOT ALLOTTED FOR A PCB STUDENT")
            elif v[0]=="C":
                 bst=int(input("enter bst marks="))
                 acc=int(input("enter acc marks="))
                 eco=int(input("enter eco marks="))
                 e=int(input("enter eng marks="))
                 print("OPTIONAL SUBJECTS:")
                 print("1.INFORMATION PRACTICE")
                 print("2.PHYSICAL EDUCATION")
                 o=input("enter the optional subject the student chose=")
                 if o=="1":
                     ip=int(input("enter ip marks="))
                     q1="update marks set bst_marks={},acc_marks={},eco_marks={},eng_marks={},ip_marks={} where admission_no={}".format(bst,acc,eco,e,ip,adno)
                     cur.execute(q1)
                 elif o=="2":
                     ped=int(input("enter ped marks="))
                     q1="update marks set bst_marks={},acc_marks={},eco_marks={},eng_marks={},ped_marks={} where admission_no={}".format(bst,acc,eco,e,ped,adno)
                     cur.execute(q1)
                 else:
                     print("THIS OPTIONAL SUBJECT IS NOT ALLOTTED FOR A PCB STUDENT")
            else:
                 print("THERE ARE ONLY THREE SETIONS A,B AND C IN THE 11TH BATCH")
        else:
            pass
    else:
        pass
    con.commit()
    print("1.TRY AGAIN")
    print("2.RETURN BACK TO MAIN MENU")
    a=int(input("enter choice="))
    if a==1:
        marks()
    elif a==2:
        main_menu()
    else:
        print("INVALID")
      
            
    
def main_menu():
    print("=============================================================================")
    print("=============================================================================")
    print("=============================================================================")
    print("WELCOME TO THE SCHOOL MANAGEMENT SYSTEM")
    print("=============================================================================")
    print("=============================================================================")
    print("=============================================================================")
    print("WHAT DO YOU WANT TO DO?")
    print("=============================================================================")
    print("FOR STUDENTSINFO TABLE")
    print("=============================================================================")
    print("1.TO ADD THE DETAILS OF A NEW STUDENT")
    print("2.TO SEARCH A STUDENT'S RECORD BY ADMISSION NO")
    print("3.TO COUNT THE NUMBER OF NEW STUDENTS IN EACH SECTION")
    print("4.TO REMOVE A STUDENT'S RECORD BY ADMISSION NUMBER")
    print("5.TO DISPLAY THE RECORDS OF ALL THE NEWLY ADMITTED STUDENTS SECTION WISE")
    print("=============================================================================")
    print("FOR TEACHERSINFO TABLE")
    print("=============================================================================")
    print("6.TO ADD THE DETAILS OF A NEW TEACHER")
    print("7.TO SEARCH A TEACHER'S RECORD BY EMPLOYEE ID")
    print("8.TO UPDATE THE SALARY OR DESIGNATION OF THE TEACHER")
    print("9.TO REMOVE THE RECORD OF A TEACHER BY EMPLOYEE ID")
    print("10.TO DISPLAY RECORDS OF ALL THE TEACHERS")
    print("=============================================================================")
    print("11.TO ADD MARKS OF THE NEW STUDENTS IF HE/SHE HAS GIVEN THE HY EXAMS")
    print("=============================================================================")
    print("12.TO KNOW THE SCHOOL RULES")
    print("13.EXIT")
    ch=int(input("enter your choice="))
    if ch==1:
        add_student()
    elif ch==2:
        search_stu_record()
    elif ch==3:
        counting()
    elif ch==4:
        remove_sturecord()
    elif ch==5:
        display()
    elif ch==6:
        add_teacher_record()
    elif ch==7:
        search_trecord()
    elif ch==8:
        update_trecord()
    elif ch==9:
        delete_trecord()
    elif ch==10:
        display_teacherstable()
    elif ch==11:
        marks()
    elif ch==12:
        schoolrules()
    elif ch==13:
        exit()
    else:
        print("INVALID CHOICE ENTERED!!!!")
    cur.close()
    con.close()
main_menu()
    
    


