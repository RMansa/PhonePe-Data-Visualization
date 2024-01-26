# PhonePe Pulse Data Visualization and Exploration



## Overview
The PhonePe Pulse project focuses on data visualization and exploration using Streamlit and Plotly. The project aims to provide a user-friendly tool to analyze and showcase insights from PhonePe's transaction data, representing digital payment habits in India.

## PhonePe Pulse
PhonePe Pulse is a website showcasing over 2000+ Crore transactions on an interactive map of India. With a 45% market share, PhonePe's data offers valuable insights into the country's digital payment landscape. The project utilizes PhonePe's transaction data, along with merchant and customer interviews, to draw meaningful conclusions.


## Libraries/Modules
- **Plotly:** For plotting and visualizing the data.
- **Pandas:** To create a DataFrame with scraped data.
- **psycopg2:** To store and retrieve data from a PostgreSQL database.
- **Streamlit:** To create a graphical user interface.
- **json:** To load JSON files.


## Workflow

### Step 1: Importing Libraries
    ```python
            # Install necessary libraries if not already installed
            # pip install ["library_name"]
            
            import pandas as pd
            import psycopg2 
            import streamlit as st
            import plotly.express as px
            import os
            import json
            from streamlit_option_menu import option_menu
            from PIL import Image
            from git.repo.base import Repo
            
            
### Step 2: Data Extraction
    ```python
        from git.repo.base import Repo
     # Clone the GitHub repository
    Repo.clone_from("GitHub Clone URL", "Path to cloned files")

### Step 3: Data Transformation
    ```python
      # Define the path to JSON files
      path1 = "Path of the JSON files"
      agg_trans_list = os.listdir(path1)

    # Define columns for DataFrame
      columns1 = {'State': [],
                  'Year': [], 
                  'Quarter': [],
                  'Transaction_type': [],
                  'Transaction_count': [], 
                  'Transaction_amount': []}

    # Loop through folders, open JSON files, and create DataFrame
      for state in agg_trans_list:
          cur_state = path1 + state + "/"
          agg_year_list = os.listdir(cur_state)

    for year in agg_year_list:
        cur_year = cur_state + year + "/"
        agg_file_list = os.listdir(cur_year)

        for file in agg_file_list:
            cur_file = cur_year + file
            data = open(cur_file, 'r')
            S= json.load(data)

            for i in S['data']['transactionData']:
                name = i['name']
                count = i['paymentInstruments'][0]['count']
                amount = i['paymentInstruments'][0]['amount']
                columns1['Transaction_type'].append(name)
                columns1['Transaction_count'].append(count)
                columns1['Transaction_amount'].append(amount)
                columns1['State'].append(state)
                columns1['Year'].append(year)
                columns1['Quarter'].append(int(file.strip('.json')))
            
      df = pd.DataFrame(columns1)
### Step 4: Database Insertion
      ```python
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="your_database_name",
        user="your_username",
        password="your_password"
    )
    cursor = conn.cursor()
    
    # Create tables (replace with your table and column names)
    cursor.execute("CREATE TABLE table_name (col1 VARCHAR(100), col2 INT, col3 INT, col4 VARCHAR(100), col5 INT, col6 DOUBLE)")
    
    # Insert data into the database
    for i, row in df.iterrows():
        sql = "INSERT INTO table_name VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, tuple(row))
        conn.commit()

### Step 5: Dashboard Creation
    ```python
      fig_pie = px.pie(df, names='Transaction_type', values='Transaction_count', title='Transaction Types Distribution')
  
  
      fig_bar = px.bar(df, x='State', y='Transaction_amount', color='Transaction_type', title='Transaction Amount by State')
      
      # Display the charts using Streamlit
      st.plotly_chart(fig_pie)
      st.plotly_chart(fig_bar)

### Conclusion

This Streamlit project, PhonePe Pulse, transforms vast transaction data into an intuitive visual experience. Seamlessly integrating Streamlit's simplicity with Plotly's dynamic charts, the app offers a compelling exploration of India's digital payment landscape. Emphasizing accessibility, the project underscores the versatility of Streamlit in democratizing data insights for both experts and enthusiasts.

