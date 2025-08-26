# # # student = 1000
# # # rating = 5.5
# # # boo = True
# # # name = "Dhruv"
# # # print(student,rating,boo,name)


# # # a=4-2
# # # print(a)

# # # b = 3
# # # b +=3
# # # print(b)

# # # a = "black"

# # # b = type(a)

# # # print(b)





# # # a = int(input("enter a number: "))
# # # b = int(input("enter a number: "))

# # # print("this is the number",a)
# # # print("this is the number",b)



# # # a = int(input("enter a number: "))
# # # b = int(input("enter a number: "))

# # # print("this is the sum", a + b)


# # # a =int(input("enter a number: "))

# # # print(a)






# # # a = int(input("Enter a number: "))
# # # b = int(input("Enter another number: "))

# # # c = a % b
# # # print(c)


# # # a = int(input("Enter a number: "))
# # # b = int(input("Enter another number: "))

# # # print("a is greater than b", a>b)





# # # name = "Dhruv"

# # # nameshort = name[-5:-1]
# # # nanu = name[0:5:2]

# # # # print(nameshort)
# # # # print(nanu)
# # # # print(len(name))
# # # # print(name.capitalize())
# # # print(name.split())



# # # name = "Dhruv"
# # # print("Good Morning!", name)




# # # name = "Dhruv"

# # # print(f"Good Morning{name}" "\n Welcome to the class")


# # letter = '''
# # dear <|Name|>,
# # you are selected!
# # <|Date|>
# # '''
# # print(letter.replace("<|Name|>", "Dhruv").replace("<|Date|>", "1st January 2024"))4

# # name =("Enter your  name")

# # print(name.find("  "))

# # list1 = ["apple", "banana", "cherry",0,2.12, True, "Dhruv"]
# # list2 = [1,2,3,4,5,6,7,8,9,10]
# # list1.append("new item")
# # list2.reverse()
# # print(list1)
# # print(list2)


# # a = (1,)
# # print(type(a))

# # a = (1,45,342,False, "Dhruv", 2.12)

# # print("a")





# # a= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# # repaeat = a * 3
# # print(repaeat)

# # fruits = []

# # f1 = input("enter fruits:")
# # fruits.append(f1)
# # f2 = input("enter fruits:")
# # fruits.append(f2)           
# # f3 = input("enter fruits:")
# # fruits.append(f3)

# # print(fruits)

# # m1 = []

# # marks = int(input("enter marks of student 1: "))
# # m1.append(marks)
# # marks = int(input("enter marks of student 2: "))
# # m1.append(marks)        
# # marks = int(input("enter marks of student 3: "))
# # m1.append(marks)

# # m1.sort()
# # print(m1)



# # what= sum([1, 2, 3, 4, 5])
# # print(what)



# # # l = [1, 2, 3, 4, 5]

# # # print(sum(l))


# # # a = (7,0,8,0,0,9)

# # # n= a.count(0)
# # # print(n)



# # marks = {
# #     "Dhruv": 98,
# #     "Aarav": 95,
# #     "Riya": 92,
# #     "Sia": 90
# # }

# # marks.update({
# #     "Aanya": 88,
# #     "Kabir": 85
# # })
# # # print(marks, type(marks))

# # # print(marks["Dhruv"])
# # # print(marks.keys())
# # # print(marks.values())
# # print(marks.items())



# # words = {
# #     "Dhruv": "A name",
# #     "Python": "A programming language",
# #     "Code": "A set of instructions",
# #     "Dhruv": "My name"  
# # }

# # word = input("enter a word you want meaning:")
 
# # print(words[word])


# s = set()

# n = int(input("Enter number: "))
# s.add(int(n))
# n = int(input("Enter number: "))
# s.add(int(n))
# n = int(input("Enter number: "))
# s.add(int(n))
# n = int(input("Enter number: "))
# s.add(int(n))
# n = int(input("Enter number: "))
# s.add(int(n))
# n = int(input("Enter number: "))
# s.add(int(n))
# n = int(input("Enter number: "))
# s.add(int(n))

# print(s)


# book = {}

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")

# book.update({name:lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")       
# book.update({name:lang})

# print(book)


# a = int(input("Enter your age: "))

# if (a>18):
#     print("You are eligible to vote")
# elif (a<0):
#     print("enter valid number")
# else:
#     print("You are not eligible to vote")   




# a = int(input("Enter number 1:"))
# b = int(input("Enter number 2:"))
# c = int(input("Enter number 3:"))       
# d = int(input("Enter number 4:"))       

# if (a>b and a>c and a>d):
#     print("a is greater")
# elif (b>a and b>c and b>d):
#     print("b is greater")
# elif (c>a and c>b and c>d):
#     print("c is greater")
# else:
#     print("d is greater")


