## The Slice() function returns a slice object.

A slice object is used to specify how to slice a sequence. You can specify where to start the slicing (inclusive), and where to end (exclusive). You can also specify the step, which allows you to e.g. slice only every other item.

I have define a generator function (my_islice_generator()) and an iterator class (my_islice_iterator()), such that it emulates islice().

Like the real islice(), it must take an iterable, a start index (inclusive) and a stop index (exclusive). 
It returns selected items from the input iterator, by index.

Files in the folder are:
    isslice_lib.py --> Implematiosn of Slice iterator class and generator function
    my_is_slice.py --> Implematiosn of Slice iterator class and generator function (Used for automation testing and debugging)
    test_my_isslice --> Unit Tests


I use pytest-watch (https://pypi.org/project/pytest-watch/) to run my tests continuously whenever I save my file. You can install it with pip install pytest-watch. To use it, in the directory I have my files, I run ptw . This will run all the functions I've defined that start with "test_", show me what went wrong, and then continue to run in the background. Whenever I change the definition of my_zip above, it automatically runs my tests again. No manually pushing that triangle button in VSCode over and over: you'll immediately know which of your tests are succeeding every time you save your file. 


This methodology is called "Test Driven Development" --> [Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development)
