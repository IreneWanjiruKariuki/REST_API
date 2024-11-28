# REST_API

A simple REST API in Python that manages a Product resource and handles JSON requests and responses.

## Prerequisites
Ensure you have the following installed in your system:
 - Python(3.12.6)
 - pip

## Setting up the environment
Follow the following steps to create and run the project:

### 1. Create a github repository
 - Go to [GitHub](https://github.com/) and create a new repository
 - Copy the repository URL

### 2. Clone the repository
 ```bash
 git clone https://github.com/IreneWanjiruKariuki/REST_API.git
 ```

 ### 3. Create and activate a virtual environment
 Create a virtual environment to isolate project dependencies:

 ```bash
 py -m venv venv
 ```

 Avtivate the virtual environment:


 ```bash
 .\venv\Scripts\Activate.ps1
 ```

 ### 4. Install requirements

 ```bash
 pip install requests fastapi uvicorn
 ```

 ### 5. Install django

 ```bash
 py -m pip install Django
 ```

 ### 6. Create a project

 ```bash
 django-admin startproject ProductResourse
 ```

 ### 7. Create app

 ```bash
 django-admin startapp products
 ```

 ### 8. Start the development server

 ```bash
 python manage.py runserver
 ```