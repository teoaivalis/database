from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
from split import div_first_last


def update_store (store_id = 0, square_meters = 0, opening_hour = 0, closing_hour = 0, city = '', postal_code = 0, street_name = '', street_number = 0):
    coma_counter = [0]*8
    attribute_list = ["store_id = ", "square_meters = ", "opening_hour = ", "closing_hour = ", "city = ", "postal_code = ", "street_name = ", "street_number = "]
    i = 0
    if store_id != 0:
		coma_counter[0] +=1
	if square_meters != 0:
		coma_counter[1] +=1
	if opening_hour != 0:
		coma_counter[2] +=1
	if closing_hour != 0:
		coma_counter[3] +=1
	if city != '':
		coma_counter[4] +=1
	if postal_code != 0:
		coma_counter[5] +=1
	if street_name != '':
		coma_counter[6] +=1
	if street_number != 0:
		coma_counter[7] +=1

	j = sum(coma_counter)
	List = ["UPDATE store SET "]



    if store_id != 0 and j!=1:
		List += attribute_list[0]
		List += store_id
		List += "',"
		j = j-1
	elif store_id != 0 and j==1:
		List += attribute_list[0]
		List += store_id
		List += ""


	if square_meters != 0 and j!=1:
		List += attribute_list[1]
		List += square_meters
		List += "',"
		j = j-1
	elif square_meters != 0 and j==1:
		List += attribute_list[1]
		List += square_meters
		List += ""


	if opening_hour != 0 and j!=1:
		List += attribute_list[2]
		List += opening_hour
		List += ","
		j = j-1
	elif opening_hour != 0 and j==1:
		List += attribute_list[2]
		List += opening_hour
		List += ""


	if closing_hour != 0 and j!=1:
		List += attribute_list[3]
		List += closing_hour
		List += ","
		j = j-1
	elif closing_hour != 0 and j==1:
		List += attribute_list[3]
		List += closing_hour
		List += ""

	if city != '' and j!=1:
		List += attribute_list[4]
		List += city
		List += "',"
		j = j-1
	elif city != '' and j==1:
		List += attribute_list[4]
		List += city
		List += "'"

	if postal_code != 0 and j!=1:
		List += attribute_list[5]
		List += postal_code
		List += "'"
		j = j-1
	elif postal_code != 0 and j==1:
		List += attribute_list[5]
		List += postal_code
		List += ""

	if street_name != '' and j!=1:
		List += attribute_list[6]
		List += street_name
		List += "',"
		j = j-1
	elif street_name != '' and j==1:
		List += attribute_list[6]
		List += street_name
		List += "'"

	if street_number != 0 and j!=1:
		List += attribute_list[7]
		List += street_number
		List += "'"
		j = j-1
    elif street_number != 0 and j==1:
		List += attribute_list[7]
		List += street_number
		List += ""

	if store_id!= 0 or  condition!='':
		List += " Where "
		if store_id != '':
			List += " store_id = '"
			List += store_id
			List += "'"
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()















def update_has (corridor = 0, shelf = 0, store_id_has = 0, product_id_has = 0):
    coma_counter = [0]*2
    attribute_list = ["corridor = '", "shelf = '"]
    i = 0
    if corridor != 0:
		coma_counter[0] +=1
	if shelf != 0:
		coma_counter[1] +=1

    j = sum(coma_counter)
	List = ["UPDATE has SET "]

    if corridor != 0 and j!=1:
		List += attribute_list[0]
		List += corridor
		List += "',"
		j = j-1
	elif corridor != 0 and j==1:
		List += attribute_list[0]
		List += corridor
		List += ""

	if shelf != 0 and j!=1:
		List += attribute_list[1]
		List += shelf
		List += "',"
		j = j-1
	elif shelf != 0 and j==1:
		List += attribute_list[1]
		List += shelf
		List += ""

	if  (store_id_has != 0 and product_id_has!= 0) or  condition!='':
		List += " Where "
		if store_id_has != 0 and product_id_has != 0:
			List += "store_id_has = '"
			List += store_id_has
			List += "', product_id_has = '"
			List += product_id_has
			List += "'"
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()











def update_product_type(type_id = 0, name_of_type = '',condition = ''):
    coma_counter = [0]*2
    attribute_list = ["type_id = '", "name_of_type = '"]
    i = 0

	if type_id != 0:
		coma_counter[0] +=1
	if name_of_type != '':
		coma_counter[1] +=1

    j = sum(coma_counter)
	List = ["UPDATE product_type SET "]

    if type_id != 0 and j!=1:
		List += attribute_list[0]
		List += type_id
		List += "',"
		j = j-1
	elif type_id != 0 and j==1:
		List += attribute_list[0]
		List += type_id
		List += ""


	if name_of_type != '' and j!=1:
		List += attribute_list[1]
		List += name_of_type
		List += "',"
		j = j-1
	elif name_of_type != '' and j==1:
		List += attribute_list[1]
		List += name_of_type
		List += "'"

    if type_id != 0 or  condition!='':
		List += " Where "
		if type_id != 0:
			List += " type_id = '"
			List += type_id
			List += "'"
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()









