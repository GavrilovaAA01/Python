Inform_total = 1.44 #Информационный объем дискеты
Number_of_pages = 100 #Количество страниц в одной книге
Number_of_lines = 50 #Число строк на одной странице
Number_of_characters = 25 #Количество символов в одной строке
Character = 4 #Вес кода одного символа
# TODO Найдите количество книг, которое можно разместить на дискете
Weight_of_one_book_B = Character * Number_of_lines * Number_of_characters * Number_of_pages #Вес одной книги в байтах
from_bytes_to_Mb = Weight_of_one_book_B / 1024 / 1024 #Переводим из байтов в мегабайты
number_of_books = round(Inform_total/ from_bytes_to_Mb)
print("Количество книг, помещающихся на дискету:", number_of_books)
