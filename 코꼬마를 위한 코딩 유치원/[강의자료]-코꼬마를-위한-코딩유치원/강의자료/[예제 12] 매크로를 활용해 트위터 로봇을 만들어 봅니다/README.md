# 매크로를 활용해 트위터 로봇을 만들어 봅니다

매크로를 활용해 로그인도 자동으로 하고, 트위터에 글도 자동으로 올려 주는 로봇을 만들어 봅니다. 

매크로를 활용한 웹 자동화 기초 훈련입니다.

## 사용 방법
> python main.py <ID\> <PS\> <CONTENTS\> 

 <ID\> 에는 아이디를, <PS\>에는 비밀번호를 입력하세요.
 
 <CONTENTS\> 에는 트위터에 업로드할 내용물이 기록된 파일을 입력합니다.
 
 이 책의 예제는 아래와 같습니다.
 
 > python main.py bot_automation <PS\> contents.txt 

## 작동 원리
#### 로그인
(1) 트위터에 접속하면 아이디 칸에서 커서가 깜빡인다.

(2) 아이디를 입력한다

(3) Tab 키를 누른다

(4) 비밀번호를 입력한다

(5) 엔터키를 친다

#### 글 쓰기
(1) 미리 작성된 내용물을 한 줄씩 불러온다.

(2) 트윗 입력창에 내용물을 붙여넣는다.

(3) 컨트롤 + 엔터키를 쳐서 업로드한다.
