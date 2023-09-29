from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from db import Datebase
from posts_db import Datebase_post
import config
import numbers
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_broadcaster import MessageBroadcaster
import datetime
from datetime import date
from aiogram import exceptions


bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

db = Datebase('database2_test.db')
db_post = Datebase_post('database2_test.db')
async def message_handler(msg: types.Message): #Photo MES
    if db.get_adm_post(msg.from_user.id) == '1' and db.get_signup(msg.from_user.id) == 'admin_true':

        # Btn_str = ''
        # with open('Inl_Btn.txt', 'r') as f:
        #     for i in f:
        #         Btn_str = Btn_str + i + '\n'
        # if Btn_str != '\n':
        #     open('Inl_Btn.txt', 'w').close()
        #     msg.reply_markup = nav.inline_but(Btn_str, msg.message_id)


        with open('Post_groups.txt', 'r') as f:
            year_post = f.read(4)
        db_post.update_tables()
        if year_post == '1111':

            if db.get_programm(msg.from_user.id) == 'Всем':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                users_1 = db.get_user_id("Журналистка")
                users_2 = db.get_user_id("Медиакоммуникации в Москве")
                users_3 = db.get_user_id("Буду поступать на обе в Москве")
                users_4 = db.get_user_id("Медиакоммуникации в Питере")
                users_5 = db.get_user_id("Буду поступать на все")
                #RepMark = nav.inline_but(msg.caption)
                #msg.reply_markup = RepMark
                await MessageBroadcaster(users_1, msg).run()
                await MessageBroadcaster(users_2, msg).run()
                await MessageBroadcaster(users_3, msg).run()
                await MessageBroadcaster(users_4, msg).run()
                await MessageBroadcaster(users_5, msg).run()

            elif db.get_programm(msg.from_user.id) == 'Особый':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                users_ = [1354467245, 1972673513, 299561163, 728131343, 730086167,
                          1028033536, 670838339, 807748810, 585705579, 387863611,
                          1145676386, 880544715, 1512704472, 627498868, 1003015874,
                          559567576, 2041741153, 917537526, 399517539, 330820504, 807686789, 542703639]
                users_ = [484623073]
                print('ok')
                await MessageBroadcaster(users_, msg).run()

            elif db.get_programm(msg.from_user.id) == 'Родители':
                db.set_adm_post(msg.from_user.id, 0)
                users = db.get_user_id_prnts()
                me_ = []
                me_.append(msg.from_user.id)
                await MessageBroadcaster(me_, msg).run()
                await MessageBroadcaster(users, msg).run()

                '''
            elif db.get_programm(msg.from_user.id) == 'Особый пост с кнопками':
                msg.reply_markup = nav.InlBtnForPost2
                mas_id = []
                with open('Polls/poll_1_no.txt') as f:
                    for i in f:
                        mas_id.append(i[:-1])
                mas_id.append(str(msg.from_user.id))
                print(mas_id)
                #await MessageBroadcaster(mas_id, msg).run()
    
            elif db.get_programm(msg.from_user.id) == 'Особый пост':
                mas_id = []
                with open('Polls/poll_2_no.txt') as f:
                    for i in f:
                        mas_id.append(i[:-1])
                mas_id.append(str(msg.from_user.id))
                print(mas_id)
                await MessageBroadcaster(mas_id, msg).run()
                '''

            elif db.get_programm(msg.from_user.id) == 'Всем в Москве':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                users_1 = db.get_user_id("Журналистка")
                users_2 = db.get_user_id("Буду поступать на обе в Москве")
                users_3 = db.get_user_id("Медиакоммуникации в Москве")
                users_4 = db.get_user_id("Буду поступать на все")
                await MessageBroadcaster(users_1, msg).run()
                await MessageBroadcaster(users_2, msg).run()
                await MessageBroadcaster(users_3, msg).run()
                await MessageBroadcaster(users_4, msg).run()

            elif db.get_programm(msg.from_user.id) == 'Медиакоммуникации в Питере':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                db.set_programm(msg.from_user.id, "Медиакоммуникации в Питере")
                users = db.get_user_id(db.get_programm(msg.from_user.id))
                users_ = db.get_user_id("Буду поступать на все")
                await MessageBroadcaster(users, msg).run()
                await MessageBroadcaster(users_, msg).run()

            elif db.get_programm(msg.from_user.id) == "Новый сегмент 240-344":
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                mas_mail = []
                with open('mail_4_jul.txt') as f:
                    for i in f:
                        if '\n' in i:
                            id_mail = db.get_user_id_mail(i[:-1])
                        else:
                            id_mail = db.get_user_id_mail(i)
                        if len(id_mail) != 0:
                            mas_mail.append(id_mail[0])
                mas_mail.append(732709582)
                mas_mail.append(484623073)
                await MessageBroadcaster(mas_mail, msg).run()

                '''
            elif db.get_programm(msg.from_user.id) == 'Абитуриенты этого года':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                users = db.get_user_id_year()
                await MessageBroadcaster(users, msg).run()

            elif db.get_programm(msg.from_user.id) == 'Абитуриенты 2022 года':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                users = db.get_user_id_year_2022()
                msg.reply_markup = nav.InlBtnForPost2022
                await MessageBroadcaster(users, msg).run()
                '''

            else:
                db.set_adm_post(msg.from_user.id, 0)
                users = db.get_user_id(db.get_programm(msg.from_user.id))
                users_ = db.get_user_id("Буду поступать на все")
                users__ = db.get_user_id("Буду поступать на обе в Москве")
                await MessageBroadcaster(users, msg).run()
                await MessageBroadcaster(users_, msg).run()
                await MessageBroadcaster(users__, msg).run()
        else:
            if db.get_programm(msg.from_user.id) == 'Всем':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                users_1 = db.get_user_id_and_year("Журналистка", year_post)
                users_2 = db.get_user_id_and_year("Медиакоммуникации в Москве", year_post)
                users_3 = db.get_user_id_and_year("Буду поступать на обе в Москве", year_post)
                users_4 = db.get_user_id_and_year("Медиакоммуникации в Питере", year_post)
                users_5 = db.get_user_id_and_year("Буду поступать на все", year_post)
                # RepMark = nav.inline_but(msg.caption)
                # msg.reply_markup = RepMark
                await MessageBroadcaster(users_1, msg).run()
                await MessageBroadcaster(users_2, msg).run()
                await MessageBroadcaster(users_3, msg).run()
                await MessageBroadcaster(users_4, msg).run()
                await MessageBroadcaster(users_5, msg).run()
                # print('da')

            elif db.get_programm(msg.from_user.id) == 'Родители':
                db.set_adm_post(msg.from_user.id, 0)
                users = db.get_user_id_prnts_and_year(year_post)
                me_ = []
                me_.append(msg.from_user.id)
                await MessageBroadcaster(me_, msg).run()
                await MessageBroadcaster(users, msg).run()


            elif db.get_programm(msg.from_user.id) == "Новый сегмент 240-344":
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                mas_mail = []
                with open('mail_4_jul.txt') as f:
                    for i in f:
                        if '\n' in i:
                            id_mail = db.get_user_id_mail(i[:-1])
                        else:
                            id_mail = db.get_user_id_mail(i)
                        if len(id_mail) != 0:
                            mas_mail.append(id_mail[0])
                mas_mail.append(732709582)
                mas_mail.append(484623073)
                await MessageBroadcaster(mas_mail, msg).run()


            elif db.get_programm(msg.from_user.id) == 'Всем в Москве':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                users_1 = db.get_user_id_and_year("Журналистка", year_post)
                users_2 = db.get_user_id_and_year("Буду поступать на обе в Москве", year_post)
                users_3 = db.get_user_id_and_year("Медиакоммуникации в Москве", year_post)
                users_4 = db.get_user_id_and_year("Буду поступать на все", year_post)
                await MessageBroadcaster(users_1, msg).run()
                await MessageBroadcaster(users_2, msg).run()
                await MessageBroadcaster(users_3, msg).run()
                await MessageBroadcaster(users_4, msg).run()

            elif db.get_programm(msg.from_user.id) == 'Медиакоммуникации в Питере':
                db.set_adm_post(msg.from_user.id, 0)
                db.set_programm(msg.from_user.id, "Буду поступать на все")
                db.set_programm(msg.from_user.id, "Медиакоммуникации в Питере")
                users = db.get_user_id_and_year("Медиакоммуникации в Питере", year_post)
                users_ = db.get_user_id_and_year("Буду поступать на все", year_post)
                await MessageBroadcaster(users, msg).run()
                await MessageBroadcaster(users_, msg).run()

            else:
                db.set_adm_post(msg.from_user.id, 0)
                users = db.get_user_id_and_year(db.get_programm(msg.from_user.id), year_post)
                users_ = db.get_user_id_and_year("Буду поступать на все", year_post)
                users__ = db.get_user_id_and_year("Буду поступать на обе в Москве", year_post)
                await MessageBroadcaster(users, msg).run()
                await MessageBroadcaster(users_, msg).run()
                await MessageBroadcaster(users__, msg).run()
        print("Photo MES")
        print(msg.caption)
        db_post.add_post(msg.caption, msg.from_user.id)


