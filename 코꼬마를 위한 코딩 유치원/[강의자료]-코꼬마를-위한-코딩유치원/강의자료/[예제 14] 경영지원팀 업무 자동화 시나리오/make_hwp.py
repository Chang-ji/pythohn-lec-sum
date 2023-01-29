import pyexcel as px
import time
import pywinmacro as pw


def start_hwp():
    # 이 함수를 실행하면 한글워드프로세서가 실행됩니다
    start_x, start_y = 37, -593
    pw.click((start_x, start_y))

    time.sleep(5)
    new_x, new_y = 622, -809
    pw.click((new_x, new_y))


def save_document(filename):
    save_x, save_y = 208, -897
    pw.click((save_x, save_y))

    time.sleep(2)
    scroll_x, scroll_y = 215, -762
    pw.move_mouse((scroll_x, scroll_y))
    for i in range(5):
        pw.mouse_upscroll()

    time.sleep(0.5)
    folder_x, folder_y = 232, -731
    pw.click((folder_x, folder_y))

    time.sleep(0.2)
    space_x, space_y = 427, -807
    pw.click((space_x, space_y))

    time.sleep(0.2)
    name_x, name_y = 433, -634
    pw.click((name_x, name_y))

    pw.type_in(filename)
    pw.key_press_once("enter")

    time.sleep(2)
    exit_x, exit_y = 1582, -1062
    pw.click((exit_x, exit_y))


def write_one_person(HEADER, pi):
    content = ""
    for i in range(len(HEADER)):
        content += (HEADER[i])
        content += "\t:\t"
        content += str(pi[i])
        content += "\n"
    pw.type_in(content)


daejang = px.get_array(file_name="임금명세.xlsx")
HEADER = daejang[0]

daejang = daejang[1:]

for i in range(len(daejang)):
    start_hwp()
    time.sleep(2)
    write_one_person(HEADER, daejang[i])
    save_document(str(i).zfill(3) + "_" + daejang[i][3])
    time.sleep(2)
