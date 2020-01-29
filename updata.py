import os
import sqlite3
from sqlite3 import Error
FOLDER_PATH = r"C:\Users\Aman\Desktop\you" #to_do

con=sqlite3.connect(r"C:\Users\Aman\PycharmProjects\try\site.db")
def insertVideo(con,entities):
    cursorObj=con.cursor()
    cursorObj.execute('INSERT INTO Video(id,start_time,end_time,filepath) VALUES(?,?, ?, ?)', entities)
    con.commit()
    cursorObj.close()


def listDir(dir):
    fileNames=os.listdir(dir)
    for file in fileNames:
        file1 = open(r"C:\Users\Aman\Desktop\myfile.txt","a")#append mode
        a=os.path.abspath(os.path.join(dir,file))
        file1.write(a+'\n')
    file1.close()


def readDir():
    file2=open(r"C:\Users\Aman\Desktop\myfile.txt")
    i=0
    for line in file2:
        i=i+1
        a=int(line[26:40])
        b=int(line[41:55])
        entities=(i,a,b,line)
        insertVideo(con,entities)
    file2.close()

if __name__=='__main__':
    listDir(FOLDER_PATH)
    readDir()
