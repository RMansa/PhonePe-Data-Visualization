import json
import streamlit as st
import pandas as pd
import requests
import psycopg2
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu



#CREATE DATAFRAMES FROM SQL
#sql connection
mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="Fluffy",
                        database="PhonePe_data",
                        port="5432")
step = mydb.cursor()


#Aggregated_transsaction
step.execute("select * from aggregated_transaction;")
mydb.commit()
table1 = step.fetchall()
Aggregate_transaction = pd.DataFrame(table1,columns = ("States", "Years", "Quarter", "Transaction_type", "Transaction_count", "Transaction_amount"))

#Aggregated_user
step.execute("select * from aggregated_user")
mydb.commit()
table2 = step.fetchall()
Aggregate_user = pd.DataFrame(table2,columns = ("States", "Years", "Quarter", "Brands", "Transaction_count", "Percentage"))

#Map_transaction
step.execute("select * from map_transaction")
mydb.commit()
table3 = step.fetchall()
Map_transaction = pd.DataFrame(table3,columns = ("States", "Years", "Quarter", "Districts", "Transaction_count", "Transaction_amount"))

#Map_user
step.execute("select * from map_user")
mydb.commit()
table4 = step.fetchall()
Map_user = pd.DataFrame(table4,columns = ("States", "Years", "Quarter", "Districts", "RegisteredUser", "AppOpens"))

#Top_transaction
step.execute("select * from top_transaction")
mydb.commit()
table5 = step.fetchall()
Top_transaction = pd.DataFrame(table5,columns = ("States", "Years", "Quarter", "Pincodes", "Transaction_count", "Transaction_amount"))

#Top_user
step.execute("select * from top_user")
mydb.commit()
table6 = step.fetchall()
Top_user = pd.DataFrame(table6, columns = ("States", "Years", "Quarter", "Pincodes", "RegisteredUser"))



def India_plot_1(df,year):
    ai= df[df["Years"] == year]
    ai.reset_index(drop= True, inplace= True)

    ai1=ai.groupby("States")[["Transaction_count", "Transaction_amount"]].sum()
    ai1.reset_index(inplace= True)



    col1,col2= st.columns(2)
    with col1:

        url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data1= json.loads(response.content)
        states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
        states_name_tra.sort()
        

        india_1= px.choropleth(ai1, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_amount", color_continuous_scale= "Blues",
                                 range_color= (ai1["Transaction_amount"].min(),ai1["Transaction_amount"].max()),
                                 hover_name= "States",title = f"{year} TRANSACTION AMOUNT",
                                 fitbounds= "locations",width =600, height= 600)
        india_1.update_geos(visible =False)
        
        st.plotly_chart(india_1)
    with col2:

        fig_amount= px.bar(ai1, x="States", y= "Transaction_amount",title= f"{year} TRANSACTION AMOUNT",
                           width=600, height= 650, color_discrete_sequence=px.colors.sequential.ice_r)
        st.plotly_chart(fig_amount)

    col1,col2= st.columns(2)
    with col1:
        fig_count= px.bar(ai1, x="States", y= "Transaction_count",title= f"{year} TRANSACTION COUNT",
                          width=550, height= 600, color_discrete_sequence=px.colors.sequential.Teal_r)
        st.plotly_chart(fig_count)

 
    with col2:

        india_2= px.choropleth(ai1, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_count", color_continuous_scale= "Blues",
                                 range_color= (ai1["Transaction_count"].min(),ai1["Transaction_count"].max()),
                                 hover_name= "States",title = f"{year} TRANSACTION COUNT",
                                 fitbounds= "locations",width =600, height= 600)
        india_2.update_geos(visible =False)
        
        st.plotly_chart(india_2)

    return ai


