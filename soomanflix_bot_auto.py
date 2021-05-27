from datetime import datetime
from discord.ext import tasks
import discord
import time

tm = time.localtime(time.time())
yoil = tm.tm_wday
client = discord.Client()

TOKEN = 'ODQ2NjMwMzA4Mjg3MzQ4NzU4.YKyT6w.q7OaAknoDe7uGTquge3LTMedFQc'


조회 = '08:55'#24hrs
일교시 = '09:10'
이교시 = '10:05'
삼교시 = '11:00'
사교시 = '11:55'
오교시 = '13:40'
육교시 = '14:35'
칠교시 = '15:30'

channel_id = '847281760286801940'



@client.event
async def on_ready():
    print('Bot Online.')
    time_check.start()
    yoil = tm.tm_wday

@tasks.loop(seconds=10.0)
async def time_check():
    now = datetime.strftime(datetime.now(), '%H:%M')
    channel = client.get_channel(int(channel_id))

    
    과학 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    과학.add_field(name = "과목", value = "과학", inline = False)
    과학.add_field(name = "줌 주소", value = "https://zoom.us/j/9394123711?pwd=V01tUjlIbW9FMkFKTU5uM0ZVRmFUQT09", inline = False)
    과학.add_field(name = "줌 아이디", value = "회의 아이디 : 939 412 3711, 비번 : 1234 ", inline = False)
    과학.set_footer(text="힘내서 열심히!")



    역사 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    역사.add_field(name = "과목", value = "역사", inline = False)
    역사.add_field(name = "줌 주소", value = "https://us02web.zoom.us/j/7567377665?pwd=SlRqMXdhR3NxWENhK3FBaXo3T3NiQT09", inline = False)
    역사.add_field(name = "줌 아이디", value = "회의 ID: 756 737 7665, 암호: uU1t5T", inline = False)
    역사.set_footer(text="힘내서 열심히!")


    국어 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    국어.add_field(name = "과목", value = "국어", inline = False)
    국어.add_field(name = "줌 주소", value = "https://us02web.zoom.us/j/5988085194?pwd=bVN4eUhkQnB2NDg2OHFyc0hYU3Npdz09", inline = False)
    국어.add_field(name = "줌 아이디", value = "회의 ID: 598 808 5194, 암호: 000000", inline = False)
    국어.set_footer(text="힘내서 열심히!")


    정보 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    정보.add_field(name = "과목", value = "정보", inline = False)
    정보.add_field(name = "줌 주소", value = "https://us02web.zoom.us/j/5168362485?pwd=TVNtOWF3NnNJZEt6L2FFODBFSW4yUT09", inline = False)
    정보.add_field(name = "줌 아이디", value = "회의 ID: 516 836 2485, 암호: 2485", inline = False)
    정보.set_footer(text="힘내서 열심히!")



    영어 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    영어.add_field(name = "과목", value = "영어", inline = False)
    영어.add_field(name = "줌 주소", value = "https://zoom.us/j/2160326605?pwd=eHdxRDlDMG0wMGo2QjM0UlI4cTJmUT09", inline = False)
    영어.add_field(name = "줌 아이디", value = "회의 ID: 216 032 6605, 암호: BthfD6", inline = False)
    영어.set_footer(text="힘내서 열심히!")



    독서 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    독서.add_field(name = "과목", value = "독서", inline = False)
    독서.add_field(name = "줌 주소", value = "https://us02web.zoom.us/j/5988085194?pwd=bVN4eUhkQnB2NDg2OHFyc0hYU3Npdz09", inline = False)
    독서.add_field(name = "줌 아이디", value = "회의 ID: 598 808 5194, 암호: 000000", inline = False)
    독서.set_footer(text="힘내서 열심히!")


    음악 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    음악.add_field(name = "과목", value = "음악", inline = False)
    음악.add_field(name = "줌 주소", value = "https://zoom.us/j/2739828430?pwd=VVZpUkIvL1pWNENzc3cyWWRvQ002UT09", inline = False)
    음악.add_field(name = "줌 아이디", value = "회의 ID: 273 982 8430, 암호: 54321 ", inline = False)
    음악.set_footer(text="힘내서 열심히!")

    체육 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    체육.add_field(name = "과목", value = "체육", inline = False)
    체육.add_field(name = "줌 주소", value = "https://zoom.us/j/4442756306?pwd=dnR6Wlp1SXUvVDJ0T3E3Q1NyZmJBUT09", inline = False)
    체육.add_field(name = "줌 아이디", value = "회의 ID: 444 275 6306, 암호: 0000", inline = False)
    체육.set_footer(text="힘내서 열심히!")



    중국어 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    중국어.add_field(name = "과목", value = "중국어", inline = False)
    중국어.add_field(name = "줌 주소", value = "https://us04web.zoom.us/j/8694988541?pwd=eGlFc2ZCSXI0bTVVa0hqQ2N0NUI4QT09", inline = False)
    중국어.add_field(name = "줌 아이디", value = "회의 ID: 869 498 8541 암호 : xzg424 ", inline = False)
    중국어.set_footer(text="힘내서 열심히!")



    스클 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    스클.add_field(name = "과목", value = "스포츠 클럽", inline = False)
    스클.add_field(name = "외발", value = "회의 ID: 516 836 2485 암호: 2485", inline = False)
    스클.add_field(name = "댄스핏", value = "회의 ID: 981 005 1152 암호: yuni111", inline = False)
    스클.add_field(name = "축구", value = "회의 ID: 444 275 6306 암호: 0000", inline = False)
    스클.add_field(name = "농구", value = "회의 ID: 315 080 0356  암호: 12345", inline = False)
    스클.add_field(name = "배트민턴", value = "회의 ID: 792 755 4583 암호: cE246G", inline = False)
    스클.add_field(name = "탁구", value = "회의ID : 878 254 6187 암호 : SMuFp9", inline = False)
    스클.add_field(name = "까롬", value = "회의 ID: 273 982 8430 암호: 54321", inline = False)
    스클.set_footer(text="힘내서 열심히!")


    사회 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    사회.add_field(name = "과목", value = "사회", inline = False)
    사회.add_field(name = "줌 주소", value = "https://zoom.us/j/4240791198?pwd=dFNKb1Ivc%20it1emZOY0cvNXVNcWZFdz09", inline = False)
    사회.add_field(name = "줌 아이디", value = "회의 ID: 424 079 1198 암호: 3qJnYr", inline = False)
    사회.set_footer(text="힘내서 열심히!")



    수학 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    수학.add_field(name = "과목", value = "수학", inline = False)
    수학.add_field(name = "줌 주소", value = "https://us02web.zoom.us/j/7921402448?pwd=blpUZjRnVHZXMlJjR3Y5NDJJSTMrUT09", inline = False)
    수학.add_field(name = "줌 아이디", value = "회의 ID: 792 140 2448, 암호: 12345 ", inline = False)
    수학.set_footer(text="힘내서 열심히!")




    진로 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    진로.add_field(name = "과목", value = "진로", inline = False)
    진로.add_field(name = "줌 주소", value = "https://zoom.us/j/8094953713?pwd=aC9Oc1RqK1dMcmlBaXBaY2lFK3hpdz09", inline = False)
    진로.add_field(name = "줌 아이디", value = "회의 ID: 809 495 3713, 암호: 0000", inline = False)
    진로.set_footer(text="힘내서 열심히!")


    동아리 = discord.Embed(title=":book: 5분 뒤 수업을 시작해요!", color=0x62c1cc)
    동아리.add_field(name = "슬기로운 세계시민", value = "회의 ID: 420 646 1131 암호: k343434", inline = False)
    동아리.add_field(name = "사방팔방 역사탐구", value = "회의 ID: 756 737 7665 암호: uU1t5T", inline = False)
    동아리.add_field(name = "재미있는 컬러링의 세계", value = "회의 ID: 491 577 8498 암호: 1234", inline = False)
    동아리.add_field(name = "생활 속 음악 세상", value = "회의 ID: 792 755 4583 암호: cE246G", inline = False)
    동아리.add_field(name = "과학책 평가하기(장지숙)", value = "회의 ID: 826 5720 3683 암호: 121314", inline = False)
    동아리.add_field(name = "음악으로 힐링하기", value = "회의 ID: 273 982 8430 암호: 54321", inline = False)
    동아리.set_footer(text="힘내서 열심히!")


    if now == str(조회):
        await channel.send(embed = 조회)

    elif now == 일교시:
        if yoil == 0:
            await channel.send(embed = 영어)
        elif yoil == 1:
            await channel.send(embed = 영어)
        elif yoil == 2:
            await channel.send(embed = 수학)
        elif yoil == 3:
            await channel.send(embed = 역사)
        elif yoil == 4:
            await channel.send(embed = 국어)

    elif now == 이교시:
        if yoil == 0:
            await channel.send(embed = 국어)
        elif yoil == 1:
            await channel.send(embed = 사회)
        elif yoil == 2:
            await channel.send(embed = 체육)
        elif yoil == 3:
            await channel.send(embed = 과학)
        elif yoil == 4:
            await channel.send(embed = 중국어)


    elif now == 삼교시:
        if yoil == 0:
            await channel.send(embed = 체육)
        elif yoil == 1:
            await channel.send(embed = 진로)
        elif yoil == 2:
            await channel.send(embed = 과학)
        elif yoil == 3:
            await channel.send(embed = 정보)
        elif yoil == 4:
            await channel.send(embed = 과학)


    elif now == 사교시:
        if yoil == 0:
            await channel.send(embed = 과학)
        elif yoil == 1:
            await channel.send(embed = 중국어)
        elif yoil == 2:
            await channel.send(embed = 동아리)
        elif yoil == 3:
            await channel.send(embed = 영어)
        elif yoil == 4:
            await channel.send(embed = 사회)

    elif now == 오교시:
        if yoil == 0:
            await channel.send(embed = 음악)
        elif yoil == 1:
            await channel.send(embed = 역사)
        elif yoil == 2:
            await channel.send(embed = 국어)
        elif yoil == 3:
            await channel.send(embed = 독서)
        elif yoil == 4:
            await channel.send(embed = 영어)

    elif now == 육교시:
        if yoil == 0:
            await channel.send(embed = 수학)
        elif yoil == 1:
            await channel.send(embed = 스클)
        elif yoil == 2:
            await channel.send(embed = 사회)
        elif yoil == 3:
            await channel.send(embed = 음악)
        elif yoil == 4:
            await channel.send(embed = 수학)

    elif now == 일교시:

        if yoil == 1:
            await channel.send(embed = 수학)

        elif yoil == 3:
            await channel.send(embed = 체육)

client.run(TOKEN)