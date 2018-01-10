# Python

[124](#1)

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
<h2 id = "1"> asdfdadfda</h2>
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

22. **List Comprehension Syntax**
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
print my_list
```
display on console:
[0, 3, 6, 9, 12, 15]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
That is mean filter has not change my_list , it create a new list

30. **Lambda Syntax**
Lambda functions are defined using the following syntax:
```
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
```
Lambdas are useful when you need a quick function to do some work for you.
If you plan on creating a function you'll use over and over, you're better off using def and giving that function a name.
Q:
Fill in the first part of the filter function with a lambda. The lambda should ensure that only "Python" is returned by the filter.
Fill in the second part of the filter function with languages, the list to filter.
```
languages = ["HTML", "JavaScript", "Python", "Ruby"]
# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)
```

31. **Time to test out filter() and lambda expressions.**
```
cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)
```
The example above is just a reminder of the syntax.
Q:
Create a list, squares, that consists of the squares of the numbers 1 to 10. A **list comprehension** could be useful here!
Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
```
squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <=70,squares)
```

32. **Iterating Over Dictionaries**
First, let's review iterating over a dict.
Call the appropriate method on movies such that it will print out all the items (hint, hint) in the dictionary—that is, each key and each value.
```
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print movies.items()
```
display on console is:
```
[("Monty Python's Life of Brian", 'Good'), ("Monty Python's Meaning of Life", 'Okay'), ('Monty Python and the Holy Grail', 'Great')]
```

33. **Comprehending Comprehensions**(理解列表解析器)
Now let's take another look at list comprehensions.
`squares = [x ** 2 for x in range(5)]`
Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 3 or 5.(找1-15中能被3或5整除的数)
```
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives
```
display on console:
`[3, 5, 6, 9, 10, 12, 15]`


34. **List Slicing**
Next up: list slicing.
```
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]
```
You can think of a Python string as a list of characters.
The string in the editor is garbled in two ways:
Our message is backwards.
The letter we want is every other letter.
Use list slicing to extract the message and save it to a variable called message.
```
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message
```
display on console is:
`I am the secret message!`


35. **Lambda Expressions**
Last but not least, let's look over some lambdas.
```
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
```
We've given you another (slightly different) garbled. Sort it out with a filter() and a lambda.
Q:
Create a new variable called message.
Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s. The second argument will be garbled.
Finally, print your message to the console.
```
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x:x != 'X',garbled)
print message
```
display on console :
`I am another secret message!`

---

## INTRODUCTION TO BITWISE OPERATORS
**Just a Little BIT**
Welcome to an intro level explanation of bitwise operations in Python!
Bitwise operations might seem a little esoteric and tricky at first, but you'll get the hang of them pretty quickly.
Bitwise operations are operations that directly manipulate bits. In all computers, numbers are represented with bits, a series of zeros and ones. In fact, pretty much everything in a computer is represented by bits. This course will introduce you to the basic bitwise operations and then show you what you can do with them.
Bitwise operators often tend to puzzle and mystify new programmers, so don't worry if you are a little bit confused at first. To be honest, you aren't really going to see bitwise operators in everyday programming. However, they do pop up from time to time, and when they do, you should have a general idea of what is going on. 
In the editor are the 6 basic bitwise operations. Click Run and see what the console prints out. All of them will be explained in due time!
```
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT
```
display on console:
```
0
10
0
13
38
-89
```

1. **Lesson 1、0: The Base 2 Number System**
When we count, we usually do it in base 10. That means that each place in a number can hold one of ten values, 0-9. In binary we count in base two, where each place can hold one of two values: 0 or 1. The counting pattern is the same as in base 10 except when you carry over to a new column, you have to carry over every time a place goes higher than one (as opposed to higher than 9 in base 10).（计算模式类似10进制，当超过1的时候你需要一个新列（进位），就像十进制中你超过9了的时候要进位一样。
For example, the numbers one and zero are the same in base 10 and base 2. But in base 2, once you get to the number 2 you have to carry over the one, resulting in the representation "10". Adding one again results in "11" (3) and adding one again results in "100" (4).
Contrary to counting in base 10, where each decimal place represents a power of 10, each place in a binary number represents a power of two (or a bit). The rightmost bit is the 1's bit (two to the zero power), the next bit is the 2's bit (two to the first), then 4, 8, 16, 32, and so on.
The binary number '1010' is 10 in base 2 because the 8's bit and the 2's bit are "on":
```
8's bit  4's bit  2's bit  1's bit
    1       0       1      0 
    8   +   0    +  2   +  0  = 10 
