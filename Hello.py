import streamlit as st
import pandas as pd

results_df = pd.DataFrame({
    'Method': ['LinearRegressor'],
    'RMSE TRAIN': [331.82],
    'RMSE TEST': [331.09],
    'MSE TRAIN': [110104.96],
    'MSE TEST': [109626.44],
    'R-squared TRAIN': [0.000203],
    'R-squared TEST': [-0.000258]
})


data = {
    'Y_test': [648.0, 798.0, 355.0, 1086.0, 1160.0, 1154.0, 630.0, 296.0, 1170.0, 596.0, 178.0, 717.0, 989.0,
               539.0, 105.0, 1062.0, 287.0, 530.0, 270.0, 599.0, 794.0, 634.0, 766.0, 228.0, 743.0, 539.0, 451.0,
               357.0, 690.0, 303.0, 742.0, 564.0, 355.0, 831.0, 525.0, 51.0, 457.0, 1142.0, 531.0, 874.0, 343.0,
               282.0, 459.0, 464.0, 500.0, 342.0, 803.0, 725.0, 716.0, 969.0],
    'Y_pred': [651.57, 801.95, 355.88, 1087.60, 1162.75, 1157.77, 631.51, 295.73, 1172.79, 596.38, 180.44, 716.72,
               992.37, 541.31, 105.29, 1062.54, 285.73, 531.28, 270.70, 601.48, 796.93, 636.56, 766.83, 230.59, 746.82,
               541.32, 451.10, 355.85, 691.67, 305.73, 741.76, 566.36, 355.89, 831.98, 526.30, 50.16, 456.11, 1142.72,
               531.24, 877.13, 345.83, 280.73, 461.14, 466.15, 501.21, 340.82, 806.92, 726.77, 716.73, 972.35]
}

df = pd.DataFrame(data)

###

st.set_page_config(
    page_title="Hello",
)

###

st.markdown("# Air BnB Price Prediction and Segmentation! 🏨🛎️📊")

st.markdown("""### Full Presentation [Portfolio](https://bit.ly/Portfolio_Oktober_2023) ❤️""")

st.markdown(
    """
    Thank you for checking out my portfolio! Before exploring this Streamlit app, feel free to take a look at my other projects. 🚀📁
    - 👚 **Development of A Color Mapping and Classification System for Batik Textile from Garut and Solo** [Bachelor Degree's Thesis](https://drive.google.com/file/d/1qY1rlhd6_S6CLhb54X8HYneTGZgYliCv/view?usp=sharing)
    - ⛔ **Machine Learning Model to Predict Hotel Booking Cancellation** [Don't Cancel!](https://bit.ly/DontCancel_RiriRaissa)
    - 📦 **SQL Query Study Case: Revolutionize Sales Unleashing the Power of Product** [SQL Query](https://bit.ly/PortfolioSQL_Nov)
    - 👋 **Hand Sign Detector on MATLAB** [Demo Video](https://bit.ly/ImageProcessing_MATLAB)

    ### Please read below before you get started 👇👇👇
"""
)





st.markdown(
    """
🏡 Air BnB is a popular online marketplace and hospitality service that allows people to rent or lease short-term lodging accommodations.

🏡 The problem is that both hosts looking to rent out their homes and guests looking to purchase are unaware of the market for the properties they are offering.
""")
st.image('4.png', caption='Heatmap of All Variable', use_column_width=True)

st.markdown(
    """
The presence of multivariate, rather than multicollinearity, indicates that it is acceptable to proceed with machine learning.

# Model 🤖
# **1. Linear Regressor 🌲**
"""
)

st.markdown(
    """
🌲 Using linear regression for error and test data prediction is not too far off, but in machine learning simulations, hotel costs are very different from the predictions of the random forest model.

🌲 These are the error metrics; it has good RMSE, MSE, and R-squared values. The model didn't experience overfitting or underfitting.
""")

st.image('RandomForestGraph.png', caption='Model Performance', use_column_width=True)

st.markdown("## Evaluation Metriks")


# Display the DataFrame with specified precision
st.table(results_df.style.format(precision=6))

st.markdown("## Prediction Value")

st.dataframe(df, hide_index=True)

###


st.markdown("# **2. K-Means Clustering 🛌**")

st.markdown("""
            
I'm utilizing K-Means Clustering to categorize Airbnb listings into 6 groups based on previously summarized variables.
            🏡✨ This approach allows for a more structured and insightful segmentation of the data 📊🔍
            """)

st.image('5.png', caption='K-Means Clustering', use_column_width=True)
st.image('6.png', caption='Air BnB Market Segmentation', use_column_width=True)

###

st.markdown(
    """
    **👈 Select any pages from the sidebar** to see some demonstration!

    Enjoy! Critiques and suggestions are welcome, you can contact me at:
    - 📨 riri.raissa12@gmail.com
    - 👷 Let's get connected on [LinkedIn](https://www.linkedin.com/in/riri-raissa/)
    - 💻 https://github.com/ririraissa
"""
)
