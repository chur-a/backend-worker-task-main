import os


def black_book(page: int):
    status_code = os.system(f"./black-book -n {page}")
    return True if status_code == 0 else False


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_book) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        black_box возвращает True, если страница есть в книге
                  возвращает False, если страницы нет в книге.
    
    
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    last_number = 10000000
    first_number = 0
    while last_number - first_number > 1:
        search_number = (last_number + first_number) // 2
        if black_book(search_number):
            first_number = search_number
        else:
            last_number = search_number
    if black_book(last_number):
        print(last_number)
    else:
        print(first_number)


if __name__ == '__main__':
    # тут явно нужен алгоритм
    main()
