# Pands-problem-sheet: 2023

This repository contains the scripts I used to complete the eight problem sheet tasks which were part of the assessment for the Programming and Scripting module of the Higher Diploma in Data Analytics from ATU. \
I had some basic familiarity with Python before I commenced this module, having completed roughly half of a 22-hour Python Bootcamp course on Udemy last summer.

I used VSCode to write my scripts and to upload them to a repository on github for assessment.

References: \
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
https://stackoverflow.com/questions/6046263/how-to-indent-a-few-lines-in-markdown-markup


## Table of contents
* [Problem sheets](#problem-sheets)
    * [Week 1 - hello world](#week-1-hello-world)
    * [Week 2 - bank](#week-2-bank)
    * [Week 3 - accounts](#week-3-accounts)
    * [Week 4 - collatz](#week-4-collatz)
    * [Week 5 - weekday](#week-5-weekday)
    * [Week 6 - square root](#week-6-square-root)
    * [Week 7 - number of es](#week-7-number-of-es)
    * [Week 8 - plot task](#week-8-plot-task)


## Problem sheets

###  Week 1 - hello world 
    
    Commit and push a file to the problem sheet (repository) called helloworld.py.
    This file should contain a python program that displays Hello World! when it is run.

The first week's homework involved installing the software required for the module, getting set up on github and creating two repositories on there; one for uploading practice work from weekly labs, and another for the 'pands problem sheets' which form part of the assessment for the module.

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



###  Week 2 - bank
    
    Prompt the user and read in two money amounts (in cent). Add the two amounts.
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

The second week's homework built upon the lectures which covered the writing of statements, and introduced arithmetic operators (+, -, * etc) and variable types (string, integer, floats and booleans). \
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



###  Week 3 - accounts
    
    Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with 
    only the last 4 digits showing (and the first 6 digits replaced with Xs).
    Extra part: Modify the program to deal with account numbers of any length, commenting on your assumptions.

The third week's homework contained two parts


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


###  Week 4 - collatz
    
    Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of 
    the following calculation.
    At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd,
    multiply it by three and add one. Have the program end if the current value is one.
    

According to Wikipedia, this conjecture asks whether repeating the two simple arithmetic operations 
below will eventually transform every positive integer into 1. The two operations are: \
&nbsp;&nbsp;&nbsp;&nbsp;If the previous term is even, the next term is one half of the previous term. \
&nbsp;&nbsp;&nbsp;&nbsp;If the previous term is odd, the next term is 3 times the previous term plus 1.

The conjecture is that for any positive integer chosen, these sequences always reach 1.


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


###  Week 5 - weekday
    
    Write a program that outputs whether or not today is a weekday

The task for this week


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


###  Week 6 - square root
    
    Write program that takes a positive floating-point number as input and outputs an approximation of its square root:
    it should be our own function, rather than using any built-in functions for square roots.

This week's task 

The Newton Raphson method can produce an accurate estimate for the square root of a number as follows:
Let 'a' be the number whose square root we are seeking, and let a = x^2 ie. x is the square root.
This is equivalent to finding the value for x at which the function f(x) = x*x - a = 0. 
Therefore f'(x) = 2x

By Newtons method, the first approximation for the square root, x(1), is equal to x(0) - (f(x(0))/ f'(x(0))), 
where x(0) is an initial guess for the square root.

Simplifying the notation, "better guess" = x - ((x*x - a)/(2*x))
Provided the inital guess is a good one, a few iterations of this formula should generate an accurate 
estimate of the square root 'x'. 

The right hand side of the formula can be rearranged to make it easier write a script:
"better guess" = 0.5(2*x - (x - (a/x)) 
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



###  Week 7 - number of e's
    
    Prompt the user and read in two money amounts (in cent). Add the two amounts.
    Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

This week's homework 


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



###  Week 8 - plot task
    
    Create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    and a plot of the function h(x)=x3 in the range [0, 10].

The final homework task required us to use the libraries NumPy and Matplotlib to create a plot and a histogram.

To make the plot look nicer, I researched online and found out how to impose a more attractive design template on to my plots using the style module in conjunction with the name of a pre-made style package.


<details>
           <summary>User point of view</summary>
           <p>
         
User call of the script is :
```
python .\08_plottask_hist.py
```
User input:
```
(N/A)
```
User output is :
```
(A histogram is generated representing a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2.
I have saved a sample of the output of this script in my pands-problem-sheet repository under the name 08_plottask_hist.png)
            
```
User call of the script is :
```
python .\08_plottask_plot.py
```
User input:
```
(N/A)
```
User output is :
```
(A plot is generated of the function h(x)=x3 in the range [0, 10].
I have saved a sample of the output of this script in my pands-problem-sheet repository under the name 08_plottask_plot.png)
```
</p>
</details>