```
Take a look at the examples in the editor. Really try to understand this pattern before moving on. Click Run when you're ready to continue.
```
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11
```
display on console:
```
1 2 3 4 5 6 7
******
4
9
```
2. **I Can Count to 1100!**
All right! Time to practice counting in binary.
To make sure you've got the hang of it, fill out the rest of the numbers all the way up to twelve. （确保你掌握，你用二进制的形式从1填到12）Please do not use the str() method or any other outside functions.
Here are a few numbers that will be good to know going forward -
```
2 ** 0 = 1
2 ** 1 = 2
2 ** 2 = 4
2 ** 3 = 8
2 ** 4 = 16
2 ** 5 = 32
2 ** 6 = 64
2 ** 7 = 128
2 ** 8 = 256
2 ** 9 = 512
2 ** 10 = 1024
```
You may recognize these numbers. Do you have a 32 or 64 bit system? Does your computer have a 256GB hard drive? Computers think in binary!
```
Fill out the rest of the numbers with their corresponding binary values up to twelve in the editor to the right, using the 0bxxx format.
```
```
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
```

3. **The bin() Function**
Excellent! The biggest hurdle you have to jump over in order to understand bitwise operators is learning how to count in base 2. Hopefully the lesson should be easier for you from here on out.
There are Python functions that can aid you with bitwise operations. In order to print a number in its binary representation, you can use the bin() function. bin() takes an integer as input and returns the binary representation of that integer **in a string**. (Keep in mind that after using the bin function, you can no longer operate on the value like a number.)(在使用bin函数后你不能再像数字一样操作它)
You can also represent numbers in base 8 and base 16 using the oct() and hex() functions. (We won't be dealing with those here, however.)
Q:
We've provided an example of the bin function in the editor. Go ahead and use print and bin() to print out the binary representations of the numbers 2 through 5, each on its own line.
```
print bin(1)
#console: 0b1
print bin(2)
#console: 0b10
print bin(3)
#console: 0b11
print bin(4)
#console: 0b100
print bin(5)
@console: 0b101
```

4. **int()'s Second Parameter**
Python has an int() function that you've seen a bit of already. It can turn non-integer input into an integer, like this:
```
int("42")
# ==> 42
```
What you might not know is that the int function actually has an optional second parameter.
```
int("110", 2)
# ==> 6
```
When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.
Q:
In the console are several different ways that you can use the int function's second parameter.On line 7, use int to print the base 10 equivalent of the binary number 11001001.
```
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# because bin() return a string of binary
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)
```
console:
```
1
2
7
4
5
201
```

5. **Slide to the Left! Slide to the Right!**
The next two operations we are going to talk about are the left and right shift bitwise operators. These operators work by shifting the bits of a number over by a designated number of slots.
The block below shows how these operators work on the bit level. Note that in the diagram, the shift is always a positive integer:
```
# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)
```
Shift operations are similar to rounding down after dividing and multiplying by 2 (respectively) for every time you shift, but it's often easier just to think of it as shifting all the 1s and 0s left or right by the specified number of slots.
Note that you can only do bitwise operations on an integer. Trying to do them on strings or floats will result in nonsensical output!
```
shift_right = 0b1100
shift_left = 0b1
# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2
print bin(shift_right)
print bin(shift_left)
```
可见，位移操作不会对原有二进制的数进行修改。So, bitwise operations has never change original binary number


6. **A BIT of This AND That**
The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1. For example:
```
     a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10
```
As you can see, the 2's bit and the 8's bit are the only bits that are on in both a and b, so a & b only contains those bits. Note that using the & operator can only result in a number that is less than or equal to the smaller of the two values.
So remember, for every given bit in a and b:
```
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
```
Therefore,
`0b111 (7) & 0b1010 (10) = 0b10`
which equals two.
Q:
print out the result of calling bin() on 0b1110 & 0b101.
See if you can guess what the output will be!
`print bin(0b1110 & 0b101)`


7. **A BIT of This OR That**
The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1. For example:
```
    a:  00101010  42
    b:  00001111  15       
================
a | b:  00101111  47
```
Note that the bitwise | operator can only create results that are greater than or equal to the larger of the two integer inputs.
So remember, for every given bit in a and b:
```
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1
```
Meaning
`110 (6) | 1010 (10) = 1110 (14)`
Q:
For practice, print out the result of using | on 0b1110 and 0b101 as a binary string. Try to do it on your own without using the | operator if you can help it.
`print bin(0b1110 | 0b101)`


8. **This XOR That?**
The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.
```
    a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37
