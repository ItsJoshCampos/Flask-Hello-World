# Flask API, Prepped for OIDC

## Local Setup for Dev
From this project directory, follow the steps:
### 1. Setup Virtual Environment
You should already have `virtualenv` already installed.
Create a virtual environment with the command below. Consider using `venv` as the name since its already added to the .gitignore file. 

```bash
python -m venv venv
```

### 2. Activate your Virtual Environment

```bash
source venv/bin/activate
```

### 3. Install Requirements.txt
Make sure pip is the latest version before installing, then install the libraries from the requirements file.
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt 
 ```

 ### 4. Setup .env file
 The command below copies the sample env file to a new file used in the application. 

 ```bash
cp .env.sample .env
 ```
Add the Flask secret key to the new `.env` file.

 ### 4. Setup oidc_settings.local file
 The command below copies the sample oidc settings file to a new file used in the application. 

 ```bash
cp oidc_settings.production.json oidc_settings.local.json
 ```
Add OIDC settings to the new `oidc_settings.local.json` settings file. __*This is required for the JWT tokens to work.*__

### SSL Issues
OIDC requires https, so additional steps may be required to setup after installing certifi from requirements.txt. You need a symlink in the OpenSSL directory for your local machine.  __These are steps for macOS.__ 

Run the following install certificates that ships with Python.  The path will vary depending on the version of Python you have installed:

```bash
cd /Applications/Python\ 3.7/
./Install\ Certificates.command
```


