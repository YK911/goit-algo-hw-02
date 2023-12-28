from queue import Queue
from collections import deque
import time

"""
=========
| Task 1
=========
"""
# Створити чергу заявок
queue = Queue()


def generate_request(request_size: 10):
    for item in range(request_size):
        queue.put(item + 1)  # normalize output


def process_request():
    if not queue.empty():
        item = queue.get()
        print(f"Working on {item}")
        time.sleep(1)
        print(f"Finished {item}")
        time.sleep(1)
        queue.task_done()
    else:
        queue.empty


"""
=========
| Task 2
=========
"""


def check_palindrome(param):
    if len(param) == 0:
        return "Empty input"

    cleaned_phrase = param.lower().replace(" ", "")

    chars_dq = deque(cleaned_phrase)
    if chars_dq == deque(reversed(chars_dq)):
        return f"{param} is a palindrome"

    return f"{param} is not a palindrome"


def is_palindrome(param):
    if len(param) == 0:
        return "Empty input"

    cleaned_phrase = param.lower().replace(" ", "")

    chars_dq = deque(cleaned_phrase)
    while len(chars_dq) > 1:
        if chars_dq.popleft() != chars_dq.pop():
            return f"{param} is not a palindrome"

    return f"{param} is a palindrome"


if __name__ == "__main__":
    try:
        # Task 1
        tasks_num = int(input("Enter the number of tasks: "))
        counter = 0

        while counter < tasks_num:
            generate_request(tasks_num)
            process_request()
            counter += 1

        # Task 2
        txt = input("Type your test phrase: ")
        res = check_palindrome(txt)
        print("res: ", res)

        res2 = is_palindrome(txt)
        print("res2: ", res2)

    except ValueError as err:
        print(err)