```
**Keep in mind that if a bit is off in both numbers, it stays off in the result. Note that XOR-ing a number with itself will always result in 0.**(有点小小疑问。off怎么理解？A little bit question，what mean “off”？)
So remember, for every given bit in a and b:
```
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```
Therefore:
`111 (7) ^ 1010 (10) = 1101 (13)`
Q:
For practice, print the result of using ^ on 0b1110 and 0b101 as a binary string. Try to do it on your own without using the ^ operator.
`print bin(0b1110 ^ 0b101)`



9. **See? This is NOT That Hard!**
The bitwise NOT operator (~) just flips all of the bits in a single number. What this actually means to the computer is actually very complicated, so we're not going to get into it. Just know that mathematically, this is equivalent to adding one to the number and then making it negative.
And with that, you've seen all of the basic bitwise operators! We'll see what we can do with these in the next section.
Click Run and observe what the console prints out.
```
print ~1
print ~2
print ~3
print ~42
print ~123
```
display on console
```
-2
-3
-4
-43
-124
```


10. **The Man Behind the Bit Mask**
A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.
```
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on"
```
In the example above, we want to see if the third bit from the right is on.
* First, we first create a variable num containing the number 12, or 0b1100.
* Next, we create a mask with the third bit on.
* Then, we use a bitwise-and operation to see if the third bit from the right of num is on.
* If desired is greater than zero, then the third bit of num must have been one.
Q:
Define a function, check_bit4, with one argument, input, an integer.
It should check to see if the fourth bit from the right is on.
If the bit is on, return "on" (not print!)
If the bit is off, return "off".
Check the Hint for some examples!
```
def check_bit4(input):
  mask = 0b1000
  result = input & mask
  if result > 0 :
    return "on"
  else:
    return "off"
```


11. **Turn It On**
You can also use masks to turn a bit in a number on using |. For example, let's say I want to make sure the rightmost bit of number a is turned on. I could do this:
```
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7
```
**Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.**
Q：
In the editor is a variable, a. Use a bitmask and the value a in order to achieve a result where the third bit from the right of a is turned on. Be sure to print your answer as a bin() string!
```
a = 0b10111011
mask = 0b100
print bin(a | mask)
```


12. **Just Flip Out(翻转)**
Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.
For example, let's say I want to flip all of the bits in a. I might do this:
```
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1
```
Q:
In the editor is the 8 bit variable a. Use a bitmask and the value a in order to achieve a result where all of the bits in a are flipped. Be sure to print your answer as a bin() string!
```
a = 0b11101110
mask = 0b11111111
print bin(a ^ mask)
```


13. **Slip and Slide**
Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.
```
a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask
```
Let's say that I want to turn on the 10th bit from the right of the integer a.
Instead of writing out the entire number, we slide a bit over using the << operator.
We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.
Q:
Define a function called flip_bit that takes the inputs (number, n).
Flip the nth bit (with the ones bit being the first bit) and store it in result.
Return the result of calling bin(result).
```
def flip_bit(number,n):
  mask = 0b1 << (n-1)
  result = number ^ mask
  return bin(result)

print flip_bit(0b011,4)
```
display on console:
`0b1011`

---

## Introduction to Classes 
Classes are a crucial part of object-oriented programming (OOP). In this lesson, we'll explain what classes are, why they're important, and how to use them effectively.
1. **Why Use Classes?**
Python is an object-oriented programming language, which means it manipulates programming constructs called objects. You can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its methods. For example, any time you call
`len("Eric")`
Python is checking to see whether the string object you passed it has a length, and if it does, it returns the value associated with that attribute. When you call
`my_dict.items()`
Python checks to see if my_dict has an items() method (which all dictionaries have) and executes that method if it finds it.
But what makes "Eric" a string and my_dict a dictionary? The fact that they're instances of the str and dict classes, respectively. A class is just a way of organizing and producing objects with similar attributes and methods.
Check out the code in the editor to the below. We've defined our own class, Fruit, and created a lemon instance.When you're ready, click Run to get started creating classes and objects of your own.
```
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
```
display on console:
I'm a yellow lemon and I taste sour.
Yep! I'm edible.


2. **Class Syntax**
A basic class consists only of the class keyword, the name of the class, and the class from which the new class inherits in parentheses. (We'll get to inheritance soon.) For now, our classes will inherit from the object class, like so:
```
class NewClass(object):
  # Class magic here
```
This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.
Q:
Create a class called Animal in the editor. For now, in the body of your class, use the pass keyword. (pass doesn't do anything, but it's useful as a placeholder in areas of your code where Python expects an expression.)
```
class Animal(object):
  pass