def India_plot_2(df,quarter):
    ai2= df[df["Quarter"] == quarter]
    ai2.reset_index(drop= True, inplace= True)

    ai3= ai2.groupby("States")[["Transaction_count", "Transaction_amount"]].sum()
    ai3.reset_index(inplace= True)

    col1,col2= st.columns(2)

    with col1:
        url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response= requests.get(url)
        data1= json.loads(response.content)
        states_name_tra= [feature["properties"]["ST_NM"] for feature in data1["features"]]
        states_name_tra.sort()

        india_3= px.choropleth(ai3, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_amount", color_continuous_scale= "Plasma",
                                 range_color= (ai3["Transaction_amount"].min(),ai3["Transaction_amount"].max()),
                                 hover_name= "States",title = f"{ai2['Years'].min()} TRANSACTION AMOUNT",
                                 fitbounds= "locations",width =600, height= 600)
        india_3.update_geos(visible =False)
        
        st.plotly_chart(india_3)
 

    with col2:
               fig_1_amount= px.bar(ai3, x= "States", y= "Transaction_amount", 
                            title= f"{ai2['Years'].min()} TRANSACTION AMOUNT",width= 600, height=650,
                            color_discrete_sequence=px.colors.sequential.Purpor_r)
               st.plotly_chart(fig_1_amount)
    col1,col2= st.columns(2)
    with col1:

           fig_2_count= px.bar(ai3, x= "States", y= "Transaction_count", 
                            title= f"{ai2['Years'].min()} TRANSACTION COUNT",width= 550, height=600,
                            color_discrete_sequence=px.colors.sequential.Magenta_r)
           st.plotly_chart(fig_2_count)
    with col2:

        india_4= px.choropleth(ai3, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                                 color= "Transaction_count", color_continuous_scale= "Plasma",
                                 range_color= (ai3["Transaction_count"].min(),ai3["Transaction_count"].max()),
                                 hover_name= "States",title = f"{ai2['Years'].min()} TRANSACTION COUNT",
                                 fitbounds= "locations",width =550, height= 650)
        india_4.update_geos(visible =False)
        
        st.plotly_chart(india_4)
    
    return ai2

def Aggregate_Transaction(df, state):
    df_state= df[df["States"] == state]
    df_state.reset_index(drop= True, inplace= True)

    at= df_state.groupby("Transaction_type")[["Transaction_count", "Transaction_amount"]].sum()
    at.reset_index(inplace= True)
    shades_of_pink = ['#FFC0CB', '#FF69B4', '#FF1493', '#FF0055', '#DB7093', '#DC143C', '#F08080', '#BC8F8F', '#FFC0CB', '#CD5C5C']



    col1,col2= st.columns(2)
    with col1:

        histbar_1= px.bar(at, x= "Transaction_count", y= "Transaction_type", orientation="h",color="Transaction_type",color_discrete_sequence=shades_of_pink, width= 600, 
                        title= f"{state.upper()} TRANSACTION TYPE AND TRANSACTION COUNT",height= 500)
        st.plotly_chart(histbar_1)

    with col2:

        histbar_2= px.bar(at, x= "Transaction_amount", y= "Transaction_type", orientation="h",
                        color_discrete_sequence=shades_of_pink, width= 600,
                        title= f"{state.upper()} TRANSACTION TYPE AND TRANSACTION AMOUNT", height= 500)
        st.plotly_chart(histbar_2)
        
def Aggregate_user_plot_1(df,year):
    au= df[df["Years"] == year]
    au.reset_index(drop= True, inplace= True)
    
    au1= pd.DataFrame(au.groupby("Brands")["Transaction_count"].sum())
    au1.reset_index(inplace= True)

    line_1= px.bar(au1, x="Brands",y= "Transaction_count", title=f"{year} BRANDS AND TRANSACTION COUNT",
                    width=1000,color_discrete_sequence=px.colors.sequential.Purp_r)
    st.plotly_chart(line_1)

    return au

def Aggregate_user_plot_2(df,quarter):
    au2= df[df["Quarter"] == quarter]
    au2.reset_index(drop= True, inplace= True)

    pie_1= px.pie(data_frame=au2, names= "Brands", values="Transaction_count", hover_data= "Percentage",
                      width=1000,title=f"{quarter} QUARTER TRANSACTION COUNT PERCENTAGE",hole=0.5, color_discrete_sequence= px.colors.sequential.Magenta_r)
    st.plotly_chart(pie_1)

    return au2

def Aggregate_user_plot_3(df,state):
    au3= df[df["States"] == state]
    au3.reset_index(drop= True, inplace= True)

    au3_1= pd.DataFrame(au3.groupby("Brands")["Transaction_count"].sum())
    au3_1.reset_index(inplace= True)

    scatter_1= px.line(au3_1, x= "Brands", y= "Transaction_count", markers= True,width=1000)
    st.plotly_chart(scatter_1)

