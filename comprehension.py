# Importujemy moduł "random" z biblioteki standardowej. Umożliwia dostęp do funkcji,
# które pozwalają na generowanie losowych liczb.
# Import module "random" from Standard Library. It provides access to functions that allows us to generate
# random numbers.
import random
# Przypisz 0 do zmiennej "guesses_taken".
# Assign 0 to "guesses_taken" variable.
guesses_taken = 0
# Wypisz "Hello! What is your name?".
# Print string "Hello! What is your name?".
print('Hello! What is your name?')
# Przypisz odpowiedz do zmiennej "myName".
# Assign user's input to "myName" variable.
myName = input()
# Przypisz losową liczbę pomiędzy 1 a 20 do zmiennej "number".
# Assign random number between 1 and 20 to "number" variable.
number = random.randint(1, 20)
# Wydrukuj napis. Miejsce nazwy zmiennej zajmie jej aktualna wartość.
# Print string with the current value of the variable "myName".
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# Pętla "while" będzie wykonywana do momentu kiedy zmienna "guesses_taken" nie bedzie mniejsza niż 6.
# "While" loop will be executed as long as the value of "guesses_taken" is below 6.
while guesses_taken < 6:
    # Wypisz 'Take a guess.'.
    # Print string 'Take a guess.'.
    print('Take a guess.')
    # Przypisz odpowiedz do zmiennej "guess".
    # Assign user's input to "guess" variable.
    guess = input()
    # Zmień typ wartości zmiennej na liczbę.
    # Change the value of the variable to integer.
    guess = int(guess)
    # Wartość zmiennej zwiekszona o 1.
    # Add 1 to the value of the variable.
    guesses_taken += 1
    # Jeśli "guess" mniejsze niż "number", wykonaj kod z wcięciem pod spodem.
    # When "guess" smaller than "number", execute the indented code below.
    if guess < number:
        # Wypisz 'Your guess is too low.'.
        # Print string 'Your guess is too low.'.
        print('Your guess is too low.')
    # Jeśli "guess" większe niż "number", wykonaj kod z wcięciem pod spodem.
    # When "guess" bigger than "number", execute the indented code below.
    if guess > number:
        # Wypisz 'Your guess is too high.'.
        # Print string 'Your guess is too high.'.
        print('Your guess is too high.')
    # Jeśli "guess" jest równe "number", wykonaj kod z wcięciem pod spodem.
    # When "guess" equals "number", execute the indented code below.
    if guess == number:
        # Wyjdz z pętli.
        # Exit out of the loop.
        break
# Jeśli "guess" jest równe "number", wykonaj kod z wcięciem pod spodem.
# When "guess" equals "number", execute the indented code below.
if guess == number:
    # Zmień typ wartości zmiennej "guesses_taken" na napis.
    # Change type of the value of variable "guesses_taken" to string.
    guesses_taken = str(guesses_taken)
    # Wydrukuj napis ze wartościami zmiennych "myName" i "guesses_taken".
    # Print string with values of the variables "myName" and "guesses_taken".
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')
# Jeśli "guess" nie jest równe "number", wykonaj kod z wcięciem pod spodem.
# When "guess" is not equal to "number", execute the indented code below.
if guess != number:
    # Zmień typ wartości zmiennej "number" na napis.
    # Change type of the value of variable "guesses_taken" to string.
    number = str(number)
    # Wydrukuj napis z wartością zmiennej "number".
    # Print string with the value of the variable "number".
    print('Nope. The number I was thinking of was ' + number)
