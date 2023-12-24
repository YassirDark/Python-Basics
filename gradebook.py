#list of last semester grades 
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
# Your code below: 
subjects = ["phsics","calculus","poetry","history"]
grades =[98,97,85,88]
gradebook = [["phsics",98],["calculus",97],["poetry",85],["history",88]]
#Add computer science and visual arts to the list
gradebook.append(["computer science",100])
gradebook.append(["visual arts",93])
#Change the grade of visual arts subjict 
gradebook[5][1]= 88
#Change same values in the list
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)
# use the + methode to combined between two lists
full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)