def map_insurance_plot_1(df,state):
    mi= df[df["States"] == state]
    mi1=mi.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    mi1.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
        bar_1= px.bar(mi1, x= "Districts", y= "Transaction_amount",
                              width=600, height=500, title= f"{state.upper()} DISTRICTS TRANSACTION AMOUNT",
                              color_discrete_sequence= px.colors.sequential.Mint_r)
        st.plotly_chart(bar_1)

    with col2:
        bar_2= px.bar(mi1, x= "Districts", y= "Transaction_count",
                              width=600, height= 500, title= f"{state.upper()} DISTRICTS TRANSACTION COUNT",
                              color_discrete_sequence= px.colors.sequential.Mint)
        
        st.plotly_chart(bar_2)

def map_insurance_plot_2(df,state):
    mi_2= df[df["States"] == state]
    mi2= mi_2.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    mi2.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
        pie_3= px.pie(mi2, names= "Districts", values= "Transaction_amount",
                              width=600, height=500, title= f"{state.upper()} DISTRICTS TRANSACTION AMOUNT",
                              hole=0.5,color_discrete_sequence= px.colors.sequential.Mint_r)
        st.plotly_chart(pie_3)

    with col2:
        pie_4= px.pie(mi2, names= "Districts", values= "Transaction_count",
                              width=600, height= 500, title= f"{state.upper()} DISTRICTS TRANSACTION COUNT",
                              hole=0.5,  color_discrete_sequence= px.colors.sequential.Oranges_r)
        
        st.plotly_chart(pie_4)

def map_user_plot_1(df, year):
    mu= df[df["Years"] == year]
    mu.reset_index(drop= True, inplace= True)
    mu1= mu.groupby("States")[["RegisteredUser", "AppOpens"]].sum()
    mu1.reset_index(inplace= True)

    user_plot_1= px.line(mu1, x= "States", y= ["RegisteredUser","AppOpens"], markers= True,
                                width=1000,height=800,title= f"{year} REGISTERED USER AND APPOPENS", color_discrete_sequence= px.colors.sequential.Pinkyl_r)
    st.plotly_chart(user_plot_1)

    return mu

def map_user_plot_2(df, quarter):
    mu_2= df[df["Quarter"] == quarter]
    mu_2.reset_index(drop= True, inplace= True)
    mu2= mu_2.groupby("States")[["RegisteredUser", "AppOpens"]].sum()
    mu2.reset_index(inplace= True)

    user_plot_2= px.line(mu2, x= "States", y= ["RegisteredUser","AppOpens"], markers= True,
                                title= f"{df['Years'].min()},  REGISTERED USER AND APPOPENS",
                                width= 1000,height=800,color_discrete_sequence= px.colors.sequential.Burg_r)
    st.plotly_chart(user_plot_2)

    return mu_2

def map_user_plot_3(df, state):
    mu_3= df[df["States"] == state]
    mu_3.reset_index(drop= True, inplace= True)
    mu3= mu_3.groupby("Districts")[["RegisteredUser", "AppOpens"]].sum()
    mu3.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
        user_plot_3= px.bar(mu3, x= "RegisteredUser",y= "Districts",orientation="h",
                                    title= f"{state.upper()} REGISTERED USER",height=800,
                                    color_discrete_sequence= px.colors.sequential.Sunset_r)
        st.plotly_chart(user_plot_3)

    with col2:
        user_plot_4= px.bar(mu3, x= "AppOpens", y= "Districts",orientation="h",
                                    title= f"{state.upper()} APPOPENS",height=800,
                                    color_discrete_sequence= px.colors.sequential.dense_r)
        st.plotly_chart(user_plot_4)

def top_user_plot_1(df,year):
    tu= df[df["Years"] == year]
    tu.reset_index(drop= True, inplace= True)

    tu1= pd.DataFrame(tu.groupby(["States","Quarter"])["RegisteredUser"].sum())
    tu1.reset_index(inplace= True)

    top_plot_1= px.bar(tu1, x= "States", y= "RegisteredUser", barmode= "group", color= "Quarter",
                            width=1000, height= 800, color_continuous_scale= px.colors.sequential.Burgyl)
    st.plotly_chart(top_plot_1)

    return tu

