import streamlit as st
import pandas as pd
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cash_flow_forecasting import (
    load_cash_flow_data,
    visualize_cash_flow,
    split_data,
    train_arima_model,
    make_predictions,
    evaluate_model
)
import matplotlib.pyplot as plt

def login_screen():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")
    if login_btn:
        # Simple hardcoded credentials
        if username == "admin" and password == "password123":
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid username or password.")

def main_app():
    # Add Cognizant logo and header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            # Try to load local logo first
            st.image("src/cognizant_logo.png", width=300)
        except:
            try:
                # Fallback to online logo
                st.image("https://www.cognizant.com/content/dam/cognizant_foundation/logo/cognizant-logo-blue.png", 
                         width=300)
            except:
                # If both fail, show text header
                st.markdown("<div style='text-align: left;'>### Cognizant</div>", unsafe_allow_html=True)
                st.markdown("### Cognizant")
    
    st.title("Intelli Cash Forecasting Agent")
    st.markdown("---")
    # Load default data
    default_file = "src/cash_flow_test.csv"
    st.markdown("**Default Data File:** Using `cash_flow_test.csv` by default. You can upload a different file if needed.")
    default_data = None
    try:
        default_data = load_cash_flow_data(default_file)
        st.write("Default Data Loaded:")
        st.dataframe(default_data)
    except FileNotFoundError:
        st.error(f"Default file `{default_file}` not found. Please upload a file.")
    
    # File upload
    uploaded_file = st.file_uploader("Upload Cash Flow Data CSV", type=["csv"])
    
    # Logic to handle both default and uploaded data
    if uploaded_file:
        # Load data from uploaded file
        data = load_cash_flow_data(uploaded_file)
        st.write("Loaded Data (Uploaded):")
    elif default_data is not None:
        # Use default data if no file is uploaded and default data exists
        data = default_data
        st.write("Loaded Data (Default):")
    else:
        st.error("No data available. Please upload a CSV file.")
        st.stop()
    
    st.dataframe(data)
    
    # Visualize data
    st.subheader("Historical Cash Flow Visualization")
    visualize_cash_flow(data)
    st.pyplot(plt)  # Render the pyplot visualizations in Streamlit
    
    # Split data
    test_size = st.slider("Test Size (as a percentage)", min_value=10, max_value=50, value=20) / 100
    train, test = split_data(data, test_size=test_size)
    
    # Train ARIMA model
    st.subheader("Train ARIMA Model")
    order = st.text_input("ARIMA Order (p, d, q)", value="1,1,1")
    order_tuple = tuple(map(int, order.split(",")))
    model_fit = train_arima_model(train, order=order_tuple)
    
    # Make predictions
    test_with_predictions = make_predictions(model_fit, test)
    st.write("Test Data with Predictions:")
    st.dataframe(test_with_predictions)
    
    # Evaluate model
    mse = evaluate_model(test_with_predictions)
    if mse is None:
        st.write("No valid data available for evaluation. Please check your input or prediction logic.")
    else:
        st.write(f"Mean Squared Error: {mse}")
    
    # Visualize predictions
    st.subheader("Actual vs Predicted Closing Balance")
    plt.figure(figsize=(10, 6))
    plt.plot(test_with_predictions.index, test_with_predictions['Closing Balance'], label='Actual Closing Balance', color='blue')
    plt.plot(test_with_predictions.index, test_with_predictions['Predicted Closing Balance'], label='Predicted Closing Balance', color='orange')
    plt.title('Actual vs Predicted Closing Balance')
    plt.xlabel('Date')
    plt.ylabel('Closing Balance')
    plt.legend()
    st.pyplot(plt)  # Render the predictions plot in Streamlit

def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if not st.session_state["authenticated"]:
        login_screen()
    else:
        main_app()

if __name__ == "__main__":
    main()
