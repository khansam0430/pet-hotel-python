from flask import Flask
import time
from flask import request, jsonify
app = Flask(__name__)
import requests
import psycopg2




@app.route('/pets', methods=['GET', 'POST', 'DELETE', 'PUT'])
def pets():
    if request.method == 'GET':
        return pet_get()
    elif request.method == 'POST':
        return pet_post()
    elif request.method == 'DELETE':
        return pet_delete()
    elif request.method == 'PUT':
        return update_pet()

@app.route('/owners', methods=['GET','POST', 'DELETE', 'PUT'])
def owners():
    if request.method == 'GET':
        return owners_get()
    elif request.method == 'POST':
        return owners_post()
    elif request.method == 'DELETE':
        return owners_delete()
    elif request.method == 'PUT':
        return update_owner()
  

def pet_get():
        connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from pets"
        cursor.execute(postgreSQL_select_Query)
        records = cursor.fetchall() 
        results = []
        
        print("Print each row and it's columns values")
        for row in records:
            obj = {
                'id' : row[0],
                'name' : row[1],
                'pet' : row[2]
            }
            results.append(obj)
        response = jsonify(results)
        # response.status_code = 200
        cursor.close()
        connection.close()
        return response 
            # print("PostgreSQL connection is closed")

def pet_post():
        connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
        cursor = connection.cursor()
       
        cursor.execute("INSERT INTO pets (owner, pet, breed, color, checked_in) VALUES ('Duncan', 'Fluffy', 'corgi', 'brown', '4/2/2020')")
        connection.commit()
        cursor.close()
        connection.close()
        return ('success post')
        
def pet_delete(pet_id):
    # pet_id = 2
    delete_sql = "DELETE FROM pets WHERE id = %s"
    connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
    cursor = connection.cursor()
    
    cursor.execute(delete_sql, (pet_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return ('success delete pet')

    # delete_sql='DELETE FROM table_1 WHERE id = %s;'  	
    # cur.execute(delete_sql, (value_1,))

def update_pet(date, pet_id):
    # date = '4/22/2020'
    # pet_id = 1
    update_sql = "UPDATE pets SET checked_in = %s WHERE id = %s"
    connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
    cursor = connection.cursor()
    
    cursor.execute(update_sql, (date, pet_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return('succesfully updated pet')


def owners_get():
        connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from owners"
        cursor.execute(postgreSQL_select_Query)
        records = cursor.fetchall() 
        results = []
        print("Print each row and it's columns values")
        for row in records:
            obj = {
                "id" : row[0],
                "name" : row[1], 
                "number of pets": row[2]
            }
            results.append(obj)
        response = jsonify(results)
        cursor.close()
        connection.close()
        return response 
        # print("PostgreSQL connection is closed")

def owners_post():
        connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
        cursor = connection.cursor()
       
        cursor.execute("INSERT INTO owners (name) VALUES ('Duncan')")
        connection.commit()
        cursor.close()
        connection.close()
        return ('success owners post')

def owners_delete(owner_id):
    # owners_id = 1
    delete_sql = "DELETE FROM owners WHERE id = %s"
    connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
    cursor = connection.cursor()
    
    cursor.execute(delete_sql, (owner_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return ('success owners delete')

def update_owner(num_pets, owner_id):
    # num_pets = '4'
    # owner_id = 1
    update_sql = "UPDATE owners SET num_pets = %s WHERE id = %s"
    connection = psycopg2.connect(user="kylegreene",
                                    password="",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="pet-hotel")
    
    cursor = connection.cursor()
    
    cursor.execute(update_sql, (num_pets, owner_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return('succesfully updated owner')
