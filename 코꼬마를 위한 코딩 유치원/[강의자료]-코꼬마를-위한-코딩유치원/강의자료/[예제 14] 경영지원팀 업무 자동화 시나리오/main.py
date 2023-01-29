import time
import random
import pyexcel as px


# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 생성할 개인정보 파일 개수를 정의합니다.
NUM_SAMPLES = 100

# 이메일 생성에 사용할 샘플 글자들을 정의합니다.
alphabet_samples = "abcdefghizklmnopqrstuvwxyz1234567890"


# 무작위로 선택된 영어 글자를 생성하는 함수입니다.
def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result


# 이름 생성에 사용할 샘플 글자들을 정의합니다.
first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"


# 무작위로 사람 이름을 생성하는 함수입니다.
def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result


# 헤더를 정의합니다.
HEADER = [
    "지급년도", "지급월", "지급일", "성명", "부서", "직책",
    "기본급", "상여금", "식대", "급여계",
    "소득세", "주민세", "고용보험", "국민연금", "장기요양", "건강보험", "공제합계",
    "차감수령액",
    "이메일"
]

position = [
    "사원", "연구원", "대리", "팀장", "차장", "과장", "부장", "인턴"
]


def make_id():
    name = random_name()
    division = random_string(3)
    pst = random.choice(position)
    email = random_string(8) + "@bhban.com"

    return (
        name, division, pst, email
    )


def make_date():
    ctime = time.ctime()
    _, month, date, _, year = ctime.split(" ")

    return (
        year, month, date
    )


def make_salary():
    gibongup = random.randint(250, 500) * 10000
    bonus = int(gibongup * 0.05 / 10) * 10
    food = 100000
    total = gibongup + bonus + food

    tax = int(total * 0.068 / 10) * 10
    citizen_tax = int(total * 0.0068 / 10) * 10
    emp_ins = int(total * 0.02 / 10) * 10
    yeongum = int(total * 0.04 / 10) * 10
    yoyang = int(total * 0.0027 / 10) * 10
    health = int(total * 0.0316 / 10) * 10
    minus_total = tax + citizen_tax + emp_ins + yeongum + yoyang + health

    final_salary = total - minus_total

    return (
        gibongup, bonus, food, total, tax, citizen_tax, emp_ins,
        yeongum, yoyang, health, minus_total, final_salary
    )


# 결과물 파일의 이름을 정의합니다.
filename = "임금명세.xlsx"
# 엑셀파일로 저장할 데이터를 담아 둘 리스트를 만듭니다.
contents = []
contents.append(HEADER)

# NUM_SAMPLES 회수만큼 반복합니다.
for i in range(NUM_SAMPLES):
    year, month, date = make_date()
    name, division, pst, email = make_id()
    gibongup, bonus, food, total, \
    tax, citizen_tax, emp_ins, yeongum, yoyang, health, \
    minus_total, final_salary = make_salary()

    personal_content = [
        year, month, date,
        name, division, pst,
        gibongup, bonus, food, total,
        tax, citizen_tax, emp_ins, yeongum, yoyang, health,
        minus_total, final_salary,
        email
    ]

    contents.append(personal_content)

# 완성된 엑셀파일을 저장합니다.
px.save_as(array=contents, dest_file_name=filename)

# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")