'''
async def message_handler_all(msg: types.Message):
    db.set_adm_post(message.from_user.id, 0)
    users = db.get_user_id(db.get_programm(msg.from_user.id))  # Your users list
    await MessageBroadcaster(users, msg).run()
'''

@dp.message_handler(commands = ['entry_admin'])
async def entry(message: types.Message):
    if str(message.chat.id) == str(732709582): #id главного админа
        await bot.send_message(message.chat.id, "Введите id пользователя, чтобы предоставить"
                                                " ему доступ в кабинет админа или 'no', чтобы"
                                                " отказать в доступе", reply_markup = nav.MainAdmin)
        db.set_signup(message.chat.id, "admin_check")
    else:
        await bot.send_message(message.from_user.id, "У нас нет такой команды. Нажмите на /help, чтобы посмотреть опции.\n\n "
                                                     "Если вам нужна помощь, напишите в поддержку: @hsemediasupport")

@dp.message_handler(commands = ['restart'])
async def rest(message: types.Message):
    await bot.send_message(message.chat.id, "Вы уверены, что хотите стереть данные о себе и перезапустить бота?",
                           reply_markup = nav.RestYN)
    #dp.register_message_handler (rest, content_types=types.ContentTypes.ANY)
    db.set_signup(message.from_user.id, 'restart')

@dp.message_handler(commands = ['help'])
async def halp(message: types.Message):
    await bot.send_message(message.chat.id, "/start - Начать работу с ботом\n"
                                            "/restart - Перезапустить бота и стереть данные о себе\n"
                                            "/help - Доступные команды")
