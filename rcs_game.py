import random


def get_user_choice():
    print("\nWelcome to Rock Paper Scissor!!!")
    user_choice = input("Pick your choice rock, paper or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'You win the round!'
    else:
        return 'You lose the round!'


def display_result(user_choice, computer_choice, result):
    print(f'You chose: {user_choice}')
    print(f'Computer chose: {computer_choice}')
    print(result)


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    return result


def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_game()

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        print(f'Score - Your: {user_score}, Computer: {computer_score}')

        play_again = input('Do you want to play the game again? (yes/no): ').lower()
        if play_again != 'yes':
            print('Thank you for playing the game! Goodbye.')
            break


if __name__ == "__main__":
    main()
