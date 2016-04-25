# -*- coding: utf-8 -*-

import config
import telebot
import server

global strn

def non(m):
    bot.send_message(m.chat.id, "Попробуйте переформулировать вопрос. К сожалению, первая версия бота несовершенна")


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
                if ('Кто' in m.text and 'Тиньков' not in m.text) or ('кто' in m.text and 'Тиньков' not in m.text):
                    bot.send_message(m.chat.id, "Бот производства BAMbot")
                else:
                  if m.text.lower()=='да' or m.text[:3].lower()=='да!' or m.text[:3].lower()=='да.' or m.text[:3].lower()=='да,':
                    bot.send_message(m.chat.id, "Рад вам помочь!")
                  elif "Нет" in m.text or " нет " in m.text:
                    non(m)
                  else:
                    inQuest = open("questionFAQ.txt", "r")

                    mes = m.text

                    mes = mes.replace(",", "")
                    mes = mes.replace(".", "")
                    mes = mes.replace("?", "")
                    mes = mes.replace("(", "")
                    mes = mes.replace(")", "")
                    mes = mes.replace("-", " ")
                    mes = mes.replace("!", "")
                    mes = mes.replace("«", "")
                    mes = mes.replace("»", "")

                    mes = mes.lower().split()
                    
                    rub =0
                    number_of_card = 0
                    phonenumber = 0

                    if (mes[0].startswith('перевести')) or (mes[0].startswith('перевод')) or (mes[0].startswith('перечислить')) or (mes[0].startswith('положи')) or (mes[0].startswith('переведи')) or (mes[0].startswith('перечисли')):
                        rub = int(mes[1])
                        if len(mes[2])!= 16:
                            bot.send_message(m.chat.id, "Неверно введен номер карты, попробуйте еще раз")
                            break
                        else:
                            number_of_card = int(mes[2])
                        print ("Summ: " + str(rub))
                        print ("Card num: " + str(number_of_card))
                        print ("Id: " + str(m.chat.id))
                        bot.send_message(m.chat.id, "Запрос принят")

                    elif (mes[0].startswith('зачислить')) or (mes[0].startswith('закинуть')) or (mes[0].startswith('положить')) or (mes[0].startswith('кинь')) or (mes[0].startswith('зачисли')) or (mes[0].startswith('положи')) or (mes[0].startswith('положить')) or (mes[0].startswith('забрось')):
                        rub=int(mes[1])
                        if len(mes[2])!=11:
                            bot.send_message(m.chat.id, "Неверно введен номер телефона, попробуйте еще раз")
                            break
                        else:
                            phonenumber = int(mes[2])
                        print ("Summ: " + str(rub))
                        print ("Phone num: " + str(phonenumber))
                        print ("Chat Id: " + str(m.chat.id))
                        bot.send_message(m.chat.id, "Запрос принят")
                    else:
                        print(mes)

                        data_list = inQuest.read().split("\n")
                        summ = 0
                        summ1 = 0
                        strn = ''

                        wordArr=[]
                        count = []
                        for line in data_list:
                            for word in line.lower().split():
                                wordArr.append(word)

                        for k in mes:
                            c = wordArr.count(k)
                            count.append(c)
                        print(count)

                        for line in data_list:
                            summ=0
                            for i in range(len(mes)):
                                if mes[i] in line.lower().split():
                                    summ = summ + 1 /count[i]
                                #print(summ)

                                if summ > summ1:
                                    summ1 = summ
                                    strn = line.lower()
                        print(strn)
                        strnumber = strn[:3]
                        print (strnumber, strn)
                        inQuest.close()

                        if (summ1>0.1):
                            inFAQ = open("questFAQ Full.txt", "r")
                            data_lines = inFAQ.read().split("\n")


                            for l in range(len(data_lines)):
                                if (str(strnumber) == data_lines[l].lower()[:3]) or (str(strnumber) == data_lines[l].lower()[:2]):
                                    bot.send_message(m.chat.id, data_lines[l+1])
                                    #print('hey', summ1)

                            inFAQ.close()

                            bot.send_message(m.chat.id, "Я ответил на ваш вопрос?")

                        else:
                            bot.send_message(m.chat.id, 'Извините, я не поняль =(')






bot = telebot.TeleBot(config.token)
bot.set_update_listener(listener)

@bot.message_handler(commands=['start'])
def command_start(m):

    bot.send_message(m.chat.id, "Здравствуйте, " + m.chat.first_name)



bot.polling()