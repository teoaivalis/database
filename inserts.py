from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from csv_reader import 	read_the_file


def insert_store(store_id,square_meters, opening_hour, closing_hour, city, postal_code,street_name,street_number):
	 query = "INSERT INTO store VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
	 args = (store_id,square_meters, opening_hour, closing_hour, city, postal_code, street_name,street_number)
	 try:
		 db_config = read_db_config()
		 conn = MySQLConnection(**db_config)

		 cursor = conn.cursor()
		 cursor.execute(query, args)

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



def insert_has(corridor,shelf,store_id_has,product_id_has):
	query = "INSERT INTO has VALUES(%s,%s,%s,%s)"
	args = (corridor,shelf,store_id_has,product_id_has)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

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




def insert_product(product_id,product_name,current_price,special_store_label):
    query = "INSERT INΤΟ product VALUES(%s,%s,%s,%s)"
    args = (product_id,product_name,current_price,special_store_label)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

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




def insert_used_to_cost(product_id_used,date_of_change_used):
	query = "INSERT INTO used_to_cost VALUES(%s,%s)"
	args = (product_id_used,date_of_change_used)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

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






def insert_past_prices(date_of_change,past_price_of_product):
	query = "INSERT INTO past_prices VALUES(%s,%s,%s)"
	args = (date_of_change,past_price_of_product)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

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









def insert_product_type(type_id,name_of_type):
	query = "INSERT INTO product_type VALUES(%s,%s,%s)"
	args = (type_id,name_of_type)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

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










def insert_purchases(quantity,product_id_purchases,card_id_purchases,transaction_id_purchases,store_id_purchases):
	query = "INSERT INTO purchases VALUES(%s,%s,%s,%s)"
	args = (quantity,product_id_purchases,card_id_purchases,transaction_id_purchases,store_id_purchases)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

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

def insert_customer_points(total_cost_of_customer_purchases,card_id_points):
	query = "INSERT INTO customer_points VALUES(%s,%s)"
	args = (total_cost_of_customer_purchases,card_id_points)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

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




def insert_transaction(transaction_id,time_of_transaction,date_of_transaction,means_of_payment,total_cost,total_amount_of_products):
	query = "INSERT INTO transaction VALUES(%s,%s,%s,%s,%s,%s)"
	args = (transaction_id,time_of_transaction,date_of_transaction,means_of_payment,total_cost,total_amount_of_products)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

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


def insert_customer(card_id,customers_city,customers_postal_code,customers_street_name,customers_street_number,first_name,second_name,last_name,marital_status,number_of_kids,sex,phone_number,birthday):
    query = "INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (card_id,customers_city,customers_postal_code,customers_street_name,customers_street_number,first_name,second_name,last_name,marital_status,number_of_kids,sex,phone_number,birthday)
    try:
    	db_config = read_db_config()
    	conn = MySQLConnection(**db_config)

    	cursor = conn.cursor()
    	cursor.execute(query, args)

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

def main():
	file_name = "store.csv"
	for x in read_the_file(file_name):
		insert_store(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])

	file_name = "has.csv"
	for x in read_the_file(file_name):
		insert_has(x[0],x[1],x[2],x[3])

	file_name = "product.csv"
	for x in read_the_file(file_name):
		insert_has(x[0],x[1],x[2],x[3])

	file_name = "usedtocost.csv"
	for x in read_the_file(file_name):
		insert_has(x[0],x[1])

    #file_name = "pastprices.csv"
	#for x in read_the_file(file_name):
	#	insert_past_prices(x[0],x[1])

	file_name = "type.csv"
	for x in read_the_file(file_name):
		insert_product_type(x[0],x[1])

    #file_name = "purchases.csv"
	#for x in read_the_file(file_name):
	#	insert_purchases(x[0],x[1],x[2],x[3],x[4])

	file_name = "customerpoints.csv"
	for x in read_the_file(file_name):
		insert_customer_points(x[0],x[1])

	file_name = "transaction.csv"
	for x in read_the_file(file_name):
		insert_transaction(x[0],x[1],x[2],x[3],x[4],x[5])

	file_name = "customer.csv"
	for x in read_the_file(file_name):
		insert_customer(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12])


if __name__ == '__main__':
	main()
