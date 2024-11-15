from create_database import create_database
import sqlite3

connection = sqlite3.connect('property.db')
cursor = connection.cursor()

Database = create_database()

with open('PROP_10000.TXT') as f:
    lines = [line.rstrip() for line in f]
    
    #Get list of all the keys and values from create_database.py
    keys = Database.keys
    values = Database.values
    tuple_keys = tuple(i for i in keys) #Creating tuple of keys

    #Traverse every line while accessing values for substring
    #Create string with the substring and add it to separate array
    for i in range(len(lines)):
        values_array = []
        for j in range(len(values)):
            element = lines[i][int(values[j][1])-1:int(values[j][2])]
            values_array.append(element)
        tuple_values = tuple(x for x in values_array)
        insert_prop = """INSERT INTO prop"""+str(tuple_keys)+" VALUES"+str(tuple_values)
        #insert_prop = """INSERT INTO prop(prop_id,prop_type_cd) VALUES (123456789123, 12345)"""
        cursor.execute(insert_prop)

    connection.commit()
    connection.close()

    
    
                  

 

