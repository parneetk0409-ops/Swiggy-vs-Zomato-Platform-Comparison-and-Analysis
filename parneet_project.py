import numpy as np
import pandas as pd                 
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st
import plotly.express as px
import os

st.set_page_config(
    page_title="swiggy_vs_zomato_3000",
    page_icon="🍔",
    layout="wide",
)
st.title("Swiggy vs Zomato: Restaurant Performance and Customer Insights Analysis")
st.markdown("----")  

st.header("Executive Summary")
st.markdown("""



* **Project Title:** *Swiggy vs Zomato: Restaurant Performance and Customer Insights Analysis.*

This Data Science project presents a comprehensive comparative analysis of restaurant data from **Swiggy** and **Zomato**, India's leading online food delivery platforms. The project aims to extract meaningful insights from restaurant data by analysing customer ratings, pricing, delivery performance, cuisine preferences, revenue, profit, and regional trends. Using Data Science techniques, the project transforms raw data into interactive visualizations that support data-driven decision-making for restaurant owners, business analysts, and researchers.

#### Key Objectives

* Compare the performance of restaurants across Swiggy and Zomato.
* Analyse customer ratings, delivery time, and pricing patterns.
* Identify popular cuisines and restaurant categories.
* Evaluate revenue and estimated profit across different locations.
* Discover regional trends and customer preferences.
* Generate meaningful business insights using Exploratory Data Analysis (EDA).
* Present interactive dashboards for easy analysis and decision-making.


#### Expected Deliverables

* Cleaned and preprocessed restaurant dataset.
* Interactive dashboard with dynamic filters.
* Comparative analysis of Swiggy and Zomato.
* Visual reports using charts and graphs.
* Business insights on ratings, pricing, cuisines, delivery performance, revenue, and profit.
* A user-friendly application that supports informed business decisions through data visualization and analytics.
""")
st.divider()
st.header("Project Description")
st.subheader("Problem Statement")
st.markdown("""

The online food delivery industry is highly competitive, with **Swiggy** and **Zomato** generating large volumes of restaurant data every day. Manually analysing this data to compare ratings, pricing, delivery performance, cuisines, and business trends is time-consuming and inefficient.

This project uses Data Science techniques to analyse and compare restaurant data from both platforms, providing meaningful insights through interactive visualizations and dashboards.

### The project helps:

* **Restaurant Owners:** Improve pricing and business performance.
* **Business Analysts:** Analyse market trends and customer preferences.
* **Food Delivery Platforms:** Compare ratings, revenue, and delivery performance.
* **Students & Researchers:** Understand Data Science through real-world restaurant data.

""")
st.subheader("Dataset Overview")

st.markdown("""The dataset contains restaurant information from **Swiggy** and **Zomato**, including:

#### **Restaurant Information**

* Restaurant id and location
* Cuisine and restaurant type
* Customer ratings
* Average cost for two
* Delivery time

#### **Business Metrics**

* Monthly revenue
* Estimated profit
* Market share
* Platform commission

### **Analysis Performed**

* Rating comparison
* Revenue and profit analysis
* Cuisine popularity
* City-wise analysis
* Interactive dashboard and visualizations""")
st.divider()
st.header(" Detailed Column Description")
st.markdown(""" #### Column Descriptions

* **restaurant_id:**  Unique identification number assigned to each restaurant.
* **restaurant_name:**  Name of the restaurant.
* **city:** City where the restaurant is located.
* **locality:** Specific area or locality of the restaurant.
* **restaurant_type:** Category of the restaurant (e.g., Café, Casual Dining, Quick Bites).
* **cuisines:** Types of cuisines served by the restaurant.
* **distance_from_city_center_km:** Distance of the restaurant from the city center (in kilometres).
* **opening_time:** Daily opening time of the restaurant.
* **closing_time:** Daily closing time of the restaurant.
* **days_operational:** Number of days the restaurant operates in a week.
* **swiggy_rating:** Customer rating of the restaurant on Swiggy.
* **swiggy_total_reviews:** Total number of customer reviews on Swiggy.
* **zomato_rating:** Customer rating of the restaurant on Zomato.
* **zomato_total_reviews:** Total number of customer reviews on Zomato.
* **average_rating_both_platforms:** Average customer rating across Swiggy and Zomato.
* **avg_cost_per_person_inr:** Average cost of food per person in Indian Rupees (₹).
* **price_category:** Price classification of the restaurant (Budget, Moderate, Premium, etc.).
* **swiggy_delivery_fee_inr:** Delivery fee charged by Swiggy (₹).
* **zomato_delivery_fee_inr:** Delivery fee charged by Zomato (₹).
* **swiggy_avg_delivery_time_minutes:** Average delivery time on Swiggy (minutes).
* **zomato_avg_delivery_time_minutes:** Average delivery time on Zomato (minutes).
* **swiggy_platform_commission_pct:** Commission percentage charged by Swiggy.
* **zomato_platform_commission_pct:** Commission percentage charged by Zomato.
* **swiggy_discount_frequency_pct:** Percentage of orders receiving discounts on Swiggy.
* **zomato_discount_frequency_pct:** Percentage of orders receiving discounts on Zomato.
* **swiggy_estimated_monthly_orders:** Estimated number of monthly orders through Swiggy.
* **zomato_estimated_monthly_orders:** Estimated number of monthly orders through Zomato.
* **swiggy_estimated_monthly_revenue_inr:** Estimated monthly revenue generated through Swiggy (₹).
* **zomato_estimated_monthly_revenue_inr:** Estimated monthly revenue generated through Zomato (₹).
* **swiggy_estimated_net_profit_inr:** Estimated monthly net profit earned from Swiggy (₹).
* **zomato_estimated_net_profit_inr:** Estimated monthly net profit earned from Zomato (₹).
* **swiggy_market_share_pct:** Estimated market share of the restaurant on Swiggy (%).
* **zomato_market_share_pct:** Estimated market share of the restaurant on Zomato (%).
* **platform_performance_better:** Indicates which platform performs better for the restaurant.
* **amenities:** Facilities and services available at the restaurant.
* **amenities_count:** Total number of amenities offered by the restaurant.
* **has_own_website:** Indicates whether the restaurant has its own official website (Yes/No).
* **has_own_app:** Indicates whether the restaurant has its own mobile application (Yes/No).
* **food_license_verified:** Indicates whether the restaurant's food licence is verified.
* **listing_date:** Date on which the restaurant was listed on the platform.
* **days_listed:** Total number of days the restaurant has been listed on the platform.
""")
st.divider()

