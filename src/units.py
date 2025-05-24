import json



def get_info_about_transactions(path_to_file: str) -> dict:
    """Функция принимает путь к файлу с транзакциями и возвращает их"""
    try:
        with open(path_to_file) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print ("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []

if __name__ == "__main__":
    file = r"eugen\PycharmProjects\WidgetForSuccessfulOperations\data\operations.json"
    print(get_info_about_transactions(file))