```


3. **Classier Classes**
We'd like our classes to do more than... well, nothing, so we'll have to replace our pass with something else.
You may have noticed in our example back in the first exercise that we started our class definition off with an odd-looking function: __init__(). This function is required for classes, and it's used to initialize the objects it creates. __init__() always takes at least one argument, self, that refers to the object being created. You can think of __init__() as the function that "boots up" each object the class creates.
Q:
Remove the pass statement in your class definition, then go ahead and define an __init__() function for your Animal class. Pass it the argument self for now; we'll explain how this works in greater detail in the next section. Finally, put the pass into the body of the __init__() definition, since it will expect an indented block.
```
class Animal(object):
  def __init__(self):
    pass
```


4. **Let's Not Get Too Selfish**
Excellent! Let's make one more tweak to our class definition, then go ahead and instantiate (create) our first object.
So far, __init__() only takes one parameter: self. This is a Python convention; there's nothing magic about the word self. However, it's overwhelmingly common to use self as the first parameter in __init__(), so you should do this so that other people will understand your code.
The part that is magic is the fact that self is the first parameter passed to __init__(). Python will use the first parameter that __init__() receives to refer to the object being created; this is why it's often called self, since this parameter gives the object being created its identity.
Q:
Let's do two things in the editor:
Pass __init__() a second parameter, name.
In the body of __init__(), let the function know that name refers to the created object's name by typing self.name = name. (This will become crystal clear in the next section.)
```
class Animal(object):
  def __init__(self,name):
    self.name = name
```


5. **Instantiating Your First Object**
Perfect! Now we're ready to start creating objects.
We can access attributes of our objects using dot notation. Here's how it works:
```
class Square(object):
  def __init__(self):
#初始化的时候不需要给任何属性。看下面。iniate don't need any attribute ,just like below
    self.sides = 4
my_shape = Square()
print my_shape.sides
```
* First we create a class named Square with an attribute sides.
* Outside the class definition, we create a new instance of Square named my_shape and access that attribute using my_shape.sides.
Q:
Outside the Animal class definition, create a variable named zebra and set it equal to Animal("Jeffrey").
Then print out zebra's name.
```
class Animal(object):
  def __init__(self, name):
    self.name = name
zebra = Animal("Jeffrey")
print zebra.name
```

6. **More on init() and self**
Now that you're starting to understand how classes and objects work, it's worth delving a bit more into __init__() and self. They can be confusing!
As mentioned, you can think of __init__() as the method that "boots up" a class' instance object: the init bit is short for "initialize."
The first argument __init__() gets is used to refer to the instance object, and by convention, that argument is called self. If you add additional arguments—for instance, a name and age for your animal—setting each of those equal to self.name and self.age in the body of __init__() will make it so that when you create an instance object of your Animal class, you need to give each instance a name and an age, and those will be associated with the particular instance you create.
Check out the examples in the editor. See how __init__() "boots up" each object to expect a name and an age, then uses self.name and self.age to assign those names and ages to each object? Add a third attribute, is_hungry to __init__(), and click Run to see the results.
```
# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age,is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry
```


7. **Class Scope**
Another important aspect of Python classes is scope. The scope of a variable is the context in which it's visible to the program.
It may surprise you to learn that not all variables are accessible to all parts of a Python program at all times. When dealing with classes, you can have variables that are available everywhere (global variables), variables that are only available to members of a certain class (member variables), and variables that are only available to particular instances of a class (instance variables).
The same goes for functions: some are available everywhere, some are only available to members of a certain class, and still others are only available to particular instance objects.
Check out the code in the editor. Note that each individual animal gets its own name and age (since they're all initialized individually), but they all have access to the member variable is_alive, since they're all members of the Animal class. Click Run to see the output!
```
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive
```
display on console:
Jeffrey 2 True
Bruce 1 True
Chad 7 True


8. **A Methodical Approach**
When a class has its own functions, those functions are called methods. You've already seen one such method: __init__(). But you can also define your own methods!
Add a method, description, to your Animal class. Using two separate print statements, it should print out the name and age of the animal it's called on. Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.
```
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("kitty",3)
hippo.description()
```


9. **They're Multiplying!**
A class can have any number of member variables. These are variables that are available to all members of a class.
```
hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive
```

* In the example above, we create two instances of an Animal.
* Then we print out True, the default value stored in hippo's is_alive member variable.
* Next, we set that to False and print it out to make sure.
* Finally, we print out True, the value stored in cat's is_alive member variable. We only changed the variable in hippo, not in cat.
Let's add another member variable to Animal.
```
class Animal(object):
  """Makes cute animals."""
  is_alive = True #line 3
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
 
sloth = Animal("lalal",4)
ocelot = Animal("hahah",7)
hippo = Animal("kitty",3)
hippo.description()
  