# marks1 = int(input("Enter marks 1 : "))
# marks2 = int(input("Enter marks 2 : "))
# marks3 = int(input("Enter marks 3 : "))
# marks4 = int(input("Enter marks 4 : "))

# total_percentage = ((marks1 + marks2 + marks3 + marks4) / 400) * 100

# if (total_percentage > 40 ):
#     print("You are passed")

# elif (total_percentage == 40):
#     print("you just passed")

# else:
#     print("You have failed")

# spam_words = ["ass", "fuck", "bitch"]
# text = input("Enter a text: ")


# print(text)
# for word in spam_words:
#     if text.__contains__(word):
#         print("the word is spam")

#     else:
#         print("the word is not spam")
        
       


# for i in range (1,10):
#     print(i)


# i = 1

# while (i<100):
#     print(i)
#     i +=1


# l = [1,"harry", 3.14, True, "Dhruv"]

# i = 0

# while(i<len(l)):
#     print(l[i])
#     i += 1



# for i in range(4):
#     print(i)

# print("Done with for loop")

# for j in range(0,100,5):
#     print(j)


# for i in range (100):
#     print("printing",i)
#     if (i== 20):
#         continue
#     if (i== 50):
#         print("done prining")

#         break
    

# for i in range(645):
#     pass

# i = 0
# while (i<45):
#     print(i)
#     i +=1


# n = int(input("enter a number: "))
# print(f"Multiplication table of {n}:")

# for i in range (1,11):
#     print(f"{n}*{i} = {n*i}")



# l = ["harry", "Dhruv", "Aarav", "Riya"]

# for name in l:
#     if(name.startswith("D")):
#         print(f"hello {name}")





# n = int(input("enter a number: "))
# i =1

# while(i<11):
#     print(f"{n}*{i} = {n*i}")
#     i += 1



# n = int(input("Enter a number: "))

# for i in range (2,n):
#     if (n%i) == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# /////

# n = int(input("Enter a number: "))

# product = 1
# for i in range(1,n+1):
#     product = product*i

# print(f"The factorial of {n} is {product}")



# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1) ,end="")
#     print(" ")


# def avg():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))  
#     c = int(input("Enter third number: "))

#     average = (a + b + c) / 3
#     print(f"The average of {a}, {b}, and {c} is {average}")

# avg()
# print("Calculating average again...")
# avg()
# print("Calculating average again...")
# avg()
# print("done with the program")




# def goodday(name,ending):
#     print("Good day!" + name)
#     print(ending)

# goodday("dhruv", "Thank you")
# goodday("Aarav", "Have a nice day")
# goodday("Riya", "See you soon") 



# def goodday(name,ending="Thank you"):
#     print(f"Good Day, {name}")
#     print(ending)

# goodday("Dhruv")


# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         return n * factorial(n-1)

    
# n = int(input("Enter a number: "))
# print(f"the factorial of {n} is {factorial(n)}")


# def greatest(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     else:
#         return c

 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: ")) 
# c = int(input("Enter third number: "))

# print(f"the greatest number is {greatest(a,b,c)}")


# def pattern(n):
#     if n == 0:
#         return
#     print("*" * n)

#     pattern(n-1)

# pattern(5)

# def multiply(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")

# n= int(input("Enter a number: "))
# multiply(n)
# print("Multiplication table completed.")


# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()



# st = "lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# f = open("myfile.txt", "w")
# f.write(st)
# f.close()


 

# f = open("file.txt")
# data = f.read()
# if data.__contains__("lorem"):
#     print("lorem is present in the file")
# else:
#     print("lorem is not present in the file")
# f.close()






# import random

# def game():
#     print("Welcome to the game!")
#     score = random.randint(1, 100)
#     print("Your score is", score)
#     return score





# age =  int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")





# class employee:
#     name = "Dhruv"
#     language = "Python"
#     salary = 100000

# dhruv = employee()
# print(dhruv.name,dhruv.language)


# class Employee:
#     language = "Python"
#     salary = 1000000

# harry = Employee()
# harry.name = "harry"
# print(harry.name,harry.language, harry.salary)

# dhruv = Employee()
# dhruv.name = "Dhruv"
# print(dhruv.name, dhruv.language, dhruv.salary)





# class Employee:
#     language = "Python"
#     salary = 1000000

#     def getInfo():
#         print(f"The language is {language} and the salary is {salary}")

  


# dhruv = Employee()
# dhruv.language = "typescript"
# dhruv.getInfo()












# def reverse_string(s):
#     result = ""
#     for char in s:
#         result = char + result  # prepend each character
#     return result




# s= "python"
# reversed_string = ""

# for char in s:
#     reversed_string = char +reversed_string

# print("Reversed String:", reversed_string)

#  re