@st.cache_data
def load_data():
    try:
        DATA_PATH = "swiggy_vs_zomato_3000.csv"
        df = pd.read_csv(DATA_PATH)
        return df,DATA_PATH
    except:
        st.error("Error loading the dataset. Please check the file path and ensure the CSV file is present.")
        return None, None
df,DATA_PATH=load_data()
st.header("Data Overview")
st.subheader("Dataset Basic Information")

col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric("Total Records",
              f"{df.shape[0]:,}")
with col2:
    st.metric("Total Columns",
              f"{df.shape[1]:,}")
with col3:
    memory_usage = df.memory_usage(deep=True).sum() / (1024 ** 2)  # Convert bytes to MB
    st.metric("Memory Usage (MB)",
                f"{memory_usage:.2f}")
with col4:
    st.metric("File Size (MB)",
              f"{os.path.getsize(DATA_PATH) / (1024 ** 2):.2f}")


tab1,tab2,tab3,tab4,tab5,tab6= st.tabs(["Column Info","Data Sample", "Data Types", "Missing Values","Statistics",'Catgorical Summary'])
with tab1:
    st.subheader("Column Information")
    column_info=pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes,
        "Non-Null Count": df.notnull().sum(),
        "Null Count": df.isnull().sum(),
        "Unique Values": df.nunique(),
    })
    st.dataframe(column_info,use_container_width=True)
    st.success("No missing value found in dataset")
with tab2:
    st.subheader("Sample Data")
    option = st.radio(
        "Select Sample",
        ["First 10 Rows","Last 10 Rows","Random 10 Rows"],

    )

    if option == "First 10 Rows":
        st.dataframe(df.head(10),use_container_width=True)
    elif option == "Last 10 Rows":
        st.dataframe(df.tail(10),use_container_width=True)
    else:
        st.dataframe(df.sample(10),use_container_width=True)
with tab3:
    st.subheader("Data Types")
    data_types=pd.DataFrame({
        "Data Type": df.dtypes.value_counts().index,
        "Count": df.dtypes.value_counts().values
    })
    st.dataframe(data_types,use_container_width=True)
with tab4:
    st.subheader("Missing Values")
    missing_values=pd.DataFrame({
        "Column Name": df.columns,
        "Missing Count": df.isnull().sum(),
        "Missing Percentage": (df.isnull().sum() / len(df)) * 100
    })
    st.dataframe(missing_values,use_container_width=True)
with tab5:
    st.subheader("Statistical Summary")
    st.markdown("#### Numerical Statistical")
    st.dataframe(df.select_dtypes(include=np.number).describe(),use_container_width=True)
    st.markdown("#### Categorical Statistical")
    categorical = df.select_dtypes(include=["object"]).describe()
    st.dataframe(categorical,use_container_width=True)

with tab6:

    st.subheader("📋 Categorical Data Summary")

    categorical_cols = [
        "city",
        "restaurant_type",
        "cuisines",
        "price_category",
        "platform_performance_better"
    ]

    for col in categorical_cols:

        st.markdown(f"### {col.replace('_', ' ').title()}")

        value_count = (
            df[col]
            .value_counts(dropna=False)
            .reset_index()
        )

        value_count.columns = [
            col.replace("_", " ").title(),
            "Count"
        ]

        st.dataframe(
            value_count,
            use_container_width=True,
            hide_index=True
        )

        st.write(f"**Total Unique Values:** {df[col].nunique()}")

        st.markdown("---")