print hippo.health
print sloth.health
print ocelot.health
```
display on console:
kitty
3
good
good
good


10. **It's Not All Animals and Fruits**
Classes like Animal and Fruit make it easy to understand the concepts of classes and instances, but you probably won't see many zebras or lemons in real-world programs.
However, classes and objects are often used to model real-world objects. The code in the editor is a more realistic demonstration of the kind of classes and objects you might find in commercial software. Here we have a basic ShoppingCart class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.
Q:
Create an instance of ShoppingCart called my_cart. Initialize it with any values you like, then use the add_item method to add an item to your cart.
```
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."
 
my_cart = ShoppingCart("fzk27")
my_cart.add_item("iPad",7000)
```


11. Warning: Here Be Dragons
Inheritance is a tricky concept, so let's go through it step by step.
Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship. For example, a Panda is a bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.
Check out the code in the editor. We've defined a class, Customer, as well as a ReturningCustomer class that inherits from Customer. Note that we don't define the display_cart method in the body of ReturningCustomer, but it will still have access to that method via inheritance. Click Run to see for yourself!
```
class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
```
display on console:
```
I'm a string that stands in for the contents of your shopping cart!
I'm a string that stands in for your order history!
```


12. **Inheritance Syntax**
In Python, inheritance works like this:
```
class DerivedClass(BaseClass):
  # code goes here
```
where DerivedClass is the new class you're making and BaseClass is the class from which that new class inherits.
Q:
On lines 1-4, we've created a class named Shape.
* Create your own class, Triangle, that inherits from Shape, like this:
```
class Triangle(Shape):
# code goes here
```
* Inside the Triangle class, write an __init__() function that takes four arguments: self, side1, side2, and side3.
* Inside the __init__() function, set self.side1 = side1, self.side2 = side2, and self.side3 = side3.
```
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self,side1,side2,side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
```
Click "Stuck? Get a hint!" for an example.
Your code should look something like this:
```
class Triangle(Shape):
#Attention class name input first letter must capitalization!
  def __init__(self, side1, side2, side3):
   self.side1 = side1
   self.side2 = side2
   self.side3 = side3
```

13. **Override!**
Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to override one or more of them.
```
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
```
Rather than have a separate greet_underling method for our CEO, we override (or re-create) the greet method on top of the base Employee.greet method. This way, we don't need to know what type of Employee we have before we greet another Employee.
Q:
Create a new class, PartTimeEmployee, that inherits from Employee.
Give your derived class a calculate_wage method that overrides Employee's. It should take self and hours as arguments.
Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set self.hours = hours.
It should return the part-time employee's number of hours worked multiplied by 12.00 (that is, they get $12.00 per hour instead of $20.00).
```
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self,hours):
    self.hours = hours
    return hours * 12.00
```

14. **This Looks Like a Job For...**
On the flip side, sometimes you'll be working with a derived class (or subclass) and realize that you've overwritten a method or attribute defined in that class' base class (also called a parent or superclass) that you actually need. Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in super call.
The syntax looks like this:
```
class Derived(Base):
  def m(self):
    return super(Derived, self).m()
```
Where m() is a method from the base class.
Q:
First, inside your PartTimeEmployee class:
* Add a new method called full_time_wage with the arguments self and hours.
* That method should return the result of a super call to the calculate_wage method of PartTimeEmployee's parent class. Use the example above for help.
Then, after your class:
* Create an instance of the PartTimeEmployee class called milton. Don't forget to give it a name.
* Finally, print out the result of calling his full_time_wage method. You should see his wage printed out at $20.00 per hour! (That is, for 10 hours, the result should be 200.00.)
```
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self,hours):
    self.hours = hours
    return hours * 12.00
    
  def full_time_wage(self,hours):
    return super(PartTimeEmployee,self).calculate_wage(hours)

