import pywinmacro as pw
import time
import pyexcel as px


def send_email():
    send_x, send_y = 65, -900
    pw.click((send_x, send_y))
    time.sleep(1)


def attach_file(filename):
    x, y = 375, -263
    pw.click((x, y))
    time.sleep(1)
    pw.type_in(filename)
    pw.key_press_once("enter")


daejang = px.get_array(file_name="임금명세.xlsx")
daejang = daejang[1:]

for i in range(len(daejang)):
    person = daejang[i]
    email = person[-1]
    year = person[0]
    month = person[1]

    title = "[경영지원팀] " + year + "년도 " + month + " 월 급여명세서 송부의 건"

    contents = "귀하의 노고에 감사드립니다."

    filename = str(i).zfill(3) + "_" + daejang[i][3] + ".hwp"

    send_email()
    pw.type_in(email)
    pw.key_press_once("tab")
    pw.type_in(title)
    pw.key_press_once("tab")
    pw.type_in(contents)

    attach_file(filename)
    time.sleep(1)

    x, y = 279, -271
    pw.click((x, y))
    time.sleep(2)



