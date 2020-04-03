from flask import Flask
import time
from flask import request, jsonify
app = Flask(__name__)
import requests
import psycopg2




@app.route('/api/pets', methods=['GET', 'POST', 'DELETE', 'PUT'])
def pets():
    if request.method == 'GET':
        return pet_get()
    elif request.method == 'POST':
        return pet_post()
    elif request.method == 'DELETE':
        return pet_delete()
    elif request.method == 'PUT':
        return update_pet()

@app.route('/api/owners', methods=['GET','POST', 'DELETE', 'PUT'])
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
        postgreSQL_select_Query = "SELECT * FROM pets join owners on owners.id = pets.owner_id;"
        cursor.execute(postgreSQL_select_Query)
        records = cursor.fetchall() 
        results = []
        
        print("Print each row and it's columns values", records)
        for row in records:
            obj = {
                'id' : row[0],
                'pet' : row[1],
                'breed' : row[2],
                'color' : row[3],
                'checked_in' : row[4],
                'owner_id' : row[5],
                'owner' : row[7],
            }
            results.append(obj)
        response = jsonify(results)
        # response.status_code = 200
        cursor.close()
        connection.close()
        return response
        # return ({'pets': response}) 
        # print("PostgreSQL connection is closed")

def pet_post():
        connection = psycopg2.connect(user="kylegreene",
                                        password="",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="pet-hotel")
       
        cursor = connection.cursor()
        # get the json coming from our post on the client side
        newPetData = request.get_json()
        newPet = [
            newPetData['pet'],
            newPetData['breed'],
            newPetData['color'],
            newPetData['owner_id'],
        ]
        print('pet to post', newPet)
        insert_sql = "INSERT INTO pets (pet, breed, color, checked_in, owner_id) VALUES (%s, %s, %s, 'no', %s)"
        cursor.execute(insert_sql, (newPet[0], newPet[1], newPet[2], newPet[3]))
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
    deleteData = request.get_json()
    pet_id = [
        deleteData ['deleteId']
    ]
    print('deleteData', deleteData)
    delete_sql = "DELETE FROM pets WHERE id = %s"
    cursor.execute(delete_sql, (deleteData,))
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
                "number_of_pets": row[2]
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
        # newOwnerData=request.get_json()
        # print('data coming from owner post', newOwnerData)
        # newOwner = str(newOwnerData)
        # print('newOwner:', newOwner)
        # insert_sql = "INSERT INTO owners (name) VALUES (%s)"
        # cursor.execute(insert_sql, newOwner)
        # connection.commit()
        # cursor.close()
        # connection.close()
        # return ('success owners post')
        newOwnerData = request.get_json()
        print('newOwnerData:', newOwnerData)
        newOwner = [
            newOwnerData['ownerName'],
            newOwnerData['num_pets'],
        ]
        print('Owner to post', newOwner)
        insert_sql = "INSERT INTO owners (name, num_pets) VALUES (%s, %s)"
        cursor.execute(insert_sql, (newOwner[0], newOwner[1]))
        connection.commit()
        cursor.close()
        connection.close()
        return ('success posting Owner')

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
