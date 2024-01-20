import os
import psycopg2
import json
import git
import pandas as pd


#aggregator transaction

part2="C:/Users/Sujay/New folder/Phone Pe/pulse/data/aggregated/transaction/country/india/state/"
aggregator_trans_list=os.listdir(part2)

col2={"States":[],"Years":[],"Quarter":[], "Transaction_type":[],"Transaction_count":[], "Transaction_amount":[]}

for state in aggregator_trans_list:
    current_state=part2+state+"/"
    year_list=os.listdir(current_state)
    
    for year in year_list:
        current_year=current_state+year+"/"
        file_list=os.listdir(current_year)
        
        for file in file_list:
            current_file=current_year+file
            info=open(current_file,"r")

            S1=json.load(info)
            for i in S1["data"]["transactionData"]:
                    Name=i["name"]
                    Count=i["paymentInstruments"][0]["count"]
                    Amount=i["paymentInstruments"][0]["amount"]
                    col2["Transaction_type"].append(Name)
                    col2["Transaction_count"].append(Count)
                    col2["Transaction_amount"].append(Amount)
                    col2["States"].append(state)
                    col2["Years"].append(year)
                    col2["Quarter"].append(int(file.strip(".json")))  


aggre_transaction = pd.DataFrame(col2)

aggre_transaction["States"] = aggre_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggre_transaction["States"] = aggre_transaction["States"].str.replace("-"," ")
aggre_transaction["States"] = aggre_transaction["States"].str.title()
aggre_transaction['States'] = aggre_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli")



#aggregate user

part3="C:/Users/Sujay/New folder/Phone Pe/pulse/data/aggregated/user/country/india/state/"
aggregator_user_list=os.listdir(part3)

col3={"States":[],"Years":[],"Quarter":[], "Brands":[],"Transaction_count":[], "Percentage":[]}

for state in aggregator_user_list:
    current_state=part3+state+"/"
    year_list=os.listdir(current_state)
    
    for year in year_list:
        current_year=current_state+year+"/"
        file_list=os.listdir(current_year)
        
        for file in file_list:
            current_file=current_year+file
            info=open(current_file,"r")

            S3=json.load(info)
            
            try: 
                for i in S3["data"]["usersByDevice"]:
                        brand=i["brand"]
                        count=i["count"]
                        percentage=i["percentage"]
                        col3["Brands"].append(brand)
                        col3["Transaction_count"].append(count)
                        col3["Percentage"].append(percentage)
                        col3["States"].append(state)
                        col3["Years"].append(year)
                        col3["Quarter"].append(int(file.strip(".json")))
            except:
                 pass 

aggre_user = pd.DataFrame(col3)

aggre_user["States"] = aggre_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
aggre_user["States"] = aggre_user["States"].str.replace("-"," ")
aggre_user["States"] = aggre_user["States"].str.title()
aggre_user['States'] = aggre_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and diu")





#map transaction
part5="C:/Users/Sujay/New folder/Phone Pe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(part5)

col5={"States":[],"Years":[],"Quarter":[], "District":[],"Transaction_count":[], "Transaction_amount":[]}

for state in map_trans_list:
    current_state=part5+state+"/"
    year_list=os.listdir(current_state)
    
    for year in year_list:
        current_year=current_state+year+"/"
        file_list=os.listdir(current_year)
        
        for file in file_list:
            current_file=current_year+file
            info=open(current_file,"r")

            S5=json.load(info)
            

            for i in S5['data']["hoverDataList"]:
                name = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                col5["District"].append(name)
                col5["Transaction_count"].append(count)
                col5["Transaction_amount"].append(amount)
                col5["States"].append(state)
                col5["Years"].append(year)
                col5["Quarter"].append(int(file.strip(".json")))

map_transaction = pd.DataFrame(col5)

map_transaction["States"] = map_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_transaction["States"] = map_transaction["States"].str.replace("-"," ")
map_transaction["States"] = map_transaction["States"].str.title()
map_transaction['States'] = map_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli")




#map_user
part6 = "C:/Users/Sujay/New folder/Phone Pe/pulse/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(part6)

col6 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUser":[], "AppOpens":[]}

