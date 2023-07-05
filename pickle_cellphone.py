import cellphone
import pickle


FILENAME = 'cellphones.dat'

def main():
    again = 'д'
    output_file = open(FILENAME, 'wb')

    while again.lower() == 'д':
        man = input('Введите производителя: ')
        mod = input('Введите модель: ')
        retail = float(input('Введите розничную цену: '))
        phone = cellphone.CellPhone(man, mod, retail)
        pickle.dump(phone, output_file)
        again = input('Хотите ввести ещё один элемент? (д/н): ')

    output_file.close()
    print(f'Данные записаны в {FILENAME}')



if __name__ == '__main__':
    main()
