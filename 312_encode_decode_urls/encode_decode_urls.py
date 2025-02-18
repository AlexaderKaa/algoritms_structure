python
import random
import string

class MarsURLEncoder:
    def __init__(self):
        self.url_storage = {}  # Словарь для хранения пар (зашифрованная ссылка: исходная)

    def generate_hash(self, length=6):
        # Набор символов для генерации хеша
        characters = string.ascii_letters + string.digits
        while True:
            # Генерация хеша
            generated_hash = ''.join(random.choice(characters) for _ in range(length))
            # Проверка на уникальность
            if generated_hash not in self.url_storage:
                return generated_hash

    def encode(self, original_url):
        # Генерируем уникальный хеш
        unique_hash = self.generate_hash()
        # Формируем зашифрованную ссылку
        encrypted_url = f'https://ma.rs/{unique_hash}'
        # Сохраняем пару (зашифрованная ссылка: исходная) в словаре
        self.url_storage[encrypted_url] = original_url
        return encrypted_url

    def decode(self, encrypted_url):
        # Проверяем, существует ли зашифрованная ссылка в словаре
        if encrypted_url in self.url_storage:
            return self.url_storage[encrypted_url]  # Возвращаем исходную ссылку
        else:
            raise ValueError("Данная зашифрованная ссылка не существует.")

# Пример использования
encoder = MarsURLEncoder()

# Шифрование ссылки
original_link = "https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html"
encrypted_link = encoder.encode(original_link)
print(f"Зашифрованная ссылка: {encrypted_link}")

# Расшифровка ссылки
decoded_link = encoder.decode(encrypted_link)
print(f"Исходная ссылка: {decoded_link}")