for state in map_user_list:
    current_states = part6+state+"/"
    map_year_list = os.listdir(current_states)
    
    for year in map_year_list:
        current_years = current_states+year+"/"
        map_file_list = os.listdir(current_years)
        
        for file in map_file_list:
            current_files = current_years+file
            data = open(current_files,"r")
            S6= json.load(data)

            for i in S6["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appopens = i[1]["appOpens"]
                col6["Districts"].append(district)
                col6["RegisteredUser"].append(registereduser)
                col6["AppOpens"].append(appopens)
                col6["States"].append(state)
                col6["Years"].append(year)
                col6["Quarter"].append(int(file.strip(".json")))

map_user = pd.DataFrame(col6)

map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_user["States"] = map_user["States"].str.replace("-"," ")
map_user["States"] = map_user["States"].str.title()
map_user['States'] = map_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



#top_transaction
part8 = "C:/Users/Sujay/New folder/Phone Pe/pulse/data/top/transaction/country/india/state/"
top_tran_list = os.listdir(part8)

col8 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for state in top_tran_list:
    current_states = part8+state+"/"
    top_year_list = os.listdir(current_states)
    
    for year in top_year_list:
        current_years = current_states+year+"/"
        top_file_list = os.listdir(current_years)
        
        for file in top_file_list:
            current_files = current_years+file
            data = open(current_files,"r")
            S8 = json.load(data)

            for i in S8["data"]["pincodes"]:
                entityName = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                col8["Pincodes"].append(entityName)
                col8["Transaction_count"].append(count)
                col8["Transaction_amount"].append(amount)
                col8["States"].append(state)
                col8["Years"].append(year)
                col8["Quarter"].append(int(file.strip(".json")))

top_transaction = pd.DataFrame(col8)

top_transaction["States"] = top_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_transaction["States"] = top_transaction["States"].str.replace("-"," ")
top_transaction["States"] = top_transaction["States"].str.title()
top_transaction['States'] = top_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")




#top_user
part9 = "C:/Users/Sujay/New folder/Phone Pe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(part9)

col9 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for state in top_user_list:
    current_states = part9+state+"/"
    top_year_list = os.listdir(current_states)

    for year in top_year_list:
        current_years = current_states+year+"/"
        top_file_list = os.listdir(current_years)

        for file in top_file_list:
            cur_files = current_years+file
            data = open(cur_files,"r")
            S9 = json.load(data)

            for i in S9["data"]["pincodes"]:
                name = i["name"]
                registeredusers = i["registeredUsers"]
                col9["Pincodes"].append(name)
                col9["RegisteredUser"].append(registereduser)
                col9["States"].append(state)
                col9["Years"].append(year)
                col9["Quarter"].append(int(file.strip(".json")))

top_user = pd.DataFrame(col9)

top_user["States"] = top_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_user["States"] = top_user["States"].str.replace("-"," ")
top_user["States"] = top_user["States"].str.title()
top_user['States'] = top_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")




#aggregated transaction table
mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
cursor = mydb.cursor()

create_query2 = '''CREATE TABLE if not exists aggregated_transaction (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Transaction_type varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''

try:
    cursor.execute(create_query2)
    mydb.commit()

    for index, row in aggre_transaction.iterrows():
        insert_query2 = '''INSERT INTO aggregated_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                           values(%s,%s,%s,%s,%s,%s)'''
        values = (row["States"],
                  row["Years"],
                  row["Quarter"],
                  row["Transaction_type"],
                  row["Transaction_count"],
                  row["Transaction_amount"]
                  )
        cursor.execute(insert_query2, values)
        mydb.commit()

except Exception as e:
    print("Error:", e)




#aggregated user table
mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
cursor = mydb.cursor()

create_query3 = '''CREATE TABLE if not exists aggregated_user (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                Brands varchar(50),
                                                                Transaction_count bigint,
                                                                Percentage float)'''
cursor.execute(create_query3)
mydb.commit()

for index,row in aggre_user.iterrows():
    insert_query3 = '''INSERT INTO aggregated_user (States, Years, Quarter, Brands, Transaction_count, Percentage)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Brands"],
              row["Transaction_count"],
              row["Percentage"])
    cursor.execute(insert_query3,values)
    mydb.commit()




#map_transaction_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
cursor = mydb.cursor()

create_query5 = '''CREATE TABLE if not exists map_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                District varchar(50),
                                                                Transaction_count bigint,
                                                                Transaction_amount float)'''
cursor.execute(create_query5)
mydb.commit()

for index,row in map_transaction.iterrows():
            insert_query5 = '''
                INSERT INTO map_Transaction (States, Years, Quarter, District, Transaction_count, Transaction_amount)
                VALUES (%s, %s, %s, %s, %s, %s)

            '''
            values = (
                row['States'],
                row['Years'],
                row['Quarter'],
                row['District'],
                row['Transaction_count'],
                row['Transaction_amount']
            )
            cursor.execute(insert_query5,values)
            mydb.commit() 




#map_user_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
cursor = mydb.cursor()

create_query6 = '''CREATE TABLE if not exists map_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Districts varchar(50),
                                                        RegisteredUser bigint,
                                                        AppOpens bigint)'''
cursor.execute(create_query6)
mydb.commit()

for index,row in map_user.iterrows():
    insert_query6 = '''INSERT INTO map_user (States, Years, Quarter, Districts, RegisteredUser, AppOpens)
                        values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Districts"],
              row["RegisteredUser"],
              row["AppOpens"])
    cursor.execute(insert_query6,values)
    mydb.commit()




#top_transaction_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
cursor = mydb.cursor()

create_query8 = '''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint)'''
cursor.execute(create_query8)
mydb.commit()

for index,row in top_transaction.iterrows():
    insert_query8 = '''INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Transaction_count"],
              row["Transaction_amount"])
    cursor.execute(insert_query8,values)
    mydb.commit()




#top_user_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
cursor = mydb.cursor()

create_query9 = '''CREATE TABLE if not exists top_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Pincodes int,
                                                        RegisteredUser bigint
                                                        )'''
cursor.execute(create_query9)
mydb.commit()

for index,row in top_user.iterrows():
    insert_query9 = '''INSERT INTO top_user (States, Years, Quarter, Pincodes, RegisteredUser)
                                            values(%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["RegisteredUser"])
    cursor.execute(insert_query9,values)
    mydb.commit()

 



 