# Ограничение ввода только цифрами
def validate_input_only_numbers(in_str, acttyp):
    if acttyp == '1':
        return in_str.isdigit()
    return True

# Ограничение ввода только буквами
def validate_input_only_letters(in_str, acttyp):
    if acttyp == '1':
        return in_str[-1].isalpha()
    return True
