# # import streamlit as st
# # import shap
# # import pandas as pd
# # import joblib
# # import matplotlib.pyplot as plt

# # # --- Load full pipeline ---
# # model = joblib.load("demand_pricing_model.pkl")  # pipeline with preprocessing + model

# # st.title("Demand Sensitivity & Pricing Impact Predictor")

# # st.write("""
# # Predicts SKU demand based on price, discount, promotion, seasonality, and other factors.
# # Provides insights on which features impact demand the most using SHAP.
# # """)

# # # --- Sidebar: User Inputs ---
# # Price = st.sidebar.number_input("Price", value=100.0)
# # Discount = st.sidebar.number_input("Discount (%)", min_value=0, max_value=100, value=10)
# # Promotion = st.sidebar.selectbox("Promotion", [0, 1])
# # Seasonality = st.sidebar.selectbox("Seasonality", ["Winter", "Spring", "Summer", "Autumn"])
# # Category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"])
# # Region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
# # Weather_Condition = st.sidebar.selectbox("Weather Condition", ["Sunny", "Rainy", "Snowy", "Cloudy"])
# # Competitor_Price = st.sidebar.number_input("Competitor Price", value=95.0)

# # # --- Prepare input dataframe ---
# # input_df = pd.DataFrame({
# #     "Price": [Price],
# #     "Discount": [Discount],
# #     "Promotion": [Promotion],
# #     "Seasonality": [Seasonality],
# #     "Category": [Category],
# #     "Region": [Region],
# #     "Weather_Condition": [Weather_Condition],
# #     "Competitor_Price": [Competitor_Price]
# # })

# # # --- Prediction ---
# # predicted_demand = model.predict(input_df)[0]

# # st.subheader("Predicted Demand")
# # st.metric("Units Expected", round(predicted_demand, 2))

# # # --- Automated Insights ---
# # st.subheader("Automated Insights")

# # if Discount > 50:
# #     st.write("⚠ High discount detected. Demand might increase significantly.")
# # if Price > Competitor_Price:
# #     st.write("💡 Price higher than competitor: demand may decrease.")
# # if Promotion == 1:
# #     st.write("🎯 Promotion active: expect demand uplift.")
# # if Seasonality == "Summer" and Category in ["Clothing", "Toys"]:
# #     st.write("☀ Summer season: higher demand for seasonal items.")

# # # --- SHAP Explainability ---
# # st.subheader("Feature Impact (SHAP Waterfall)")

# # # Extract the model (e.g., RandomForestRegressor) from pipeline
# # reg_model = model.named_steps['model']
# # X_processed = model.named_steps['preprocess'].transform(input_df)

# # explainer = shap.TreeExplainer(reg_model)
# # shap_values = explainer(X_processed)

# # # Waterfall plot for single instance
# # single_shap = shap_values[0]
# # plt.figure(figsize=(10,6))
# # shap.plots.waterfall(single_shap, show=False)
# # st.pyplot(plt.gcf())
# # plt.clf()



# import streamlit as st
# import shap
# import pandas as pd
# import joblib
# import matplotlib.pyplot as plt

# # --- Load full pipeline ---
# model = joblib.load("demand_pricing_model.pkl")  # pipeline with preprocessing + model

# st.title("Demand Sensitivity & Pricing Impact Predictor")

# st.write("""
# Predicts SKU demand based on price, discount, promotion, seasonality, and other factors.
# Provides insights on which features impact demand the most using SHAP.
# """)

# # --- Sidebar: User Inputs ---
# # Price = st.sidebar.number_input("Price", value=100.0)
# # Discount = st.sidebar.number_input("Discount (%)", min_value=0, max_value=100, value=10)
# # Promotion = st.sidebar.selectbox("Promotion", [0, 1])
# # Seasonality = st.sidebar.selectbox("Seasonality", ["Winter", "Spring", "Summer", "Autumn"])
# # Category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"])
# # Region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
# # Weather_Condition = st.sidebar.selectbox("Weather Condition", ["Sunny", "Rainy", "Snowy", "Cloudy"])
# # Competitor_Price = st.sidebar.number_input("Competitor Price", value=95.0)

# # # --- Add missing columns with default values ---
# # Epidemic = st.sidebar.selectbox("Epidemic", [0, 1])  # 0 = No epidemic, 1 = Epidemic
# # Price_Gap = st.sidebar.number_input("Price Gap vs Competitor", value=0.0)