'''
async def rest(msg: types.Message):
    if msg.text == "Да":
        db.kill_user(msg.from_user.id)
        await bot.send_message(message.chat.id, "Отправь /start\nЧтобы начать всё сначала.",
                               reply_markup = types.ReplyKeyboardMarkup())
    else:
        await bot.send_message(message.chat.id, "Главное меню...",
                               reply_markup=nav.mainMenu)
'''

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    print(message.from_user.id)
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.chat.id,
                         "Привет, {0.first_name}!\nЭто бот Института медиа Вышки. \n\n"
                         "Он поможет абитуриентам получать все важные новости про поступление удобнее,"
                         " чем в электронной почте или на сайте. \n\n"
                         "Чтобы все заработало, пожалуйста, пройдите регистрацию.\n\n"
                         "Напишите фамилию и имя — это нужно, чтобы в дальнейшем регистрировать вас на события "
                         "Института медиа.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup = types.ReplyKeyboardRemove())
        #await bot.send_message(message.from_user.id, "Напишите ваше ФИО")
    elif db.get_signup(message.from_user.id) != 'done' and db.get_signup(message.from_user.id) != 'done_prnt'\
            and db.get_signup(message.from_user.id) != 'admin_true':
        await bot.send_message(message.from_user.id, "Нажмите продолжить", reply_markup = nav.Next)
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!", reply_markup = nav.mainMenu)

