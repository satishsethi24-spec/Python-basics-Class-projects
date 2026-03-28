# Exam Eligibility Check

# if person is present

# if person attendence percentage is greater = 75

# if person is having medical certicate


present = input("Is the person present for the exam (Y/N))")

present = present.lower()

if present == 'n':

    print("Person is absent for the exam")

else:

    attendence_per = float(input("Enter the attendence percentage : "))

    if attendence_per >= 75:

        print("You are eligible for the exam")

        medical_cert = input("Do you have medical certification (Y/N) : ")

        medical_cert = medical_cert.lower()


        if medical_cert == 'y':

            print("You are allowed for the exam")

        else:

            print("You are not allowed for exam")

    else:

        print("You are not eligible for the exam")