def update_product(product_id = 0, product_name = '', current_price = 0, special_store_label = '', condition = ''):
    coma_counter = [0]*4
    attribute_list = ["product_id = '", "product_name = '", "current_price = '", "special_store_label = '"]
    i = 0

    if product_id != 0:
		coma_counter[0] +=1
	if product_name != '':
		coma_counter[1] +=1
	if current_price != 0:
		coma_counter[2] +=1
	if special_store_label != '':
		coma_counter[3] +=1
	j = sum(coma_counter)

    if product_id != 0 and j!=1:
		List += attribute_list[0]
		List += product_id
		List += ","
		j = j-1
	elif product_id != 0 and j==1:
		List += attribute_list[0]
		List += product_id
		List += ""


	if product_name != '' and j!=1:
		List += attribute_list[1]
		List += product_name
		List += "',"
		j = j-1
	elif product_name != '' and j==1:
		List += attribute_list[1]
		List += product_name
		List += "'"


	if current_price != 0 and j!=1:
		List += attribute_list[2]
		List += current_price
		List += "',"
		j = j-1
	elif current_price != 0 and j==1:
		List += attribute_list[2]
		List += current_price
		List += ""


	if special_store_label != '' and j!=1:
		List += attribute_list[3]
		List += special_store_label
		List += "',"
		j = j-1
	elif special_store_label != '' and j==1:
		List += attribute_list[3]
		List += special_store_label
		List += "'"

	if product_id != 0 or  condition !='':
		List += " Where "
		if product_id != 0:
			List += "product_id = '"
			List += product_id
			List += "'"
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()










def update_transaction(transaction_id = 0, time_of_transaction = 0, date_of_transaction = '', means_of_payment = '', total_cost = 0, total_amount_of_products = 0, condition = ''):
    coma_counter = [0]*6
	attribute_list = ["transaction_id = ", "time_of_transaction = '", "date_of_transaction = '", "means_of_payment = '", "total_cost = '", "total_amount_of_products = '"]
	i = 0

	if transaction_id != 0:
		coma_counter[0] +=1
	if time_of_transaction != 0:
		coma_counter[1] +=1
	if date_of_transaction != '':
		coma_counter[2] +=1
	if means_of_payment != '':
		coma_counter[3] +=1
    if total_cost != 0:
		coma_counter[4] +=1
	if total_amount_of_products != 0:
		coma_counter[5] +=1
	j = sum(coma_counter)
	List = ["UPDATE transaction SET "]

	if transaction_id != 0 and j!=1:
		List += attribute_list[0]
		List += transaction_id
		List += ","
		j = j-1
	elif transaction_id != 0 and j==1:
		List += attribute_list[0]
		List += transaction_id
		List += ""

	if time_of_transaction != 0 and j!=1:
		List += attribute_list[1]
		List += time_of_transaction
		List += "',"
		j = j-1
	elif time_of_transaction != 0 and j==1:
		List += attribute_list[1]
		List += time_of_transaction
		List += ""

	if date_of_transaction != '' and j!=1:
		List += attribute_list[2]
		List += date_of_transaction
		List += "',"
		j = j-1
	elif date_of_transaction != '' and j==1:
		List += attribute_list[2]
		List += date_of_transaction
		List += "'"

	if means_of_payment != '' and j!=1:
		List += attribute_list[3]
		List += means_of_payment
		List += "',"
		j = j-1
	elif means_of_payment != '' and j==1:
		List += attribute_list[3]
		List += means_of_payment
		List += "'"

	if total_cost != 0 and j!=1:
		List += attribute_list[4]
		List += total_cost
		List += "',"
		j = j-1
	elif total_cost != 0 and j==1:
		List += attribute_list[4]
		List += total_cost
		List += ""

	if total_amount_of_products != 0 and j!=1:
		List += attribute_list[5]
		List += total_amount_of_products
		List += "',"
		j = j-1
	elif total_amount_of_products != 0 and j==1:
		List += attribute_list[5]
		List += total_amount_of_products
		List += ""

	if transaction_id != 0 or  condition!='':
		List += " Where "
		if transaction_id != 0:
			List += "transaction_id = '"
			List += transaction_id
			List += "'"
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()










