import json
import sys

def count_questions(data: dict):
    counter = 0
    for round_ in data['game']['rounds']:
        counter += len(round_['questions'])
    print(counter)


def print_right_answers(data: dict):
    correct_answers = []
    for round_ in data['game']['rounds']:
        for question in round_['questions']:
            correct_answers.append(question['correct_answer'])
    print(correct_answers)


def print_max_answer_time(data: dict):
    maximum_time = float('-inf')
    for round_ in data['game']['rounds']:
        maximum_time = max(round_['settings'].get('time_to_answer'), maximum_time)
        for question in round_['questions']:
            maximum_time = max(question.get('time_to_answer', 0), maximum_time)
    print(maximum_time)


def main(file):
    data = json.load(file) # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        main(f)

