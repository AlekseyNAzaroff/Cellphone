import pickle
import cellphone

FILENAME = 'cellphones.dat'


def main():
    end_of_file = False
    input_file = open(FILENAME, 'rb')
    while not end_of_file:
        try:
            phone = pickle.load(input_file)
            display_data(phone)
        except EOFError:
            end_of_file = True

    input_file.close()


def display_data(phone):
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Модель: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price():,.2f}')


if __name__ == '__main__':
    main()
