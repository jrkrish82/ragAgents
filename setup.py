from setuptools import setup, find_packages

setup(
    name="cashflow_forecasting",
    version="1.0.0",
    packages=find_packages(where="src"),  # Specify the source directory
    package_dir={"": "src"},  # Map the root package to the "src" directory
    install_requires=[
        "streamlit",
        "pandas",
        "numpy",
        "matplotlib",  
        "scikit-learn",
        "seaborn",
        "openpyxl",
        "pytest",
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "cashflow_forecasting=cash_flow_forecasting_ui:main",  # Adjusted to match your file structure
        ],
    },
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify the minimum Python version
)