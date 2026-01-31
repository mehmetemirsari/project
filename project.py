from datetime import datetime,timedelta
import random
def menu():
    print("You may select one of the following:\n\t1) Add Student\n\t2) Search student\n\t3) Search course\n\t4) Add course completion\n\t5) Show student's record\n\t0) Exit")
def major():
    print("Please select student's major:\n\tCE: Computational Engineering\n\tEE: Electrical Engineering\n\tET: Energy Technology\n\tME: Mechanical Engineering\n\tSE: Software Engineering")
def generate_id():
    ids = []
    ffil = open("students.txt", "r")
    lin = ffil.readlines()
    ffil.close()

    for bart in lin:
        bart = bart.strip()
        partingen = bart.split(",")
        ids.append(partingen[0])

    while True:
        newidd = random.randint(10000, 99999)
        if str(newidd) not in ids:
            return newidd

while True:
    try:
        menu()
        se = int(input("What is your selection?\n"))
        if se==0:
            print("Program ended successfully.")
            break

        elif se == 1:
            stu=[]
            while True:
                name=input("Please enter the name of the student:\n")
                if not name.isalpha() or name[0] != name[0].upper():
                    print("Names must contain only letters and start with capitals!")
                else:
                    id=generate_id()
                    stu.append(id)
                    break
            while True:
                surname=input("Please enter the last name of the student:\n")
                if not surname.isalpha() or surname[0] != surname[0].upper():
                    print("Last names must contain only letters and start with capitals!")
                else:
                    stu.append(surname)
                    stu.append(name)
                    break
            while True:
                middle=input("Please enter the middle name of the student (press enter and leave it blank if no middle name):\n")
                if not middle:
                        stu.append(middle)
                        amail = f"{name}.{surname}@lut.fi"
                        email=amail.lower()
                        stu.append(email)
                        stu.append(datetime.now().strftime("%Y"))
                        break
                if not middle.isalpha() or middle[0] != middle[0].upper():
                    print("Last names must contain only letters and start with capitals!")
                else:
                    stu.append(middle)
                    amail = f"{name.lower()}.{surname.lower()}@lut.fi"
                    email=amail.lower()
                    stu.append(email)
                    stu.append(datetime.now().strftime("%Y"))
                    break
            while True:
                major()
                sel=input("Please enter your choice:\n")
                if sel!="CE" and sel!="EE" and sel!="ET" and sel!="ME" and sel!="SE":
                    print("Please enter a valid choice!")
                else:
                    stu.append(sel)
                    break
            fil=open("students.txt","a")
            final = ""
            for i in range(len(stu)):
                final += str(stu[i])
                if i < len(stu) - 1:
                    final += ","
            fil.write(final+"\n")
            print("Student added successfully!")
            fil.close()
        elif se == 2:
            stu = input("Give at least 3 characters of the students first,last or middle name:\n")
            stu = stu.lower()

            if len(stu) < 3:
                print("Students must have at least 3 characters.")
            else:
                filingen = open("students.txt", "r")
                linet = filingen.readlines()
                filingen.close()

                muck = False
                for a in linet:
                    a = a.strip()
                    checkku = a.lower()

                    if stu in checkku:
                        parts = a.split(",")
                        studentid = parts[0]
                        surname = parts[1]
                        name = parts[2]
                        middle = parts[3]
                        print(f"ID: {studentid}, {surname}, {name} {middle}")

                        muck = True

                if not muck:
                    print("No matching students.")
        elif se == 3:
            cou=input("Give at least 3 characters of the name of the course or the teacher:")
            cou=cou.lower()
            if len(cou) < 3:
                print("Course must have at least 3 characters.")
            else:
                coursingen=open("courses.txt","r")
                line=coursingen.readlines()
                coursingen.close()
                bucks=False
                for b in line:
                    b=b.strip()
                    cheek=b.lower()
                    if cou in cheek:
                        parts=b.split(",")
                        id=parts[0]
                        name=parts[1]
                        listeacher=parts[3:]
                        teacher=""
                        for item in listeacher:
                            if teacher=="":
                                teacher=item
                            else:
                                teacher+=", "+item
                        print(f"ID: {id}, Name: {name}, Teacher(s): {teacher}")
                        bucks=True
                if not bucks:
                    print("No matching courses.")
        elif se == 4:
            stutext = open("students.txt", "r")
            stulines = stutext.readlines()
            stutext.close()

            coutext = open("courses.txt", "r")
            coulines = coutext.readlines()
            coutext.close()

            courseids = []
            stuids = []


            for c in coulines:
                parte = c.strip().split(",")
                courseids.append(parte[0])


            for s in stulines:
                splits = s.strip().split(",")
                stuids.append(splits[0])


            while True:
                courseid = input("Give the course ID: ")
                if courseid not in courseids:
                    print("Course not found.")
                else:
                    break


            while True:
                studentsid = input("Give the student ID: ")
                if studentsid not in stuids:
                     print("Student not found.")
                else:
                    break


            ffil = open("passed.txt", "r")
            lines = ffil.readlines()
            ffil.close()

            old_line = None
            old_grade = None

            for line in lines:
                pv = line.strip().split(",")
                if pv[0] == courseid and pv[1] == studentsid:
                    old_line = line
                    old_grade = int(pv[3])
                    break


            if old_line == None:


                while True:
                    try:
                        grade = int(input("Give the grade:\n"))
                        if grade < 1 or grade > 5:
                            print("Grade is not a correct grade.")
                            continue
                        gradet = grade
                        break
                    except ValueError:
                        print("Please enter a number.")

                while True:
                    try:
                        datestr = input("Enter a date (YYYY-MM-DD): ")
                        datepass = datetime.strptime(datestr, "%Y-%m-%d")
                        today = datetime.today()
                        limit = today - timedelta(days=30)

                        if datepass > today:
                            print("Date is in the future. Try again.")
                        elif datepass < limit:
                            print('Input date is older than 30 days. Contact "opinto".')
                            date_valid = False
                            break
                        else:
                            print("Input date is valid.")
                            date_valid = True
                            break
                    except:
                        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                if not date_valid:
                    continue

                newline = courseid + "," + studentsid + "," + datestr + "," + str(gradet) + "\n"

                fv = open("passed.txt", "a")
                fv.write(newline)
                fv.close()

                print("New record added.")
            else:
                while True:
                    try:
                        grade = int(input("Give the grade:\n"))
                        if grade < 1 or grade > 5:
                            print("Grade is not a correct grade.")
                            continue

                        if grade < old_grade:
                            print("New grade cannot be lower than the old grade.")
                            continue

                        gradet = grade
                        break

                    except ValueError:
                        print("Please enter a number.")

                date_valid = False
                while True:
                    try:
                        datestr = input("Enter a date (YYYY-MM-DD):\n")
                        datepass = datetime.strptime(datestr, "%Y-%m-%d")
                        today = datetime.today()
                        limit = today - timedelta(days=30)

                        if datepass > today:
                            print("Date is in the future. Try again.")
                        elif datepass < limit:
                            print('Input date is older than 30 days. Contact "opinto".')
                            date_valid = False
                            break
                        else:
                            print("Input date is valid.")
                            date_valid = True
                            break
                    except ValueError:
                        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                if not date_valid:
                    continue
                new_line = courseid + "," + studentsid + "," + datestr + "," + str(gradet) + "\n"

                for i in range(len(lines)):
                    if lines[i] == old_line:
                        lines[i] = new_line
                        break

                fv = open("passed.txt", "w")
                fv.writelines(lines)
                fv.close()

                print("Record updated successfully.")
        elif se==5:
            try:
                zart=input("Give the student ID:\n")
                fiail = open("students.txt", "r")
                linet = fiail.readlines()
                fiail.close()

                goo = False
                for z in linet:
                    z = z.strip()
                    checkku = z.lower()

                    if zart in checkku:
                        barts = z.split(",")
                        idd = barts[0]
                        surnamee = barts[1]
                        namee = barts[2]
                        middlee = barts[3]
                        mail = barts[4]
                        year = barts[5]

                        major_code = barts[6].strip()

                        if major_code == "CE":
                            major = "Computational Engineering"
                        elif major_code == "ME":
                            major = "Mechanical Engineering"
                        elif major_code == "EE":
                            major = "Electrical Engineering"
                        elif major_code == "ET":
                            major = "Energy Technology"
                        elif major_code == "SE":
                            major = "Software Engineering"

                        print(f"Student ID: {idd}\nName: {surnamee}, {namee} {middlee}\nStarting year: {year}\nMajor: {major}\nEmail: {mail}")

                        goo = True
                if not goo:
                    print("No matching student.")
                if goo:
                    pfile = open("passed.txt", "r")
                    plines = pfile.readlines()
                    pfile.close()
                    records=[]
                    for lin in plines:
                        p=lin.strip().split(",")
                        if p[1]==idd:
                            records.append(p)
                    if len(records)==0:
                        print("\nNo passed courses.")
                    else:
                        cfile = open("courses.txt", "r")
                        clines = cfile.readlines()
                        cfile.close()
                        totalcredits=0
                        totalgrade=0
                        countgrade=0
                        for rec in records:
                            cid=rec[0]
                            cdate=rec[2]
                            gradet=rec[3]
                            cname="Unknown"
                            credits="0"
                            teachers=""
                            for cl in clines:
                                partingen=cl.strip().split(",")
                                if partingen[0]==cid:
                                    cname=partingen[1]
                                    credits=partingen[2]
                                    tlist=partingen[3:]
                                    for t in tlist:
                                        if teachers=="":
                                            teachers=t
                                        else:
                                            teachers=teachers+", "+t
                                    break
                            print(f"Course ID: {cid}, Name: {cname}, Credits: {credits}\nDate: {cdate}, Teachers: {teachers}, grade: {gradet}")
                            totalgrade+=int(gradet)
                            countgrade+=1
                            totalcredits+=int(credits)
                        avg=float(totalgrade/countgrade)
                        print(f"Total credits: {totalcredits}, average grade: {avg:.1f}")
            except ValueError:
                print("Please enter numbers.")
    except ValueError:
        print("Please enter a number between 0-5.")


