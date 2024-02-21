# Data-Driven Web Applications

I created  a Data-Driven Web Applications using Flask to perform CRUD operations: Create, Read, Update and Delete.

Used a list of dictionaries to emulate a database.

1. showBook.html
   - When "assignment2.py" is executed, the "showBook.html" must be the first webpage to be rendered by the browser.
   - This page must list all available books. For each book, it must provide the user with the options to either edit the book       title or delete the book's data from the dictionary. 

2. editBook.html

  - The user reaches this page after choosing to edit the title of one of the books in the page "showBook.html".\
  - If the user enters a string in the displayed textbox, this string must replace the book's title in the corresponding             dictionary.

3. deleteBook.html

  - The user reaches this page after choosing the option delete in the page "showBook.html".
  - If the user hits the delete button,  the corresponding dictionary of that book, i.e., the title and the id, will be deleted     from the list of the available books.


4. newBook.html
   - The user reaches to this page when typing in the following URL into the browser.
   - http://127.0.0.1:5000/book/new/ Links to an external site.
   - If the user enters a string in the displayed textbox, a new dictionary will be added to the list of available books. The     Dictionary will have the entered string and assigns it the next available id (i.e., the first found empty slot)
