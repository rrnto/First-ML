# 🛳️ Titanic Survival Classifier

An interactive Python GUI app that predicts whether a passenger would have survived the Titanic disaster based on their **class, sex, and age**. Built with **Tkinter** and a **K-Nearest Neighbors (KNN)** machine learning model from **scikit-learn**, this app is both educational and fun for exploring **machine learning** concepts!  

---

## 📸 Preview

![App Screenshot](screenshot.png)  
*Example of the interface predicting survival probability for a passenger.*

---

## 🚀 Features

- ✅ Enter a **passenger name** for personalized predictions  
- ✅ Select **Passenger Class** (1, 2, 3) from a dropdown menu  
- ✅ Select **Sex** (Male / Female) from a dropdown menu  
- ✅ Enter **Age** manually  
- ✅ Predict survival probability and display result in a **friendly message**  
- ✅ Simple, clean, and intuitive **Tkinter GUI**

---

## 🧪 How It Works

The app uses a **K-Nearest Neighbors (KNN)** classifier trained on the **Titanic dataset** from seaborn. The GUI collects user input, converts it into numeric features, and passes it to the model. It displays a result like:

"Alice is predicted to Survive (85.3% confidence)"

Only the **most probable outcome** is shown along with its probability.  

---

## 🧰 Technologies Used

| Library          | Purpose                                |
|-----------------|----------------------------------------|
| `tkinter`       | GUI components (inputs, buttons, labels) |
| `scikit-learn`  | KNN machine learning model              |
| `numpy`         | Input array formatting for prediction   |
| `joblib`        | Save and load trained model             |

---

## 🛠 Installation

1. **Clone the repository** or download the files.  
2. **Install dependencies**:
```bash
pip install numpy scikit-learn joblib
```
> `tkinter` is included with Python, no separate installation needed.

3. **Run the GUI app**:
```bash
python gui.py
```

4. Enter passenger details and click **Predict Survival** to see results.  

---

## 🎨 Customization

- Modify **GUI layout, colors, and fonts** in `gui.py`  
- Train your own model using additional Titanic features (e.g., `fare`, `siblings`, `embarked`)  
- Replace KNN with other classifiers like **Random Forest** or **Logistic Regression**  

---

## 📚 Educational Use

This tool helps learners:  

- Understand **supervised machine learning** with KNN  
- Explore **data preprocessing** for categorical and numeric features  
- Build **interactive GUIs** in Python  
- See **real-time predictions** based on user input  

Ideal for ML beginners, students, or coding workshops.  

---

## 👤 Author

Developed by **Ranto Ny Aina ANDRIAMANANA**  

---

## 🪐 Future Improvements

- Add **more Titanic features** to improve accuracy  
- Enable **batch predictions** from CSV files  
- Save user predictions locally  
- Enhance GUI layout with **better spacing and alignment**  
- Display **charts for probability distributions**  

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share!  

---

**Made with Python — Powered by Curiosity 🚀**


