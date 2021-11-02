class MyValueError(Exception):
    @classmethod
    def validate(self, item):
        if item.isdigit():
            return True
        return False


main_list = []
cont = True
while cont:
    line = input('Enter number (numbers by spaces) or q to exit: ').split()
    if line[-1] == 'q':
        line.pop()
        cont = False
    try:
        for el in line:
            if MyValueError.validate(el):
                main_list.append(float(el))
            else:
                raise MyValueError()
    except MyValueError:
        print('Invalid enter')

print(main_list)
