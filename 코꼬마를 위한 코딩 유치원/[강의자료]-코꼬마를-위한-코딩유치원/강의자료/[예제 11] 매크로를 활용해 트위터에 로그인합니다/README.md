# 매크로를 활용해 트위터에 로그인합니다

매크로를 활용해 로그인을 자동으로 수행하는 방법을 알아봅니다. 

매크로를 활용한 웹 자동화의 기본이 됩니다.

책의 예제에서는 트위터 로그인을 시도합니다. 코드를 수정하시면 여러 사이트의 로그인을 구현할 수 있습니다.

## 사용 방법
> python main.py <SITE\> <ID\> <PS\>

(twitter / daum )

<SITE>에는 로그인하려는 사이트를 입력합니다. 괄호 안의 내용물 중 하나를 입력하세요. 여기 없는 사이트의 로그인을 구현하고 싶으시다면, 주소를 그대로 붙여넣기 하세요. 예를 들어 네이버 로그인을 구현하고 싶으면 <SITE> 위치에 "https://nid.naver.com/nidlogin.login?" 을 입력하면 됩니다. 단, 커서가 자동으로 ID 입력창에 위치하고 있지 않다면 ID 입력창을 클릭하는 코드를 삽입하셔야 합니다.

 <ID\> 에는 아이디를, <PS\>에는 비밀번호를 입력하세요.
 
 이 책의 예제는 아래와 같습니다.
 
 > python main.py twitter bot_automation <PS\> 

## 작동 원리
(1) 로그인 사이트로 이동한다

(2) 아이디를 입력한다

(3) Tab 키를 누른다

(4) 비밀번호를 입력한다

(5) 엔터키를 친다

