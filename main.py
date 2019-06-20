
import json
import re

# code start from  hear........


class Admin:

# start code for student is here..................

    @classmethod
    def add_students(cls):
        flag = 1
        sic_no = int(input("please enter the sic No :- "))
        f1 = open("students.json" , "r");
        f1.readline()
        if f1.tell() != 0:
            f1.seek(0)
            b_data = json.load(f1)
            for student in b_data["students"]:
                if student["sic_no"] == sic_no:
                    print(f"{sic_no} is already registerd ")
                    flag = 0
                    break
            
        if flag != 0 :
            if f1.tell() == 0:
                b_data = {}
                b_data['students'] = []
            s_name = input("please enter the student name :- ")
            r = r"^[6-9][0-9]{9}"
            e = r"^[a-zA-z]{1,30}[0-9]*(@)[a-zA-z]{2,10}(.)(com|in|edu)"
            while True:
                phone = input("enter the mobile number:- ")
                if not re.match(r , phone):
                    print("please enter valid phone number:- ")
                else:
                    break
            while True:
                email = input("enter the mail id :- ")
                if not re.match(e , email):
                    print("please enter valid phone number:- ")
                else:
                    break

            b_data["students"].append({
                "sic_no" : sic_no,
                "name" : s_name,
                "phone" : phone,
                "email" : email
            })
            print("successfully added ")
        f1.close()
        f2 = open("students.json" , "w");
        json.dump(b_data , f2 , indent=2)
        f2.close()
        

    @classmethod
    def del_student(cls):
        sic_no = int(input("please enter the sic No which you want to deregister :- "))
        flag = 1
        i = 0
        f = open("students.json" , "r");
        b_data = json.load(f)
        f.close()
        for student in b_data["students"]:
            if student['sic_no'] == sic_no:
                del b_data["students"][i]
                flag = 0
                print("delete successfully")
                break
            i=+1
       
        if flag != 0:
            print(f"{sic_no} is not available in database:- ")
        f = open("students.json" , "w");
        json.dump(b_data , f , indent=2)
        f.close()

    @classmethod
    def avail_student(cls):
        
        f = open("students.json" , "r");
        b_data = json.load(f)
        for student in b_data["students"]:
            a = f"\n student SIC NO = {student['sic_no']} , Student Name = {student['name']} , Phone No = {student['phone']} , Email Id = {student['email']}"
            print(a)
        f.close()


    @classmethod
    def modify_student(cls):
        flag = 1
        
        sic = int(input("please enter the SIC NO "))
        f = open("students.json" , "r");
        b_data = json.load(f)
        for student in b_data["students"]:
            
            if student['sic_no'] == sic:
                a = f"\n student SIC NO = {student['sic_no']} , Student Name = {student['name']} , Phone No = {student['phone']} , Email Id = {student['email']}"
                print(a)
                s_name = input("enter the student name ")
                phone = input("enter the Phone number ")
                email = (input("enter the emailId"))
                student['name'] = s_name
                student['phone'] = phone
                student['email'] = email
                flag = 0
                break
            
        f.close()
        if flag != 0:
            print("this student info is not available in database")
        f = open("students.json" , "w");
        json.dump(b_data , f , indent=2)
        f.close()




    # here show all info about yhe books in this module has a error chexk leter error:- in books json file data is require
    @classmethod
    def add_books(cls):
        flag = 1
        b_name = input("please enter the book name :- ")
        a_name = input("please enter the author name :- ")
        total_copie = int(input("total copies ? :- "))

        f1 = open("books.json" , "r");
        f1.readline()
        if f1.tell() != 0:
            f1.seek(0)
            b_data = json.load(f1)

            for book in b_data["books"]:
                print(book["book_name"])
                if (book["book_name"] == b_name and book["author_name"] == a_name) :
                    book["copies"] += total_copie
                    flag = 0
                    break
            
        if flag != 0 :
            if f1.tell() == 0:
                b_data = {}
                b_data['books'] = []
            b_data["books"].append({
                "id" : len(b_data["books"]) + 1,
                "book_name" : b_name,
                "author_name" : a_name,
                "copies" : total_copie  
            })
            
        f1 = open("books.json" , "w");
        json.dump(b_data , f1 , indent=2)
        f1.close()
        print("successfully added ")

    @classmethod
    def del_books(cls):
        b_name = input("please enter the book name which you want to delete ")
        a_name = input("please enter the author name ")
        flag = 1
        i = 0
        f = open("books.json" , "r");
        b_data = json.load(f)
        for book in b_data["books"]:
            print(book["book_name"])
            if (book["book_name"] == b_name and book["author_name"] == a_name) :
                del b_data["books"][i]
                flag = 0
                break
            i=+1
        f.close()
        if flag != 0:
            print(f"{b_name} book is not available in database")
        f = open("books.json" , "w");
        json.dump(b_data , f , indent=2)
        f.close()

    @classmethod
    def avail_book(cls):
        
        f = open("books.json" , "r");
        b_data = json.load(f)
        for book in b_data["books"]:
            a = f"\n Book id = {book['id']} Book name = {book['book_name']} , Author Name = {book['author_name']} and Total Copies = {book['copies']}"
            print(a)
        f.close()

    @classmethod
    def modify_books(cls):
        flag = 1
        
        id = int(input("please enter the book id "))
        f = open("books.json" , "r");
        b_data = json.load(f)
        for book in b_data["books"]:
            
            if book['id'] == id:
                a = f"\n book name is {book['book_name']} , Author Name = {book['author_name']} and Total Copies = {book['copies']}"
                print(a)
                b_name = input("enter the book name ")
                a_name = input("enter the author name ")
                c = int(input("enter the copies"))
                book['book_name'] = b_name
                book['author_name'] = a_name
                book['copies'] = c
                flag = 0
                break
            
        f.close()
        if flag != 0:
            print("this type of book is not available in database")
        f = open("books.json" , "w");
        json.dump(b_data , f , indent=2)
        f.close()

