
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import datetime
from datetime import date
from posts_db import Datebase_post

db_post = Datebase_post('database2.db')

btnProfile = KeyboardButton ('Профиль')
btnurl = KeyboardButton ('Полезные ссылки')
btPod = KeyboardButton ('Задать вопрос')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile, btnurl, btPod)


btnMedia = KeyboardButton("Медиакоммуникации в Москве")
btnJur = KeyboardButton("Журналистика")
btnMedia_Jur = KeyboardButton("Буду поступать на обе в Москве")
btnMediaSpb = KeyboardButton("Медиакоммуникации в Питере")
btnAll = KeyboardButton("Буду поступать на все")

ProgMenu = ReplyKeyboardMarkup(resize_keyboard = True)
ProgMenu.add(btnMedia, btnJur, btnMedia_Jur, btnMediaSpb,btnAll)


btnNext = KeyboardButton("Продолжить")

Next = ReplyKeyboardMarkup(resize_keyboard = True)
Next.add(btnNext)


btnProfLast = KeyboardButton("Назад в меню")
btnProNew = KeyboardButton("Заполнить заново")

Prof = ReplyKeyboardMarkup(resize_keyboard = True)
Prof.add(btnProfLast, btnProNew)


btnPost = KeyboardButton("Пост")
btnPostBtn = KeyboardButton("Пост с кнопками")
btnExAdm = KeyboardButton("Выйти из меню админа")
btnEditPost = KeyboardButton("Редактировать или удалить пост")

AdmMenu = ReplyKeyboardMarkup(resize_keyboard = True)
AdmMenu.add(btnPost, btnExAdm, btnEditPost)


btnMedia_Adm = KeyboardButton("Медиакоммуникации в Москве_")
btnJur_Adm = KeyboardButton("Журналистика_")
btnMedia_Jur_Adm = KeyboardButton("Всем_")
btnMedia_allMsk = KeyboardButton("Всем в Москве_")
btnMedia_Spb = KeyboardButton("Медиакоммуникации в Питере_")
#btnNowYear_Adm = KeyboardButton("Абитуриенты этого года_")
#btnNowYear2022_Adm = KeyboardButton("Абитуриенты 2022 года_")
#btnOs = KeyboardButton("Особый пост_")
#btnOs2 = KeyboardButton("Особый пост с кнопками_")

btnMedia_Adm = KeyboardButton("Медиакоммуникации в Москве_")
btnJur_Adm = KeyboardButton("Журналистика_")
btnMedia_Jur_Adm = KeyboardButton("Всем_")
btnMedia_allMsk = KeyboardButton("Всем в Москве_")
btnMedia_Spb = KeyboardButton("Медиакоммуникации в Питере_")
btnPostPrnt = KeyboardButton("Родители_")

AdmPostMenu = ReplyKeyboardMarkup(resize_keyboard = True)
AdmPostMenu.add(btnMedia_Adm, btnJur_Adm, btnMedia_Jur_Adm,
                btnMedia_allMsk, btnMedia_Spb, btnPostPrnt) #, btnNowYear_Adm, btnNowYear2022_Adm) #, btnOs, btnOs2)



btnAdmPostProgBack = KeyboardButton("Назад к выбору факультета")

AdmPostProgBack = ReplyKeyboardMarkup(resize_keyboard = True)
AdmPostProgBack.add(btnAdmPostProgBack)



dt_now = datetime.datetime.now()
september = datetime.datetime(int(dt_now.year), 9, 1)
#print(dt_now)
#print(september)
if dt_now > september:
    year1 = str(int(dt_now.year)+1)
    year2 = str(int(year1)+1)
    year2_2 = str(int(year1) - 1)
else:
    year1 = str(int(dt_now.year))
    year2 = str(int(year1)+1)
    year2_2 = str(int(year1) + 1)

btnYEAR_1 = KeyboardButton(year1)
btnYEAR_2 = KeyboardButton(year2)
btnYEAR_P = KeyboardButton("Позже")

YEAR_BTN = ReplyKeyboardMarkup(resize_keyboard = True)
YEAR_BTN.add(btnYEAR_1, btnYEAR_2, btnYEAR_P)


btnAdmPostYear1 = KeyboardButton(year1 + '_')
btnAdmPostYear2 = KeyboardButton(year2_2 + '_')
btnAdmPostYearAll = ('Все года_')
AdmPostMenuYear = ReplyKeyboardMarkup(resize_keyboard = True)
AdmPostMenuYear.add(btnAdmPostYear1, btnAdmPostYear2, btnAdmPostYearAll)