def top_user_plot_2(df,state):
    tu_2= df[df["States"] == state]
    tu_2.reset_index(drop= True, inplace= True)

    tu2= pd.DataFrame(tu_2.groupby("Quarter")["RegisteredUser"].sum())
    tu2.reset_index(inplace= True)

    top_plot_2= px.bar(tu_2, x= "Quarter", y= "RegisteredUser",barmode= "group",
                           width=1000, height= 800,color= "Pincodes",hover_data="Pincodes",
                            color_continuous_scale= px.colors.sequential.Magenta)
    st.plotly_chart(top_plot_2)

def ques1():
    brand= Aggregate_user[["Brands","Transaction_count"]]
    brand1= brand.groupby("Brands")["Transaction_count"].sum().sort_values(ascending=False)
    brand2= pd.DataFrame(brand1).reset_index()

    fig_1= px.bar(brand2, y= "Transaction_count", x= "Brands", color_discrete_sequence=px.colors.sequential.Blackbody_r,
                       title= "Top Mobile Brands of Transaction_count")
    return st.plotly_chart(fig_1)


def ques2():
    hight= Map_transaction[["Districts", "Transaction_amount"]]
    hight1= hight.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=False)
    hight2= pd.DataFrame(hight1).head(10).reset_index()

    fig_2= px.pie(hight2, values= "Transaction_amount", names= "Districts", title="Top 10 districts with highest transaction amount?",
                    color_discrete_sequence=px.colors.sequential.Greens_r)
    return st.plotly_chart(fig_2)

def ques3():
    lowt= Map_transaction[["Districts", "Transaction_amount"]]
    lowt1= lowt.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    lowt2= pd.DataFrame(lowt1).head(10).reset_index()

    fig_3= px.bar(lowt2, y= "Transaction_amount", x= "Districts", title="Top 10 districts with lowest transaction amount?",
                    color_discrete_sequence=px.colors.sequential.Pinkyl_r)
    return st.plotly_chart(fig_3)


def ques4():
    sha= Map_user[["States", "AppOpens"]]
    sha1= sha.groupby("States")["AppOpens"].sum().sort_values(ascending=False)
    sha2= pd.DataFrame(sha1).reset_index().head(10)

    fig_4= px.pie(sha2, names= "States", values= "AppOpens", title="Top 10 states with highest number of App Opens?",
                color_discrete_sequence= px.colors.sequential.deep_r)
    return st.plotly_chart(fig_4)

def ques5():
    sla= Map_user[["States", "AppOpens"]]
    sla1= sla.groupby("States")["AppOpens"].sum().sort_values(ascending=True)
    sla2= pd.DataFrame(sla1).reset_index().head(10)

    fig_5= px.bar(sla2, x= "States", y= "AppOpens", title="10 states with least number of App Opens?",
                color_discrete_sequence= px.colors.sequential.Peach_r)
    return st.plotly_chart(fig_5)

def ques6():
    sltc= Aggregate_transaction[["States", "Transaction_count"]]
    sltc1= sltc.groupby("States")["Transaction_count"].sum().sort_values(ascending=True)
    sltc2= pd.DataFrame(sltc1).reset_index()

    fig_6= px.pie(sltc2, names= "States", values= "Transaction_count", title= "States with lowest transaction count?",
                    color_discrete_sequence= px.colors.sequential.ice_r)
    return st.plotly_chart(fig_6)

def ques7():
    slta= Aggregate_transaction[["States", "Transaction_amount"]]
    slta1= slta.groupby("States")["Transaction_amount"].sum().sort_values(ascending= True)
    slta2= pd.DataFrame(slta1).reset_index().head(10)

    fig_7= px.bar(slta2, x= "States", y= "Transaction_amount",title= "States with lowest transaction amount",
                    color_discrete_sequence= px.colors.sequential.Agsunset_r)
    return st.plotly_chart(fig_7)