# end of the admin functions


# starting of the librarian module


# end of the code books..........


# check admin user name and password

def check_pswd(usr , pswd):
    f = open('admin_pswd.json')
    data = json.load(f)

    for admin in data["admins"]:
        if admin['username'] == usr and admin['password'] == pswd:
            return True
    f.close()
    return False

# add admin in app

def add_admin():
    
    usr = input("please enter the user anme ")
    flag = 0
    while True:
        password = input("enter pswd which has atlist 1[a-z] , 1[A-Z] , 1[0-9] 1[special charecter] and length between[6-12] ")
        if (len(password)<6 and len(password) >12): 
            flag = -1
            break
        elif not re.search("[a-z]", password): 
            flag = -1
            break
        elif not re.search("[A-Z]", password): 
            flag = -1
            break
        elif not re.search("[0-9]", password): 
            flag = -1
            break
        elif not re.search("[!@#$%&]", password): 
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            print("successfully added") 
            f = open('admin_pswd.json',"r")
            data = json.load(f)
            f.close()
            data['admins'].append({
            'username' : usr,
            'password':password
        })
        f = open('admin_pswd.json' , 'w')
        json.dump(data , f , indent=2)
        f.close()
        break
    
    if flag ==-1: 
        print("Not a Valid Password") 


class Librarian(Admin):
    @classmethod
    def issue_book(cls):
        b_name = input("please enter the book name ")
        a_name = input("please enter the author name ")
        sic_no = int(input("enter the sic no "))
        name = input("enter your name")
        f1 = open("books.json" , "r")
        flag = 1
        f1.readline()
        if f1.tell() != 0:
            f1.seek(0)
            b_data = json.load(f1)
            i = 0
            for book in b_data['books']:
                if book['book_name'] == b_name and book['author_name'] == a_name and book['copies'] > 0:  # it check available book in library
                    flag = 0
                    f3 = open("issue_book.json")
                    f3.readline()
                    
                    if f3.tell() != 0:   #it check issue book is empty
                        f3.seek(0)
                        
                        is_data = json.load(f3)
                        i = 0
                        for data in is_data['issue']:
                            if data['sic_no'] == sic_no:  # it check student not take more than 2 book 
                                i+=1
                                
                            if data['b_name'] == b_name and data['b_a_name'] == a_name and data['sic_no'] == sic_no:  # it student has already its book
                                i = 10
                                print("you have already this book you cant issue this book")
                                break
                        f3.close()
                        if i<2:
                            
                            book['copies'] -=1
                            f1.close()
                            f1 = open('books.json' , "w")
                            json.dump(b_data , f1 , indent=2);
                            f2 = open('issue_book.json' ,'r')
                            i_data = json.load(f2)
                            f2.close()
                            f2 = open('issue_book.json' ,'w')
                            i_data["issue"].append({
                        "sic_no" : sic_no,
                        "name" : name ,
                        "b_id" : book['id'],
                        "b_name" : b_name,
                        "b_a_name" : a_name
                    })
                            print("successfully issue")
                            json.dump(i_data , f2 , indent=2)
                            f2.close()
                        elif i == 2:
                            print("hey you have already 2 books ")
                        elif i == 10:
                            print("you have this book")
                    else:
                        book['copies'] -= 1
                        f1.close()
                        f1 = open('books.json' , "w")
                        json.dump(b_data , f1 , indent=2);
                        f1.close()
                        i_data ={}
                        i_data["issue"] = []
                        f2 = open('issue_book.json' ,'w')
                        
                        i_data["issue"].append({
                        "sic_no" : sic_no,
                        "name" : name ,
                        "b_id" : book['id'],
                        "b_name" : b_name,
                        "b_a_name" : a_name
                    })
                        print("successfully issue")
                        json.dump(i_data , f2 , indent=2)
                        f2.close()
            
            if flag == 1:
                print("this book is not available in our library")
        else:
            print("library is empty")



    @classmethod
    def return_book(cls):
        print("plese enter your sic no:- ")
        sic = int(input())
        print("please enter the book name :- ")
        b_name = input()
        a_name = input("please enter the author name :- ")
        f1 = open("issue_book.json")
        data = json.load(f1)
        f1.close()
        i = 0
        flag2 = 1
        flag1 = 1
        for book in data['issue']:
            if book['sic_no'] == sic and book['b_name'] == b_name and book['b_a_name'] == a_name:  #check book available in issue book 
                del data['issue'][i]
                f1 = open("issue_book.json" , "w")
                json.dump(data , f1 , indent=2)
                f1.close()
                f2 = open("books.json")
                f2.readline()
                if f2.tell() != 0:
                    f2.seek(0)
                    data1 = json.load(f2)
                    f2.readline()
                    f2.close()
                    
                    
                    for b1 in data1['books']:
                        if b1['book_name'] == b_name and b1['author_name'] == a_name: # check book available in books.json
                            
                            b1['copies'] += 1
                            f2 = open("books.json" , "w")
                            json.dump(data1 , f2 , indent=2)
                            f2.close()
                            flag2 = 0
                            print("successfully return book")
                            break
                        i+=1
                else:
                    data1 = {}
                    data1["books"] = []
                    f2 = open("books.json" , "w")
                   
                    data1["books"].append({
                        'id' : i + 1,
                        'book_name' : b_name,
                        'author_name' : a_name,
                        'copies' : 1
                    })
                    flag2 = 0
                    json.dump(data1 , f2 , indent=2)
                    print("successfully return book")
                    f2.close()
                if flag2 == 1:
                    data1 = json.load(f2)
                    f2.close()
                    f2 = open("books.json" , "w")
                   
                    data1["books"].append({
                        'id' : i + 1,
                        'book_name' : b_name,
                        'author_name' : a_name,
                        'copies' : 1
                    })
                    json.dump(data1 , f2 , indent=2)
                    print("successfully return book")
                f2.close()
                flag1 = 0
        if flag1 == 1:
            print("you did'nt issue this book")


        f1.close()



