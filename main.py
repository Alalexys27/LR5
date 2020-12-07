import os
import math
import timeit
import time
import sys
import signal
from sys import argv
import multiprocessing as mp


def method(n: int, i: int):
    print(f">> Запуск {i} процесса")
    fname = f"Proc_{i}.txt"
    # создание массива с n+1 количеством элементов
    list0 = [False] * (n+1)
    with open(fname, "w", encoding='utf-8') as file:
        for x in list0:
            s = str(x) + '\n'
            file.write(s) 
            
    a = True
    print("\n>> Вычисления!")
    for x in range(i+1,n+1,3):
        for y in range(1,int(math.sqrt(n)) + 1):
            if x != y and y != 1:
                if x % y == 0:
                    a = False
                    break
        if a == True:
            list0[x] = True
        a = True

    with open(fname, "w", encoding='utf-8') as file:
            for x in list0:
                s = str(x) + '\n'
                file.write(s)
    
    print(f">> Завершение {i} процесса\n")
    
def read_files():
    fname1="Proc_1.txt"
    fname2="Proc_2.txt"
    fname3="Proc_3.txt"
    #fname4="Proc_4.txt

    with open(fname1,'r',encoding='utf-8') as f1:
        text = f1.read()
        val_1 = text.split("\n")
    with open(fname2,'r',encoding='utf-8') as f2:
        text = f2.read()
        val_2 = text.split("\n")
    with open(fname3,'r',encoding='utf-8') as f3:
        text = f3.read()
        val_3 = text.split("\n")
        '''
    with open(fname4,'r',encoding='utf-8') as f4:
        text = f4.read()
        val_4 = text.split("\n")
        '''
    values=[False]*len(val_1)
    for i in range(0,len(val_1)):
        if val_1[i]=="False":
            a=False
        else: a=True
        if val_2[i]=="False":
            b=False
        else: b=True
        if val_3[i]=="False":
            c=False
        else: c=True
        '''
        if val_4[i]=="False":
            d=False
        else: d=True
        '''
        values[i]=(a+b+c)%2

    val_all=[False]*len(values)
    # Функция enumerate создает объект из двух элементов [index, item]
    for index, x in enumerate(values):
        if x==1:
            val_all[index]=index
    
    # Текущая директроия
    fname = os.getcwd()
    # Удаление временных файлов
    os.unlink(os.path.join(fname, fname1))
    os.unlink(os.path.join(fname, fname2))
    os.unlink(os.path.join(fname, fname3))
    #os.unlink(os.path.join(fname, fname4))
    return val_all

def end():
    raise KeyboardInterrupt
# Обратока сигналов. SIGINT - прерывание с клавиатуры , SIG_IGN - игнорировать сигнал.
def init_work():
    signal.signal(signal.SIGINT, end)

# Main функция
if __name__ == '__main__':
    # Проверка на наличие аргумента
    try:
        if int(argv[1]) > 0:
            pass
        elif int(argv[1]) <= 0:
            raise Exception
        else:
            raise Exception
        limit = int(argv[1])
        try:
            # Запуск 3х процессов
            with mp.Pool(3, init_work) as pool:
                pool.starmap(method,iterable=[[limit, 1],[limit, 2],[limit, 3]],) #[limit, 4]],)
                
            # Чтение из временых файлов
            list1 = read_files()
            
            # .pop возвращает элемент удаляя последний из списка, т.к. не указан индекс в ()
            # Удаление лишних значений в списке
            while len(list1)>limit:
                list1.pop()
            
            result=list()
            # 'False' - вычеркнутые значения. Получаем только простые числа из списка, дописываем в конец result.
            for index, elem in enumerate(list1):
                if elem is not False:
                    result.append(elem)

            result.sort()

            print("\n---------------------------------\n>> Начата запись в результирующий файл!")

            # Запись в результирующий файл
            with open("result.txt", "w", encoding='utf-8') as file:
                for i in result:
                    str0 = ''+str(i)+"\n"
                    file.write(str0)
        except KeyboardInterrupt:   
            print(">> Программа остановлена!")
        
        print(f">> Программа завершена. Время работы:{timeit.default_timer()} сек.\n")

    # Обработка исключений
    except FileNotFoundError:
        pass
    except Exception:
        print(">> Укажите аргумент!")
    except KeyboardInterrupt:
        print(">> Программа остановлена!")
        pool.terminate()
    except:
        print(">> Некорректное завершение!")

