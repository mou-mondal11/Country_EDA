import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import altair as alt
import plotly.figure_factory as ff
from PIL import Image

data = pd.read_csv('countries.csv')
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.gifer.com/LzYa.gif');
        background-size: cover;
        background-position: center center;

        opacity: 0.8
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style="font-size:60px;font-family:Courier New, monospace; color: White; text-align: center ;
    ">🗺 Country GDP 🗺</h1>
    """,
    unsafe_allow_html=True
)
# Use of streamlit Expender
expander = st.expander("**:blue[Used terms:-] GDP, IMF GDP, UN GDP, GDP Per Capita**")
B = expander.button("See Explanation")
if B:
    st.write(
        ":red[GDP:-] GDP measures the monetary value of final goods and services—that is,those that are bought by the final user—produced in a country in a given period of time")
    st.write(
        ":red[IMF GDP:-] Gross domestic product is the most commonly used single measure of a country's overall economic activity.It represents the total value of final goods and services produced within a country during a specified time period, such as one year.")
    st.write(
        ":red[UN GDP:-] GDP is composed of goods and services produced for sale in the market and also includes some nonmarket production, such as defense or education services provided by the government. An alternative concept, gross national product, or GNP, counts all the output of the residents of a country.")
    st.write(
        ":red[GDP Per Capita:-] GDP per capita is the sum of gross value added by all resident producers in the economy plus any product taxes (less subsidies) not included in the valuation of output, divided by mid-year population")
    L = expander.button("Less Explanation")
st.markdown(
    """
    <h1 style="font-size:40px;font-family:Courier New, monospace; color: pink; text-align: center;
    ">Details of Every Continents</h1>
    """,
    unsafe_allow_html=True
)

Country = data.groupby("Continent")["Country"].count()
st.markdown(
    """
    <h1 style="font-size:20px;font-family:Courier New, monospace; color: White; text-align: center;
    ">Count of country by Continents</h1>
    """,
    unsafe_allow_html=True
)
chart1 = pd.DataFrame(Country)
st.bar_chart(chart1)

st.markdown(
    """
    <h1 style="font-size:30px;font-family:Courier New, monospace; color: White; text-align: center ;
    ">🤔Guess your Country's population🤔</h1>
    """,
    unsafe_allow_html=True
)

# img= Image.open('Population.png')
# st.image(img)
st.image("https://www.rdniehaus.com/app/uploads/2021/10/census-header.png")
st.markdown(
    """
    <h1 style="font-size:25px;font-family:Courier New, monospace; color: White; text-align: left;
    ">Choose the number😎</h1>
    """,
    unsafe_allow_html=True
)
x = st.slider(' ', min_value=0, max_value=1000000000, step=10000000)
if x > 0:
    st.write("According to you population 😯: ", x)

st.markdown(
    """
    <h1 style="font-size:30px;font-family:Courier New, monospace; color: White; text-align: center;
    ">To See Top 10 country press [🔎]</h1>
    """,
    unsafe_allow_html=True
)

Button = st.button('🔎')

if Button:
    # use of stremlit Tab and column
    st.title("🏆🏆Top 10 Country🏆🏆")
    tab, tab1, tab2, tab3, tab4 = st.tabs(
        ["Options", "Population Wise", "IMF GDP Wise", "UN GDP Wise", "GDP per capita wise"])
    with tab:
        img = Image.open('9vWI.gif')
        st.image(img)
    with tab1:
        col1, col2 = st.columns([2, 1])
        count1 = data.groupby("Country")["Population"].mean()
        st.markdown('**:green[Top 10 Country by Population]**')
        Top10_1 = count1.sort_values(ascending=False).head(10)
        col1.subheader("Chart Data")
        col1.bar_chart(Top10_1)
        col2.subheader("Table Data")
        col2.write(Top10_1)

    with tab2:
        col3, col4 = st.columns([2, 1])
        count2 = data.groupby("Country")["IMF_GDP"].mean()
        st.markdown('**:green[Top 10 Country by IMF_GDP]**')
        Top10_2 = count2.sort_values(ascending=False).head(10)
        col3.subheader("Chart Data")
        col3.bar_chart(Top10_2)
        col4.subheader("Table Data")
        col4.write(Top10_2)

    with tab3:
        col5, col6 = st.columns([2, 1])
        count3 = data.groupby("Country")["UN_GDP"].mean()
        st.markdown('**:green[Top 10 Country by UN_GDP]**')
        Top10_3 = count3.sort_values(ascending=False).head(10)
        col5.subheader("Chart Data")
        col5.bar_chart(Top10_3)
        col6.subheader("Table Data")
        col6.write(Top10_3)

    with tab4:
        col7, col8 = st.columns([2, 1])
        count4 = data.groupby("Country")["GDP_per_capita"].mean()
        st.markdown('**:green[Top 10 Country by GDP_per_capita]**')
        Top10_4 = count4.sort_values(ascending=False).head(10)
        col7.subheader("Chart Data")
        col7.bar_chart(Top10_4)
        col8.subheader("Table Data")
        col8.write(Top10_4)

st.markdown(
    """
    <h1 style="font-size:30px;font-family:Courier New, monospace; color: White; text-align: left;
    ">Where do you live?🤨</h1>
    """,
    unsafe_allow_html=True
)

option = st.selectbox(' ', ('Select One', 'Africa', 'Asia', 'Europe', 'North America', 'Ociania', 'South America'))
st.write('So, you live in:', option, ' 😀')
st.markdown(
    """
    <h1 style="font-size:30px;font-family:Courier New, monospace; color: White; text-align: left;
    ">Do you want to know about GDP of your country?</h1>
    """,
    unsafe_allow_html=True
)

check_box1 = st.radio(" ", options=["No", "Yes"])
if check_box1 == "No":
    st.markdown(
        """
        <h1 style="font-size:10px;font-family:Courier New, monospace; color: White; text-align: left;
        ">Thank You</h1>
        """,
        unsafe_allow_html=True
    )
else:
    if option != 'Select One':
        # Filter the data based on the selected continent
        filtered_data = data[data['Continent'] == option]

        # Create a line chart for the selected continent
        st.title(option)

        col9, col10 = st.columns([2, 2])
        col9.markdown("Population")
        col9.line_chart(filtered_data, x='Year', y='Population')
        col10.write("GDP")
        col10.line_chart(filtered_data, x='Year', y=['IMF_GDP', 'UN_GDP', 'GDP_per_capita'])
        st.write("Full Data about", option)
        st.write(filtered_data)
    st.markdown(
        """
        <h1 style="font-size:20px;font-family:Courier New, monospace; color: White; text-align: center;
        ">Country Population by year</h1>
        """,
        unsafe_allow_html=True
    )
    Country2 = data.groupby("Continent")["Population"].sum()
    plt1 = px.scatter(data, x='Year', y='Population', color='Country', hover_name='IMF_GDP', size='Population',
                      log_x=True, size_max=50, range_y=[0, '1.6M'], animation_frame='Continent')
    st.plotly_chart(plt1, theme="streamlit", use_container_width=True)

    st.markdown(
        """
        <h1 style="font-size:20px;font-family:Courier New, monospace; color: White; text-align: center;
        ">GDP Per Capita on the basis of Population</h1>
        """,
        unsafe_allow_html=True
    )
    fig1 = px.bar(data, x="GDP_per_capita", y="Population", color="Country", animation_frame='Continent')
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown(
        """
        <h1 style="font-size:20px;font-family:Courier New, monospace; color: White; text-align: center;
        ">IMF GDP on the basis of Population</h1>
        """,
        unsafe_allow_html=True
    )
    fig2 = px.bar(data, x="IMF_GDP", y="Population", color="Country", animation_frame='Continent')
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown(
        """
        <h1 style="font-size:20px;font-family:Courier New, monospace; color: White; text-align: center;
        ">UN GDP on the basis of Population</h1>
        """,
        unsafe_allow_html=True
    )
    fig3 = px.bar(data, x="UN_GDP", y="Population", color="Country", animation_frame='Continent')
    st.plotly_chart(fig3, use_container_width=True)