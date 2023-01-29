#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_tweet as tb


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# Ʈ���� ������� ���� ������ �Է¹޽��ϴ�.
filename = sys.argv[3]

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = tb.TwitterBot(filename)

# �α����� �õ��մϴ�.
BOT.login(id, ps)

# Ʈ���Ϳ� ��� ����� �ø��ϴ�.
BOT.tweet_all()


# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
