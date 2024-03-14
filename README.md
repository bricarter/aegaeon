# vulnerableauth1

An intentionally vulnerable, authentication system designed for beginners to explore the concepts of username enumeration and password brute-force. 

**vulnerableauth1** is easy enough to solve manually, but it could be worthwhile to use automated security tools.


## Warnings:
1. This project is vulnerable ON PURPOSE.  
DO NOT send issues, pull requests, security reports, or CVEs.  They will all be IGNORED.
1. This application is highly insecure, and as such, should not be deployed on internet facing servers.
1. By installing, you take full responsibility for using it.
1. Hacking is ILLEGAL unless given permission by the target. :)


## Installation:

Make sure Python 3.10 is installed.  

```
python3 --version
```  

<br>

Clone this repository.  

```
git clone https://github.com/bricarter/vulnerableauth1.git
```

<br>

Move into the `vulnerableauth1/` directory.  

```
cd vulnerableauth1/
```

<br>

(Recommended) Create a virtual environment to hold the application's dependencies. 

Here is the command to create a virtual environment using python's built in venv module.

```
python3 -m venv <venv_name> 
``` 

<br>

If you created a virtual environment in the previous step, activate the environment per your shell instructions.  

Here are commands to activate virtual environments created using python's built in venv module.

| Shell | Command |
|-------|---------|
| bash/zsh | `source <venv_name>/bin/activate` |
| fish | `source <venv_name>/bin/activate.fish` |
| csh/tcsh | `source <venv_name>/bin/activate.csh` |
| PowerShell | `<venv_name>/bin/Activate.ps1` |
| (Windows) PowerShell | `<venv_name>/Scripts/Activate.ps1` |
| (Windows) cmd.exe | `<venv_name>/Scripts/activate.bat` |

<br>

(Optional) Upgrade pip.

```
pip install --upgrade pip
```

<br>

Install the dependencies found in the `requirements.txt` file.  

```
pip install -r requirements.txt
```

<br>

Run the application.  

```
flask run
```

<br>

The development server should then be started on `localhost:5000`

Happy learning! 