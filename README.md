# Pands-problem-sheet: 2023

This repository contains the scripts I used to complete the eight problem sheet tasks which were part of the assessment for the Programming and Scripting module of the Higher Diploma in Data Analytics from ATU. 
I had some basic familiarity with Python before I commenced this module, having completed roughly half of a 22-hour 'Python Bootcamp' course on Udemy in summer 2022.

I used Visual Studio Code (version 1.77.3) to write my scripts and to upload them to a repository on github for assessment. 

I have included references for tasks as part of the comments within the python scripts. For the first three weeks, my source of information was simply the lecture material, coupled with W3 schools as suggested by the lecturer. From week 4 onwards, my range of references expanded to other material found online. I have also included references within this README file where I thought they might be useful to understand how I came to my solutions.

At the end of this script I have included reference for material I used to write this README file itself.

&nbsp; 

## Table of contents
* [Problem sheets](#problem-sheets)
    * [Week 1 - hello world](#hello-world)
    * [Week 2 - bank](#bank)
    * [Week 3 - accounts](#accounts)
    * [Week 4 - collatz](#collatz)
    * [Week 5 - weekday](#weekday)
    * [Week 6 - square root](#square-root)
    * [Week 7 - number of es](#number-of-es)
    * [Week 8 - plot task](#plot-task)
* [References](#references)

&nbsp; 


## Problem sheets

### Hello world 
    
    Commit and push a file to the problem sheet (repository) called helloworld.py.
    This file should contain a python program that displays Hello World! when it is run.

The first week's task involved installing the software required for the module, getting set up on github and creating two repositories on there; one for uploading practice work from weekly labs, and another for the 'pands problem sheets' which form part of the assessment for the module.

I found I needed to follow the lecturers instructions carefully to get my machine set up on github and to correctly push code from my machine on to github, but once I got set up I found it very user-friendly.

I also familiarised myself with VSCode.


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the script is :

```
python .\01_helloworld.py
```
User input:
```
(N/A)     
```
User output is :
```
Hello World!
```
</p>
</details>

&nbsp; 

### Bank
    
    Prompt the user and read in two money amounts (in cent). Add the two amounts.
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

The second week's task built upon the lectures which covered the writing of statements, and introduced arithmetic operators (+, -, * etc) and variable types (string, integer, floats and booleans). \
It was also a chance to get more practice using VSCode and pushing to github. Initially I had difficulty completing the task, so I decided that I would come back to it after a few weeks of lectures, hoping that it would seem easier then. 

I later answered the question by using the float variable and dividing the amount in cents by 100, which is a relatively simple solution. Following the lecturers feedback, however, I was made aware that a goal of the task was to implement a solution without needing to use floats or indirect floats (eg. dividng by 100), so I used a roundabout solution of converting the total in cents to a string, and placing a decimal point in between the last two digits and the remaining digits to the left of the decimal point. I found it reassuring that, while this solution didn't occur to me initially, I did think of it straight away when I saw the lecturers feedback, and was able to implement it relatively easily. This gave me confidence that I have been absorbing the information in this module over the past two months, and that I can hope to keep improving into the future.


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the script is :
```
python .\02_bank.py
```
User input:
```
Enter amount 1 in cents: 88
Enter amount 2 in cents: 67        
```
User output is :
```
€1.55
```
</p>
</details>

&nbsp; 

### Accounts
    
    Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with 
    only the last 4 digits showing (and the first 6 digits replaced with Xs).
    Extra part: Modify the program to deal with account numbers of any length, commenting on your assumptions.

The third week's task built upon the topics covered in week 3: variables, built-in functions, manipulating strings, and using f-strings to print out Python expressions in a string format.\
It consisted of two parts: the first part had explicit instructions, whereas the second part required us to set out our assumptions behind our script. 

I placed a lower limit of seven digits for the account number, because a five or six digit account number doesn't gain from having only one or two of its digits hidden. I did not make assumptions on the upper bound of how many digits an account number can be, in order to stick to the instructions for the exercise, even if in practice it is unusual for an account number to contain, for example, 100 digits.


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the first script is :

```
python .\03_accounts.py
```
User input:
```
Please enter a ten digit number: 3456345678
```
User output is : 
```
XXXXXX5678
```
User call of the second script is :
```
python .\03_accounts.extra.py
```
User input:
```
Please enter a number containing seven or more digits: 67891234567      
```
User output is : 
```
XXXXXXX4567
```
</p>
</details>

&nbsp; 

### Collatz
    
    Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of 
    the following calculation.
    At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd,
    multiply it by three and add one. Have the program end if the current value is one.

Week 4 covered the area of controlling the flow of a Python script; if, elif and else statements, and while and for loops. 

The weekly task involved using:
* a while loop to account for the situation where an inputted number is negative, where the user is asked again to input a positive integer
* once a number is positive, another while loop is used to ensure that the numerical operations described by the Collatz conjecture will be carried out until a value of 2 is reached, at which point the sequence will end
* within this second while loop, an if statement is used in conjunction with the modulus operator to ensure that even numbers are divided by 2
* and an else statement is used to ensure that odd numbers are multipled by 3 and the result added to 1.

The Collatz conjecture is that for any positive integer chosen and subjected to the operations above, the sequence will always reach 1.

I found this task helpful for improving my abilities to implement if statements and while loops correctly, and I enjoyed finding out how to test a mathemetical conjecture in this way using Python.


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the script is :
```
python .\04_collatz.py
```
User input:
```
Enter an integer greater than 1: 75
```
User output is :
```
75 226 113 340 170 85 256 128 64 32 16 8 4 2 1 :
And so another positive integer succumbs to the gravitational pull of the Collatz conjecture
```
</p>
</details>

&nbsp; 

### Weekday
    
    Write a program that outputs whether or not today is a weekday

Week 5 covered the topics of lists, tuples and dictionaries, and the lectures walked through some examples of how to use these data structures in Python. \
The completion of this task required us to import the datetime module (https://www.w3schools.com/python/python_datetime.asp). This allows us to create an object which displays the current date, which we can further manipulate for the purpose of completing this task.

Next, the method .weekday() allows us to attribute an integer 0 to 4 inclusive to the five weekdays, and 5 and 6 to the two weekend days. We can use the output of this method within an f-string to output a statement about whether it is a weekday or weekend.
(https://pynative.com/python-get-the-day-of-week/#:~:text=Use%20the%20weekday()%20method,its%20weekday%20number%20is%200.)

We didn't cover functions and modules in much depth until Week 6, so this task required some research to complete at the time the task was assigned.


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the script is :
```
python .\05_weekday.py
```
User input:
```
(N/A)       
```
User output on a weekday (example) :
```
Today it is Monday, which unfortunately is a weekday!
```
User output on a weekend (example) :
```
Today it is Saturday, which thankfully is the weekend!
```
</p>
</details>

&nbsp; 

### Square root
    
    Write program that takes a positive floating-point number as input and outputs an approximation of its square root:
    it should be our own function, rather than using any built-in functions for square roots.

The lectures for Week 6 covered functions (defining and calling), passing arguments into functions and returning variables.\
The task required us to research how to create a function which takes in an input of a positive floating point number, and outputs an approximation of its square root.
I took the lecuturers suggestion on board of researching the Newton Raphson method to use for the task, and I firstly read the Wikipedia page to familirise myself with the algebra. I saw that arranging the formula could produce what is called the Babylonian method of finding square roots, which takes a simpler formula than the unarranged form, and from searching on YouTube I found a very helpful video which outlined how to implement this formula in python (https://www.youtube.com/watch?v=xdlIFw5EM4w).

On outline for how the Newton Raphson method can produce an accurate estimate for the square root of a number is as follows: 
* Let 'a' be the number whose square root we are seeking, and let a = x^2 ie. x is the square root.
  This is equivalent to finding the value for x at which the function f(x) = x^2 - a = 0. 
  Therefore f'(x) = 2x
* By Newtons method, the first approximation for the square root, x(1), is equal to x(0) - (f(x(0))/ f'(x(0))), 
  where x(0) is an initial guess for the square root.
* Simplifying the notation, "better guess" = x - ((x^2 - a)/(2* x))
  Provided the inital guess is a good one, a few iterations of this formula should generate an accurate 
  estimate of the square root 'x'. 
* The right hand side of the formula can be rearranged to make it easier write a script:
  "better guess" = 0.5(2* x - (x - (a/x)) 
  = 0.5(x + (a/x)) 


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the script is :
```
python .\06_square.root.py
```
User input:
```
Choose a positive floating-point number: 499
```
User output is :
```
22.338307903688676
```
</p>
</details>

&nbsp; 

### Number of es
    
    Write a program that reads in a text file and outputs the number of e's it contains, documenting any assumptions you are making.
    The program should take the filename from an argument on the command line.
  
This week's lecturers covered reading files and writing to files, and covered the file types of JSON and CSV files.

The weekly taks required us to research how to read in a file from the command line which is to be used in a script. The solution consisted of:
* firstly importing the sys module
* then assigning the filename of the text document being tested in the script to be the first argument following the name of the script (this is done using filename = sys.argv[1]). For the text file I used the first chapter of Charles Dickens' 'Hard Times'. 
* opening the file in text mode and reading its contents. I used the sites https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python and https://www.knowledgehut.com/blog/programming/sys-argv-python-examples to understand how to do this step.
* and finally using a function called count() to count the number of times the letter 'e' appears as a small letter and all the times it appears as a capitalised letter. I used the site https://www.programiz.com/python-programming/methods/string/count to find out about the count function.

<details>
           <summary>User point of view</summary>
           <p>
         
User call of the script is :
```
python .\07_numberofes.py hardtimeschapter1.txt
```
User input:
```
(N/A) - the script runs correctly when the user includes the name of the text file to be read as the first argument 
following the name of the script, when calling the script.
```
User output is :
```
The letter 'e' appears in the file '.\hardtimes_chapter1.txt' 181 times.
```
</p>
</details>

&nbsp; 

### Plot task
    
    Create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    and a plot of the function h(x)=x^3 in the range [0, 10].

Week 8 covered NumPy (used for mathematical operations) and Matplotlib (used for data visualisation). The final weekly taskrequired us to use these two libraries  and to create a plot and a histogram.

To make the histogram and plot look more appealing, I researched online and found out how to impose a more attractive design template on to my plots using the style module in conjunction with the name of a pre-made style package. 

I saved the the histogram and plot in .png format in the pands-problem-sheet folder to upload to Github; from there I could obtain a http link to the histogram and plot to allow me to include it in this README file.


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the histogram script is :    
```
python .\08_plottask_hist.py          
```
User input:          
```
(N/A)         
```
              
User output is :
              
![image](https://user-images.githubusercontent.com/108928457/231457162-623a5b16-187f-4d96-8c72-a48f200d484b.png)

```      
```
User call of the plot script is :
```
python .\08_plottask_plot.py
```
User input:
```
(N/A)
```
User output is :

![image](https://user-images.githubusercontent.com/108928457/231454780-25e9478b-0715-4a95-bb11-fed77d277e7d.png)

      
</p>
</details>
              
&nbsp; 

## References:

   * https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax (For getting familiar with writing in Markdown).
   * https://stackoverflow.com/questions/6046263/how-to-indent-a-few-lines-in-markdown-markup  (For help with creating more space between sections).
   * https://stackoverflow.com/questions/2822089/how-to-link-to-part-of-the-same-document-in-markdown (For help in creating links within the document).
   * https://raw.githubusercontent.com/sandraelekes/GMIT-ps/master/README.md  (For help in formatting certain parts of README file, especially the 'user call of the script' dropdown to demonstrate the code).

              
