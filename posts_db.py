import sqlite3
import datetime
from datetime import date
from datetime import datetime
from google_db import Google_DateBase

class Datebase_post:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_post(self, post_txt, admin_id):
        now = datetime.now()
        date_today = now.strftime("%d-%m-%Y %H:%M")
        with self.connection:
            self.cursor.execute(
                'UPDATE "posts" SET text = (SELECT text FROM `posts` WHERE `post_table_name` = "post_4")'
                ' WHERE `post_table_name` = "post_5"')
            self.cursor.execute(
                'UPDATE "posts" SET admin_id = (SELECT admin_id FROM `posts` WHERE `post_table_name` = "post_4")'
                ' WHERE `post_table_name` = "post_5"')
            self.cursor.execute(
                'UPDATE "posts" SET date = (SELECT date FROM `posts` WHERE `post_table_name` = "post_4")'
                ' WHERE `post_table_name` = "post_5"')
            self.cursor.execute(
                'UPDATE "posts" SET `del/edit` = (SELECT `del/edit` FROM `posts` WHERE `post_table_name` = "post_4")'
                ' WHERE `post_table_name` = "post_5"')


            self.cursor.execute(
                'UPDATE "posts" SET text = (SELECT text FROM `posts` WHERE `post_table_name` = "post_3")'
                ' WHERE `post_table_name` = "post_4"')
            self.cursor.execute(
                'UPDATE "posts" SET admin_id = (SELECT admin_id FROM `posts` WHERE `post_table_name` = "post_3")'
                ' WHERE `post_table_name` = "post_4"')
            self.cursor.execute(
                'UPDATE "posts" SET date = (SELECT date FROM `posts` WHERE `post_table_name` = "post_3")'
                ' WHERE `post_table_name` = "post_4"')
            self.cursor.execute(
                'UPDATE "posts" SET `del/edit` = (SELECT `del/edit` FROM `posts` WHERE `post_table_name` = "post_3")'
                ' WHERE `post_table_name` = "post_4"')

            self.cursor.execute(
                'UPDATE "posts" SET text = (SELECT text FROM `posts` WHERE `post_table_name` = "post_2")'
                ' WHERE `post_table_name` = "post_3"')
            self.cursor.execute(
                'UPDATE "posts" SET admin_id = (SELECT admin_id FROM `posts` WHERE `post_table_name` = "post_2")'
                ' WHERE `post_table_name` = "post_3"')
            self.cursor.execute(
                'UPDATE "posts" SET date = (SELECT date FROM `posts` WHERE `post_table_name` = "post_2")'
                ' WHERE `post_table_name` = "post_3"')
            self.cursor.execute(
                'UPDATE "posts" SET `del/edit` = (SELECT `del/edit` FROM `posts` WHERE `post_table_name` = "post_2")'
                ' WHERE `post_table_name` = "post_3"')

            self.cursor.execute(
                'UPDATE "posts" SET text = (SELECT text FROM `posts` WHERE `post_table_name` = "post_1")'
                ' WHERE `post_table_name` = "post_2"')
            self.cursor.execute(
                'UPDATE "posts" SET admin_id = (SELECT admin_id FROM `posts` WHERE `post_table_name` = "post_1")'
                ' WHERE `post_table_name` = "post_2"')
            self.cursor.execute(
                'UPDATE "posts" SET date = (SELECT date FROM `posts` WHERE `post_table_name` = "post_1")'
                ' WHERE `post_table_name` = "post_2"')
            self.cursor.execute(
                'UPDATE "posts" SET `del/edit` = (SELECT `del/edit` FROM `posts` WHERE `post_table_name` = "post_1")'
                ' WHERE `post_table_name` = "post_2"')

            self.cursor.execute('UPDATE `posts` SET `del/edit` = 0 WHERE "post_table_name" = "post_1";')
            self.cursor.execute('UPDATE `posts` SET admin_id = ? WHERE "post_table_name" = "post_1";', (admin_id,))
            self.cursor.execute('UPDATE `posts` SET date = ? WHERE "post_table_name" = "post_1";', (date_today, ))
            return self.cursor.execute('UPDATE `posts` SET text = ? WHERE "post_table_name" = "post_1";', (post_txt,))

    def add_mes_id(self, chat_id, mes_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `post_1` (`user_id`, `post_id`) VALUES (?, ?)", (chat_id, mes_id))

    def update_tables(self):
        with self.connection:
            self.cursor.execute('DELETE FROM `post_5`')
            self.cursor.execute('INSERT INTO `post_5` SELECT * FROM `post_4`')
            self.cursor.execute('DELETE FROM `post_4`')
            self.cursor.execute('INSERT INTO `post_4` SELECT * FROM `post_3`')
            self.cursor.execute('DELETE FROM `post_3`')
            self.cursor.execute('INSERT INTO `post_3` SELECT * FROM `post_2`')
            self.cursor.execute('DELETE FROM `post_2`')
            self.cursor.execute('INSERT INTO `post_2` SELECT * FROM `post_1`')
            self.cursor.execute('DELETE FROM `post_1`')

    # def del_post(self, post_id):
    #     with self.connection:
    #         return self.cursor.execute('UPDATE `posts` SET del/edit = 1 WHERE "post_id" = ?', (post_id,))

    def get_users_mes_id(self, post_id):
        users_id_ = []
        table_name = 'post_' + str(post_id)
        sel_1 = "SELECT `user_id` FROM " + table_name
        sel_2 = "SELECT `post_id` FROM " + table_name
        with self.connection:
            result_1 = self.cursor.execute(sel_1).fetchall()
            result_2 = self.cursor.execute(sel_2).fetchall()
            for i in range (len(result_1)):
                users_id_.append([int(result_1[i][0]), int(result_2[i][0])])
            return users_id_

    def get_post_date(self, post_id):
        with self.connection:
            result = self.cursor.execute('SELECT `date` FROM `posts` WHERE `post_id` = ?', (post_id,)).fetchall()
            for row in result:
                date_ = str(row[0])
            return date_

    def get_post_text(self, post_date):
        with self.connection:
            result = self.cursor.execute('SELECT `text` FROM `posts` WHERE `date` = ?', (post_date,)).fetchall()
            for row in result:
                text_ = str(row[0])
            return text_

    def set_del_edit(self, flag, post_date):
        with self.connection:
            return self.cursor.execute('UPDATE `posts` SET `del/edit` = ? WHERE "date" = ?', (flag, post_date))

    def get_date_from_deledit(self):
        with self.connection:
            result = self.cursor.execute('SELECT `date` FROM `posts` WHERE `del/edit` = -1').fetchall()
            for row in result:
                date_ = str(row[0])
            return date_

    def get_id_from_deledit(self):
        id = '1'
        with self.connection:
            result = self.cursor.execute('SELECT `post_id` FROM `posts` WHERE `del/edit` = -1').fetchall()
            for row in result:
                id = str(row[0])
            return id

    def edit_text(self, post_text, id):
        with self.connection:
            return self.cursor.execute('UPDATE `posts` SET text = ? WHERE `post_id` = ? ', (post_text, id))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))
