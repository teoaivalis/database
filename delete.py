from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from csv_reader import 	read_the_file
from split import div_first_last

def delete_store(store_id = 0,condition = ''):
    if store_id == 0 and condition == '':
        query = "DELETE FROM store;"
        try:
            db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif store_id != 0:
        query = "DELETE FROM store WHERE store_id = '"
		query += store_id
		query +="';"
    else:
		query = "DELETE FROM store WHERE  "
		query += condition
		query +=";"
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()




def delete_customer(card_id = 0,condition = ''):
    if card_id == 0 and condition == '':
        query = "DELETE FROM customer;"
        try:
            db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif card_id != 0:
        query = "DELETE FROM customer WHERE card_id = "
		query += card_id
		query +="';"
	else:
		query = "DELETE FROM customer WHERE  "
		query += condition
		query +=";"
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()





def delete_transaction (transaction_id = 0,condition = ''):
    if transaction_id == 0 and condition == '':

        query = "DELETE FROM transaction;"
        try:
            db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif transaction_id!= 0:
		query = "DELETE FROM transaction WHERE transaction_id = "
		query += transaction_id
		query += ";"
	else:
		query = "DELETE FROM transaction WHERE "
		query += condition
		query += ";"
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()





def delete_type(type_id = 0,condition = ''):
    if type_id == 0 and condition == '':
        query = "DELETE FROM type;"
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif type_id!= 0:
		query = "DELETE FROM type WHERE type_id = "
		query += type_id
		query += "';"
	else:
		query = "DELETE FROM type WHERE "
		query += condition
		query += ";"

    try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()




def delete_product (product_id = 0,condition = ''):
    if product_id == 0 and condition == '':
        query = "DELETE FROM product;"
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif product_id!= 0:
		query = "DELETE FROM product WHERE product_id = "
		query += product_id
		query += "';"
	else:
		query = "DELETE FROM product WHERE "
		query += condition
		query += ";"

    try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()






def delete_past_prices (date_of_change = '',condition =''):
    if date_of_change == '' and condition == '':
        query = "DELETE FROM past_prices;"
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif date_of_change!= '':
		query = "DELETE FROM past_prices WHERE date_of_change = "
		query += Staff_StaffID
		query += "';"
	else:
		query = "DELETE FROM past_prices WHERE "
		query += condition
		query += ";"
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()









def delete_has (store_id_has = 0,product_id_has = 0,condition = ''):
    if store_id_has == '0':
        store_id_has = 0
    if product_id_has == '0':
        product_id_has = 0
    if store_id_has == 0 and product_id_has == 0 and condition =='':
        query = "DELETE FROM has;"
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif store_id_has!= 0 and product_id_has!= 0:
		query = "DELETE FROM has WHERE MemberID = "
		query += store_id_has
		query += ", product_id_has = '"
		query += product_id_has
		query += ";"
	else:
		query = "DELETE FROM has WHERE "
		query += condition
		query += ";"
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()






def delete_customer_points (card_id_points = 0,condition =''):
    if card_id_points == 0 and condition == '':
        query = "DELETE FROM customer_points;"
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif card_id_points!= 0:
		query = "DELETE FROM customer_points WHERE card_id_points = '"
		query += card_id_points
		query += "';"
	else:
		query = "DELETE FROM customer_points WHERE "
		query += condition
		query += ";"
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()



def delete_purchases (product_id_purchases = 0,card_id_purchases = 0, transaction_id_purchases = 0, store_id_purchases = 0, condition = ''):
    if product_id_purchases == '0':
        product_id_purchases = 0
    if card_id_purchases == '0':
        card_id_purchases = 0
    if transaction_id_purchases == '0':
        transaction_id_purchases = 0
    if store_id_purchases == '0':
        store_id_purchases = 0

    if product_id_purchases == 0 and card_id_purchases == 0 and transaction_id_purchases == 0 and store_id_purchases == 0 and condition =='':
        query = "DELETE FROM purchases;"
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)

			cursor = conn.cursor()
			cursor.execute(query)

			if cursor.lastrowid:
				print('done')
			else:
				print('last insert id not found')

			conn.commit()
		except Error as error:
			print(error)

		finally:
			cursor.close()
			conn.close()

    elif product_id_purchases!= 0 and card_id_purchases!= 0 and transaction_id_purchases != 0 and store_id_purchases != 0:
		query = "DELETE FROM purchases WHERE product_id_purchases = "
		query += product_id_purchases
		query += ", card_id_purchases = '"
		query += card_id_purchases
        query += ", transaction_id_purchases = '"
		query += transaction_id_purchases
        query += ", store_id_purchases = '"
		query += store_id_purchases
		query += ";"
    else:
		query = "DELETE FROM purchases WHERE "
		query += condition
		query += ";"
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last insert id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
    
