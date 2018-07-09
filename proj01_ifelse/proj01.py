# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.
#var name
user_name = raw_input("Enter your name: ")
# user_grade = raw_input("Enter your grade: ")
# grad_year = 12 - int(user_grade)
# print user_name + ", you will graduate from high school in", grad_year,  "years!"
# # Part II:
# # This program asks the user for his/her name and birth month.
# # Then, it prints a sentence that says the number of days and months until their birthday
# user_name_gram = user_name[0:1].upper() + user_name[1:].lower()
# print user_name_gram

user_month = raw_input("Enter your birth month (number): ")
user_day = raw_input("Enter your birth day (number): ")
user_month = int(user_month)
user_day = int(user_day)
current_month = 7
current_day = 9
if user_month >= current_month:
     birth_month_count = user_month - current_month
else:
      birth_month_count = 12 - (current_month - user_month)
if user_day >= current_day:
    birth_day_count = user_day - current_day
else:
    birth_day_count = 30 - (user_day - current_day)
    birth_month_count = birth_month_count - 1
print user_name + ", your birthday is in ", birth_month_count, "months and", birth_day_count, "days!"

user_age = raw_input("Enter your age: ")
user_age = int(user_age)
if user_age <= 7:
    print "you can only watch G rated movies"
elif user_age > 7 and user_age < 13:
    print "you can watch G and PG rated movies"
elif user_age >= 13 and user_age < 18:
    print "you can watch G, PG and PG-13 rated movies"
else:
    print "you can watch G, PG, PG-13 and R rated movies"

user_dog_count = raw_input("How many dogs do you have?: ")
user_dog_count = int(user_dog_count)
if user_dog_count == 0:
    print "I suggest you get a dog, they are really fun!"
elif user_dog_count > 0 and user_dog_count <= 3:
    print "Good for you!"
else:
    print "Wow that's a lot of dogs!"



      
    















# If you complete extensions, describe your extensions here!

