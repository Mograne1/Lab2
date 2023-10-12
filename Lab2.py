def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

decimal_number = int(input("Введіть десяткове число: "))

conversion_type = input("Оберіть систему числення (б - бінарна, в - вісімкова, ш - шістнадцяткова): ")

if conversion_type == 'б':
    result = decimal_to_binary(decimal_number)
    print(f"Результат в бінарній системі: {result}")
elif conversion_type == 'в':
    result = decimal_to_octal(decimal_number)
    print(f"Результат в вісімковій системі: {result}")
elif conversion_type == 'ш':
    result = decimal_to_hexadecimal(decimal_number)
    print(f"Результат в шістнадцятковій системі: {result}")
else:
    print("Невірний вибір системи числення. Виберіть 'б', 'в' або 'ш'.")
