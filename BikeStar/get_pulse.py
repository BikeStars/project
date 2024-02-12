import sqlite3
import requests

url = "https://dt.miet.ru/ppo_it/api/watch"

headers = {
    "x-access-tokens": "az4fvf7nzi1XPIsYiMEu"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data_1 = response.json()
    
    print(data_1)

    if 'data' in data_1 and 'pulse' in data_1['data']:
        pulse_data = data_1['data']['pulse']
    
        min_pulse = pulse_data.get('min')
        max_pulse = pulse_data.get('max')
        avg_pulse = pulse_data.get('avg')
    
        #print("Минимальное значение пульса:", min_pulse)
        #print("Максимальное значение пульса:", max_pulse)
        #print("Среднее значение пульса:", avg_pulse)
        
    else:
        print("Данные о пульсе отсутствуют в словаре.")

else:
    print("Ошибка при запросе данных:", response.status_code)


sqlite_connection = sqlite3.connect('db.sqlite3')
cursor = sqlite_connection.cursor()

sqlite_insert_query = """INSERT INTO routes
                          (id, pulsemid, pulsemin, pulsemax)
                          VALUES
                          (8, avg_pulse, min_pulse, max_pulse);"""
    
count = cursor.execute(sqlite_insert_query)
sqlite_connection.commit()
cursor.close()

if sqlite_connection:
    sqlite_connection.close()