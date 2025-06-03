1
try:
    temperature = float(input("Введіть температуру (°C): "))
    humidity = float(input("Введіть вологість (%): "))

    if temperature > 30 and humidity > 70:
        print("Активація системи охолодження")
    else:
        print("Умови нормальні")

except ValueError:
    print("Помилка: введіть числові значення температури та вологості.")

2
try:
    number = int(input("Введіть число від 1 до 100: "))

    if 1 <= number <= 100:
        print("Число в межах допустимого діапазону.")
    else:
        print("Помилковий ввід: число має бути від 1 до 100.")

except ValueError:
    print("Помилка: введено не ціле число.")

3
try:
    age = int(input("Вік кандидата: "))
    experience = int(input("Роки досвіду: "))
    qualification_input = input("Чи має кандидат спеціальну кваліфікацію? (True/False): ")

    # Приводимо введене значення до типу bool
    qualification = qualification_input.strip().lower() == "true"

    if 25 <= age <= 50 and (experience >= 3 or qualification):
        print("Кандидат відповідає вимогам.")
    else:
        print("Кандидат не відповідає вимогам.")

except ValueError:
    print("Помилка: перевірте правильність введених значень.")