def ques8():
    shtc= Aggregate_transaction[["States", "Transaction_count"]]
    shtc1= shtc.groupby("States")["Transaction_count"].sum().sort_values(ascending=False)
    shtc2= pd.DataFrame(shtc1).reset_index()

    fig_8= px.pie(shtc2, names= "States", values= "Transaction_count", title= "States with highest transaction count?",
                    color_discrete_sequence= px.colors.sequential.Magenta_r)
    return st.plotly_chart(fig_8)

def ques9():
    ht= Aggregate_transaction[["States", "Transaction_amount"]]
    ht1= ht.groupby("States")["Transaction_amount"].sum().sort_values(ascending= False)
    ht2= pd.DataFrame(ht1).reset_index().head(10)

    fig_9= px.bar(ht2, x= "States", y= "Transaction_amount",title= "States with highest transaction amount?",
                    color_discrete_sequence= px.colors.sequential.gray_r)
    return st.plotly_chart(fig_9)

def ques10():
    dt= Map_transaction[["Districts", "Transaction_amount"]]
    dt1= dt.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    dt2= pd.DataFrame(dt1).reset_index().head(50)

    fig_10= px.pie(dt2, names= "Districts", values= "Transaction_amount", title= "Districts with lowest transaction amount?",
                color_discrete_sequence= px.colors.sequential.Brwnyl_r)
    return st.plotly_chart(fig_10)



