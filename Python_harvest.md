# Python

## **Iterating over a list in a function**
Now that we've learned about range, we have two ways of iterating through a list.

**Method 1** - for item in list:
```
for item in list:
  print item
```
**Method 2** - iterate through indexes:
```
for i in range(len(list)):
  print list[i]
```
**Method 1** is useful to loop through the list, but it's not possible to modify the list this way.
**Method 2** uses indexes to loop through the list, making it possible to also modify the list if needed. Because if you want to modify the list, you need indexes.

## **While / else**
Something completely different about Python is the while/else construction. while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition is evaluated to False. This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.
```
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"
```
In this example, the loop will break if a 5 is generated, and the else will not execute. Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.

## **practice:**
**1.** Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)
method 1:hard version
```
def digit_sum (n):
  n_times = len(str(n))
  result = 0
  while n_times > 0:
    result += n % 10
    n = n // 10
    n_times -= 1
  return result
```
method 2:  easy version
```
def digit_sum (n):
  n_times = str(n)
  result = 0
  for i in n_times:
    result += int(i)
  return result
```
**2. Factorial**
Let's try a factorial problem.
To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:
factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.
```
def factorial (x):
  result = 1
  while x > 0 :
    result *= x
    x -= 1
  return result

```
**3. is_prime**
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. 
质数是一个除了1和它本身以外没有任何正的除数的数。
In other words, if you want to test if a number in a variable x is prime, then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not.
If there is a number between 1 and x that goes in evenly, then x is not prime.
```
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
```
**4.** Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".
You may not use reversed or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @, or “#").
```
def reverse (text):
  result = []
  for i in text[len(text)::-1]:
    result += i
  return "".join(result)
```
**5.** Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.
```
def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
```
**6. scrabble_score**
Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter (we'll leave out the double and triple letter and word scores for now).
To the right is a dictionary containing all of the letters in the alphabet with their corresponding Scrabble point values.
```
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
```
For example: the word "Helix" would score 15 points due to the sum of the letters: 4 + 1 + 1 + 1 + 8.
Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
Assume your input is only one word containing no spaces or punctuation.
As mentioned, no need to worry about score multipliers!
Your function should work even if the letters you get are uppercase, lowercase, or a mix.
Assume that you're only given non-empty strings.
```
def scrabble_score (word):
  result = 0
  for item in word:
    if item in " ,.@#$%^&*~!" or word == "":
      print "invalid input!"
    else:
      result += score[item.lower()]
  return result
```
**7.** Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. For example:
```
censor("this hack is wack hack", "hack") 
```
should return:
```
"this **** is wack ****"
```
Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
```
def censor (text,word):
  result = text.split(word)
  stars = len(word) * "*"
  return stars.join(result)
```
Hint:
You can use
```
string.split()
# and 
" ".join(list)
```
to help you here.
Remember: "*" * 4 equals "****"
After splitting the string with string.split(), you can loop through the indices in the list and replace the words you are looking for with their asterisk equivalent. Join the list at the end to get your sentence!
string.split(),this method can construct a list ,item splited with a “”(none string).
just like this example:
```
string_new = "ni hao woshi"
print string_new.split("ni")
```
the result display in console is:
```
['', ' hao woshi']
```
**8.** Define a function called count that has two arguments called sequence and item.
Return the number of times the item occurs in the list.
For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).
There is a list method in Python that you can use for this, but you should do it the long way for practice.
Your function should return an integer.
The item you input may be an integer, string, float, or even another list!
Be careful not to use list as a variable name in your code—it's a reserved word in Python!
```
def count (sequence,item):
  sum = 0
  for thing in sequence:
    if thing == item:
      sum += 1
  return sum
```
**9.** Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example, purify([1,2,3]) should return [2].
Do not directly modify the list you are given as input; instead, return a new list with only the even numbers. (even numbers : 偶数)
```
def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res
```
**10.** Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list. For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
Don't worry about the list being empty.
Your function should return an integer. 
```
def product (numbers):
  result = 1
  for number in numbers:
    result *= number
  return result
```
**11.  Write a function ~remove_duplicates~ that takes in a list and removes elements of the list that are the same.**
For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].
Don't remove every occurrence, since you need to keep a single occurrence of a number.
The order in which you present your output does not matter. So returning [1, 2, 3] is the same as returning [3, 1, 2].
Do not modify the list you take as input! Instead, return a new list.
```
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
# Sort the input list from low to high    
    inputlist = sorted(inputlist)
# Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
```
**12. median**
Great work! You've covered a lot in these exercises. Last but not least, let's write a function to find the median of a list.
The median is the middle number in a sorted sequence of numbers.
Finding the median of [7, 12, 3, 1, 6] would first consist of sorting the sequence into [1, 3, 6, 7, 12] and then locating the middle value, which would be 6.
If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.
For example, the median of the sequence [7, 3, 1, 4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.
You can sort the sequence using the sorted() function, like so:
```
sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
```
Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.
The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
If the list contains an even number of elements, your function should return the average of the middle two.
```
def median (lst):
  if len(lst) == 0:
    print "Don't have a median!"
  elif len(lst) == 1:
    return lst[0]
  else:
    tem = sorted(lst)
    if len(tem) % 2 == 0:
      return (tem[len(tem)/2-1] + tem[len(tem)/2]) / 2.0
    else:
      return tem[len(tem) / 2]
```
---
**13.** Define a function on line 3 called print_grades with one argument, a list called grades_input.
Inside the function, iterate through grades_input and print each item on its own line.
After your function, call print_grades with the grades list as the parameter.
```
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  string_list = []
  for num in grades_input:
    string_list.append(str(num))
  print ",".join(string_list)
print_grades(grades)
```
**14.** Now that we have a function to print the grades, let's create another function to **compute the sum** of all of the test grades.
This will be super-helpful when we need to compute the average score.
I know what you're thinking, "let's just use the built-in sum function!" The built-in function would work beautifully, but it would be too easy.
Computing the sum manually involves computing a rolling sum. As you loop through the list, add the current grade to a variable that keeps track of the total, let's call that variable total.
Q:
define a function, grades_sum, that does the following:
Takes in a list of scores, scores
Computes the sum of the scores
Returns the computed sum.
Call the newly created grades_sum function with the list of grades and print the result.
```
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum (scores):
  total = 0
  for score in scores:
    total += score
  return total
print grades_sum(grades)
```
15. **Computing the Average:**
The average test grade can be found by dividing the sum of the grades by the total number of grades.
Luckily, we just created an awesome function, grades_sum to compute the sum.
Q:
Define a function, grades_average, below the grades_sum function that does the following:
* Has one argument, grades_input, a list
* Calls grades_sum with grades_input
* Computes the average of the grades by dividing that sum by float(len(grades_input)).
* Returns the average.
```
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum (scores):
  total = 0
  for score in scores:
    total += score
  return total
print grades_sum(grades)

def grades_average(grades_input):
  average = grades_sum(grades_input) / float(len(grades_input))
  return average
print grades_average(grades)
```
### We're going to use the average for computing the variance. The variance allows us to see how widespread the grades were from the average.
16. **The Variance**
Let's see how the grades varied against the average. This is called computing the variance.
A very large variance means that the students' grades were all over the place, while a small variance (relatively close to the average) means that the majority of students did fairly well.
Q:
 define a new function called grades_variance that accepts one argument, scores, a list.
First, create a variable average and store the result of calling grades_average(scores).
Next, create another variable variance and set it to zero. We will use this as a rolling sum.
for each score in scores: Compute its squared difference: (average - score) ** 2 and add that to variance.
Divide the total variance by the number of scores.
Then, return that result.
Finally, after your function code, print grades_variance(grades).
```
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)
print grades_variance(grades)
```
17. **Standard Deviation**
Great job computing the variance! The last statistic will be much simpler: standard deviation.
The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.
Q:
Define a function, grades_std_deviation, that takes one argument called variance.
return the result of variance ** 0.5
After the function, create a new variable called variance and store the result of calling grades_variance(grades).
Finally print the result of calling grades_std_deviation(variance).
```
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  return variance / len(scores)
print grades_variance(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)
```

**Review**
You've done a great job completing this program.
We've created quite a few meaningful functions. Namely, we've created helper functions to print a list of grades, compute the sum, average, variance, and standard deviation about a set of grades.
Let's wrap up by printing out all of the statistics.
Who needs to pay for grade calculation software when you can write your own? :)

