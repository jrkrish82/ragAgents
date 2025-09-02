import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the Streamlit app
from cash_flow_forecasting_ui import main

if __name__ == "__main__":
    main()
