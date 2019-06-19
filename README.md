Project – Building a Library Management System using PYTHON
You need to build a library Management System which have 2 modules:

    - Admin Module
    - Librarian Module
As part of Admin module, you should be able to do the following functions:

    - Add/ Delete/ Modify Books
    - Add/ Delete/ Modify Students
    - List books available in library (Total number of books and Availability)
    - List of Students registered in Library
As part of Librarian module, you should be able to do the followings:

    - List books available in library (Total number of books and Availability)
    - Issues book to student
    - Return book
Please note the followings:

    - Each book should have Unique Book id, Book Name, Author Name, No of copies (there 
    could be multiple copies of a Book)
    - Each student should have SIC no, Name, Valid Phone no and Valid email-id (validity of 
phone no and email-id to be checked)
    - Need to have a module to load books and students data from json file
    - Students cannot be assigned more than 2 books at a time
    - Student cannot take same book multiple times at the same time
    - Should check the availability of the book before assignment

imporatant

      - Admin module should have user-id and password check
      - Check for valid password based on the following criteria:
            o At least 1 letter between [a-z]
      o At least 1 number between [0-9]
      o At least 1 letter between [A-Z]
      o At least 1 special character from [!@#$%&]
      o Minimum length of password: 6
      o Maximum length of password: 12
      - Librarian should be able to see list of books assigned to a student
      - Librarian should be able to see list of students who took a specific book