if __name__ == "__main__":

    while True:

        print("press 1. admin login ")
        print("press 2. librarian login ")
        print("press 3. exit")
        ch = input()
        if ch == '1':

            usr = input("enter the user name")
            pswd = input("enter the password")
            if check_pswd(usr , pswd):
                print("press 1: add another admin ")
                print("press 2: use admin module ")
                inp = input()

                if inp == '1':
                    add_admin()
                elif inp == '2':

                    while True:
                        print("1. add books in library")
                        print("2. delete books in library")
                        print("3. student register in library")
                        print("4. deregister student in library")

                        print("5. log out ")

                        print("6. show avilable books")

                        print("7. show avilable student")
                        print("8. modify book details ")
                        print("9. modify student details ")
                        print("\n enter your choice : - ") 
                        ch = input();

                        if ch == '1':
                            Admin.add_books()
                        elif ch == '2':
                            Admin.del_books()
                        elif ch == '3':
                            Admin.add_students()
                        elif ch == '4':
                            Admin.del_student()
                        elif ch == '5':
                            break
                        elif ch == '6':
                            Admin.avail_book()
                        elif ch == '7':
                            Admin.avail_student()
                        elif ch == '8':
                            Admin.modify_books()
                        elif ch == '9':
                            Admin.modify_student()
                        else:
                            print("please enter valid choice : - ")
                else:
                    print("invalid choice ")
            else:
                print("invalid user name or password")
        elif ch =='2':
            while True:

                print("press 1. show available books in library ")
                print("press 2. issue book to student ")
                print("press 3. return book ")
                print("press 4. log out")
                ch = input()
                if ch == '1':
                    
                    Librarian.avail_book()
                elif ch == '2':
                    Librarian.issue_book()
                
                elif ch == '3':
                    Librarian.return_book()
                    
                elif ch == '4':
                    break
                else:
                    print("invalid input proggramme closed ")
                    break
        elif ch == '3':
            break
        else:
            print("invalid input proggramme closed ")
            break
