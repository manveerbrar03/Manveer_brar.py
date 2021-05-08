#Manveer_singh and pahuljot singh
def main():
    #inputs for users
    name = input('What is your name? ')
    age = int(input('How old are you? '))
    number = int(input('What is your favourite number? '))

    #printout for the text
    print('your name is %s' % (name))
    print('you are %i years old' % (age))
    
    # condition to choose either the number is positive 
    #or the number is negative
    if number > 0:
        print('your favourite number is %i and it is greater than 0' % (number))
    if number < 0:
        print('your favourite number is %i and it is less than 0' % (number))
    if number == 0:
        print('your favourite number is %i and it is equal to 0' % (number))

    #ask user for per month salary as well as expences
    salary = int(input('Enter your salary: '))
    expences = int(input('Enter your expences: '))

    #variable that equals to the total earning of the month
    saving = salary - expences
     
    # condition to determine if money is gained or lose by users
    if saving > 0:
        print('congrats on saving')
    else:
        print('keep trying')
    
    num = (saving/salary)*100

    #saved less or equal to 0
    if num <= 0:
        print("you Saved less than or equal to 0")

    #saved less than 30%
    elif num <= 30:
        print("you saved less than 30%")
    
    #saved less than 50%
    elif num <= 50:
        print("you saved less than 50%")

    #saved less than 70%
    elif num <= 70:
        print("you saved less than 70%")

    #saved less than 90%
    elif num <= 90:
        print("you saved less than 90%")

    #saved 100%
    if num == 100:
        print("you saved 100% ")

    #ask the user for 5 largest expenses 
    exp1 = int(input("Enter your 5 biggest expenses: "))
    exp2 = int(input())
    exp3 = int(input())
    exp4 = int(input())
    exp5 = int(input())

    average = int((exp1+exp2+exp3+exp4+exp5)/5)
    total = exp1+exp2+exp3+exp4+exp5

    print("Average - $%i" % (average))
    print("Total - $%i" % (total))
if __name__ == '__main__':
    main() 
