# **PLANIT-SDET-ASSESSMENT REPO**

![alt test pass](/TEST_PASS.png)

# Objective:

- Solve challenges from Planit - SDET - Assessment.
- Gain experience in Testing using different technologies.
- Improve Python coding skills.

# Technologies used:

- Python: 3.8.9
- Python virtual environment (venv)
- Selenium: 4.3.0
- Chromedriver: 103.80 LTS
- Google Chrome: 103.0.5060
- Mac OS: 12.4
- Visual Studio Code: 1.69.1 (Mac)

# Environment to run:

- This project is optimised for Python and venv, to reduce conflicts with local Python packages and projects.
- Highly recommended install pip packages from [requirements.txt](/Task1/requirements.txt) (locate in Task1 directory).
- [Chromedriver](/Task1/chromedriver) saves to Task 1 directory for conveniently locating but not required.

# Installation:

1. Clone or download the repo from GitHub.
2. Setup environmental path, for Mac:  
   **sudo nano /etc/paths**  
    enter local password, then add path of chromedriver at the end of the file, e.g: _/Users/username/Documents/GitHub/Planit-SDET-Assessment/Task1/chromedriver_  
   Type **Y** then **Ctrl+C** to save
3. Setup Python virtual environment:  
   **python3 -m venv env**  
   include env folder in [.gitignore](/Task1/.gitignore) file  
   Activate a virtual environment (Mac):  
   **source env/bin/activate**  
   Deactivate a venv, at CLI run: **deactivate**
4. To install all dependencies, at CLI run: **python3 -m pip install -r requirements.txt**
5. At CLI, run **./tesh.sh** (an optimised shell script to run all 10 test cases)

# Folder structure:

Task1  
|_\_\001_Navigate_Shop_Page  
|\_\_test.py  
|_\_\002_Buy_Shop_Page  
|\_\_\_\_test.py  
|...  
| .gitignore  
| chromedriver  
| PLANIT_SDET_TESTING_TASK1_TESTING_CASES.csv  
| README.md  
| [requirements.txt](/Task1/requirements.txt)  
| [test.sh](/Task1/test.sh)  
Task2  
| \_\_[challenge_002.py](/Task2/challenge_002.py)  
| \_\_[challenge_006.py](/Task2/challenge_006.py)  
| README.md

# Acknowledgement:

- This project uses resources from Selenium, Python docs and other sites
- Credits to Planit Testing for giving me a chance to delve deeper to automation test and test planning.

# Final words:

- This is the first time I use Selenium, as I always use Jest framework for testing but Selenium is built for webscraping and automation test, therefore I have no other choice with the requested e-commerce site.
- My code seems repetitive with boilerplates DOM elements targeting and import modules lines, but my unit_test directory is incomplete so I do not feel too confident with that approach even though testing with Page Object Models and Unittest library is the most appropriate method for this kind of blackbox test.
- Test planning with test cases is truly handy process which helps testers see the picture more clearly and precisely. A clear plan will avoid Hit & Miss approach.

Thanks,

**Tony Nguyen**
