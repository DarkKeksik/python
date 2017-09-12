import requests, time, vk, vk_api, random, time

idNumber = []
# Проверяем не писали ли раньше сообщения
vkIdNumber = open("logVk.txt", "r")
for i in vkIdNumber:
    idNumber.append(i)
vkIdNumber.close()


vk = vk_api.VkApi(login = '89244275834', password = 'LoniPoni4152123321')
vk.auth()

# Шаблоны сообщений
dictFemale = {
    "1": """
        This is message Female
    """
}
dictMale = {
    "1": """
        This is message Male
    """        
    }

# Функция "написать сообщение"
def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})


# Начинаем хаос _____________________________________________________

# Массив из счастливчиков
luckUser = []

# Создаем массив из 20 пользователей (у вк ограничение, можно написать только 20 людям, которые не находятся в друзьях) и парсим их пол (сразу и проверим существование странички)
for i in range (0, 19, 1):

    luckUser.append(random.randint(900, 9000000))
    informUser = requests.get("https://api.vk.com/method/users.get", params={'user_ids':i+1, 'fields':'sex'})
    informUser = informUser.json()
    informUser = informUser["response"][0]
    
    if informUser["sex"] == 1:
        randomMessage = str(random.randint(1, len(dictFemale)))
        write_msg(luckUser[i], dictFemale[randomMessage])
    elif informUser["sex"] == 2:
        randomMessage = str(random.randint(1, len(dictMale)))
        write_msg(luckUser[i], dictMale[randomMessage])
        
    print ("Сообщений отослали уже: ", i)
    time.sleep( random.randint(66, 104) )

    vkIdNumber = str(vkIdNumber)

print("Готово, поздравляю тебя создатель ^^")
