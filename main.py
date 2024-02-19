import bcrypt


def check_password(password):
    if len(password) < 8:
        return "Пароль должен содержать не менее 8 символов"

    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Пароль должен содержать и прописные, и строчные буквы"

    if not any(char.isdigit() for char in password):
        return "Пароль должен содержать хотя бы одну цифру"

    return True


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


password = input("Введите пароль: ")

result = check_password(password)
if result == True:
    hashed_password = hash_password(password)
    print("Пароль соответсвует требованиям")
    print("Хэш-значение пароля:", hashed_password)
else:
    print("Пароль не соответствует требованиям сложности.")
    print("Причина:", result)