# Price = st.sidebar.number_input("Price", value=100.0)
# Discount = st.sidebar.number_input("Discount (%)", min_value=0, max_value=100, value=10)
# Promotion = st.sidebar.selectbox("Promotion", [0, 1])
# Seasonality = st.sidebar.selectbox("Seasonality", ["Winter", "Spring", "Summer", "Autumn"])
# Category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"])
# Region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
# Weather_Condition = st.sidebar.selectbox("Weather Condition", ["Sunny", "Rainy", "Snowy", "Cloudy"])
# Epidemic = st.sidebar.selectbox("Epidemic?", [0, 1])
# Price_Gap = st.sidebar.number_input("Price Gap vs Competitor", value=0.0)
# Competitor_Price = st.sidebar.number_input("Competitor Price", value=95.0)


# # --- Prepare input dataframe ---
# input_df = pd.DataFrame({
#     "Price": [Price],
#     "Discount": [Discount],
#     "Promotion": [Promotion],
#     "Seasonality": [Seasonality],
#     "Category": [Category],
#     "Region": [Region],
#     "Weather_Condition": [Weather_Condition],
#     "Competitor_Price": [Competitor_Price],
#     "Price_Gap": [Price_Gap],
#     "Epidemic": [Epidemic]
# })

# # --- Prediction ---
# # predicted_demand = model.predict(input_df)[0]

# # st.subheader("Predicted Demand")
# # st.metric("Units Expected", round(predicted_demand, 2))

# # # --- Automated Insights ---
# # st.subheader("Automated Insights")
# # if Discount > 50:
# #     st.write("⚠ High discount detected. Demand might increase significantly.")
# # if Price > Competitor_Price:
# #     st.write("💡 Price higher than competitor: demand may decrease.")
# # if Promotion == 1:
# #     st.write("🎯 Promotion active: expect demand uplift.")
# # if Seasonality == "Summer" and Category in ["Clothing", "Toys"]:
# #     st.write("☀ Summer season: higher demand for seasonal items.")
# # if Epidemic == 1:
# #     st.write("⚠ Epidemic active: demand might be affected.")

# # # --- SHAP Explainability ---
# # st.subheader("Feature Impact (SHAP Waterfall)")

# # Extract the model (e.g., RandomForestRegressor) from pipeline
# reg_model = model.named_steps['model']
# X_processed = model.named_steps['preprocess'].transform(input_df)


# predicted_demand = reg_model.predict(X_processed)[0]
# st.metric("Predicted Demand", round(predicted_demand, 2))

# explainer = shap.TreeExplainer(reg_model)
# shap_values = explainer(X_processed)

# # Waterfall plot for single instance
# single_shap = shap_values[0]
# plt.figure(figsize=(10,6))
# shap.plots.waterfall(single_shap, show=False)
# st.pyplot(plt.gcf())
# plt.clf()



import streamlit as st
import pandas as pd
import joblib

# --- Load full pipeline ---
model = joblib.load("demand_pricing_model.pkl")  # pipeline with preprocessing + model

st.title("Demand Sensitivity & Pricing Impact Predictor")

st.write("""
Predicts SKU demand based on price, discount, promotion, seasonality, 
and other business factors.
""")

# --- Sidebar: User Inputs ---
Price = st.sidebar.number_input("Price", value=100.0)
Discount = st.sidebar.number_input("Discount (%)", min_value=0, max_value=100, value=10)
Promotion = st.sidebar.selectbox("Promotion", [0, 1])
Seasonality = st.sidebar.selectbox("Seasonality", ["Winter", "Spring", "Summer", "Autumn"])
Category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"])
Region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
Weather_Condition = st.sidebar.selectbox("Weather Condition", ["Sunny", "Rainy", "Snowy", "Cloudy"])
Epidemic = st.sidebar.selectbox("Epidemic?", [0, 1])
Price_Gap = st.sidebar.number_input("Price Gap vs Competitor", value=0.0)
Competitor_Price = st.sidebar.number_input("Competitor Price", value=95.0)

# --- Prepare input dataframe ---
input_df = pd.DataFrame({
    "Price": [Price],
    "Discount": [Discount],
    "Promotion": [Promotion],
    "Seasonality": [Seasonality],
    "Category": [Category],
    "Region": [Region],
    "Weather_Condition": [Weather_Condition],
    "Competitor_Price": [Competitor_Price],
    "Price_Gap": [Price_Gap],
    "Epidemic": [Epidemic]
})

# --- Prediction ---
predicted_demand = model.predict(input_df)[0]

st.subheader("Predicted Demand")
st.metric("Units Expected", round(predicted_demand, 2))

# --- Business Insights ---
st.subheader("Automated Business Insights")

if Discount > 50:
    st.warning("High discount applied — demand is expected to increase.")

if Price > Competitor_Price:
    st.info("Price is higher than competitor — demand may reduce.")

if Promotion == 1:
    st.success("Promotion active — positive impact on demand expected.")

if Seasonality == "Summer" and Category in ["Clothing", "Toys"]:
    st.success("Seasonal uplift expected for this category.")

if Epidemic == 1:
    st.warning("Epidemic impact enabled — demand may fluctuate.")



