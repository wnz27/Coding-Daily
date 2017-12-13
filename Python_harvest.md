# Python

## **Iterating over a list in a function**
Now that we've learned about range, we have two ways of iterating through a list.
Method 1 - for item in list:
```
for item in list:
  print item
```
Method 2 - iterate through indexes:
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
1. Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)
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
2. Factorial
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
3. is_prime
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
4. Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".
You may not use reversed or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @, or “#").
```
def reverse (text):
  result = []
  for i in text[len(text)::-1]:
    result += i
  return "".join(result)
```
5. Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
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
6. scrabble_score
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
7. Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. For example:
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
8. Define a function called count that has two arguments called sequence and item.
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
9. Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example, purify([1,2,3]) should return [2].
Do not directly modify the list you are given as input; instead, return a new list with only the even numbers. (even numbers : 偶数)
```
def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res
```
10. Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list. For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
Don't worry about the list being empty.
Your function should return an integer. 
```
def product (numbers):
  result = 1
  for number in numbers:
    result *= number
  return result
```
11.  Write a function ~remove_duplicates~ that takes in a list and removes elements of the list that are the same.
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
12. median
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
13. Define a function on line 3 called print_grades with one argument, a list called grades_input.
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
14. 





#code习得