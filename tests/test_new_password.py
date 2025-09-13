import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_password_length():
    length = 25
    password = generate_password(length)
    assert len(password) == length


def test_password_different():
    password_1 = generate_password(10000)
    password_2 = generate_password(10000)
    assert password_1 != password_2