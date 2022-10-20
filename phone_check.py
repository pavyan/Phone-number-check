import requests 

numbers_list = []
correct_count = 0
incorrect_count = 0
no_answer_count = 0
key = '0' #ключ для проверки того, получены ли данные по номеру или нет r'C:\prog\qa_test\numbers.txt'  r'C:\prog\qa_test\numbers_sorted.txt'

input_file_path = input('Введите адрес файла:')
output_file_path = input_file_path[0:-4] + '_sorted.txt'


with open(input_file_path, "r", encoding="utf-8") as numbers_file:
    numbers_lines = numbers_file.read().splitlines() 
    
for i in range(len(numbers_lines)):
    splitter = numbers_lines[i].split(",")
    numbers_list.append(splitter)
    
def get_operator(number):
    response = requests.get(f'http://rosreestr.subnets.ru/?get=num&format=json&num={number}')
    
    if (key in response.json()):
        response_json = response.json()['0']['operator']
    else:
        response_json = 0
                
    return(response_json)
    
#Получаем операторов по номерам через апи
for i in numbers_list:
    i.append(get_operator(i[0]))
    
#Сверяем оператора в файле и из апи
for i in numbers_list:
    if (i[1] == i[2]):
        i.append('1')
        correct_count+= 1
    elif (i[2] == 0):
        i.append('2')
        no_answer_count+= 1
    else:
        i.append('0')
        incorrect_count+= 1
    
print(f'Совпало: {correct_count}, Не совпало: {incorrect_count}, Нет ответа: {no_answer_count}.')

with open(output_file_path, 'w') as fp:
    for i in numbers_list:
        fp.write("%s\n" % i)