def update_customer (card_id = 0, customers_city = '', customers_postal_code = 0, customers_street_name = '', customers_street_number = 0, first_name = '', second_name = '', last_name = '', marital_status = '', number_of_kids = 0, sex = '', phone_number = 0, birthday = ''):
    coma_counter = [0]*13
	attribute_list = ["card_id = '", "customers_city = '", "customers_postal_code = ", "customers_street_name = ", "customers_street_number = '", "first_name = '", "second_name = '", "last_name = '", "marital_status = '", "number_of_kids = '", "sex = '", "phone_number = '", "birthday = '"]
	i = 0

	if card_id != 0:
		coma_counter[0] +=1
	if customers_city != '':
		coma_counter[1] +=1
	if customers_postal_code != 0:
		coma_counter[2] +=1
	if customers_street_name != '':
		coma_counter[3] +=1
	if customers_street_number != 0:
		coma_counter[4] +=1
	if first_name != '':
		coma_counter[5] +=1
	if second_name != '':
		coma_counter[6] +=1
	if last_name != '':
		coma_counter[7] +=1
    if marital_status != '':
		coma_counter[8] +=1
	if number_of_kids != 0:
		coma_counter[9] +=1
	if sex != '':
		coma_counter[10] +=1
	if phone_number != 0:
		coma_counter[11] +=1
	if birthday != '':
		coma_counter[12] +=1

	j = sum(coma_counter)
	List = ["UPDATE customer SET "]

    if card_id != 0 and j!=1:
		List += attribute_list[0]
		List += card_id
		List += "',"
		j = j-1
	elif card_id != 0 and j==1:
		List += attribute_list[0]
		List += card_id
		List += ""


	if customers_city != '' and j!=1:
		List += attribute_list[1]
		List += customers_city
		List += "',"
		j = j-1
	elif customers_city != '' and j==1:
		List += attribute_list[1]
		List += customers_city
		List += "'"


	if customers_postal_code != 0 and j!=1:
		List += attribute_list[2]
		List += customers_postal_code
		List += ","
		j = j-1
	elif customers_postal_code != 0 and j==1:
		List += attribute_list[2]
		List += customers_postal_code
		List += ""

    if customers_street_name != '' and j!=1:
		List += attribute_list[3]
		List += customers_street_name
		List += "',"
		j = j-1
	elif street_name != '' and j==1:
		List += attribute_list[3]
		List += street_name
		List += "'"


	if customers_street_number != 0 and j!=1:
		List += attribute_list[4]
		List += customers_street_number
		List += ","
		j = j-1
	elif customers_street_number != 0 and j==1:
		List += attribute_list[4]
		List += customers_street_number
		List += ""

    if first_name != '' and j!=1:
		List += attribute_list[5]
		List += first_name
		List += ","
		j = j-1
	elif first_name != '' and j==1:
		List += attribute_list[5]
		List += first_name
		List += "'"

    if second_name != '' and j!=1:
		List += attribute_list[6]
		List += second_name
		List += ","
		j = j-1
	elif second_name != '' and j==1:
		List += attribute_list[6]
		List += second_name
		List += "'"

    if last_name != '' and j!=1:
		List += attribute_list[7]
		List += last_name
		List += ","
		j = j-1
	elif last_name != '' and j==1:
		List += attribute_list[7]
		List += last_name
		List += "'"

    if marital_status != '' and j!=1:
		List += attribute_list[8]
		List += marital_status
		List += ","
		j = j-1
	elif marital_status != '' and j==1:
		List += attribute_list[8]
		List += marital_status
		List += "'"

    if number_of_kids != 0 and j!=1:
		List += attribute_list[9]
		List += number_of_kids
		List += ","
		j = j-1
	elif number_of_kids != 0 and j==1:
		List += attribute_list[9]
		List += number_of_kids
		List += ""

    if sex != '' and j!=1:
		List += attribute_list[10]
		List += sex
		List += ","
		j = j-1
	elif sex != '' and j==1:
		List += attribute_list[10]
		List += sex
		List += "'"

    if phone_number != 0 and j!=1:
		List += attribute_list[11]
		List += phone_number
		List += ","
		j = j-1
	elif phone_number != '' and j==1:
		List += attribute_list[11]
		List += phone_number
		List += ""

    if birthday != '' and j!=1:
		List += attribute_list[12]
		List += birthday
		List += ","
		j = j-1
	elif birthday != '' and j==1:
		List += attribute_list[12]
		List += birthday
		List += "'"

    if customer_id != 0 or  condition!='':
		List += " Where "
		if customer_id != 0:
			List += "customer_id = '"
			List += customer_id
			List += ""
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()











