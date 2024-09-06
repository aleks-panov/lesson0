team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
print("В команде Мастера кода участников: %s !" %team1_num)
print("В команде Волшебники данных участников: %s !" %team2_num)
print("Итого сегодня в командах участников: %(name1)s и %(name2)s !" % {"name1":team1_num, "name2":team2_num})
print("Команда Мастера кода решила задач: {}".format(score_1))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Мастера кода решили задачи за {}".format(team1_time))
print("Волшебники данных решили задачи за {}" . format(team2_time))
print(f"Команды решили {score_1} и {score_2} задач")
print(f"{challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")



