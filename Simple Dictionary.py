dic = {
    "Harry":"on of the best teacher in the world",
    "CodewithHarry":"Youtube channel of Harry",
    "Python":"Programming language I am learning right now",
    "Mutable":"Can Change",
    "Immutable":"Can not Change"
}
print()
print("You will have to type 1st letter in capital")
print("\nWord you can get meaning of:\n 1) Harry\n 2) CodewithHarry\n 3) Python\n 4) Mutable\n 5) Immutable ")
userinp = input()

dicsearch = dic[userinp]
print("\n\nThe meaning of",userinp, "is:", dicsearch,"\n\n")

print("Press enter to close")
a= input()
