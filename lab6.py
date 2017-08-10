import _mysql

buffer = "true"



def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="skateboard",db="skateshop")
	db.query("""SELECT * FROM decks;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="skateboard",db="skateshop")
	db.query("""SELECT * FROM trucks;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def phillyDecks():
	db = _mysql.connect(host="localhost",user="root",passwd="skateboard",db="skateshop")
	db.query("""SELECT * FROM decks2skateshops where shopID = 1""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()
	

def tokyoDecks():
	db = _mysql.connect(host="localhost",user="root",passwd="skateboard",db="skateshop")
	db.query("""SELECT * FROM decks2skateshops where shopID = 5""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def newYorkDecks():
	db = _mysql.connect(host="localhost",user="root",passwd="skateboard",db="skateshop")
	db.query("""SELECT * FROM decks2skateshops where shopID = 2""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()
	
while buffer:
	print("""
	0.Exit
	1.See Deck Selection
	2.See Truck Selection
	3.See DeckId's in Philadelphia
	4.See DeckId's in NewYork
	5.See DeckId's in Tokyo
	""")
	buffer=input("what would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		phillyDecks()
	if buffer == 4:
		newYorkDecks()
	if buffer == 5:
		tokyoDecks()
	