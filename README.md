# Car_Price_Prediction🚗 Car Price Prediction
This project is a Machine Learning web application built with Streamlit to predict the selling price of used cars based on various features such as brand, model, year, fuel type, mileage, and more.
The ML model is trained using a Random Forest Regressor pipeline that includes preprocessing steps for both categorical and numerical features. The dataset used is Cardetails.csv.
📌 Features
Select car brand and model from dropdown menus.
Choose categorical features like fuel type, transmission, owner type.
Enter numerical details like year, kilometers driven, mileage, engine, max power, seats.
Instant predicted selling price output.
User-friendly Streamlit interface.
📂 Project Structure
Car_Price_Prediction/
│
├── app.py                # Streamlit app code
├── model.joblib           # Trained ML model
├── Cardetails.csv         # Dataset
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
⚙️ Installation & Usage
1️⃣ Clone the repository
git clone https://github.com/yourusername/Car_Price_Prediction.git
cd Car_Price_Prediction
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit app
streamlit run app.py
🧠 Model Details
Algorithm: Random Forest Regressor
Preprocessing: OneHotEncoding for categorical features, passthrough for numerical features.
Target Variable: Selling Price (in INR).
📊 Dataset
The dataset Cardetails.csv contains:
Categorical Features: name, fuel, seller_type, transmission, owner
Numerical Features: year, km_driven, mileage, engine, max_power, seats
Target Variable: selling_price
📌 Example Prediction
Input:
Brand: Maruti
Model: Maruti Swift VXI
Year: 2015
Fuel: Petrol
Transmission: Manual
Mileage: 18.0 kmpl
Engine: 1197 CC
Max Power: 82 bhp
Seats: 5
Kilometers Driven: 45,000
Output:
💰 Estimated Selling Price: ₹4,85,000
🛠 Technologies Used
Python
Pandas, NumPy
Scikit-learn
Joblib
Streamlit
