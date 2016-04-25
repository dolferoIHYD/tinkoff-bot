# -*- Coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer

class GetHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        request = self.rfile.read(length)
        response = "Привет! Вы спросили: " + request.strip().decode('utf-8')
        content_len = len(response)
        self.send_response(200)
        self.end_headers()

        req = request.strip().decode('utf-8')

        if "Здравствуйте" in req or "здравствуйте" in req or "Добрый" in req or "Доброго" in req or "Доброе" in req or "добрый" in req or "доброго" in req or "доброе" in req or "привет" in req or "здарова" in req or "йоу" in req :
                response =  "Здравствуйте!"
        else:
                if ("Кто" in req) and ('Тиньков' not in req):
                    response = "Бот производства BAMbot"

                else:
                  if req.lower()=='да' or req[:3].lower()=='да!' or req[:3].lower()=='да.' or req[:3].lower()=='да,':
                    response =  "Рад вам помочь!"
                  elif "Нет" in req or " нет " in req:
                    response = "Попробуйте переформулировать вопрос. К сожалению, первая версия бота несовершенна"
                  else:
                    inQuest = open("questionFAQ.txt", "r")

                    mes = req
                    print(req)

                    mes = mes.replace(",", "")
                    mes = mes.replace(".", "")
                    mes = mes.replace("?", "")
                    mes = mes.replace("(", "")
                    mes = mes.replace(")", "")
                    mes = mes.replace("-", "")
                    mes = mes.replace("!", "")
                    mes = mes.replace("«", "")
                    mes = mes.replace("»", "")

                    mes = mes.lower().split()
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
                            print(summ)

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
                                response =  data_lines[l+1]
                                #print('hey', summ1)

                        inFAQ.close()


                    else:
                        response =  'Извините, я не поняль =('


        self.wfile.write(response.strip().encode('utf-8'))
        print(response)
        return

if __name__ == '__main__':
    from http.server import HTTPServer
    host = '10.5.0.220'
    server = HTTPServer((host, 8000), GetHandler)
    print ('Starting server at http://' + host + ':8000')
    server.serve_forever()
