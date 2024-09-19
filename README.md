# Customer-Churn-Prediction-APP
This is a web-based application built with Streamlit that predicts customer churn using embeded machine learning models. The app allows users to upload customer data, preprocess it, and run predictions to identify which customers are at risk of churning (stop using a service/product), whose main aim is to ease usage to stakeholders who don't have the technical knowledge to read a Jupyter Notebook

The models (Random Forest, Gradient Boosting Model and Support Vector Machine) are located in the "models" folder, while the source codes are available in the "pages" folder and the Home.py file. The required CSV/XLSX files can be found in the "data" folder.

**💻 Getting Started**
To get a local copy up and running, follow these steps.

**Prerequisites**
In order to run this project, you need:
-Python
-Streamlit
-Setup
-Clone this repository to your desired folder:

- cd my-folder
- git clone <https://github.com/Njuraita/Customer-Churn-Prediction-APP.git>
- Change into the cloned repository

- Create a virtual environment

```
python -m venv env
```

- Activate the virtual environment

```
env/Scripts/activate
```

- Here, you need to repeatedly install the packages in the requirements.txt file using the command below

```
 pip install -r requirements.txt
``` 

- Usage
To run the project, execute the following command:

```
 streamlit run Home.py
``` 

- A webpage opens up to view the app.
- Login to the app with username **Churn_Classifier_1** and password **CL&331F13R_1**
- Finally test a prediction by clicking on the predictions page.



*Contributing Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change*

Contact me via email: njerisharon06@gmail.com
Article Link: https://medium.com/@njerisharon06/customer-prediction-app-ac2be6e0a560
