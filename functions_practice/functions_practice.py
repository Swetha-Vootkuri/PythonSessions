def welcome_message(Welcome):
    return Welcome

def main():
    output = welcome_message("Hi")
    print(output)

if __name__ == "__main__":
    main()


def welcome_with_name(string="Hello", name = "Swe"):
    welcome_name = string + " " + name
    return welcome_name

def len_list(list):
    len_of_list = len(list)
    return len_of_list

def main():
    output = welcome_with_name(name = "SWE")
    print(output)
    a = [1,2,3]
    len_of_list = len_list(a)
    print(len_of_list)

if __name__ == "__main__":
    main()

def my_function():
    my_function = 2*3
    return my_function
print(my_function())


def my_sum(fnum, lnum):
    return fnum+lnum
print(my_sum(2,3))


def my_func(fname):
    print(fname +" " + "Hi")
my_func("Swetha")

def my_name(fname="Swetha"):
    return fname
print(my_name())

def my_name(fname="Swetha"):
    return fname
print(my_name(fname= "swet"))


def my_name(fname):
    return fname
print(my_name("Hey"))
print(my_name("happy"))

def my_name(fname, lname):
    return fname +" " + lname
print(my_name("swetha", "V"))

def my_name(lname, fname = "Swetha"):
    return fname +" " + lname
print(my_name( "V"))

def my_name(lname, fname= "Swetha"):
    return fname +" " + lname
print(my_name("V", fname = "swetha"))

def my_funct(fruit):
    for x in fruit:
        print(x)
fruitbasket = ["Apple", "Banana"]
my_funct(fruitbasket)


cars = ["Honda", "Toyota", "Lexus"]
for x in cars:
    print(x)

print(cars[0])
print(cars.index("Honda"))
print(len(cars))
cars.append("Hyundai")
print(cars)
cars.pop()
cars.pop(0)
print(cars)
cars.remove("Toyota")
cars.insert(0,"Honda")
print(cars)
cars.sort()
print(cars)








