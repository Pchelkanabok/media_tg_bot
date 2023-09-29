import sqlite3
import datetime
from datetime import date
from google_db import Google_DateBase

class Datebase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        #self.google_db = Google_DateBase("15IEysmp2vNkzQ_5mrQbNIHRwrBvLOTrZIE45jhHRVG0")

    def count_all(self, table):
        count_ = []
        with self.connection:
            str = "SELECT count(*) FROM `" + table + "`"
            result = self.cursor.execute(str)
            for row in result:
                count_.append(int(row[0]))
            return count_[0]

    def get_last_row(self, table, user_id):
        str = "SELECT * FROM `" + table + "` WHERE user_id = " + user_id
        la_row = []
        with self.connection:
            result = self.cursor.execute(str)
            for row in result:
                la_row.append(int(row[0]))
            return row

    def add_user(self, user_id):
        #self.google_db.set_one_value ("users", "B", str(self.count_all("users")+2), user_id)
        #print(self.get_last_row("users", user_id))
        with self.connection:
            self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
            # self.google_db.set_one_str("users", "I", str(self.count_all("users") + 1),
            #                            self.get_last_row("users", user_id))


    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))


    def get_user_id(self, prog):
        user_id_s = []
        with self.connection:
            result = self.cursor.execute("SELECT `user_id` FROM `users` WHERE `programm` = ?", (prog,)).fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            return user_id_s

    def get_user_id_all(self):
        user_id_s = []
        with self.connection:
            result = self.cursor.execute("SELECT `user_id` FROM `users`").fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            return user_id_s

    def get_user_id_prnts(self):
        user_id_s = []
        with self.connection:                                                           #strftime("%Y", date("now"))
            result = self.cursor.execute('SELECT `user_id` FROM `users` WHERE `signup` = "done_prnt"').fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            print(user_id_s)
            return user_id_s

    def get_user_id_prnts_and_year(self, year):
        user_id_s = []
        year_ = str(year)
        with self.connection:                                                           #strftime("%Y", date("now"))
            result = self.cursor.execute('SELECT `user_id` FROM `users` WHERE `signup` = "done_prnt" AND `year_p` == ?',
                                         (year_,)).fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            print(user_id_s)
            return user_id_s


    def get_user_id_and_year(self, prog, year):
        user_id_s = []
        with self.connection:
            year_ = str(year)
            result = self.cursor.execute("SELECT `user_id` FROM `users` WHERE `programm` = ? AND `year_p` == ?",
                                         (prog, year_)).fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            return user_id_s


    def get_user_id_year(self):
        user_id_s = []
        dt_now = datetime.datetime.now()
        september = datetime.datetime(int(dt_now.year), 9, 1)
        # print(dt_now)
        # print(september)
        if dt_now >= september:
            year1 = str(int(dt_now.year) + 1)
        else:
            year1 = str(int(dt_now.year))
        with self.connection:                                                           #strftime("%Y", date("now"))
            result = self.cursor.execute('SELECT `user_id` FROM `users` WHERE `year_p` == ?', (year1,)).fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            print(user_id_s)
            return user_id_s

    def get_user_id_year_2022(self):
        user_id_s = []
        with self.connection:                                                           #strftime("%Y", date("now"))
            result = self.cursor.execute('SELECT `user_id` FROM `users` WHERE `year_p` == 2022').fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            print(user_id_s)
            return user_id_s


    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `name` = ? WHERE `user_id` = ?", (name, user_id,))


    def get_name(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `name` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                name = str(row[0])
            return name


    def set_phone(self, user_id, phone):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `phone` = ? WHERE `user_id` = ?", (phone, user_id,))


    def get_phone(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `phone` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                phone = str(row[0])
            return phone


    def set_adm_post(self, user_id, adm_post):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `adm_post` = ? WHERE `user_id` = ?", (adm_post, user_id,))

    def get_adm_post(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `adm_post` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                adm_post = str(row[0])
            return adm_post


    def set_programm(self, user_id, programm):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `programm` = ? WHERE `user_id` = ?", (programm, user_id,))


    def get_programm(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `programm` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                programm = str(row[0])
            return programm


    def set_year_p(self, user_id, year_p):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `year_p` = ? WHERE `user_id` = ?", (year_p, user_id,))


    def get_year_p(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `year_p` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                year_p = str(row[0])
            return year_p


    def set_mail(self, user_id, mail):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `mail` = ? WHERE `user_id` = ?", (mail, user_id,))


    def get_mail(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `mail` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                mail = str(row[0])
            return mail


    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id` = ?", (signup, user_id,))


    def kill_user(self, user_id):
        with self.connection:
            self.cursor.execute("DELETE FROM `users` WHERE `user_id` = ?", (user_id,))

    def to_google(self, table):
        with self.connection:
            str = "SELECT *  FROM `" + table + "`"
            result = self.cursor.execute(str).fetchall()
            return result




