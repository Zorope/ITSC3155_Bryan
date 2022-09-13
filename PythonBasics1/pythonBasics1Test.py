
import pythonBasics1
# main() is already set up to call the functions
# we want to test with a few different inputs,
# printing 'OK' when each function is correct.
# the simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Calls the functions in pythonBasics1 with interesting inputs.
def main():
    # set which functions to test
    check_odd_range = True
    check_has_lower_case = False
    check_fizz_buzz = False

    if check_odd_range:
        print('Testing odd_range:')
        test(pythonBasics1.odd_range(1, 5), [1, 3])
        test(pythonBasics1.odd_range(2, 6), [3, 5])
        test(pythonBasics1.odd_range(100, 111), [101, 103, 105, 107, 109])
        test(pythonBasics1.odd_range(0, 0), [])
        test(pythonBasics1.odd_range(0, 10), [1, 3, 5, 7, 9])
        test(pythonBasics1.odd_range(10, 5), [])
        test(pythonBasics1.odd_range(9, 14), [9, 11, 13])
        test(pythonBasics1.odd_range(100, 100), [])
        test(pythonBasics1.odd_range(-100, -90), [-99, -97, -95, -93, -91])
        test(pythonBasics1.odd_range(-5, -1), [-5, -3])
        test(pythonBasics1.odd_range(-6, -2), [-5, -3])
        test(pythonBasics1.odd_range(5, 7), [5])

    if check_has_lower_case:
        print("---------------------------------------------------------")
        print('Testing has_lower_case:')
        test(pythonBasics1.has_lower_case("i am a strinG"), True)
        test(pythonBasics1.has_lower_case("no upper case here"), True)
        test(pythonBasics1.has_lower_case("I Have Multiple Lower Case Chars"), True)
        test(pythonBasics1.has_lower_case("HELLO"), False)
        test(pythonBasics1.has_lower_case("I start with an UPPER CASE CHAR"), True)
        test(pythonBasics1.has_lower_case("ALL UPPER CASE"), False)
        test(pythonBasics1.has_lower_case(" "), False)
        test(pythonBasics1.has_lower_case("M"), False)
        test(pythonBasics1.has_lower_case("o"), True)
        test(pythonBasics1.has_lower_case("Hello"), True)
        test(pythonBasics1.has_lower_case("gOODBYE"), True)
        test(pythonBasics1.has_lower_case("001101"), False)
        test(pythonBasics1.has_lower_case("2 b or not 2 B"), True)
        test(pythonBasics1.has_lower_case("2 DO OR NOT 2 DO"), False)

    if check_fizz_buzz:
        print("-------------------------------------------------------")
        print('Testing fizz_buzz')
        test(pythonBasics1.fizz_buzz(6),"Fizz")
        test(pythonBasics1.fizz_buzz(45),"FizzBuzz")
        test(pythonBasics1.fizz_buzz(2),"2")
        test(pythonBasics1.fizz_buzz(-3),"-3")
        test(pythonBasics1.fizz_buzz(15),"FizzBuzz")
        test(pythonBasics1.fizz_buzz(10),"Buzz")
        test(pythonBasics1.fizz_buzz(21),"Fizz")
        test(pythonBasics1.fizz_buzz(0),"0")
        test(pythonBasics1.fizz_buzz(25),"Buzz")
        test(pythonBasics1.fizz_buzz(101),"101")

if __name__ == '__main__':
  main()
