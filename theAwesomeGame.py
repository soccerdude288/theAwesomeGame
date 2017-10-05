#!/usr/bin/python

import mysql.connector


config = {
	'user':'taylor',
	'password':'Taylorcs!',
	'host':'127.0.0.1',
	'database':'theAwesomeGame'
}

#Board is 100x100 (102x102)

#### DB 
####	x (int)
####	y (int)
####	value (int) 1 alive/0 dead


try:
	cnx = mysql.connector.connect(**config)
					
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
	cnx.close()
	
cursor = cnx.cursor()

query = ("SELECT x, y FROM dataPoints WHERE value='1'")

w, h = 33, 33;
oldGameBoard = [[0 for x in range(w)] for y in range(h)] 
newGameBoard = [[0 for x in range(w)] for y in range(h)] 

cursor.execute(query)

for (x, y) in cursor:
	oldGameBoard[x][y] = 1
	
for(x, y) in cursor:
	count = 0;
	#check row above
	if(oldGameBoard[x-1][y-1] == 1):
		count++;
	
	if(oldGameBoard[x][y-1] == 1):
		count++;
	
	if(oldGameBoard[x+1][y-1] == 1):
		count++;
	
	
	#check row
	if(oldGameBoard[x-1][y] == 1):
		count++;
	
	#if(oldGameBoard[x][y] == 1){
	#	count++;
	#}
	if(oldGameBoard[x+1][y] == 1):
		count++;
	
	
	#check row below
	if(oldGameBoard[x-1][y+1] == 1):
		count++;
	
	if(oldGameBoard[x][y+1] == 1):
		count++;
	
	if(oldGameBoard[x+1][y+1] == 1):
		count++;
	
	#check all live cells
	if(count < 2):
		newGameBoard[x][y] = 0
	elif(count < 4 && count >= 2):
		newGameBoard[x][y] = 1	
	else:
		newGameBoard[x][y] = 0

for(x in range(1, 33)):
	for(y in range(1, 33)):
			count = 0;
			#check row above
			if(oldGameBoard[x-1][y-1] == 1):
				count++;
			
			if(oldGameBoard[x][y-1] == 1):
				count++;
			
			if(oldGameBoard[x+1][y-1] == 1):
				count++;
			
			
			#check row
			if(oldGameBoard[x-1][y] == 1):
				count++;
			
			#if(oldGameBoard[x][y] == 1){
			#	count++;
			#}
			if(oldGameBoard[x+1][y] == 1):
				count++;
			
			
			#check row below
			if(oldGameBoard[x-1][y+1] == 1):
				count++;
			
			if(oldGameBoard[x][y+1] == 1):
				count++;
			
			if(oldGameBoard[x+1][y+1] == 1):
				count++;
			
			if(count == 3):
				newGameBoard[x][y] = 1

insertSql = "";				
for(x in range(1, 33)):
	for(y in range(1, 33)):
		if(newGameBoard[x][y] == 1):
			insertSql += "UPDATE dataPoints SET value=1 WHERE x=" + x + " AND y=" + y + ";"
		else:
			insertSql += "UPDATE dataPoints SET value=0 WHERE x=" + x + " AND y=" + y + ";"
			
cursor.execute(insertSql)
cursor.close()