@st.cache_data
def cleaned_data():
    try:
        cleaned_df = pd.read_csv("swiggy_vs_zomato_3000.csv")
        cleaned_df.drop(columns=["restaurant_name"], inplace=True)
        cleaned_df["opening_time"] = pd.to_datetime(cleaned_df["opening_time"])
        cleaned_df["closing_time"] = pd.to_datetime(cleaned_df["closing_time"])
        cleaned_df["listing_date"] = pd.to_datetime(cleaned_df["listing_date"])
        return cleaned_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

cleaned_df = cleaned_data()

cleaned_df=cleaned_data()
if "selected_city" not in st.session_state:
    st.session_state.selected_city = cleaned_df["city"].unique()

if "selected_restaurant_type" not in st.session_state:
    st.session_state.selected_restaurant_type = cleaned_df["restaurant_type"].unique()

if "selected_cuisine" not in st.session_state:
    st.session_state.selected_cuisine = cleaned_df["cuisines"].unique()

if "selected_rating" not in st.session_state:
    st.session_state.selected_rating = (
        float(cleaned_df["average_rating_both_platforms"].min()),
        float(cleaned_df["average_rating_both_platforms"].max())
    )

if "selected_cost" not in st.session_state:
    st.session_state.selected_cost = (
        int(cleaned_df["avg_cost_per_person_inr"].min()),
        int(cleaned_df["avg_cost_per_person_inr"].max())
    )


st.sidebar.title("👩‍💻 Student Information")

st.sidebar.markdown("""
**Name:** Parneet Kaur

**Roll No:** 24801076

**Course:** B.Tech CSE (AI & ML)

**University:** Sant Baba Bhag Singh University

**Project:** Swiggy vs Zomato: Restaurant Performance and Customer Insights Analysis

**Technologies Used:** Python | Pandas | Plotly | Streamlit
""")
with st.sidebar:


    st.title("🍴 Dashboard Filters")

    city = st.multiselect(
        "Select City",
        options=cleaned_df["city"].unique()
    )

    restaurant_type = st.multiselect(
        "Restaurant Type",
        options=cleaned_df["restaurant_type"].unique()
    )

    cuisine = st.multiselect(
        "Select Cuisine",
        options=cleaned_df["cuisines"].unique()
    )

    rating = st.slider(
        "Average Rating",
        min_value=float(cleaned_df["average_rating_both_platforms"].min()),
        max_value=float(cleaned_df["average_rating_both_platforms"].max()),
        value=st.session_state.selected_rating
    )

    cost = st.slider(
        "Average Cost (₹)",
        min_value=int(cleaned_df["avg_cost_per_person_inr"].min()),
        max_value=int(cleaned_df["avg_cost_per_person_inr"].max()),
        value=st.session_state.selected_cost
    )

    col1, col2 = st.columns(2)

    with col1:
        apply = st.button("Apply", type="primary", use_container_width=True)

    with col2:
        reset = st.button("Reset", use_container_width=True)
if apply:
    st.session_state.selected_city = city
    st.session_state.selected_restaurant_type = restaurant_type
    st.session_state.selected_cuisine = cuisine
    st.session_state.selected_rating = rating
    st.session_state.selected_cost = cost
if reset:

    st.session_state.selected_city = cleaned_df["city"].unique()

    st.session_state.selected_restaurant_type = cleaned_df["restaurant_type"].unique()

    st.session_state.selected_cuisine = cleaned_df["cuisines"].unique()

    st.session_state.selected_rating = (
        float(cleaned_df["average_rating_both_platforms"].min()),
        float(cleaned_df["average_rating_both_platforms"].max())
    )

    st.session_state.selected_cost = (
        int(cleaned_df["avg_cost_per_person_inr"].min()),
        int(cleaned_df["avg_cost_per_person_inr"].max())
    )
filtered_df = cleaned_df[
    (cleaned_df["city"].isin(st.session_state.selected_city))
    &
    (cleaned_df["restaurant_type"].isin(st.session_state.selected_restaurant_type))
    &
    (cleaned_df["cuisines"].isin(st.session_state.selected_cuisine))
    &
    (cleaned_df["average_rating_both_platforms"].between(
        st.session_state.selected_rating[0],
        st.session_state.selected_rating[1]
    ))
    &
    (cleaned_df["avg_cost_per_person_inr"].between(
        st.session_state.selected_cost[0],
        st.session_state.selected_cost[1]
    ))
]
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Dashboard Summary")

st.sidebar.metric("🍽️ Restaurants", filtered_df.shape[0])

st.sidebar.metric("🏙️ Cities", filtered_df["city"].nunique())

st.sidebar.metric("🍜 Cuisines", filtered_df["cuisines"].nunique())

st.sidebar.metric(
    "⭐ Avg Rating",
    round(filtered_df["average_rating_both_platforms"].mean(), 2)
)

st.sidebar.metric(
    "💰 Avg Cost",
    f"₹{round(filtered_df['avg_cost_per_person_inr'].mean(),0):,.0f}"
)
st.sidebar.metric(
    "🟠 Swiggy Avg Revenue",
    f"₹{filtered_df['swiggy_estimated_monthly_revenue_inr'].mean():,.0f}"
)

st.sidebar.metric(
    "🔴 Zomato Avg Revenue",
    f"₹{filtered_df['zomato_estimated_monthly_revenue_inr'].mean():,.0f}"
)

