# count=1
# while count<=10:
#     if count==6:
#         break
#     print(count)
#     count+=1


# count=0
# while count<10:
#     count+=1
#     if count==6:
#         continue
#     print(count)
    
      

    # factorial:-

# a=int(input("enter a number"))
# factorial=1
# for i in range(1,a+1):
#    factorial=factorial*i
# print(factorial)    




# import random

# def choose_word():
#     words = ['python', 'java', 'ruby', 'javascript', 'php', 'swift', 'kotlin', 'html', 'css']
#     return random.choice(words)

# def display_word(word, guessed_letters):
#     displayed_word = ''
#     for letter in word:
#         if letter in guessed_letters:
#             displayed_word += letter + ' '
#         else:
#             displayed_word += '_ '
#     return displayed_word.strip()

# def hangman():
#     print("Welcome to Hangman!")
#     word = choose_word()
#     guessed_letters = []
    # attempts = 6

    # while True:
    #     print("\nAttempts left:", attempts)
    #     displayed_word = display_word(word, guessed_letters)
    #     print(displayed_word)

    #     if '_' not in displayed_word:
    #         print("\nCongratulations! You guessed the word:", word)
    #         break

    #     guess = input("Guess a letter: ").lower()

    #     if guess in guessed_letters:
    #         print("You already guessed that letter!")
    #         continue

    #     guessed_letters.append(guess)

    #     if guess not in word:
    #         attempts -= 1
    #         print("Wrong guess!")

    #     if attempts == 0:
    #         print("\nGame over! The word was:", word)
    #         break

    # play_again = input("\nDo you want to play again? (yes/no): ").lower()
    # if play_again == 'yes':
    #     hangman()
    # else:
    #     print("Thanks for playing!")

        



# import Calendar

# def print_calendar(year, month):
#     # Print the calendar for the given year and month
#     cal = calendar.month(year, month)
#     print(cal)

# # Specify the year and months
# year = 2024
# months = [4, 11]  # April and November

# # Print calendars for each month
# for month in months:
#     print(f"Calendar for {calendar.month_name[month]} {year}:")
#     print_calendar(year, month)
#     print("\n")