#Streamlit

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        .big-font {
            font-size: 30px !important;
            font-weight: bold;
            background-color: #e6e6fa; /* Light Purple */
            padding: 10px;
            border-radius: 10px;
            color: black; /* Black Text Color */
        }

        .dark-purple-title {
            background-color: #e6e6fa; /* Light Purple */
            color: #4b0082; /* Dark Bluish Purple Text Color */
            text-align: center; /* Center-align the text */
            font-size: 48px !important;
            font-weight: bold;
            padding: 15px;
            border-radius: 20px;

        }

        .menu-buttons {
            display: flex;
            justify-content: space-around;
            margin-top: 10px;
        }

        .menu-button {
            background-color: #800080 !important; /* Dark Purple */
            color: white; /* White Text Color */
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<p class='dark-purple-title'>PHONEPE DATA VISUALIZATION AND EXPLORATION</p>", unsafe_allow_html=True)


import streamlit as st

home_icon = "🏡"
data_exploration_icon = "📈"
insights_icon = "📊"

# Menu Options
selected_option = st.radio("Select an option", [f"{home_icon} Home", f"{data_exploration_icon} Data Exploration", f"{insights_icon} Insights"])

st.markdown(
    """
    <style>
        .radio-group > * {
            display: inline-block !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


if selected_option == f"{home_icon} Home":

    st.markdown("<h2 style='color: white; text-decoration: underline;'>OVERVIEW</h2>", unsafe_allow_html=True)
    # Introduction Section
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image("phonepe-logo.png", use_column_width=True)
    with col2:
        st.markdown("<h1>PHONEPE</h1>", unsafe_allow_html=True)
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown(
            "PhonePe is an Indian digital payments and financial technology company."
        )

    # Features Section
    st.markdown("<h2 style='text-decoration: underline;'>FEATURES</h2>", unsafe_allow_html=True)
    st.write("1.UPI (Unified Payments Interface): PhonePe is built on the UPI, which is a real-time payment system developed by the National Payments Corporation of India (NPCI). Users can link their bank accounts to the PhonePe app and make seamless peer-to-peer transactions.")
    st.write("2.Wallet: PhonePe has a digital wallet feature that allows users to store money securely. This wallet can be used for various transactions and payments within the PhonePe ecosystem.")
    st.write("3.Banking Services: Users can check their bank account balance, view transaction history, and manage their bank accounts through the PhonePe app.")
    st.write("4.Merchant Payments: PhonePe is widely accepted by online and offline merchants. Users can make quick payments at various establishments using the app.")
    st.write("5.Rewards and Cashback: PhonePe often offers cashback and rewards for transactions made through the platform. This encourages users to use PhonePe for their payments.")
 

   
    st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")

    # Videos Section
    st.markdown("<h2 style='text-decoration: underline;'>VIDEOS</h2>", unsafe_allow_html=True)
    col3, col4, col5 = st.columns(3)

    with col3:
        st.video("https://youtu.be/aXnNA4mv1dU")

    with col4:
        st.video("https://youtu.be/sziiEhS-tgc")

    with col5:
        st.video("https://www.youtube.com/watch?v=zGlDkrNxDU8")

    # Additional Information Section
    st.markdown("<h2 style='text-decoration: underline;'>ADDITIONAL INFORMATION</h2>", unsafe_allow_html=True)
    col6, col7 = st.columns(2)

    with col6:
        st.write("1.Gold and Mutual Fund Investments: PhonePe allows users to buy and sell digital gold through the app. Additionally, the platform facilitates investment in mutual funds, providing users with the option to explore different investment opportunities.")
        st.write("2.PhonePe for Business: In addition to serving individual users, PhonePe has introduced services for businesses. It provides solutions for merchants, allowing them to accept digital payments easily. This includes the use of QR codes, POS (Point of Sale) devices, and other payment acceptance methods.")
        st.write("3.Partnerships and Collaborations: PhonePe has collaborated with various entities to enhance its services. This includes partnerships with financial institutions, government bodies, and other technology companies to expand its offerings and reach a broader user base.")
        st.write("4.Insurance Products: PhonePe has introduced insurance products, enabling users to purchase insurance coverage through the app. This includes health insurance, term life insurance, and other insurance offerings.")
        st.write("5.User Interface and Experience: PhonePe is known for its user-friendly interface, making it accessible to a diverse user demographic. The app is designed to be intuitive, with features such as a transaction history, notifications, and a dashboard for managing finances.")
   
    with col7:
        st.image("phonepe_transaction.png", width=350)




elif selected_option == f"{data_exploration_icon} Data Exploration":
    st.title(":purple[Data Exploration Page]")
    st.write("Explore your data here!")
    
 # Improve tab styling with larger font and purple color
    st.markdown(
        """
        <style>
            .streamlit-tabs > div > div > div > div {
                font-size: 20px !important;
                color: purple !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

    with tab1:
        method = st.radio("**Select the Analysis Method**",["Transaction Analysis", "User Analysis"])

            
        if method == "Transaction Analysis":
            col1, col2 = st.columns(2)

            with col1:
        
                years = st.slider(
                    label="Select the Year(at)",
                    min_value=Aggregate_transaction["Years"].min(),
                    max_value=Aggregate_transaction["Years"].max(),
                    value=Aggregate_transaction["Years"].min(),
                    step=1,
                    format="%d",
                    help="Choose a year for transaction analysis",
                )

            aggregate_transaction = India_plot_1(Aggregate_transaction, years)

            col1,col2=st.columns(2)
            with col1:
            
                quarters = st.slider(
                    label="Select the Quarter(at)",
                    min_value=aggregate_transaction["Quarter"].min(),
                    max_value=aggregate_transaction["Quarter"].max(),
                    value=aggregate_transaction["Quarter"].min(),
                    step=1,
                    format="%d",
                    help="Choose a quarter for transaction analysis",
                )

            aggregate_transaction_1 = India_plot_2(aggregate_transaction, quarters)

    
            state_aggregate = st.selectbox("Select the State(at)", aggregate_transaction["States"].unique())

            Aggregate_Transaction(aggregate_transaction_1, state_aggregate)


        elif method == "User Analysis":
            year= st.selectbox("Select the Year(au)",Aggregate_user["Years"].unique())
            aggregate_user= Aggregate_user_plot_1(Aggregate_user,year)

            quarter= st.selectbox("Select the Quarter(au)",aggregate_user["Quarter"].unique())
            aggregate_user_1= Aggregate_user_plot_2(aggregate_user,quarter)

            state_user= st.selectbox("**Select the State(au)**",aggregate_user["States"].unique())
            Aggregate_user_plot_3(aggregate_user_1,state_user)

    with tab2:
        method_map = st.radio("**Select the Analysis Method(MAP)**",[ "Map Transaction Analysis", "Map User Analysis"])

        
        if method_map == "Map Transaction Analysis":
            col1, col2 = st.columns(2)

            with col1:
                
                years = st.slider(
                    label="Select the Year(mt)",
                    min_value=Map_transaction["Years"].min(),
                    max_value=Map_transaction["Years"].max(),
                    value=Map_transaction["Years"].min(),
                    step=1,
                    format="%d",
                    help="Choose a year for map transaction analysis",
                )

            map_transaction = India_plot_1(Map_transaction, years)

            col1, col2 = st.columns(2)
            with col1:
                state_map = st.selectbox("Select the State", map_transaction["States"].unique())

            map_insurance_plot_1(map_transaction, state_map)

            
            col1, col2 = st.columns(2)
            with col1:
                
                quarters = st.slider(
                    label="Select the Quarter(mt)",
                    min_value=map_transaction["Quarter"].min(),
                    max_value=map_transaction["Quarter"].max(),
                    value=map_transaction["Quarter"].min(),
                    step=1,
                    format="%d",
                    help="Choose a quarter for map transaction analysis",
                )

            map_transaction_1 = India_plot_2(map_transaction, quarters)

            col1, col2 = st.columns(2)
            with col1:
                state_mtran = st.selectbox("Select the State(mt)", map_transaction_1["States"].unique())

            map_insurance_plot_2(map_transaction_1, state_mtran)

        elif method_map == "Map User Analysis":
            col1,col2= st.columns(2)
            with col1:
                year= st.selectbox("Select the Year(mu)",Map_user["Years"].unique())
            map_user= map_user_plot_1(Map_user, year)

            col1,col2= st.columns(2)
            with col1:
                quarter= st.selectbox("Select the Quarter(mu)",map_user["Quarter"].unique())
            map_user_1= map_user_plot_2(map_user,quarter)

            col1,col2= st.columns(2)
            with col1:
                state_muser= st.selectbox("Select the State(mu)",map_user_1["States"].unique())
            map_user_plot_3(map_user_1, state_muser)

    with tab3:
        method_top = st.radio("**Select the Analysis Method(TOP)**",[ "Top Transaction Analysis", "Top User Analysis"])

        
        if method_top == "Top Transaction Analysis":
            col1,col2= st.columns(2)
            with col1:
                years= st.slider("Select the Year(tt)", Top_transaction["Years"].min(), Top_transaction["Years"].max(),Top_transaction["Years"].min())
 
            top_tran= India_plot_1(Top_transaction,years)

            
            col1,col2= st.columns(2)
            with col1:
                quarters_t2= st.slider("Select the Quarter(tt)", top_tran["Quarter"].min(), top_tran["Quarter"].max(),top_tran["Quarter"].min())

            top_tran_1= India_plot_2(top_tran, quarters_t2)

        elif method_top == "Top User Analysis":
            col1,col2= st.columns(2)
            with col1:
                years= st.selectbox("Select the Year(tu)", Top_user["Years"].unique())

            top_user= top_user_plot_1(Top_user,years)

            col1,col2= st.columns(2)
            with col1:
                state_tuser= st.selectbox("Select the State(tu)", top_user["States"].unique())

            top_user_1= top_user_plot_2(top_user,state_tuser)



elif selected_option == f"{insights_icon} Insights":
    question= st.selectbox("**Select the Question**",('What are the mobile brands with the highest transaction count?',
                                                  'What are the top 10 districts with the highest transaction amount?',
                                                  'Which are the top 10 districts with the lowest transaction amount?',
                                                  'What are the top 10 states with the highest number of App Opens?',
                                                  'Which are the lowest 10 states with the least number of App Opens',
                                                  'Which states have the lowest transaction count?',
                                                  'Which states have the lowest transaction amount?',
                                                  'Which states have the highest transaction count?',
                                                  'Which states have the highest transaction amount?',
                                                  'Which districts have the lowest transaction amount?'))
    
    if question=="What are the mobile brands with the highest transaction count?":
        ques1()

    elif question=="What are the top 10 districts with the highest transaction amount?":
        ques2()

    elif question=="Which are the top 10 districts with the lowest transaction amount?":
        ques3()

    elif question=="What are the top 10 states with the highest number of App Opens?":
        ques4()

    elif question=="Which are the lowest 10 states with the least number of App Opens":
        ques5()

    elif question=="Which states have the lowest transaction count?":
        ques6()

    elif question=="Which states have the lowest transaction amount?":
        ques7()

    elif question=="Which states have the highest transaction count?":
        ques8()

    elif question=="Which states have the highest transaction amount?":
        ques9()

    elif question=="Which districts have the lowest transaction amount?":
        ques10()
