## How to Run the Project

1. Clone the repository 

2. Create and activate virtual environment 
(if required bypass execution policy using and then activate virtual env. : Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  )

In terminal :
python -m venv venv
venv\Scripts\activate

3. Install dependencies using requirements.txt (~200MB data required for downloading)

pip install -r requirements.txt

4. Launch Jupyter Notebook and open '01_Data_Preprocessing.ipynb' present in 'notebooks' folder. Run this notebook cell by cell in order to obtain processed data.

5. Open next notebook '02_Exploratory_Data_Analysis.ipynb' and run cell by cell to see detailed data analysis.

6. Open last notebook '03_Model_Training+Feature Importance.ipynb' and run cell by cell create and save best model then display top 10 features that affect student's final grade.
