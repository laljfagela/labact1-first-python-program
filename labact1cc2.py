#Programmed by: FAGELA, LUCCI ANIA LUISSE J. 
#Program Date: September 07, 2023

#Pounds to Kilograms 

Weight_in_pounds = input("Input weight in pounds: ")

Weight_in_Kilograms = float(Weight_in_pounds)*0.453592

print("Weight in pounds: " + Weight_in_pounds)
print("Weight converted to Kilograms: " + str(Weight_in_Kilograms))
print("=============================================")

#Miles to Kilometers 

Distance_in_Miles = input("Input distance in Miles: ")

Distance_in_Kilometers = float(Distance_in_Miles)*1.60934

print("Distance in pounds: " + Distance_in_Miles)
print("Distance converted to Kilometers: " + str(Distance_in_Kilometers))
print("=============================================") 

# Fahrenheit to Celsius 

Temperature_in_Fahrenheit = int(input("Input temperature in Fahrenheit: "))

Temperature_in_Celsius = (Temperature_in_Fahrenheit - 32) / 1.8

print("Temperature in Fahrenheit: " + str(Temperature_in_Fahrenheit))
print("Temperature converted to Kilometers: " + str(Temperature_in_Celsius))
print("=============================================") 


#Age of All Students: Asking the user input 

Student_1 = int(input("Student 1 age: "))
Student_2 = int(input("Student 2 age: "))
Student_3 = int(input("Student 3 age: "))
Student_4 = int(input("Student 4 age: "))
Student_5 = int(input("Student 5 age: "))
Student_6 = int(input("Student 6 age: "))
Student_7 = int(input("Student 7 age: "))
Student_8 = int(input("Student 8 age: "))
Student_9 = int(input("Student 9 age: "))
Student_10 = int(input("Student 10 age: "))

Total = Student_1 + Student_2 + Student_3 + Student_4 + Student_5 + Student_6 + Student_7 + Student_8 + Student_9 + Student_10
Average_Age = float(Total) / 10

print("The average age of student is " + str(Average_Age))
print("=============================================") 

#Age of All Student 2: Inout is already provided 

Student_Ages = [19,19,19,18,17,16,19,20,17,16]

print("Student 1: " , Student_Ages[0])
print("Student 2: " , Student_Ages[1])
print("Student 3: " , Student_Ages[2])
print("Student 4: " , Student_Ages[3])
print("Student 5: " , Student_Ages[4])
print("Student 6: " , Student_Ages[5])
print("Student 7: " , Student_Ages[6])
print("Student 8: " , Student_Ages[7])
print("Student 9: " , Student_Ages[8])
print("Student 10: " , Student_Ages[9])

Sum = (Student_Ages[0] + Student_Ages[1] + Student_Ages[2] + Student_Ages[3] + Student_Ages[4] + Student_Ages[5] + Student_Ages[6] + Student_Ages[7] + Student_Ages[8] + Student_Ages[9]  )
Average = (Sum) / len(Student_Ages)

print("The average age of student is " + str(Average))
print("=============================================")

#Story 

Story = """ In the Royal Flash Kingdom, 5 lads possessed different magical powers and capabilities. 
      Vox Akuma,  the Voice Demon, has the power to influence others with his voice. 
      Luca Kaneshiro, the mean and evil mafia boss from the past. 
      Mysta Rias, the genius detective, is also a fox in nature. 
      Ike Eveland, is a novelist who can travel through time using his Blue-Diamond Pen. 
      And finally, Shu Yamino, a sorcerer with the ability to control his victim’s 
      minds through his magical purple flames.
      They are heroes. As they ventured through Diamond City Lights, 
      they were met with various elements that affected their powers gradually,
      the Pomu Leaf, remnants of Pomu Fairies who died because of a so-called angel,
      Enna Alouette. Enna Alouette used the Pomu Leaf to lure the five lads to her. 
      However, before they arrive in Enna’s kingdom, they met a flaming purple dragoon,
      Selen Tatsuki. Selen attacked the five lads,
      and they fought their hardest to defend and attack. 
      But, Selen’s final fiery blow was so powerful, and Mysta sacrificed himself. 
      Taking the attack, to help save his friends. Mysta died. """ 
      
print(Story)
print("=============================================")