@dp.message_handler(commands = ['admin'])
async def admin(message: types.Message):
    if db.get_signup(message.from_user.id) != 'admin_true':
        await bot.send_message(message.from_user.id, "Вы не вошли, как админ", reply_markup = nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, "Меню админа!", reply_markup=nav.AdmMenu)
        db.set_adm_post(message.from_user.id, 0)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        #print(message.message_id)
        #print(message.chat.id)
        print(message.message_id)


        dt_now = datetime.datetime.now()
        september = datetime.datetime(int(dt_now.year), 9, 1)
        if dt_now > september:
            year1 = str(int(dt_now.year) + 1)
            year2 = str(int(year1) -1)
        else:
            year1 = str(int(dt_now.year))
            year2 = str(int(year1) + 1)


        if message.text == 'Профиль':
            #print(message.chat.id)

            str_d = "Данные вашего профиля:\n" \
                  "Вас зовут: " + db.get_name(message.from_user.id) +\
                  "\n" + "Телефон: " + db.get_phone(message.from_user.id) +\
                  "\n" + "Email: " + db.get_mail(message.from_user.id) +\
                  "\n" + "Программа: " + db.get_programm(message.from_user.id) +\
                  "\n" + "Год поступления: " + db.get_year_p(message.from_user.id)

            await bot.send_message(message.from_user.id, str_d, reply_markup = nav.Prof)

        elif message.text == 'Задать вопрос':
            url = "https://t.me/hsemediasupport"
            await bot.send_message(message.from_user.id, url, parse_mode="html")

        elif message.text == 'Полезные ссылки':
            urls = "<strong>Журналистика:</strong> \n" \
                   "🔹<a href='https://www.hse.ru/ba/journ/about'>О программе</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/tracks'>Траектория поступления</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/requirements'>Подготовка</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/key-disciplines'>Ключевые дисциплины</a>\n" \
                    "🔹<a href='https://cmd.hse.ru/mediaday/'>Расписание дней открытых дверей</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/foreign_students'>Важная информация для иностранных студентов</a>\n" \
                    "🔹<a href='https://chat.hse.media/'>Записаться на индивидуальную консультацию</a>\n\n" \
                    "<strong>Медикоммуникации:</strong> \n" \
                    "🔹<a href='https://www.hse.ru/ba/media/about'>О программе</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/tracks'>Траектория поступления</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/requirements'>Подготовка</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/career'>Будущая профессия</a>\n" \
                    "🔹<a href='https://cmd.hse.ru/mediaday/'>Расписание дней открытых дверей</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/foreign_students'>Важная информация для иностранных студентов</a>\n" \
                    "🔹<a href='https://chat.hse.media/'>Записаться на индивидуальную консультацию</a>\n" \
                    "🔹<a href='https://spb.hse.ru/ba/mediacom/tracks'>Программа «Медиакоммуникации» в Питере</a>\n"
            await bot.send_message(message.from_user.id, urls, parse_mode="html")

        elif message.text == 'Назад в меню':
            await bot.send_message(message.from_user.id, "Главное меню...", reply_markup = nav.mainMenu)

        elif  message.text == 'Заполнить заново':
            db.set_signup(message.from_user.id, 'setname')
            await bot.send_message(message.from_user.id, "Напишите фамилию и имя")

        elif message.text == 'Выйти из меню админа' and db.get_signup(message.from_user.id) == 'admin_true':
            await bot.send_message(message.from_user.id, "Главное меню...", reply_markup=nav.mainMenu)

        elif message.text == 'Пост' and db.get_signup(message.from_user.id) == 'admin_true':
            db.set_adm_post(message.from_user.id, 2)
            print(year1+'_')
            await bot.send_message(message.from_user.id, "Выберите год группы, которой отправить пост...",
                                   reply_markup=nav.AdmPostMenuYear)
        elif message.text == 'Пост с кнопками' and db.get_signup(message.from_user.id) == 'admin_true':
            await bot.send_message(message.from_user.id, "Отправьте название кнопок (каждая новая кнопка на новой строке)",
                                   reply_markup = types.ReplyKeyboardRemove())
            db.set_adm_post(message.from_user.id, 10) #GO
        elif message.text == 'Редактировать или удалить пост' and db.get_signup(message.from_user.id) == 'admin_true':
            db.set_adm_post(message.from_user.id, 4)
            PostEditMarks = nav.Update_Edit_mark()
            await bot.send_message(message.from_user.id, "Выберите по времени рассылки какой пост отредактировать"
                                                         " или удалить",
                                   reply_markup=PostEditMarks)

        elif db.get_signup(message.from_user.id) == 'admin_true' and db.get_adm_post(message.from_user.id) == '4':
            db.set_adm_post(message.from_user.id, 5)
            db_post.set_del_edit(-1, message.text)
            str_edit_post = "<strong>Дата и время отправки поста:</strong>" + "\n" + message.text + "\n"\
                            + "<strong>Текст поста:</strong>" + "\n" + db_post.get_post_text(message.text)
            await bot.send_message(message.from_user.id, str_edit_post,
                                   reply_markup=nav.EditPost2, parse_mode="html")

        elif (db.get_signup(message.from_user.id) == 'admin_true' and db.get_adm_post(message.from_user.id) == '5'
            and message.text == 'Вернуться к выбору'):
            db_post.set_del_edit(0, db_post.get_date_from_deledit())
            db.set_adm_post(message.from_user.id, 4)
            PostEditMarks = nav.Update_Edit_mark()
            await bot.send_message(message.from_user.id, "Выберите по времени рассылки какой пост отредактировать"
                                                         " или удалить",
                                   reply_markup=PostEditMarks)

        elif (db.get_signup(message.from_user.id) == 'admin_true' and db.get_adm_post(message.from_user.id) == '5'
              and message.text == 'Редактиорвать этот пост'):
            db.set_adm_post(message.from_user.id, 6)
            await bot.send_message(message.from_user.id, "Отправьте на какой текст заменить текущий...",
                                   reply_markup=types.ReplyKeyboardRemove())

        elif (db.get_signup(message.from_user.id) == 'admin_true' and db.get_adm_post(message.from_user.id) == '6'):
            db.set_adm_post(message.from_user.id, 0)
            db_post.set_del_edit(2, db_post.get_date_from_deledit())
            for i in db_post.get_users_mes_id(db_post.get_id_from_deledit()):
                try:
                    await bot.edit_message_text(text=message.text, message_id=i[1], chat_id=i[0])
                except exceptions.TelegramAPIError:
                    await bot.edit_message_caption(caption=message.text, message_id=i[1], chat_id=i[0])
            db_post.edit_text(message.text, db_post.get_id_from_deledit())
            await bot.send_message(message.from_user.id, "Пост успешно отредактирован", reply_markup=nav.AdmMenu)

        elif (db.get_signup(message.from_user.id) == 'admin_true' and db.get_adm_post(message.from_user.id) == '5'
              and message.text == 'Удалить этот пост'):
            db.set_adm_post(message.from_user.id, 7)
            await bot.send_message(message.from_user.id, "Точно?",
                                   reply_markup=nav.RestYN)

        elif ((db.get_signup(message.from_user.id) == 'admin_true' and
              db.get_adm_post(message.from_user.id) == '7') and message.text == 'Да') :
            db.set_adm_post(message.from_user.id, 0)
            for i in db_post.get_users_mes_id(db_post.get_id_from_deledit()):
                print(db_post.get_users_mes_id(db_post.get_id_from_deledit()))
                await bot.delete_message(
                    chat_id=i[0],
                    message_id=i[1],
                )
            db_post.set_del_edit(1, db_post.get_date_from_deledit())
            await bot.send_message(message.from_user.id, "Пост успешно удалён", reply_markup=nav.AdmMenu)

        elif ((db.get_signup(message.from_user.id) == 'admin_true' and
               db.get_adm_post(message.from_user.id) == '7') and message.text == 'Нет'):
            db_post.set_del_edit(0, db_post.get_date_from_deledit())
            db.set_adm_post(message.from_user.id, 4)
            PostEditMarks = nav.Update_Edit_mark()
            await bot.send_message(message.from_user.id, "Выберите по времени рассылки какой пост отредактировать"
                                                         " или удалить",
                                   reply_markup=PostEditMarks)

        elif db.get_signup(message.from_user.id) == 'admin_true' and db.get_adm_post(message.from_user.id) == '10':
            str_btn = str(message.text)
            with open('Inl_Btn.txt', 'w') as f:
                #print()
                f.write(str_btn)
            await bot.send_message(message.from_user.id, "Выберите год группы, которой отправить пост...",
                                   reply_markup=nav.AdmPostMenuYear)
            db.set_adm_post(message.from_user.id, 2)

        elif db.get_signup(message.from_user.id) == 'admin_true' and\
            db.get_adm_post(message.from_user.id) == '2' and\
            (message.text == year1 + '_' or
             message.text == year2 + '_' or
             message.text == 'Все года_'):
            if message.text == 'Все года_':
                with open('Post_groups.txt', 'w+') as f:
                    f.write(str(1111))
                    f.write('\n')
            else:
                with open('Post_groups.txt', 'w+') as f:
                    if message.text == year1 + '_':
                        f.write(str(year1))
                        db.set_year_p(message.from_user.id, year1)
                    else:
                        f.write(str(year2))
                        db.set_year_p(message.from_user.id, year2)
            db.set_adm_post(message.from_user.id, 3)
            await bot.send_message(message.from_user.id, "Выберите какой группе людей отправить пост...",
                                   reply_markup=nav.AdmPostMenu)

        elif (message.text == 'Медиакоммуникации в Москве_' or
              message.text == 'Особый_' or
              message.text == 'Особый пост с кнопками_' or
              message.text == 'Журналистика_' or
              message.text == 'Всем_' or
              message.text == 'Всем в Москве_' or
              message.text == 'Родители_' or
              message.text == 'Новый сегмент 240-344_' or
              message.text == 'Медиакоммуникации в Питере_') and \
                db.get_signup(message.from_user.id) == 'admin_true' and \
                db.get_adm_post(message.from_user.id) == '3':
            group = message.text[:-1]
            db.set_programm(message.from_user.id, group)
            str_v = "Выбрано: " + group + "\n" + "Отправьте теперь сам пост..."
            db.set_adm_post(message.from_user.id, 1)
            await bot.send_message(message.from_user.id, str_v, reply_markup = nav.AdmPostProgBack)
            dp.register_message_handler(message_handler, content_types=types.ContentTypes.ANY)
        elif message.text == 'Назад к выбору факультета' and db.get_signup(message.from_user.id) == 'admin_true':
            db.set_adm_post(message.from_user.id, 2)
            await bot.send_message(message.from_user.id, "Выберите год группый, которой отправить пост...",
                                   reply_markup=nav.AdmPostMenuYear)

        else:
            if db.get_signup(message.from_user.id) == 'setname':
                if '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрещённыый символ")
                else:
                    if message.text == 'hse_admin_log_cjx': #ЛОГИН ДЛЯ АДМИНА
                        db.set_signup(message.from_user.id, 'admin')
                        await bot.send_message(message.from_user.id, "Введите пароль для админа")
                    else:
                        db.set_name(message.from_user.id, message.text)
                        db.set_signup(message.from_user.id, 'setphone')
                        await bot.send_message(message.from_user.id, "Укажите номер телефона в формате 89*********"
                                                                     " — это нужно, чтобы держать с вами оперативную"
                                                                     " связь во время вступительной кампании.",
                                               reply_markup = types.ReplyKeyboardRemove())

            elif db.get_signup(message.from_user.id) == 'setphone':
                if message.text[0] != '8':
                    await bot.send_message(message.from_user.id, 'Введите телефон, начиная с 8')
                elif not message.text.isnumeric():
                    await bot.send_message(message.from_user.id, 'Введите только цифры без пробелов и других символов')
                else:
                    if len(message.text) != 11:
                        await bot.send_message(message.from_user.id,
                                               'Кажется, телефон должен содержать ровно 11 цифр')
                    else:
                        db.set_phone(message.from_user.id, int(message.text))
                        db.set_signup(message.from_user.id, 'setmail')
                        await bot.send_message(message.from_user.id, 'Укажите почту. \nЕсли вы уже подписаны на'
                                                                     ' <a href="https://forms.sendpulse.com/8952ed9f6b/">'
                                                                     'дайджест Школы медиа</a>'
                                                                     ' НИУ ВШЭ на эту почту, мы не будем дублировать рассылки:'
                                                                     ' будем присылать все новости здесь.',parse_mode="HTML")

            elif db.get_signup(message.from_user.id) == 'setyear':
                if len(message.text) != 4 and message.text != 'Позже':
                    await bot.send_message(message.from_user.id, 'Что-то не так с годом')
                elif not message.text.isnumeric() and message.text != 'Позже':
                    await bot.send_message(message.from_user.id, 'Введите только цифры без пробелов и других символов')
                elif message.text < str(int(datetime.datetime.now().year)) and message.text != 'Позже':
                    await bot.send_message(message.from_user.id, 'Что-то не так с годом.'
                                                                 ' Кажется, все абитуриенты этого года поступили')
                else:
                    if message.text != 'Позже':
                        db.set_year_p(message.from_user.id, int(message.text))
                    else:
                        db.set_year_p(message.from_user.id, 0)
                    db.set_signup(message.from_user.id, 'setprogramm')
                    await bot.send_message(message.from_user.id, "На какую программу?",
                                               reply_markup = nav.ProgMenu)


            elif db.get_signup(message.from_user.id) == 'setprogramm':
                if not (message.text == "Медиакоммуникации в Москве" or
                        message.text == "Журналистика" or
                        message.text == "Медиакоммуникации в Питере" or
                        message.text == "Буду поступать на обе в Москве" or
                        message.text == "Буду поступать на все" ):
                    await bot.send_message(message.from_user.id, 'Выберите ответ из предложенного списка',
                                           reply_markup = nav.ProgMenu)
                else:
                    db.set_programm(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'done')
                    if db.get_adm_post(message.from_user.id) == '77':
                        db.set_signup(message.from_user.id, 'done_prnt')
                        db.set_adm_post(message.from_user.id, -1)
                    await bot.send_message(message.from_user.id, "Поздравляю! Вы успешно зарегистрировались!"
                                                                 " Заодно советуем подписаться на наш "
                                                                 "телеграм-журнал про медиа, диджитал "
                                                                 "и студенческую жизнь Вышки: https://t.me/hsemedia",
                                           reply_markup=nav.mainMenu)
            elif db.get_signup(message.from_user.id) == 'setmail':
                if "@" in message.text:
                    db.set_mail(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'set_p')
                    await bot.send_message(message.from_user.id, "Вы абитуриент или родитель?",
                                           reply_markup = nav.PrntOrAbit)
                else:
                    await bot.send_message(message.from_user.id, 'Это что-то не похоже на электронную почту')


            elif db.get_signup(message.from_user.id) == 'set_p':
                if message.text == "Абитуриент":
                    db.set_signup(message.from_user.id, 'setyear')
                    await bot.send_message(message.from_user.id, "В каком году вы планируете поступать?",
                                           reply_markup=nav.YEAR_BTN)
                elif message.text == "Родитель":
                    db.set_signup(message.from_user.id, 'setyear')
                    db.set_adm_post(message.from_user.id, 77)
                    await bot.send_message(message.from_user.id, "В каком году вaш ребёнок планирует поступать?",
                                           reply_markup=nav.YEAR_BTN)

            elif db.get_signup(message.from_user.id) == 'admin':
                db.set_signup(message.from_user.id, 'done')
                if message.text == 'hse_media_22_[ct': #ПАРОЛЬ ДЛЯ АДМИНА
                    await bot.send_message(message.from_user.id, "Дождитесь подтверждения главного админа")
                    main_adm_str = 'Пользоавиель с id: ' + str(message.from_user.id) +\
                                   ' запрашивает доступ для вход в меню админа. \n' + 'Используйте команду "/entry_admin"'
                    await bot.send_message(732709582, main_adm_str) #id главного админа
                    with open('check_id_admin.txt', 'w') as f:
                        f.write(str(message.from_user.id))

                    '''
                    db.set_signup(message.from_user.id, 'admin_true')
                    db.set_adm_post(message.from_user.id, 0)
                    await bot.send_message(message.from_user.id, "Вы успешно вошли в меню админа!", reply_markup= nav.AdmMenu)
                    '''
                else:
                    db.set_signup(message.from_user.id, 'done')
                    await bot.send_message(message.from_user.id, "У вас нет доступа!!!")

            elif db.get_signup(message.from_user.id) == 'admin_check':
                items_in_f = []
                with open('check_id_admin.txt', 'r') as f:
                    for item in f:
                        items_in_f.append(item)
                print(items_in_f[0])
                if message.text == str(items_in_f[0]):
                    db.set_signup(int(items_in_f[0]), 'admin_true')
                    db.set_adm_post(int(items_in_f[0]), 0)
                    await bot.send_message(int(items_in_f[0]), "Вам был предоставлен досуп в меню админа!",
                                           reply_markup=nav.AdmMenu)
                    await bot.send_message(message.from_user.id, "Пользователю был предоставлен доступ в кабинет админа",
                                           reply_markup=nav.AdmMenu)
                    db.set_signup(message.from_user.id, 'admin_true')
                elif message.text == 'no':
                    db.set_signup(int(items_in_f[0]), 'done')
                    db.set_adm_post(int(items_in_f[0]), -1)
                    await bot.send_message(int(items_in_f[0]), "Вам отказанов доступе",
                                           reply_markup=nav.mainMenu)
                    await bot.send_message(message.from_user.id,
                                           "Пользователю было отказано в доступе",
                                           reply_markup=nav.AdmMenu)
                    db.set_signup(message.from_user.id, 'admin_true')
                else:
                    db.set_signup(message.from_user.id, 'admin_true')
                    await bot.send_message(message.from_user.id, "Введено что-то не то, повторите команду",
                                           reply_markup=nav.AdmMenu)


            elif db.get_signup(message.from_user.id) == 'restart':
                if message.text == "Да":
                    db.kill_user(message.from_user.id)

                    await bot.send_message(message.chat.id, "Отправь /start\nЧтобы начать всё сначала.",
                                           reply_markup = nav.Start_)
                else:
                    if db.get_adm_post(message.from_user.id) == '0':
                        db.set_signup(message.from_user.id, 'admin_true')
                    else:
                        db.set_signup(message.from_user.id, 'done')
                    await bot.send_message(message.chat.id, "Главное меню...",
                                           reply_markup=nav.mainMenu)


            else:

                if db.get_adm_post(message.from_user.id) == '1' and db.get_signup(message.from_user.id) == 'admin_true': #СДЕЛАЙ В БД ФЛАГ НА ДАННОЕ ИСКЛЮЧЕНИЕ
                    msg = message

                    # Btn_str = ''
                    # with open('Inl_Btn.txt', 'r') as f:
                    #     for i in f:
                    #         Btn_str = Btn_str + i + '\n'
                    # if Btn_str != '\n':
                    #     open('Inl_Btn.txt', 'w').close()
                    #     msg.reply_markup = nav.inline_but(Btn_str, msg.message_id)
                    #msg.message_id = 10
                    #msg.mess


                    with open('Post_groups.txt', 'r') as f:
                        year_post = f.read(4)
                    db_post.update_tables()
                    if year_post == '1111':

                        if db.get_programm(msg.from_user.id) == 'Всем':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            users_1 = db.get_user_id("Журналистка")
                            users_2 = db.get_user_id("Медиакоммуникации в Москве")
                            users_3 = db.get_user_id("Буду поступать на обе в Москве")
                            users_4 = db.get_user_id("Медиакоммуникации в Питере")
                            users_5 = db.get_user_id("Буду поступать на все")
                            # RepMark = nav.inline_but(msg.caption)
                            # msg.reply_markup = RepMark
                            await MessageBroadcaster(users_1, msg).run()
                            await MessageBroadcaster(users_2, msg).run()
                            await MessageBroadcaster(users_3, msg).run()
                            await MessageBroadcaster(users_4, msg).run()
                            await MessageBroadcaster(users_5, msg).run()
                            # print('da')

                        elif db.get_programm(msg.from_user.id) == 'Особый':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            users_ = [1354467245, 1972673513, 299561163, 728131343, 730086167,
                                      1028033536, 670838339, 807748810, 585705579, 387863611,
                                      1145676386, 880544715, 1512704472, 627498868, 1003015874,
                                      559567576, 2041741153, 917537526, 399517539, 330820504, 807686789, 542703639]
                            users_ = [484623073]
                            print('ok')
                            await MessageBroadcaster(users_, msg).run()

                        elif db.get_programm(msg.from_user.id) == 'Родители':
                            db.set_adm_post(msg.from_user.id, 0)
                            users = db.get_user_id_prnts()
                            me_ = []
                            me_.append(msg.from_user.id)
                            await MessageBroadcaster(me_, msg).run()
                            await MessageBroadcaster(users, msg).run()

                        elif db.get_programm(msg.from_user.id) == "Новый сегмент 240-344":
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            mas_mail = []
                            with open('mail_4_jul.txt') as f:
                                for i in f:
                                    if '\n' in i:
                                        id_mail = db.get_user_id_mail(i[:-1])
                                    else:
                                        id_mail = db.get_user_id_mail(i)
                                    if len(id_mail) !=0:
                                        mas_mail.append(id_mail[0])
                            mas_mail.append(732709582)
                            mas_mail.append(484623073)
                            await MessageBroadcaster(mas_mail, msg).run()

                            '''
                        elif db.get_programm(msg.from_user.id) == 'Особый пост с кнопками':
                            msg.reply_markup = nav.InlBtnForPost2
                            mas_id = []
                            with open('Polls/poll_1_no.txt') as f:
                                for i in f:
                                    mas_id.append(i[:-1])
                            mas_id.append(str(msg.from_user.id))
                            print(mas_id)
                            #await MessageBroadcaster(mas_id, msg).run()

                        elif db.get_programm(msg.from_user.id) == 'Особый пост':
                            mas_id = []
                            with open('Polls/poll_2_no.txt') as f:
                                for i in f:
                                    mas_id.append(i[:-1])
                            mas_id.append(str(msg.from_user.id))
                            print(mas_id)
                            await MessageBroadcaster(mas_id, msg).run()
                            '''

                        elif db.get_programm(msg.from_user.id) == 'Всем в Москве':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            users_1 = db.get_user_id("Журналистка")
                            users_2 = db.get_user_id("Буду поступать на обе в Москве")
                            users_3 = db.get_user_id("Медиакоммуникации в Москве")
                            users_4 = db.get_user_id("Буду поступать на все")
                            await MessageBroadcaster(users_1, msg).run()
                            await MessageBroadcaster(users_2, msg).run()
                            await MessageBroadcaster(users_3, msg).run()
                            await MessageBroadcaster(users_4, msg).run()

                        elif db.get_programm(msg.from_user.id) == 'Медиакоммуникации в Питере':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            db.set_programm(msg.from_user.id, "Медиакоммуникации в Питере")
                            users = db.get_user_id(db.get_programm(msg.from_user.id))
                            users_ = db.get_user_id("Буду поступать на все")
                            await MessageBroadcaster(users, msg).run()
                            await MessageBroadcaster(users_, msg).run()

                            '''
                        elif db.get_programm(msg.from_user.id) == 'Абитуриенты этого года':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            users = db.get_user_id_year()
                            await MessageBroadcaster(users, msg).run()

                        elif db.get_programm(msg.from_user.id) == 'Абитуриенты 2022 года':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            users = db.get_user_id_year_2022()
                            msg.reply_markup = nav.InlBtnForPost2022
                            await MessageBroadcaster(users, msg).run()
                            '''

                        else:
                            db.set_adm_post(msg.from_user.id, 0)
                            users = db.get_user_id(db.get_programm(msg.from_user.id))
                            users_ = db.get_user_id("Буду поступать на все")
                            users__ = db.get_user_id("Буду поступать на обе в Москве")
                            await MessageBroadcaster(users, msg).run()
                            await MessageBroadcaster(users_, msg).run()
                            await MessageBroadcaster(users__, msg).run()

                    else:
                        if db.get_programm(msg.from_user.id) == 'Всем':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            users_1 = db.get_user_id_and_year("Журналистка", year_post)
                            users_2 = db.get_user_id_and_year("Медиакоммуникации в Москве", year_post)
                            users_3 = db.get_user_id_and_year("Буду поступать на обе в Москве", year_post)
                            users_4 = db.get_user_id_and_year("Медиакоммуникации в Питере", year_post)
                            users_5 = db.get_user_id_and_year("Буду поступать на все", year_post)
                            # RepMark = nav.inline_but(msg.caption)
                            # msg.reply_markup = RepMark
                            await MessageBroadcaster(users_1, msg).run()
                            await MessageBroadcaster(users_2, msg).run()
                            await MessageBroadcaster(users_3, msg).run()
                            await MessageBroadcaster(users_4, msg).run()
                            await MessageBroadcaster(users_5, msg).run()
                            # print('da')

                        elif db.get_programm(msg.from_user.id) == 'Родители':
                            db.set_adm_post(msg.from_user.id, 0)
                            users = db.get_user_id_prnts_and_year(year_post)
                            me_ = []
                            me_.append(msg.from_user.id)
                            await MessageBroadcaster(me_, msg).run()
                            await MessageBroadcaster(users, msg).run()


                        elif db.get_programm(msg.from_user.id) == "Новый сегмент 240-344":
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            mas_mail = []
                            with open('mail_4_jul.txt') as f:
                                for i in f:
                                    if '\n' in i:
                                        id_mail = db.get_user_id_mail(i[:-1])
                                    else:
                                        id_mail = db.get_user_id_mail(i)
                                    if len(id_mail) !=0:
                                        mas_mail.append(id_mail[0])
                            mas_mail.append(732709582)
                            mas_mail.append(484623073)
                            await MessageBroadcaster(mas_mail, msg).run()


                        elif db.get_programm(msg.from_user.id) == 'Всем в Москве':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            users_1 = db.get_user_id_and_year("Журналистка", year_post)
                            users_2 = db.get_user_id_and_year("Буду поступать на обе в Москве", year_post)
                            users_3 = db.get_user_id_and_year("Медиакоммуникации в Москве", year_post)
                            users_4 = db.get_user_id_and_year("Буду поступать на все", year_post)
                            await MessageBroadcaster(users_1, msg).run()
                            await MessageBroadcaster(users_2, msg).run()
                            await MessageBroadcaster(users_3, msg).run()
                            await MessageBroadcaster(users_4, msg).run()

                        elif db.get_programm(msg.from_user.id) == 'Медиакоммуникации в Питере':
                            db.set_adm_post(msg.from_user.id, 0)
                            db.set_programm(msg.from_user.id, "Буду поступать на все")
                            db.set_programm(msg.from_user.id, "Медиакоммуникации в Питере")
                            users = db.get_user_id_and_year("Медиакоммуникации в Питере", year_post)
                            users_ = db.get_user_id_and_year("Буду поступать на все", year_post)
                            await MessageBroadcaster(users, msg).run()
                            await MessageBroadcaster(users_, msg).run()

                        else:
                            db.set_adm_post(msg.from_user.id, 0)
                            users = db.get_user_id_and_year(db.get_programm(msg.from_user.id), year_post)
                            users_ = db.get_user_id_and_year("Буду поступать на все", year_post)
                            users__ = db.get_user_id_and_year("Буду поступать на обе в Москве", year_post)
                            await MessageBroadcaster(users, msg).run()
                            await MessageBroadcaster(users_, msg).run()
                            await MessageBroadcaster(users__, msg).run()
                    print("TEXT MES")
                    print(msg.text)
                    db_post.add_post(msg.text, msg.from_user.id)
                else:
                    await bot.send_message(message.from_user.id, "У нас нет такой команды. Нажмите на /help, чтобы посмотреть опции.\n\n"
                                                     "Если вам нужна помощь, напишите в поддержку: @hsemediasupport")