def update_past_prices(date_of_change = '', past_price_of_product = 0, condition = ''):
    coma_counter = [0]*1
    attribute_list = ["date_of_change = '", "past_price_of_product = "]
	i = 0
	if date_of_change != '':
		coma_counter[0] +=1
	if past_price_of_product != 0:
		coma_counter[1] +=1

    j = sum(coma_counter)
	List = ["UPDATE past_prices SET "]

	if date_of_change != '' and j!=1:
		List += attribute_list[0]
		List += date_of_change
		List += "',"
		j = j-1
	elif date_of_change != '' and j==1:
		List += attribute_list[0]
		List += date_of_change
		List += "'"

    if past_price_of_product != 0 and j!=1:
		List += attribute_list[1]
		List += past_price_of_product
		List += ","
		j = j-1
	elif past_price_of_product != 0 and j==1:
		List += attribute_list[1]
		List += past_price_of_product
		List += ""


    if date_of_change!= '' or  condition!='':
		List += " Where "
		if date_of_change != '':
			List += " date_of_change = '"
			List += date_of_change
			List += "'"
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def update_customer_points(card_id_points = 0, total_cost_of_customer_purchases = 0, condition = ''):
    coma_counter = [0]*1
    attribute_list = ["card_id_points = ", "total_cost_of_customer_purchases = "]
	i = 0

    if card_id_points != 0 :
		coma_counter[0] +=1
	if total_cost_of_customer_purchases != 0:
		coma_counter[1] +=1

	j = sum(coma_counter)
	List = ["UPDATE customer_points SET "]

    if card_id_points != 0 and j!=1:
		List += attribute_list[0]
		List += card_id_points
		List += ","
		j = j-1
	elif card_id_points != 0 and j==1:
		List += attribute_list[0]
		List += card_id_points
		List += ""

    if total_cost_of_customer_purchases != 0 and j!=1:
		List += attribute_list[1]
		List += total_cost_of_customer_purchases
		List += ","
		j = j-1
	elif total_cost_of_customer_purchases != 0 and j==1:
		List += attribute_list[1]
		List += total_cost_of_customer_purchases
		List += ""

    if card_id_points != 0 or  condition!='':
		List += " Where "
		if card_id_points != 0:
			List += " card_id_points = '"
			List += card_id_points
			List += ""
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def update_purchases(product_id_purchases = 0, card_id_purchases = 0, transaction_id_purchases = 0, store_id_purchases = 0, quantity = 0, condition = ''):
    coma_counter = [0]*4
    attribute_list = ["product_id_purchases = ", "card_id_purchases = ", "transaction_id_purchases = ", "store_id_purchases = ", "quantity = "]
	i = 0

    if product_id_purchases != 0 :
		coma_counter[0] +=1
	if card_id_purchases != 0:
		coma_counter[1] +=1
    if transaction_id_purchases != 0 :
		coma_counter[2] +=1
	if store_id_purchases != 0:
		coma_counter[3] +=1
    if quantity != 0 :
		coma_counter[4] +=1

    j = sum(coma_counter)
	List = ["UPDATE purchases SET "]


    if product_id_purchases != 0 and j!=1:
		List += attribute_list[0]
		List += product_id_purchases
		List += "',"
		j = j-1
	elif product_id_purchases != 0 and j==1:
		List += attribute_list[0]
		List += product_id_purchases
		List += ""


	if card_id_purchases != 0 and j!=1:
		List += attribute_list[1]
		List += card_id_purchases
		List += "',"
		j = j-1
	elif card_id_purchases != 0 and j==1:
		List += attribute_list[1]
		List += card_id_purchases
		List += ""


	if transaction_id_purchases != 0 and j!=1:
		List += attribute_list[2]
		List += transaction_id_purchases
		List += ","
		j = j-1
	elif transaction_id_purchases != 0 and j==1:
		List += attribute_list[2]
		List += transaction_id_purchases
		List += ""


	if store_id_purchases != 0 and j!=1:
		List += attribute_list[3]
		List += store_id_purchases
		List += ","
		j = j-1
	elif store_id_purchases != 0 and j==1:
		List += attribute_list[3]
		List += store_id_purchases
		List += ""

	if quantity != 0 and j!=1:
		List += attribute_list[4]
		List += quantity
		List += "',"
		j = j-1
	elif quantity != 0 and j==1:
		List += attribute_list[4]
		List += quantity
		List += ""


    if  (product_id_purchases != 0 and card_id_purchases!= 0 and transaction_id_purchases!= 0 and store_id_purchases!= 0) or  condition!='':
		List += " Where "
		if product_id_purchases != 0 and card_id_purchases != 0 and transaction_id_purchases != 0 and store_id_purchases != 0:
			List += " product_id_purchases = '"
			List += product_id_purchases
			List += "', card_id_purchases = '"
			List += card_id_purchases
			List += "', transaction_id_purchases = '"
			List += transaction_id_purchases
			List += "', store_id_purchases = '"
			List += store_id_purchases
            List += "'"
		else:
			List += condition
	List += ";"

	query = ''.join(List)
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query)

		if cursor.lastrowid:
			print('done')
		else:
			print('last update id not found')

		conn.commit()
	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()
