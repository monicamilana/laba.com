import requests

class YandexMetrikaAPI:
    """Класс для работы с API Яндекс Метрики с обработкой ошибок и логированием."""
    
    def __init__(self, token, counter_id):
        if not token or not counter_id:
            raise ValueError("Токен и ID счётчика должны быть указаны.")
        self.token = token
        self.counter_id = counter_id
        self.base_url = "https://api-metrika.yandex.net/stat/v1/data"

    def get_data(self, metrics, date1="7daysAgo", date2="today"):
        """Получает данные по указанным метрикам с обработкой ошибок."""
        params = {
            "ids": self.counter_id,
            "metrics": metrics,
            "date1": date1,
            "date2": date2
        }
        headers = {"Authorization": f"OAuth {self.token}"}

        try:
            response = requests.get(self.base_url, params=params, headers=headers)
            response.raise_for_status()  # Проверяем статус ответа
            data = response.json()
            
            if "data" not in data or not data["data"]:
                print("⚠ API вернул пустой ответ или данные недоступны.")
                return None
            
            return data
        except requests.exceptions.RequestException as e:
            print(f"🚨 Ошибка запроса к API: {e}")
            return None

    def get_visits(self):
        """Получает количество визитов на сайт."""
        return self.get_data("ym:s:visits")

    def get_views(self):
        """Получает количество просмотров страниц."""
        return self.get_data("ym:s:pageviews")

    def get_visitors(self):
        """Получает количество уникальных посетителей."""
        return self.get_data("ym:s:users")

# Использование класса
TOKEN = "y0__xCZ9I2JCBji4TYg0NLX3xIbJftfM1Kjiutcmdw8j2JdUBJGQA"
COUNTER_ID = "100820749"

api = YandexMetrikaAPI(TOKEN, COUNTER_ID)

# Проверяем API перед выполнением
metrics = {
    "Визиты": api.get_visits(),
    "Просмотры": api.get_views(),
    "Посетители": api.get_visitors()
}

# Выводим результаты
for metric, value in metrics.items():
    if value:
        print(f"{metric}: {value}")
    else:
        print(f"⚠ Данные {metric} недоступны.")