btnRestYe = KeyboardButton("Да")
btnResrNo = KeyboardButton("Нет")

RestYN = ReplyKeyboardMarkup(resize_keyboard = True)
RestYN.add(btnRestYe, btnResrNo)


btnStart = KeyboardButton('/start')

Start_ = ReplyKeyboardMarkup(resize_keyboard = True)
Start_.add(btnStart)


btnCheckAdminNo = KeyboardButton('no')
MainAdmin = ReplyKeyboardMarkup(resize_keyboard = True)
MainAdmin.add(btnCheckAdminNo)


InlBtnForPost2022 = InlineKeyboardMarkup()
InlBtnYes1 = InlineKeyboardButton(text = 'Да', callback_data = 'yes_2022')
InlBtnNo1 = InlineKeyboardButton(text = 'Нет', callback_data = 'no_2022')
InlBtnForPost2022.add(InlBtnYes1, InlBtnNo1)

InlBtnForPost2022_2 = InlineKeyboardMarkup()
InlBtnYes1_2 = InlineKeyboardButton(text = 'Планирую перепоступать', callback_data = 'ye_2022')
InlBtnNo1_2 = InlineKeyboardButton(text = 'Поступил(а) в другой вуз', callback_data = 'another_uni_2022')
InlBtnForPost2022_2.add(InlBtnYes1_2)
InlBtnForPost2022_2.add(InlBtnNo1_2)

btnAbitur = KeyboardButton("Абитуриент")
btnPrnt = KeyboardButton("Родитель")
PrntOrAbit = ReplyKeyboardMarkup(resize_keyboard = True)
PrntOrAbit.add(btnAbitur, btnPrnt)

def Update_Edit_mark():
    EditPost = ReplyKeyboardMarkup(resize_keyboard=True)
    EditPost.add(KeyboardButton(db_post.get_post_date(1)),
           KeyboardButton(db_post.get_post_date(2)),
           KeyboardButton(db_post.get_post_date(3)),
           KeyboardButton(db_post.get_post_date(4)),
           KeyboardButton(db_post.get_post_date(5)))
    return EditPost


#EditPost = ReplyKeyboardMarkup(resize_keyboard = True)
#EditPost.add(Update_Edit_mark()[0], Update_Edit_mark()[1],
 #            Update_Edit_mark()[2], Update_Edit_mark()[3], Update_Edit_mark()[4])

btnEditPost2_Edit = KeyboardButton("Редактиорвать этот пост")
btnEditPost2_Del = KeyboardButton("Удалить этот пост")
btnEditPost2_Back = KeyboardButton("Вернуться к выбору")
EditPost2 = ReplyKeyboardMarkup(resize_keyboard = True)
EditPost2.add(btnEditPost2_Edit, btnEditPost2_Del, btnEditPost2_Back)

"""
InlBtnForPost1 = InlineKeyboardMarkup()
InlBtnYes1 = InlineKeyboardButton(text = 'Да', callback_data = 'yes1')
InlBtnNo1 = InlineKeyboardButton(text = 'Нет', callback_data = 'no1')
InlBtnForPost1.add(InlBtnYes1, InlBtnNo1)

InlBtnForPost2 = InlineKeyboardMarkup()
InlBtnYes2 = InlineKeyboardButton(text = 'Да', callback_data = 'yes2')
InlBtnNo2 = InlineKeyboardButton(text = 'Нет', callback_data = 'no2')
InlBtnForPost2.add(InlBtnYes2, InlBtnNo2)
"""

'''
def inline_but(in_str: str, mes_id):
    InlBtnForPost = InlineKeyboardMarkup()
    str_ = in_str.split("\n\n")
    str_[len(str_)-1] = str_[-1][:-1]

    f_name_main = 'Polls/' + str(mes_id) + '.txt'
    f_main = open(f_name_main, 'w+')
    for i in range(len(str_)):
        InlBut = InlineKeyboardButton(text = str_[i], callback_data = str(i))
        InlBtnForPost.add(InlBut)
        name_f ='Polls/' + str(mes_id) + '_' + str_[i] + '.txt'
        f = open(name_f, 'w+')
        f.close()
    f_main.close()
    return InlBtnForPost
'''
