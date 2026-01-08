import admin
import quiz
import leaderboard
import sqlite3 as db
import os

conn=db.connect("Quiz.db")
cur=conn.cursor()
def main():
    global conn
    while(True):
        os.system("cls")
        choice=int(input('''
        Main Menu
        1)Login
        2)Play Quiz
        3)Show Leader Board
        4)Exit
        Enter your choice:-'''))
        if(choice==1):
            admin.auth(conn)
        elif(choice==2):
            quiz.quizGame(conn)
        elif(choice==3):
            leaderboard.printLeaderBoard(conn)
        elif(choice==4):
            return
        else:
            print("Invalid Choice")




if __name__=="__main__":
    main()