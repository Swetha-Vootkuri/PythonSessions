#Return sum of two numbers

def get_sum_of_two_numbers(num1=None, num2=None):
    return (num1+num2)

if __name__ == "__main__":
    sum_of_two_num = get_sum_of_two_numbers(num1=2,num2=3)
    print(sum_of_two_num)

x = input("Enter any string: ")
#take input from user
a = x.split(",")
print(a)
#use split method to split at whitespaces
a.reverse()
#reverse all the elements of the string
print(' '.join(a))
#concatenate them into a string