import threading
import time
from time import sleep

all_files = [10, 30, 200, 100]

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = time.time()

for i in range(4):
    write_words(all_files[i], f'example{i + 1}.txt')

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time} секунд")

start_time_threads = time.time()

threads = []

for i in range(4):
    thread = threading.Thread(target=write_words, args=(all_files[i], f'example{i + 5}.txt'))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Все потоки завершены.")

end_time_threads = time.time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads} секунд")