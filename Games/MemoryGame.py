import tkinter
import random

# Generates sequence of random numbers by difficulty level
def generate_sequence(difficulty):
    random_list = []
    for number in range(1, int(difficulty+1)):
        ran_num = random.randint(1, 101)
        random_list.append(ran_num)
    return random_list

# prompt to the user a list of number for 0.7 seconds by difficulty level
def prompt_list(nums):
    window = tkinter.Tk()
    window.title('Memory Game')
    label = tkinter.Label(window, text=nums, font=('Arial Bold', 20))
    label.grid(column=0, row=2)
    label.after(700, lambda: label.config(text='Remember the numbers?\n Type them now!', font=('Arial', 10)))
    btn = tkinter.Button(window, text='Close', command=window.destroy)
    btn.grid(column=0, row=0)
    window.geometry('200x100')
    window.attributes("-topmost", True)
    window.mainloop()

# get list from user
def get_list_from_user(nums):
    user_list = []
    for number in range(len(nums)):
        while True:
            try:
                temp_num = int(input(f'Enter your {number+1} number:'))
                if 101 >= temp_num >= 1:
                    user_list.append(temp_num)
                    break
                else:
                    print('Value should be between 1-101 !')
            except ValueError:
                print('Value should be a number')
    return user_list

# comparing
def is_list_equal(user_list, random_list):
    if user_list == random_list:
        return True
    else:
        return False

# call all the functions above
def play_memory_game(dif_level):
    call_generate = generate_sequence(dif_level)
    call_prompt = prompt_list(call_generate)
    call_user_list = get_list_from_user(call_generate)
    result = is_list_equal(call_user_list,call_generate)
    if result == True:
        print('You are the winner of Memory Game !')
    else:
        print('You lost ..Try again ')
    return result


# x = play_memory_game()