st.header("Visualization")
st.subheader("1️⃣ Bar Graph")
st.subheader(" Restaurants by City")

city_count = (
    filtered_df.groupby("city")
    .size()
    .reset_index(name="Restaurant Count")
)

fig = px.bar(
    city_count,
    x="city",
    y="Restaurant Count",
    color="Restaurant Count",
    text="Restaurant Count",
    title="Restaurants Available in Each City"
)

st.plotly_chart(fig, use_container_width=True)
#st.plotly_chart(fig1, use_container_width=True)
st.markdown("#### Insights:")
st.markdown("""

* Compares the number of restaurant listings across different cities.
* Highlights whether **Swiggy** or **Zomato** performs better in each city.
* Identifies cities where one platform has a clear competitive advantage.
* Reveals highly competitive cities with similar platform performance.
* Helps restaurants identify the strongest platform for their city.""")

#Line Chart
st.subheader("2️⃣ Line Chart")
st.subheader("Average Delivery Time vs Distance from City Center")

# Plot
df["distance"] = df["distance_from_city_center_km"].round()

line_df = (
    df.groupby("distance")[[
        "swiggy_avg_delivery_time_minutes",
        "zomato_avg_delivery_time_minutes"
    ]]
    .mean()
    .reset_index()
)

fig2 = px.line(
    line_df,
    x="distance",
    y=[
        "swiggy_avg_delivery_time_minutes",
        "zomato_avg_delivery_time_minutes"
    ],
    markers=True,
    title="Average Delivery Time vs Distance"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("#### Insights:")
st.markdown("""
* Delivery time increases as the distance from the city center increases.
* Swiggy and Zomato show nearly identical delivery time trends.
* Both platforms offer faster deliveries for nearby locations.
* Longer distances result in a noticeable rise in delivery time.
* The small gap between the two lines indicates similar delivery efficiency.
* Minor fluctuations suggest the impact of traffic and operational factors.
* Overall, distance has a greater impact on delivery time than the choice of platform.
""")



#Pie Chart

# Group the data
#  Pie Chart
st.subheader("3️⃣ Pie Chart")
st.subheader("Distribution of Better-Performing Platforms")

platform_share = (
    filtered_df.groupby("platform_performance_better")
    .size()
    .reset_index(name="Restaurant Count")
)

fig = px.pie(
    platform_share,
    names="platform_performance_better",
    values="Restaurant Count",
    title="Distribution of Better-Performing Platforms",
    hole=0.4,
    color="platform_performance_better",
    color_discrete_map={
        "Swiggy": "#FC8019",
        "Zomato": "#E23744"
    }
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

fig.update_layout(
    template="plotly_white",
    legend_title="Platform",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# Insights
st.markdown("####  Insights:")
st.markdown("""
- Shows the overall share of restaurants where each platform performs better.
- Highlights whether **Swiggy** or **Zomato** dominates in the selected filters.
- Displays both **percentage** and **platform name** inside the chart.
""")

#Scatter Plot
st.subheader("4️⃣ Scatter Plot")
st.subheader("Relationship Between Restaurant Pricing and Customer Ratings")

# Create scatter plot

fig = px.scatter(
    filtered_df,
    x="avg_cost_per_person_inr",
    y="average_rating_both_platforms",
    color="price_category",
    size="amenities_count",
    title="Relationship Between Restaurant Pricing and Customer Ratings",
    labels={
        "avg_cost_per_person_inr": "Average Cost Per Person (₹)",
        "average_rating_both_platforms": "Average Rating",
        "price_category": "Price Category",
        "amenities_count": "Amenities Count"
    }
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    xaxis_title="Average Cost Per Person (₹)",
    yaxis_title="Average Rating",
    legend_title="Price Category"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("####  Insights:")
st.markdown("""
- Shows the relationship between **restaurant pricing** and **customer ratings**.
- Compares ratings across different **price categories**.
- Larger bubbles represent restaurants with **more amenities**.
- Helps identify **high-performing** and **outlier restaurants** based on price, rating, and amenities.
- Makes it easier to observe whether **higher-priced restaurants generally receive better ratings**.
""")



#Histogram chart
st.subheader("5️⃣ Histogram")
st.subheader("Distribution of Average Cost by Price Category")

# Create histogram

fig = px.histogram(
    filtered_df,
    x="avg_cost_per_person_inr",
    color="price_category",
    nbins=20,
    title="Distribution of Average Cost by Price Category",
    labels={
        "avg_cost_per_person_inr": "Average Cost per Person (₹)",
        "price_category": "Price Category"
    },
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig.update_layout(
    template="plotly_white",
    xaxis_title="Average Cost per Person (₹)",
    yaxis_title="Number of Restaurants",
    legend_title="Price Category",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("####  Insights:")
st.markdown("""
- Shows the **distribution of average cost per person** across restaurants.
- Compares cost distribution among different **price categories**.
- Highlights the **most common price range** of restaurants.
- Identifies whether restaurants are concentrated in **budget, mid-range, or premium** categories.
- Helps understand the overall **pricing pattern** in the filtered dataset.
""")


#Box Plot
st.subheader("6️⃣ Box Plot")
st.subheader("Pricing Distribution Across Price Categories")

# Create box plot
fig6 = px.box(
    df,
    x='price_category',
    y='avg_cost_per_person_inr',
    color='platform_performance_better',
    points='outliers',  # Show only outlier points
    title='Pricing Distribution Across Price Categories',
    labels={
        'price_category': 'Price Category',
        'avg_cost_per_person_inr': 'Average Cost Per Person (₹)',
        'platform_performance_better': 'Better Performing Platform'
    }
)

fig6.update_layout(
    template='plotly_white',
    xaxis_title='Price Category',
    yaxis_title='Average Cost Per Person (₹)',
    legend_title='Platform Performance'
)

st.plotly_chart(fig6, use_container_width=True)

st.markdown("#### Insights:")
st.markdown("""
* Compares the **pricing distribution** across different price categories.
* Identifies **median cost** and variability within each category.
* Highlights **outlier restaurants** with unusually high or low prices.
* Compares pricing patterns where **Swiggy**, **Zomato**, or **Balanced** performs better.
* Reveals the **spread and consistency** of restaurant prices across categories.

""")


#Violin Chart
st.subheader("7️⃣ Violin Chart")
st.subheader("Distribution of Restaurant Ratings by Better Performing Platform")

# Create violin plot
fig7 = px.violin(
    df,
    x='platform_performance_better',
    y='average_rating_both_platforms',
    color='platform_performance_better',
    box=True,
    points='all',
    title='Distribution of Restaurant Ratings by Better Performing Platform',
    labels={
        'platform_performance_better': 'Better Performing Platform',
        'average_rating_both_platforms': 'Average Rating'
    }
)

fig7.update_layout(
    template='plotly_white',
    xaxis_title='Better Performing Platform',
    yaxis_title='Average Rating',
    legend_title='Platform Performance'
)

st.plotly_chart(fig7, use_container_width=True)

st.markdown("#### Insights:")
st.markdown("""
* Compares the **distribution of ratings** across better-performing platforms.
* Reveals the **spread and density** of customer ratings.
* Highlights differences in **median and variability** between Swiggy and Zomato.
* Identifies **clusters and outliers** in restaurant ratings.
* Helps determine which platform has **more consistently rated restaurants**.
""")


#Treemap Chart
st.subheader("8️⃣ Treemap")
st.subheader("Revenue Contribution by City and Restaurant Type")

# Group the data
treemap_data = (
    df.groupby(['city', 'restaurant_type'])
      .agg({
          'swiggy_estimated_monthly_revenue_inr': 'sum',
          'average_rating_both_platforms': 'mean'
      })
      .reset_index()
)

# Create treemap
fig8 = px.treemap(
    treemap_data,
    path=['city', 'restaurant_type'],
    values='swiggy_estimated_monthly_revenue_inr',
    color='average_rating_both_platforms',
    color_continuous_scale='RdYlGn',
    title='Revenue Contribution by City and Restaurant Type',
    labels={
        'swiggy_estimated_monthly_revenue_inr': 'Monthly Revenue (₹)',
        'average_rating_both_platforms': 'Average Rating'
    }
)

fig8.update_layout(
    template='plotly_white'
)

st.plotly_chart(fig8, use_container_width=True)

st.markdown("#### Insights:")
st.markdown("""
* Shows the **revenue contribution** of each city and restaurant type.
* Highlights **high-revenue cities** and restaurant categories.
* Uses color to indicate the **average customer rating**.
* Identifies **top-performing restaurant segments** within each city.
* Helps compare **revenue distribution and customer satisfaction** across locations and restaurant types.
""")

#Sunburst Chart
st.subheader("9️⃣ Sunburst Chart")
st.subheader("Restaurant Hierarchy by Restaurant Type and Better Performing Platform")

fig9 = px.sunburst(
    filtered_df,
    path=[
        #"city",
        "restaurant_type",
        "price_category",
        "platform_performance_better"
    ],
    values="swiggy_estimated_monthly_revenue_inr",
    color="average_rating_both_platforms",
    color_continuous_scale="RdYlGn",
    title="Restaurant Hierarchy by restaurant type and Better Performing Platform",
    labels={
        "city": "City",
        "restaurant_type": "Restaurant Type",
        "platform_performance_better": "Better Platform",
        "swiggy_estimated_monthly_revenue_inr": "Monthly Revenue (₹)",
        "average_rating_both_platforms": "Average Rating"
    },
    hover_data={
        "average_rating_both_platforms":":.2f"
    }
)

fig9.update_layout(
    template="plotly_white",
    title_x=0.5,
    margin=dict(t=70, l=20, r=20, b=20)
)

st.plotly_chart(fig9, use_container_width=True)

st.markdown("#### Insights:")
st.markdown("""
* Displays the **hierarchical distribution** of restaurants across **cities and restaurant types**.
* Shows which **platform performs better** within each restaurant category.
* Uses **segment size** to represent the estimated monthly revenue.
* Uses **color intensity** to indicate the average customer rating.
* Helps identify **high-performing cities, restaurant types, and platforms** in a single interactive visualization.
""")

#Bubble Chart
st.subheader("1️⃣0️⃣ Bubble Chart")
st.subheader("Swiggy vs Zomato Monthly Revenue Comparison")

# Create Bubble Chart

fig = px.scatter(
    filtered_df,
    x="swiggy_estimated_monthly_revenue_inr",
    y="zomato_estimated_monthly_revenue_inr",
    size="average_rating_both_platforms",
    color="city",
    hover_data={
        "restaurant_type": True,
        "price_category": True,
        "average_rating_both_platforms": ":.2f",
        "swiggy_estimated_monthly_revenue_inr": ":,.0f",
        "zomato_estimated_monthly_revenue_inr": ":,.0f"
    },
    title="Swiggy vs Zomato Monthly Revenue Comparison",
    labels={
        "swiggy_estimated_monthly_revenue_inr": "Swiggy Monthly Revenue (₹)",
        "zomato_estimated_monthly_revenue_inr": "Zomato Monthly Revenue (₹)",
        "average_rating_both_platforms": "Average Rating",
        "city": "City"
    }
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    xaxis_title="Swiggy Estimated Monthly Revenue (₹)",
    yaxis_title="Zomato Estimated Monthly Revenue (₹)",
    legend_title="City"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("####  Insights:")
st.markdown("""
- Compares **Swiggy** and **Zomato estimated monthly revenue** for each restaurant.
- Larger bubbles represent restaurants with **higher average ratings**.
- Different colors distinguish restaurants across **cities**.
- Helps identify restaurants performing well on **both platforms**.
- Makes it easy to compare revenue patterns after applying the selected dashboard filters.
""")

#Density Heatmap 
st.subheader("1️⃣1️⃣ Density Heatmap")
st.subheader("Density of Restaurants by Price and Customer Rating")

# Create Density Heatmap
fig11 = px.density_heatmap(
    df,
    x='avg_cost_per_person_inr',
    y='average_rating_both_platforms',
    nbinsx=30,
    nbinsy=20,
    color_continuous_scale='Viridis',
    title='Density of Restaurants by Price and Customer Rating',
    labels={
        'avg_cost_per_person_inr': 'Average Cost Per Person (₹)',
        'average_rating_both_platforms': 'Average Rating'
    }
)

fig11.update_layout(
    template='plotly_white',
    xaxis_title='Average Cost Per Person (₹)',
    yaxis_title='Average Rating',
    coloraxis_colorbar_title='Restaurant Count'
)

st.plotly_chart(fig11, use_container_width=True)

st.markdown("#### Insights:")
st.markdown("""
* Shows **high-density regions** based on restaurant price and ratings.
* Identifies the **most common price–rating combinations**.
* Reveals clusters of **similarly priced and rated restaurants**.
* Highlights areas with **low restaurant concentration**.
* Helps understand the relationship between **pricing and customer ratings** across the dataset.
""")



#Funnel Chart
st.subheader("1️⃣2️⃣ Funnel Chart")
st .subheader("Restaurant Count by Price Category and Better Performing Platform")

# Group the data
funnel_data = (
    df.groupby(['price_category', 'platform_performance_better'])
      .size()
      .reset_index(name='Restaurant Count')
)

# Create Funnel Chart
fig12 = px.funnel(
    funnel_data,
    y='price_category',
    x='Restaurant Count',
    color='platform_performance_better',
    title='Restaurant Count by Price Category and Better Performing Platform',
    labels={
        'price_category': 'Price Category',
        'Restaurant Count': 'Number of Restaurants',
        'platform_performance_better': 'Better Performing Platform'
    }
)

fig12.update_layout(
    template='plotly_white',
    legend_title='Platform Performance'
)

st.plotly_chart(fig12, use_container_width=True)

st.markdown("#### Insights:")
st.markdown("""
* Shows the **number of restaurants** in each price category.
* Compares **Swiggy and Zomato performance** within each price category.
* Identifies the **price categories with the highest restaurant concentration**.
* Highlights categories where **one platform has a competitive advantage**.
* Helps understand **platform performance across different pricing segments**.
""")
df = pd.read_csv("swiggy_vs_zomato_3000.csv")   # <-- Replace with your file name

# Calculate Average Ratings
swiggy_avg = df["swiggy_rating"].mean()
zomato_avg = df["zomato_rating"].mean()

# DataFrame for Plotly
rating_df = pd.DataFrame({
    "Platform": ["Swiggy", "Zomato"],
    "Average Rating": [swiggy_avg, zomato_avg]
})

# Title
st.subheader("⭐ Average Rating Comparison")

# Plotly Chart
fig = px.bar(
    rating_df,
    x="Platform",
    y="Average Rating",
    color="Platform",
    text="Average Rating",
    color_discrete_map={
        "Swiggy": "#FC8019",
        "Zomato": "#E23744"
    }
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig.update_layout(
    yaxis_title="Average Rating",
    xaxis_title="Platform",
    yaxis=dict(range=[0,5]),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# KPI Cards
col1, col2 = st.columns(2)

col1.metric("Swiggy Avg Rating", f"{swiggy_avg:.2f}")
col2.metric("Zomato Avg Rating", f"{zomato_avg:.2f}")

# Conclusion
st.subheader("Conclusion")

if swiggy_avg > zomato_avg:
    st.success(f"Swiggy has the highest average rating ({swiggy_avg:.2f}).")

elif zomato_avg > swiggy_avg:
    st.success(f"Zomato has the highest average rating ({zomato_avg:.2f}).")

else:
    st.info("Both platforms have the same average rating.")
st.title(" Major Findings & Insights")
st.markdown("Key characteristics of the restaurant dataset")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.write(f"""
### 🌍Geographical Distribution

Cities Covered:**{df['city'].nunique()}**

- Restaurants are available across multiple cities.
- Supports city-wise comparative analysis.
- Provides geographical coverage of the dataset.
""")

with col2:
    st.write(f"""
### ⭐ Customer Satisfaction

**Average Rating:** **{round(df['average_rating_both_platforms'].mean(),2)}**

- Represents overall customer satisfaction.
- Useful for comparing restaurant performance.
- Helps identify rating trends.
""")

with col3:
    st.write(f"""
### 🍽️ Restaurant Types

**Restaurant Categories:** **{df['restaurant_type'].nunique()}**

- Shows the diversity of restaurant types.
- Includes different dining formats.
- Useful for category-wise analysis.
""")


col4, col5, col6 = st.columns(3)

with col4:
    st.write(f"""
### 🍜 Cuisine Diversity

**Unique Cuisines:** **{df['cuisines'].nunique()}**

- Represents the variety of cuisines.
- Helps analyse food preferences.
- Supports cuisine-based comparison.
""")

with col5:
    st.write(f"""
### 💰 Pricing Overview

**Average Cost:** **₹{round(df['avg_cost_per_person_inr'].mean(),0):,.0f}**

- Shows the average cost per person.
- Useful for affordability analysis.
- Helps compare pricing levels.
""")

with col6:
    st.write(f"""
### 🏆 Platform Performance

**Performance Categories:** **{df['platform_performance_better'].nunique()}**

- Compares Swiggy and Zomato performance.
- Highlights the better-performing platform.
- Useful for platform-wise comparison.
""")

# ---------------- Row 3 ----------------
col7, col8, col9 = st.columns(3)

with col7:
    st.write(f"""
### 📈 Revenue Overview

- **Swiggy Avg Revenue :** **₹{round(df['swiggy_estimated_monthly_revenue_inr'].mean(),0):,.0f}**
- **Zomato Avg Revenue:** **₹{round(df['zomato_estimated_monthly_revenue_inr'].mean(),0):,.0f}**

- Represents estimated monthly revenue.
- Useful for revenue comparison.
- Indicates business performance.
""")

with col8:
    st.write(f"""
### 💵 Profit Overview

- **Swiggy Avg Profit:** **₹{round(df['swiggy_estimated_net_profit_inr'].mean(),0):,.0f}**
- **Zomato Avg Profit:** **₹{round(df['zomato_estimated_net_profit_inr'].mean(),0):,.0f}**

- Represents estimated monthly profit.
- Helps analyse profitability.
- Useful for financial comparison.
""")

with col9:
    st.write(f"""
### 📅 Dataset Coverage

**Days Listed:** **{int(df['days_listed'].mean())} Days**

- Indicates the average listing duration.
- Useful for analysing restaurant visibility.
- Supports performance evaluation.
""")
st.divider()
st.title("📌Implications & 💡Recommendations")
st.markdown("Business insights derived from Swiggy vs Zomato analysis")
st.divider()

# ---------------- Row 1 ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌍 Expand City Presence")

    with st.expander("📌 Implication"):
        st.markdown("""
- Cities with higher restaurant activity indicate strong demand.
- Market expansion opportunities can be identified.
""")

    with st.expander("💡 Recommendation"):
        st.markdown("""
- Target high-demand cities for business growth.
""")
with col2:
    st.markdown("### ⭐ Improve Customer Experience")
    with st.expander("📌 Implication"):
        st.markdown("""

- Ratings reflect customer satisfaction.
- Better service improves restaurant visibility.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Focus on food quality, delivery speed, and reviews.
""")

with col3:
    st.markdown("### 🍽️ Optimize Cuisine Strategy")
    with st.expander("📌 Implication"):
        st.markdown("""

**Implication:**

- Popular cuisines attract more customers.
- Food trends influence ordering behaviour.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Promote high-demand cuisines and diversify menus.
""")


# ---------------- Row 2 ----------------
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("### 💰 Smart Pricing Strategy")
    with st.expander("📌 Implication"):
        st.markdown("""

**Implication:**

- Pricing affects customer purchase decisions.
- Affordable options attract more users.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Create balanced pricing with value-based offers.
""")

with col5:
    st.markdown("### 🏆 Platform Optimization")
    with st.expander("📌 Implication"):
        st.markdown("""
    
**Implication:**

- Swiggy and Zomato performance varies by factors.
- Platform choice impacts visibility.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Use platform-specific strategies for better reach.
""")

with col6:
    st.markdown("### 📦 Delivery Performance")
    with st.expander("📌 Implication"):
        st.markdown("""

**Implication:**

- Faster delivery improves customer satisfaction.
- Delays can impact ratings.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Optimize delivery operations and logistics.
""")


# ---------------- Row 3 ----------------
col7, col8, col9 = st.columns(3)

with col7:
    st.markdown("### 📈 Revenue Growth")
    with st.expander("📌 Implication"):
        st.markdown("""

**Implication:**

- High-performing restaurants generate better revenue.
- Data helps identify growth opportunities.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Use analytics-driven marketing campaigns.
""")

with col8:
    st.markdown("### 💵 Profit Improvement")
    with st.expander("📌 Implication"):
        st.markdown("""

**Implication:**

- Revenue does not always indicate profitability.
- Cost management is important.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Reduce operational costs and improve margins.
""")

with col9:
    st.markdown("### 📊 Data-Driven Decisions")
    with st.expander("📌 Implication"):
        st.markdown("""
    

**Implication:**

- Analytics helps understand market patterns.
- Insights support strategic planning.""")
    with st.expander("💡 Recommendation"):
        st.markdown("""

**Recommendation:**

Continuously monitor KPIs for better decisions.
""")
st.title("📌 Final Conclusion")
st.markdown("Key Performance Summary of Swiggy vs Zomato Analysis")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🏙️ Cities Covered",
        f"{df['city'].nunique()}"
    )

with col2:
    st.metric(
        "⭐ Average Rating",
        f"{df['average_rating_both_platforms'].mean():.2f}/5"
    )

with col3:
    st.metric(
        "🍽️ Restaurant Categories",
        f"{df['restaurant_type'].nunique()}"
    )


col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "🍜 Cuisine Diversity",
        f"{df['cuisines'].nunique()}"
    )

with col5:
    st.metric(
        "💰 Avg Cost Per Person",
        f"₹{df['avg_cost_per_person_inr'].mean():,.0f}"
    )

with col6:
    platform_share = (
        df['platform_performance_better']
        .value_counts(normalize=True)
        .max()*100
    )

    st.metric(
        "🏆 Leading Platform Share",
        f"{platform_share:.1f}%"
    )


col7, col8, col9 = st.columns(3)

with col7:
    st.metric(
        "💵 Avg Net Profit",
        f"₹{df['swiggy_estimated_net_profit_inr'].mean():,.0f}"
    )

with col8:
    st.metric(
        "📅 Avg Listing Duration",
        f"{df['days_listed'].mean():.0f} Days"
    )
with col9:
    st.metric(
    "🚚 Avg Delivery Time",
    f"{filtered_df['swiggy_avg_delivery_time_minutes'].mean():.1f} min"
)
with st.expander("🏆 Top Restaurant by Estimated Profit", expanded=False):

    top_profit = (
        df.assign(
            Total_Profit=df["swiggy_estimated_net_profit_inr"] +
                         df["zomato_estimated_net_profit_inr"]
        )
        .sort_values("Total_Profit", ascending=False)
        [["restaurant_id", "Total_Profit","platform_performance_better"]]
        .head(1)
    )

    top_profit.columns = ["Restaurant's id", "Profit","Better Performing Platform"]

    top_profit["Profit"] = top_profit["Profit"].apply(lambda x: f"₹{x:,.0f}")

    st.dataframe(
        top_profit,
        use_container_width=True,
        hide_index=True
    )
avg_swiggy_rev = filtered_df["swiggy_estimated_monthly_revenue_inr"].mean()
avg_zomato_rev = filtered_df["zomato_estimated_monthly_revenue_inr"].mean()

best = "Swiggy" if avg_swiggy_rev > avg_zomato_rev else "Zomato"

with st.expander("💰 Highest Revenue Platform"):
    st.write(f"**Swiggy Average Revenue:** ₹{avg_swiggy_rev:,.0f}")
    st.write(f"**Zomato Average Revenue:** ₹{avg_zomato_rev:,.0f}")
    st.success(f"**Conclusion:** {best} generates higher estimated monthly revenue.")
swiggy_time = filtered_df["swiggy_avg_delivery_time_minutes"].mean()
zomato_time = filtered_df["zomato_avg_delivery_time_minutes"].mean()

best = "Swiggy" if swiggy_time < zomato_time else "Zomato"

with st.expander("🚚 Fastest Delivery Platform"):
    st.write(f"**Swiggy Average Delivery Time:** {swiggy_time:.1f} minutes")
    st.write(f"**Zomato Average Delivery Time:** {zomato_time:.1f} minutes")
    st.success(f"**Conclusion:** {best} delivers food faster on average.")

st.header("Project Impact")
st.markdown("Impact of Swiggy vs Zomato Analytics Project")
st.divider()
st.write("""
- This project helps in understanding restaurant market trends using data analysis.
- It provides insights into customer preferences, ratings, pricing, and platform performance.
- The analysis supports restaurants in improving their services and business strategies.
- Swiggy and Zomato performance comparison helps identify strengths and improvement areas.
- Data-driven insights help in making better decisions related to revenue, customer satisfaction, and growth.
- The project demonstrates how analytics can convert raw data into meaningful business insights.
""")