milton = PartTimeEmployee("fzk")
print milton.full_time_wage(10)
```

15. **Class Basics**
First things first: let's create a class to work with.
Q:
Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__() method (see the Hint for more).
```
class Triangle(object):
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
```


16. **Class It Up**
Great! Now let's add a member variable and a method to our class.
Inside the Triangle class:
Create a variable named number_of_sides and set it equal to 3.
Create a method named check_angles. The sum of a triangle's three angles should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
```
class Triangle(object):
  number_of_sides = 3
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False
```

17. **Instantiate an Object**
Let's go ahead and create an instance of our Triangle class.
Q:
Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
Print out my_triangle.number_of_sides
Print out my_triangle.check_angles()
```
class Triangle(object):
  number_of_sides = 3
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False 
my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()
```

18. **Inheritance**
Finally, let's create an Equilateral class that inherits from our Triangle class. (An equilateral triangle is a triangle whose angles are all 60˚, which also means that its three sides are equal in length.)
Q:
Create a class named Equilateral that inherits from Triangle.
Inside Equilateral, create a member variable named angle and set it equal to 60.
Create an __init__() function with only the parameter self, and set self.angle1, self.angle2, and self.angle3 equal to self.angle (since an equilateral triangle's angles will always be 60˚).
```
class Triangle(object):
  number_of_sides = 3
  def __init__(self,angle1,angle2,angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  def check_angles(self):
    if self.angle1 + self.angle2 + self.angle3 == 180:
      return True
    else:
      return False
    
my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
```


## Class basics
1. Classes can be very useful for storing complicated objects with their own methods and variables. Defining a class is much like defining a function, but we use the class keyword instead. We also use the word object in parentheses because we want our classes to inherit the object class. This means that our class has all the properties of an object, which is the simplest, most basic class. Later we'll see that classes can inherit other, more complicated classes. An empty class would look like this:
```
class ClassName(object):
  # class statements go here
```
Define a new class named "Car". For now, since we have to put something inside the class, use the pass keyword.
```
class Car(object):
  pass
```

2. **Create an instance of a class**
We can use classes to create new objects, which we say are instances of those classes.
Creating a new instance of a class is as easy as saying:
`newObject = ClassName()`
Below your Car class, create a new object named my_car that is an instance of Car.
```
class Car(object):
  pass
my_car = Car()
```


3. **Class member variables**
Classes can have member variables that store information about each class object. We call them member variables since they are information that belongs to the class object.
Creating member variables and assigning them initial values is as easy as creating any other variable:
```
class ClassName(object):
  memberVariable = "initialValue"
```
Inside your Car class, replace the pass statement with a new member variable named condition and give it an initial value of the string "new".
```
class Car(object):
  condition = "new"
my_car = Car()
```


4. **Calling class member variables**
Each class object we create has its own set of member variables. Since we've created an object my_car that is an instance of the Car class, my_car should already have a member variable named condition. This attribute gets assigned a value as soon as my_car is created.
At the end of your code, use a print statement to display the condition of my_car.
```
class Car(object):
  condition = "new"
my_car = Car()
print my_car.condition
```


5. **Initializing a class**
There is a special function named __init__() that gets called whenever we create a new instance of a class. It exists by default, even though we don't see it. However, we can define our own __init__() function inside the class, overwriting the default version. We might want to do this in order to provide more input variables, just like we would with any other function.
The first argument passed to __init__() must always be the keyword self - this is how the object keeps track of itself internally - but we can pass additional variables after that.
In order to assign a variable to the class (creating a member variable), we use dot notation. For instance, if we passed newVariable into our class, inside the __init__() function we would say:
`self.new_variable = new_variable`
Define the __init__() function of the Car class to take four inputs: self, model, color, and mpg. Assign the last three inputs to member variables of the same name by using the self keyword.
Then, modify the object my_car to provide the following inputs at initialization:
```
model = "DeLorean"
color = "silver"
mpg = 88
```
You don't need to include the self keyword when you create an instance of a class, because self gets added to the beginning of your list of inputs automatically by the class definition.
```
class Car(object):
  condition = "new"
  def __init__(self,model,color,mpg):
    self.model = model
    self.color = color
    self.mpg = mpg
my_car = Car("DeLorean","silver",88)
print my_car.condition
```


6. **Referring to member variables**
Calling class member variables works the same whether those values are created within the class (like our car's condition) or values are passed into the new object at initialization. We use dot notation to access the member variables of classes since those variables belong to the object.
For instance, if we had created a member variable named new_variable, a new instance of the class named new_object could access this variable by saying:
`new_object.new_variable`
Now that you've created my_car print its member variables:
* First print the model of my_car. Click "Stuck? Get a hint!" for an example.
* Then print out the color of my_car.
* Then print out the mpg of my_car.
```
class Car(object):
  condition = "new"
  def __init__(self,model,color,mpg):
    self.model = model
    self.color = color
    self.mpg = mpg

my_car = Car("DeLorean","silver",88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
```


7. **Creating class methods**
Besides member variables, classes can also have their own methods. For example:
```
class Square(object):
  def __init__(self, side):
    self.side = side

  def perimeter(self):
    return self.side * 4
```
The perimeter() class method is identical to defining any other function, except that it is written inside of the Square class definition.
Just like when we defined __init__(), you need to provide self **as the first argument of any class method.**
Q:
Inside the Car class, add a method named display_car to Car that will reference the Car's member variables to return the string, "This is a [color] [model] with [mpg] MPG." You can use the str() function to turn your mpg into a string when creating the display string.
Replace the individual print statements with a single print command that displays the result of calling my_car.display_car()
```
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

my_car = Car("DeLorean", "silver", 88)
my_car.display_car()
```

8. Modifying member variables
We can modify variables that belong to a class the same way that we initialize those member variables. This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.
Inside the Car class, add a method drive_car that sets self.condition to the string "used".
Remove the call to my_car.display_car() and instead print only the condition of your car.
Then drive your car by calling the drive_car method.
Finally, print the condition of your car again to see how its value changes.
```
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
  
  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition
```



9. **Inheritance**
One of the benefits of classes is that we can create more complicated classes that inherit variables or methods from their parent classes. This saves us time and helps us build more complicated objects, since these child classes can also include additional variables or methods.
We define a "child" class that inherits all of the variables and functions from its "parent" class like so:
```
class ChildClass(ParentClass):
  # new variables and functions go here
```
Normally we use object as the parent class because it is the most basic type of class, but by specifying a different class, we can inherit more complicated functionality.
Q：
Create a class ElectricCar that inherits from Car. Give your new class an __init__() method of that includes a battery_type member variable in addition to the model, color and mpg.
Then, create an electric car named my_car with a "molten salt" battery_type. Supply values of your choice for the other three inputs (model, color and mpg).
```
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
  
  def drive_car(self):
    self.condition = "used"

class ElectricCar(Car):
  def __init__(self,model,color,mpg,battery_type):
    self.model = model
    self.color = color
    self.mpg = mpg
    self.battery_type = battery_type
       
my_car = ElectricCar("DeLorean", "silver", 88,"molten salt")
my_car.display_car()
print my_car.condition
my_car.drive_car()
print my_car.condition
```


10. **Overriding methods**
Since our ElectricCar is a more specialized type of Car, we can give the ElectricCar its own drive_car() method that has different functionality than the original Car class's.
Inside ElectricCar add a new method drive_car that changes the car's condition to the string "like new".
Then, outside of ElectricCar, print the condition of my_car
Next, drive my_car by calling the drive_car function
Finally, print the condition of my_car again
```
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
  
  def drive_car(self):
    self.condition = "used"

class ElectricCar(Car):
  def __init__(self,model,color,mpg,battery_type):
    self.model = model
    self.color = color
    self.mpg = mpg
    self.battery_type = battery_type
  def drive_car(self):
    self.condition = "like new"
        
my_car = ElectricCar("DeLorean", "silver", 88,"molten salt")
my_car.display_car()
print my_car.condition
my_car.drive_car()
print my_car.condition
```


11. **Building useful classes**
Chances are, you won't be designing Car classes in the real world anytime soon. Usually, classes are most useful for holding and accessing abstract collections of data.
One useful class method to override is the built-in __repr__() method, which is short for representation; by providing a return value in this method, we can tell Python how to represent an object of our class (for instance, when using a print statement).
Q:
Define a Point3D class that inherits from object
Inside the Point3D class, define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables self.x, self.y, self.z
Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to represent this object in the following format: (x, y, z).
Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3.
Finally, print my_point.
```
class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
    
my_point = Point3D(1, 2, 3)
print my_point
```

---

## File Input/Output
Now that you understand Python syntax and have been introduced to some Python best practices, 
let's apply what you've learned to a real-world application: writing data to a file.

1. 1. **See It to Believe It**
Until now, the Python code you've been writing comes from one source and only goes to one place: you type it in at the keyboard and its results are displayed in the console. But what if you want to read information from a file on your computer, and/or write that information to another file?
This process is called file I/O (the "I/O" stands for "input/output"), and Python has a number of built-in functions that handle this for you.
Check out the code in the editor to the right.
Click Run! You just wrote all the contents of my_list to a text file called output.txt.
```
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10
f = open("output.txt", "w")
for item in my_list:
  f.write(str(item) + "\n")
f.close()
```
the output.txt file content is :
```
1
4
9
16
25
36
49
64
81
100
```

2. The open() Function
Let's walk through the process of writing to a file one step at a time.
The first code that you saw executed in the previous exercise was this:
`f = open("output.txt", "w")`
This told Python to open output.txt in "w" mode ("w" stands for "write"). We stored the result of this operation in a file object, f.
Doing this opens the file in write-mode and prepares Python to send data into the file.
You can open files in any of the following modes:
write-only mode ("w")
read-only mode ("r")
read and write mode ("r+")
append mode ("a"), which adds any new data you write to the file to the end of the file.
**two attributes must string!!!**
Q:
Create a variable, my_file, and set it equal to calling the open() function on output.txt. In this case, pass "r+" as a second argument to the function so the file will allow you to read and write to it! (See the Hint for details.)
`my_file = open("output.txt","r+")`


3. **Writing**
Good work! Now it's time to write some data to a new .txt file.
We added the list comprehension from the first exercise to the code in the editor. Our goal in this exercise will be to write each element of that list to a file called output.txt. The output.txt file that you write to will be created in your current folder - for simplicity, the folder has been hidden. output.txt will list each number on its own line.
We can write to a Python file like so:
`my_file.write("Data to be written")`
The .write() method takes a string argument, so we'll need to do a few things here:
You must close the file. You do this simply by calling my_file.close() (we did this for you in the last exercise). If you don't close your file, Python won't write to it properly. From here on out, you gotta close your files!
Q:
Iterate over my_list to get each value.
Use my_file.write() to write each value to a text file called, output.txt.
Make sure to call str() on the iterating data so .write() will accept it.
Make sure to add a newline (+ "\n") after each element to ensure each will appear on its own line.
Use my_file.close() to close the file when you're done.
Passing the exercise means that you successfully wrote my_list to output.txt!
```
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
# Add your code below!
for item in my_list:
  my_file.write(str(item) + "\n")
my_file.close()
```


4. **Reading**
Excellent! You're a pro.
Finally, we want to know how to read from our output.txt file. As you might expect, we do this with the read() function, like so:
`print my_file.read()`
Q：
Declare a variable, my_file, and set it equal to the file object returned by calling open() with both "output.txt" and "r".
Next, print the result of using .read() on my_file, like the example above.
Make sure to .close() your file when you're done with it! All kinds of doom will happen if you don't.
```
my_file  = open("output.txt","r")
print my_file.read()
my_file.close()
```

5. **Reading Between the Lines**
What if we want to read from a file line by line, rather than pulling the entire file in at once. Thankfully, Python includes a .readline() method that does exactly that.
**If you open a file and call .readline() on the file object, you'll get the first line of the file; subsequent calls to .readline() will return successive lines.**
Q:
Declare a new variable my_file and store the result of calling open() on the "text.txt" file in "r"ead-only mode.
On three separate lines, print out the result of calling my_file.readline(). See how it gets the next line each time?
Don't forget to .close() your file when you're done with it!)
```
my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()
```

6. **PSA: Buffering Data**
We keep telling you that you always need to close your files after you're done writing to them. Here's why!
During the I/O process, data is buffered: this means that it is held in a temporary location before being written to the file.
Python doesn't flush the buffer—that is, write data to the file—until it's sure you're done writing. One way to do this is to close the file. If you write to a file without closing, the data won't make it to the target file.
Q:
Check out our extremely bad code in the editor. Click Run—you'll note that our read_file.read() didn't read any data back!
Add a write_file.close() call after writing to the file but before reading it.
Add a read_file.close() call after the print read_file.read() line
Run the code again.
This time, you'll see the data come through!
```
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")
# Open the file for reading
read_file = open("text.txt", "r")
# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()
# Try to read from the file
print read_file.read()
read_file.close()
```


7. **The 'with' and 'as' Keywords**
Programming is all about getting the computer to do the work. Is there a way to get Python to automatically close our files for us?
Of course there is. This is Python.
You may not know this, but file objects contain a special pair of built-in methods: __enter__() and __exit__(). The details aren't important, but what is important is that when a file object's __exit__() method is invoked, it automatically closes the file. How do we invoke this method? With with and as.
The syntax looks like this:
```
with open("file", "mode") as variable:
  # Read or write to the file
```
Q:
Check out the example in the editor. Note that we don't explicitly close() our file, and remember that if we don't close a file, our data will get stuck in the buffer. Click Run!
Success! is written to a file called text.txt.
```
with open("text.txt", "w") as textfile:
  textfile.write("Success!")
```


8. **Try It Yourself**
It worked! Our Python program successfully wrote to text.txt.
Q:
Now you try: write any data you like to a file called text.txt using with...as. Give your file object the usual name: my_file.
```
with open("text.txt","w") as my_file:
  my_file.write("hahhhaa")
#write method must string or letter or character as input
```


9. **Case Closed?**

Finally, we'll want a way to test whether a file we've opened is closed. 
Sometimes we'll have a lot of file objects open, and if we're not careful, 
they won't all be closed. How can we test this?

```
f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True
```

Python file objects have a closed attribute which is True when the file is closed and False otherwise.
By checking file_object.closed, we'll know whether our file is closed and can call close() on it if it's still open.

Q:

Below your with...as code, do two things:

Check if the file is not closed.
If that's the case, call .close() on it.

(You don't need an else here, since your if statement should do nothing if closed is True.)

After your if statement, print out the value of my_file.closed to make sure your file is really closed.

```
with open("text.txt","w") as my_file:
  my_file.write("hahhhaa")

if not my_file.closed:
  my_file.close()
#test closed
print my_file.closed
```






#code习得
