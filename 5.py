import os
import re

def task1():
    # в папке test найти все файлы filenames вывести колличество
    counter = 0
    for root, folder, file in os.walk('test'):
        for filename in file:
            if 'filenames' in filename:
                counter += 1
    print(counter)
    


def task2():
    email_set = set()
    for root, folder, files in os.walk('test'):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                for line in f:
                    emails = re.findall(r"^(?:(?:[\w\.\-_]+@[\w\d]+(?:\.[\w]{2,6})+)[,;]?\s?)+$", line[:-1])
                    email_set.update(emails)                   
    print(email_set)
                        
    
    


def main():
    task1()
    task2()
    # дополнительно: придумать механизм оптимизации 2-й задачи


if __name__ == '__main__':
    main()