'''
@dp.callback_query_handler(text="yes_2022")
async def option_1 (call: types.CallbackQuery):
    #prin('dadada')
    with open('Polls/poll_2022_yes.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
    await call.answer(text="Ваш ответ учтён", show_alert=True)
    await bot.send_message(call.from_user.id, "Рады, что вы теперь с нами! \n"
                                              "<a href = 'https://t.me/hsemedia'>"
                                              "Загляните в наш телеграм-канал о студенческой жизни Института медиа</a>."
                                              " Там мы публикуем полезные посты об учебе, саморазвитии и работе,"
                                              " а еще делимся подборками классных мероприятий в Москве и не только",
                           parse_mode="html")
'''
'''
@dp.callback_query_handler(text="no_2022")
async def option_1 (call: types.CallbackQuery):
    with open('Polls/poll_2022_no.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
    await call.answer(text="Ваш ответ учтён", show_alert=True)
    await bot.send_message(call.from_user.id, "Ответьте на несколько вопросов, чтобы могли настроить бот под вас",
                           parse_mode="html")
    await bot.send_message(call.from_user.id, "Вы планируете перепоступать или поступили в другой вуз?",
                           parse_mode="html", reply_markup = nav.InlBtnForPost2022_2)
'''
'''
@dp.callback_query_handler(text="ye_2022")
async def option_1 (call: types.CallbackQuery):
    #prin('dadada')
    with open('Polls/poll_2022_pere.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
    await call.answer(text="Ваш ответ учтён", show_alert=True)
    await bot.send_message(call.from_user.id, "Обновите регистрацию в боте,"
                                              " чтобы получать актуальную информацию о поступлении."
                                              "\n1. Зайдите в «Меню»,"
                                              "\n2. Нажмите «Перезапустить бота и стереть данные о себе»"
                                              "\n3. Пройдите регистрацию снова и укажите год поступления «2023»",
                           parse_mode="html")


@dp.callback_query_handler(text="another_uni_2022")
async def option_1 (call: types.CallbackQuery):
    with open('Polls/poll_2022_another.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
    await call.answer(text="Ваш ответ учтён", show_alert=True)
    await bot.send_message(call.from_user.id, "Здорово, желаем вам интересной учебы! "
                                              "Загляните в <a href = 'https://t.me/hsemedia'>"
                                              "наш телеграм-канал о студенческой жизни</a>."
                                              " Там мы публикуем полезные посты об учебе, "
                                              "саморазвитии и работе, а еще делимся подборками классных "
                                              "мероприятий в Москве и не только.",
                           parse_mode="html")
'''
'''
@dp.callback_query_handler(text="yes1")
async def option_1 (call: types.CallbackQuery):
    with open('Polls/poll_1_yes.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
        await call.answer(text="Ваш ответ учтён", show_alert=True)

@dp.callback_query_handler(text="no1")
async def option_1 (call: types.CallbackQuery):
    with open('Polls/poll_1_no.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
        await call.answer(text="Ваш ответ учтён", show_alert=True)


@dp.callback_query_handler(text="yes2")
async def option_1 (call: types.CallbackQuery):
    with open('Polls/poll_2_yes.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
        await call.answer(text="Ваш ответ учтён", show_alert=True)

@dp.callback_query_handler(text="no2")
async def option_1 (call: types.CallbackQuery):
    with open('Polls/poll_2_no.txt', 'a') as f:
        f.write(str(call.from_user.id))
        f.write('\n')
        await call.answer(text="Ваш ответ учтён", show_alert=True)
        
'''
'''
@dp.callback_query_handler(text="0")
async def option_1 (call: types.CallbackQuery):
    print(call.from_user.id)
    print(call.message.message_id)
    print('0')
    #print(call.message.)
@dp.callback_query_handler(text="1")
async def option_2 (call: types.CallbackQuery):
    print(call.from_user.id)
    print(call.message.message_id)
    print('1')
    #print(call.inline_message_id)
@dp.callback_query_handler(text="2")
async def option_3 (call: types.CallbackQuery):
    print(call.from_user.id)
    print(call.message.message_id)
    print('2')

@dp.callback_query_handler(text="3")
async def option_3 (call: types.CallbackQuery):
    print(call.from_user.id)
    print(call.message.message_id)
    print('3')

@dp.callback_query_handler(text="4")
async def option_3 (call: types.CallbackQuery):
    print(call.from_user.id)
    print(call.message.message_id)
    print('4')
'''
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)