---

18. **Iterators for Dictionaries**
Let's start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.
Note that the .items() method doesn't return key/value pairs **in any specific order**.like this:
```
d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
```
Q:
Create your own Python dictionary, my_dict, in the editor to the right with two or three key/value pairs.
Then, print the result of calling the my_dict.items().
```
my_dict = {
  "Name":27,
  "Gender":True,
  "genre":"666",
}
print my_dict.items()
```
display in console:
[(‘genre', '666'), ('Gender', True), ('Name', 27)]

19. **keys() and values()**
While **.items()** returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:
The **.keys()** method returns a list of the dictionary's keys, and
The **.values()** method returns a list of the dictionary's values.
Again, these methods will not return the keys or values from the dictionary in any specific order.
You can think of a tuple as an immutable (that is, unchangeable) list. Tuples are surrounded by ()s and can contain any data type.
Q:
Remove your call to .items() and replace it with a call to .keys() and a call to .values(), each on its own line. Make sure to print both!
```
my_dict = {
  "Name":27,
  "Gender":True,
  "genre":"666",
}
print my_dict.keys()
print my_dict.values()
```
display in console:
['genre', 'Gender', 'Name']
['666', True, 27]
has no any specific order

20. **The 'in' Operator**
For iterating over lists, tuples, dictionaries, and strings, Python also includes a special keyword: in. You can use in very intuitively, like so:
```
for number in range(5):
  print number,

d = { 
  "name": "Eric",
  "age": 26
}
for key in d:
  print key, d[key],

for letter in "Eric":
  print letter,  # note the comma!
```
* In the example above, first we create and iterate through a range, printing out 0 1 2 3 4. Note that the trailing **comma** ensures that we keep printing on the **same line**.
* Next, we create a dictionary and iterate through, printing out age 26 name Eric. Dictionaries **have no specific order**.
* Finally, we iterate through the letters of a string, printing out E r i c.
Q:
For each key in my_dict: print out the key , then a space, then the value stored by that key. (You should use print a, b rather than print a + " " + b.)
```
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print my_dict.keys()
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]
```

21. **Building Lists**
Let's say you wanted to build a list of the numbers from 0 to 50 (inclusive). We could do this pretty easily:
`my_list = range(51)`
But what if we wanted to generate a list according to some logic—for example, 
a list of all the even numbers from 0 to 50?
Python's answer to this is the list comprehension. 
List comprehensions are a powerful way to generate lists using the for/in and if keywords we've learned.
```
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
```
display on console:
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

22. List Comprehension Syntax
Here's a simple example of list comprehension syntax:
```
new_list = [x for x in range(1, 6)]
# => [1, 2, 3, 4, 5]
```
This will create a new_list populated by the numbers one to five. If you want those numbers doubled, you could use:
```
doubles = [x * 2 for x in range(1, 6)]
# => [2, 4, 6, 8, 10]
```
And if you only wanted the doubled numbers that are evenly divisible by three:
```
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# => [6]
```
Q:
Use a list comprehension to build a list called even_squares in the editor.
Your even_squares list should include the squares of the even numbers between 1 to 11. 
Your list should start [4, 16, 36...] and go from there.
```
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1,12) if x % 2 == 0]

print even_squares
```

23. **Now You Try List Comprehension**
Great work! Now it's time for you to create a list comprehension all on your own.
```
c = ['C' for x in range(5) if x < 3]
print c
```
The example above creates and prints out a list containing ['C', 'C', 'C'].
Q:
Use a list comprehension to create a list, cubes_by_four.
The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
Finally, print that list to the console.
Note that in this case, the cubed number should be evenly divisible by 4, not the original number.
```
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four
```

24. **List Slicing Syntax**
Sometimes we only want part of a Python list. 
Maybe we only want the first few elements;
maybe we only want the last few.
Maybe we want every other element!
List slicing allows us to access elements of a list in a concise manner.
The syntax looks like this:
`[start:end:stride]`
Where start describes where the slice starts (inclusive), 
end is where it ends (exclusive), and stride describes the space between items in the sliced list. 
For example, a stride of 2 would select every other item from the original list to place in the sliced list.
Q：
We've generated a list with a list comprehension in the editor to the right,
and we're about to print a selection from the list using list slicing. 
Can you guess what will be printed out? Click Run when you think you know!

```
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]
```
display on console:
[9, 25, 49, 81]

25. **Omitting Indices**
If you don't pass a particular index to the list slice,
Python will pick a default.
```
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']
```
* The default starting index is 0.
* The default ending index is the end of the list.
* The default stride is 1.
Q:
Use list slicing to print out every odd element of my_list from start to finish.
Omit the start and end index. You only need to specify a stride.
```
my_list = range(1, 11) # List of numbers 1 - 10
# Add your code below!
print my_list[::2]
```

26. **Reversing a List**
We have seen that a positive stride progresses through the list from left to right.
A negative stride progresses through the list from right to left.
```
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
```
In the example above, we print out ['E', 'D', 'C', 'B', 'A'].
Q:
Create a variable called backwards and set it equal to the reversed version of my_list.
Make sure to reverse the list in the editor by passing your list slice a negative stride, like in the example above.
```
my_list = range(1, 11)
# Add your code below!
backwards = my_list[::-1]
```

27. **Stride Length**
A positive stride length traverses the list from left to right, 
and a negative one traverses the list from right to left.
Further, a stride length of 1 traverses the list "by ones," 
a stride length of 2 traverses the list "by twos," and so on.
Q:
Create a variable, backwards_by_tens, 
and set it equal to the result of going backwards through to_one_hundred by tens.
Go ahead and print backwards_by_tens to the console.
(反方向每十个数遍历to_one_hundred，并打印到控制台。)
```
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens
```

28. **Let's do one more, just to prove you really know your stuff.**  
Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). 
Use list slicing for this one instead of a list comprehension.
Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.
```
to_21 = range(1,22)
odds = to_21[::2]
#odds = range(1,22)[::2]
#说明第一个方法没有改变to_21的变量，是复制的操作
#it means the first odds's method has not change the to_21, slice is a duplicate manipulate
middle_third = to_21[len(to_21)/3:len(to_21) * 2 / 3:]
```
reason, I try on editor this:
```
to_21 = range(1,22)
odds = to_21[::2]
print to_21
print odds
```
and this :
```
to_21 = range(1,22)
odds = range(1,22)[::2]
print to_21
print odds
```
above all display on console always:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
**so I said:**
**说明第一个方法没有改变to_21的变量，是复制的操作**
**（it means the first odds's method has not change the to_21, slice is a duplicate manipulate）**

29. **Anonymous Functions**
      One of the more powerful aspects of Python is that it allows for
      a style of programming called functional programming,
      which means that you're allowed to pass functions around just 
      as if they were variables or values. Sometimes we take this for granted, 
      but not all languages allow this!
      Check out the code at the right. See the lambda bit? Typing
      `lambda x: x % 3 == 0`
      Is the same as
```
def by_three(x):
  return x % 3 == 0
```
Only we don't need to actually give the function a name; 
it does its work and returns a value without one. 
That's why the function the lambda creates is an anonymous function.
When we pass the lambda to filter, filter uses the lambda to determine what to filter,
and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
```
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
```
display on console:
[0, 3, 6, 9, 12, 15]
























#code习得
