# FILE NAME - grade_converter.py

# NAME: Rob Warner
# DATE: March 1, 2026
# BRIEF DESCRIPTION:  convert grade to letter



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

grade = int(input('Enter the grade (between 0 and 100): '))

if grade >= 90:
    print('Your grade is an A')
elif grade >= 80:
    print('Your grade is a B')
elif grade >= 70:
    print('Your grade is a C')
elif grade >= 65:
    print('Your grade is a D')
elif grade >= 0:
    print('Your grade is an F')
else:
    print('Invalid grade')

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab? be careful with elif statements. They can get you good. 







'''
