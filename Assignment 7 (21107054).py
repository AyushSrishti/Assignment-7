# Q1
# import all functions/classes from the tkinter
from tkinter import *


# Function for finding GST rate
def findGst():
    # take a value from the respective entry boxes
    # get method returns current text as string
    org_cost = int(org_priceField.get())

    N_price = int(net_priceField.get())

    # calculate GST rate
    gst_rate = ((N_price - org_cost) * 100) / org_cost;

    # insert method inserting the
    # value in the text entry box.
    gst_rateField.insert(10, str(gst_rate) + " % ")


# Function for clearing the
# contents of all text entry boxes
def clearAll():
    # deleting the content from the entry box
    org_priceField.delete(0, END)

    net_priceField.delete(0, END)

    gst_rateField.delete(0, END)


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.configure(background="light green")

    # set the name of tkinter GUI window
    gui.title("GST Rate Finder")

    # Set the configuration of GUI window
    gui.geometry("300x300")

    # Create a Original Price: label
    org_price = Label(gui, text="Original Price",
                      bg="blue")

    # Create a Net Price : label
    net_price = Label(gui, text="Net Price",
                      bg="blue")

    # Create a Find Button and attached to
    # findGst function
    find = Button(gui, text="Find", fg="Black",
                  bg="Red",
                  command=findGst)

    # Create a Gst Rate : label
    gst_rate = Label(gui, text="Gst Rate", bg="blue")

    # Create a Clear Button and attached to
    # clearAll function
    clear = Button(gui, text="Clear", fg="Black",
                   bg="Red",
                   command=clearAll)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    # padx attributed provide x-axis margin
    # from the root window to the widget.

    # pady attributed provide y-axis
    # margin from the widget.
    org_price.grid(row=1, column=1, padx=10, pady=10)

    net_price.grid(row=2, column=1, padx=10, pady=10)

    find.grid(row=3, column=2, padx=10, pady=10)

    gst_rate.grid(row=4, column=1, padx=10, pady=10)

    clear.grid(row=5, column=2, padx=10, pady=10)

    # Create a text entry box for filling or typing the information.
    org_priceField = Entry(gui)

    net_priceField = Entry(gui)

    gst_rateField = Entry(gui)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    org_priceField.grid(row=1, column=2, padx=10, pady=10)

    net_priceField.grid(row=2, column=2, padx=10, pady=10)

    gst_rateField.grid(row=4, column=2, padx=10, pady=10)

    # Start the GUI
    gui.mainloop()

# Q2

# import all methods and classes from the tkinter
from tkinter import *

# import calendar module
import calendar


# Function for showing the calendar of the given year
def showCal():
    # Create a GUI window
    new_gui = Tk()

    # Set the background colour of GUI window
    new_gui.config(background="white")

    # set the name of tkinter GUI window
    new_gui.title("CALENDAR")

    # Set the configuration of GUI window
    new_gui.geometry("550x600")

    # get method returns current text as string
    fetch_year = int(year_field.get())

    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)

    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row=5, column=1, padx=20)

    # start the GUI
    new_gui.mainloop()


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background="white")

    # set the name of tkinter GUI window
    gui.title("CALENDAR")

    # Set the configuration of GUI window
    gui.geometry("250x140")

    # Create a CALENDAR : label with specified font and size
    cal = Label(gui, text="CALENDAR", bg="dark gray",
                font=("times", 28, 'bold'))

    # Create a Enter Year : label
    year = Label(gui, text="Enter Year", bg="light green")

    # Create a text entry box for filling or typing the information.
    year_field = Entry(gui)

    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text="Show Calendar", fg="Black",
                  bg="Red", command=showCal)

    # Create a Exit Button and attached to exit function
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    # start the GUI
    gui.mainloop()

# Q3

# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()


# Q4

# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = []
arr.append(int(input("Enter a number:")))
arr.append(int(input("Enter a number:")))
arr.append(int(input("Enter a number:")))
arr.append(int(input("Enter a number:")))
arr.append(int(input("Enter a number:")))
arr.append(int(input("Enter a number:")))
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])


# Q5

# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Python Program to search an element
# in a sorted and pivoted array

# Searches an element key in a pivoted
# sorted array arrp[] of size n
def pivotedBinarySearch(arr, n, key):
    pivot = findPivot(arr, 0, n - 1);

    # If we didn't find a pivot,
    # then array is not rotated at all
    if pivot == -1:
        return binarySearch(arr, 0, n - 1, key);

    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot - 1, key);
    return binarySearch(arr, pivot + 1, n - 1, key);


# Function to get pivot. For array
# 3, 4, 5, 6, 1, 2 it returns 3
# (index of 6)
def findPivot(arr, low, high):
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)


# Standard Binary Search function*/
def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high,
                            key);
    return binarySearch(arr, low, (mid - 1), key);


# Driver program to check above functions */
# Let us search 3 in below array
arr1 = []
arr1.append(int(input("Enter a number:")))
arr1.append(int(input("Enter a number:")))
arr1.append(int(input("Enter a number:")))
arr1.append(int(input("Enter a number:")))
arr1.append(int(input("Enter a number:")))
arr1.append(int(input("Enter a number:")))
n = len(arr1)
key = int(input("Enter the element to search for: "))
print(arr1)

insertionSort(arr1)
for i in range(len(arr1)):
    print("% d" % arr1[i])
print("Index of the element is : ",
      pivotedBinarySearch(arr1, n, key))
print(arr1.count(key))


# Q6
# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = []
duplicate.append(int(input("Enter a number:")))
duplicate.append(int(input("Enter a number:")))
duplicate.append(int(input("Enter a number:")))
duplicate.append(int(input("Enter a number:")))
duplicate.append(int(input("Enter a number:")))
duplicate.append(int(input("Enter a number:")))
print(Remove(duplicate))