import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_password_complexity():
    """Тест, что пароль содержит букву, цифру и спецсимвол"""
    password = generate_password(20)
    letter = any(char in string.ascii_letters for char in password)
    digit = any(char in string.digits for char in password)
    punct = any(char in string.punctuation for char in password)
    assert letter and digit and punct

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""