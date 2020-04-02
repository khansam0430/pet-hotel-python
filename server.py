from flask import Flask
from flask import request
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
        
        print("Print each row and it's columns values")
        for row in records:
            print("Id = ", row[0], )
            print("name = ", row[1], )
            print("pet = ", row[2],"\n" )

        cursor.close()
        connection.close()
        return ('success get')  
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
        
def pet_delete():
    connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM pets WHERE id = 3")
    connection.commit()
    cursor.close()
    connection.close()
    return ('success delete')

    # delete_sql='DELETE FROM table_1 WHERE id = %s;'  	
    # cur.execute(delete_sql, (value_1,))

def update_pet():
    connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
    cursor = connection.cursor()
    
    cursor.execute("UPDATE pets SET checked_in = '4/2/2020' WHERE id = 2")
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
        
        print("Print each row and it's columns values")
        for row in records:
            print("Id = ", row[0], )
            print("name = ", row[1], )
            print("number of pets = ", row[2],"\n" )

        cursor.close()
        connection.close()
        return ('success get')  
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

def owners_delete():
    connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM owners WHERE id = 2")
    connection.commit()
    cursor.close()
    connection.close()
    return ('success owners delete')

def update_owner():
    connection = psycopg2.connect(user="kylegreene",
                                    password="",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="pet-hotel")
    
    cursor = connection.cursor()
    
    cursor.execute("UPDATE owners SET num_pets=3 WHERE id = 1")
    connection.commit()
    cursor.close()
    connection.close()
    return('succesfully updated owner')
