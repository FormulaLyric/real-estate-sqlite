import PyPDF2
import json
import re
import sqlite3

class create_database:
   """
   Objective:
   Using the PDF file, create a script that will build the table `prop` necessary to hold all data from the `PROP.TXT` file. 
   You may assume that all numeric values are integers and date fields are strings. Dates will need to be converted when inserted below. 
   You do not have to load all 400+ fields. Start with `prop_id` and end with `land_acres`. Any fields named `filler` can be skipped.
   This script should delete the `prop` table if it exists prior to rebuilding. 
   """
   
   #Creating a pdf file object
   pdf_file = open('New-Legacy8.0.25_2-Appraisal Export Layout.pdf', 'rb')

   #Creating a pdf reader object
   pdfReader = PyPDF2.PdfFileReader(pdf_file)
   number_of_pages = pdfReader.getNumPages()
   page = pdfReader.getPage(0) #This value here will need to be changed
   page_content = page.extractText()
   #print(page_content)

   #Creating json object to store all field names and data types
   field_names = {}
   #Turns field name and data type fields into json 
   def get_data(page_content, page_number_element):
       _dict = {}
       page = page_content.splitlines()
       i = page_number_element
       """
       if page_number == 0: #For first page only
            i = 43
       elif page_number == 1: #For second page only
            i = 10
       """
       while i<len(page):
         if '_' not in page[i]:
            return
         if 'filler' in page[i]:
            return
         if re.search("entity_agent_id",page[i]): #Stop after land_acres on second page
            break
         field_and_data = page[i].split(" ")
         key, value = field_and_data[0], field_and_data[1]
         start, end = field_and_data[2], field_and_data[3]
         _dict[key.strip()] = value.strip(), start, end
         #field_names.update(_dict)
         return _dict

   #get_data method works     
   page_data = get_data(page_content,45)
   json_data = json.dumps(page_data, indent=4)
   #print(json_data)

   #Go through all the pages and apply the get_data method, all the field keys and data values should be added to a
   #json object so that it can be traversed when making the SQL table
   total_json = []
   page_number = 0
   while page_number <=2:
      pages = pdfReader.getPage(page_number)
      pages_content = pages.extractText()
      if page_number == 0:
         a = 43
         while a<52:
            data_one = get_data(pages_content,a)
            if data_one == None:
                a+=1
            else:
               data_json = json.dumps(data_one)
               total_json.append(data_one)
               #print(total_json)
               a+=1
      elif page_number == 1:
         b = 0
         while b<52:
            data_two = get_data(pages_content,b)
            if data_two == None:
                b+=1
            else:
               data_json_two = json.dumps(data_two)
               total_json.append(data_two)
               #print(total_json)
               b+=1
      elif page_number == 2:
        c = 0
        while c<52: #random value
           data_three = get_data(pages_content,c)
           if data_three == None:
              c+=1
           else:
              data_json_three = json.dumps(data_three)
              total_json.append(data_three)
              #print(total_json)
              c+=1   
      page_number+=1
   #print(total_json)
     
   #print(total_json.keys())
   keys_array = []
   values_array = []
   keys = []
   values = []
   length = len(total_json)
   for i in range(length):
    keys_array.append(list(total_json[i].keys()))
    values_array.append(list(total_json[i].values()))
   lengths = len(keys_array)
   lengthys = len(values_array)
   for k in range(lengths):
    keys.append(keys_array[k][0])
   for z in range(lengthys):
    values.append(values_array[z][0])
   #print(keys)
   #print(values)
   
   #Creating the prop table
   connection = sqlite3.connect('property.db')
   cursor = connection.cursor()
   cursor.execute("DROP TABLE IF EXISTS prop")
   create_table = """ CREATE TABLE IF NOT EXISTS prop(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT)
                  """
   cursor.execute(create_table)
   
   #Successfully created table with column names and constraints
   l1 = len(keys)
   for l in range(l1):
    modify = """ALTER TABLE prop
                ADD COLUMN """ +keys[l]+" "+values[l][0]
    cursor.execute(modify)

   connection.commit()
 
   
    
        
