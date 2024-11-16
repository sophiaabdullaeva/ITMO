import maintask_and_extratask3
import extratask1
import time
start1 = time.time()
for i in range(1, 100):
    maintask_and_extratask3.json_to_yaml()
my_method = time.time() - start1
print(f"Время выполнения ручного перевода из JSON в YAML: {my_method} секунд")
start2 = time.time()
for j in range(1, 100):
    extratask1.json_to_yaml_with_lib()
lib_method = time.time() - start2
print(f"Время выполнения перевода из JSON в YAML с помощью библиотеки: {lib_method} секунд")
print(f"Ручной перевод из JSON в YAML быстрее библиотеки в {lib_method/my_method} раз")
