import os
import psycopg2
import json
import git
import pandas as pd


#aggregator transaction

part1="C:/Users/Sujay/New folder/Phone Pe/pulse/data/aggregated/transaction/country/india/state/"
aggregator_trans_list=os.listdir(part1)

col1={"States":[],"Years":[],"Quarter":[], "Transaction_type":[],"Transaction_count":[], "Transaction_amount":[]}

for state in aggregator_trans_list:
    current_state=part1+state+"/"
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
                    col1["Transaction_type"].append(Name)
                    col1["Transaction_count"].append(Count)
                    col1["Transaction_amount"].append(Amount)
                    col1["States"].append(state)
                    col1["Years"].append(year)
                    col1["Quarter"].append(int(file.strip(".json")))  


aggregate_transaction = pd.DataFrame(col1)



#aggregate user

part2="C:/Users/Sujay/New folder/Phone Pe/pulse/data/aggregated/user/country/india/state/"
aggregator_user_list=os.listdir(part2)

col2={"States":[],"Years":[],"Quarter":[], "Brands":[],"Transaction_count":[], "Percentage":[]}

for state in aggregator_user_list:
    current_state=part2+state+"/"
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
                        col2["Brands"].append(brand)
                        col2["Transaction_count"].append(count)
                        col2["Percentage"].append(percentage)
                        col2["States"].append(state)
                        col2["Years"].append(year)
                        col2["Quarter"].append(int(file.strip(".json")))
            except:
                 pass 

aggregate_user = pd.DataFrame(col2)




#map transaction
part3="C:/Users/Sujay/New folder/Phone Pe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(part3)

col3={"States":[],"Years":[],"Quarter":[], "District":[],"Transaction_count":[], "Transaction_amount":[]}

for state in map_trans_list:
    current_state=part3+state+"/"
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
                col3["District"].append(name)
                col3["Transaction_count"].append(count)
                col3["Transaction_amount"].append(amount)
                col3["States"].append(state)
                col3["Years"].append(year)
                col3["Quarter"].append(int(file.strip(".json")))

map_transaction = pd.DataFrame(col3)




#map_user
part4 = "C:/Users/Sujay/New folder/Phone Pe/pulse/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(part4)

col4 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUser":[], "AppOpens":[]}

for state in map_user_list:
    current_states = part4+state+"/"
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
                col4["Districts"].append(district)
                col4["RegisteredUser"].append(registereduser)
                col4["AppOpens"].append(appopens)
                col4["States"].append(state)
                col4["Years"].append(year)
                col4["Quarter"].append(int(file.strip(".json")))

map_user = pd.DataFrame(col4)



#top_transaction
part5 = "C:/Users/Sujay/New folder/Phone Pe/pulse/data/top/transaction/country/india/state/"
top_tran_list = os.listdir(part5)

col5 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for state in top_tran_list:
    current_states = part5+state+"/"
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
                col5["Pincodes"].append(entityName)
                col5["Transaction_count"].append(count)
                col5["Transaction_amount"].append(amount)
                col5["States"].append(state)
                col5["Years"].append(year)
                col5["Quarter"].append(int(file.strip(".json")))

top_transaction = pd.DataFrame(col5)




#top_user
part6 = "C:/Users/Sujay/New folder/Phone Pe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(part6)

col6 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for state in top_user_list:
    current_states = part6+state+"/"
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
                col6["Pincodes"].append(name)
                col6["RegisteredUser"].append(registereduser)
                col6["States"].append(state)
                col6["Years"].append(year)
                col6["Quarter"].append(int(file.strip(".json")))

top_user = pd.DataFrame(col6)



#aggregated transaction table
mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
step = mydb.cursor()

create_query1 = '''CREATE TABLE if not exists aggregated_transaction (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Transaction_type varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''

try:
    step.execute(create_query1)
    mydb.commit()

    for index, row in aggregate_transaction.iterrows():
        insert_query1 = '''INSERT INTO aggregated_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                           values(%s,%s,%s,%s,%s,%s)'''
        values = (row["States"],
                  row["Years"],
                  row["Quarter"],
                  row["Transaction_type"],
                  row["Transaction_count"],
                  row["Transaction_amount"]
                  )
        step.execute(insert_query1, values)
        mydb.commit()

except Exception as e:
    print("Error:", e)



#aggregated user table
mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
step = mydb.cursor()

create_query2 = '''CREATE TABLE if not exists aggregated_user (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                Brands varchar(50),
                                                                Transaction_count bigint,
                                                                Percentage float)'''
step.execute(create_query2)
mydb.commit()

for index,row in aggregate_user.iterrows():
    insert_query2 = '''INSERT INTO aggregated_user (States, Years, Quarter, Brands, Transaction_count, Percentage)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Brands"],
              row["Transaction_count"],
              row["Percentage"])
    step.execute(insert_query2,values)
    mydb.commit()




#map_transaction_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
step = mydb.cursor()

create_query3 = '''CREATE TABLE if not exists map_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                District varchar(50),
                                                                Transaction_count bigint,
                                                                Transaction_amount float)'''
step.execute(create_query3)
mydb.commit()

for index,row in map_transaction.iterrows():
            insert_query3 = '''
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
            step.execute(insert_query3,values)
            mydb.commit() 




#map_user_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
step = mydb.cursor()

create_query4 = '''CREATE TABLE if not exists map_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Districts varchar(50),
                                                        RegisteredUser bigint,
                                                        AppOpens bigint)'''
step.execute(create_query4)
mydb.commit()

for index,row in map_user.iterrows():
    insert_query4 = '''INSERT INTO map_user (States, Years, Quarter, Districts, RegisteredUser, AppOpens)
                        values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Districts"],
              row["RegisteredUser"],
              row["AppOpens"])
    step.execute(insert_query4,values)
    mydb.commit()




#top_transaction_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
step = mydb.cursor()

create_query5 = '''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint)'''
step.execute(create_query5)
mydb.commit()

for index,row in top_transaction.iterrows():
    insert_query5 = '''INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Transaction_count"],
              row["Transaction_amount"])
    step.execute(insert_query5,values)
    mydb.commit()




#top_user_table

mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
step = mydb.cursor()

create_query6 = '''CREATE TABLE if not exists top_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Pincodes int,
                                                        RegisteredUser bigint
                                                        )'''
step.execute(create_query6)
mydb.commit()

for index,row in top_user.iterrows():
    insert_query6 = '''INSERT INTO top_user (States, Years, Quarter, Pincodes, RegisteredUser)
                                            values(%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["RegisteredUser"])
    step.execute(insert_query6,values)
    mydb.commit()

 



 