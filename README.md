# Bike Sharing Dashboard 

## Setup environment - Anaconda

conda create --name bike-env python=3.9
conda activate bike-env
pip install pandas matplotlib seaborn streamlit

## Setup environment - Terminal

mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## Run streamlit app

streamlit run dashboard/dashboard.py