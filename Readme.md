# 1. Test requirements
API = https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false

Acceptance Criteria:

    Name = "Carbon credits"
    CanRelist = true
    The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
Instructions:

    Your test needs to be written using a programming language of your choice (not a tool like SoapUI). Ensure you include a clear ReadMe
    Submit your test to us in a format that lets us execute and review the code (it must be submitted in a public repository like Bitbucket or Github)
    Your test must validate all the three acceptance criteria
    Points will be awarded for meeting the criteria, style and the use of good practices and appropriate use of source control
    We want to see your best work - no lazy coding or comments.

# 2.  Analysis

2.1 Test method: pytest

2.2 Exiting conditions:
* a. Json file
* b. URL

2.3 In Scope: 
* Verification output for: HTTPS + API + Json
* Deployment: Github

2.4  Out of Scope:
* Report, Security, efficiency


# 3. Test implementation
## 3.1 Test environment: 
Suggest to run with: Windows 10(64) + python 3.10.8 + pycharm professional(2022.1.1) + pytest

Tested: Windows 11 + python 3.10.4(64) + pycharm community(2022.1) + pytest are also workable
## 3.2 tools installation:
1. [x] download and install the latest python 3.10.8: https://www.python.org/downloads/
2. [x] download pycharm(professional or community): https://www.jetbrains.com/pycharm/
3. [x] download and install pip:https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
   * upgrade to  the latest version: pip install --upgrade pip

## 3.3 Get source code from git
Clone project from git

   https://github.com/qdtomzhang/assurity_test
  
## 3.4  Setup virtual environment

A note before beginning: As time limit, ideally we can run the test from 4 different environments: cmd, PowerShell, git bash, and PyCharm. 
I just tested and strongly recommend PyCharm and cmd. And I also strongly recommend against PowerShell.

Best practice is to maintain virtual environments for different python projects to avoid dependency conflicts. `cd` into the `assurity_api_test` directory and run.

`$ python -m venv venv` 

` $ .\venv\Scripts\activate`

Then install the requirements:

`(venv) $ python -m pip install -r requirements.txt`

Now you can run pytest!

`cd` to "assurity_test", or you may need try `cd` to "test", as different environments may have differences

`(venv) $ pytest`

```(venv) PS E:\pythonProject\assurity_test\test> pytest
(venv) PS D:\assurity_test> pytest
=========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.10.4, pytest-7.1.3, pluggy-1.0.0
rootdir: D:\assurity_test
collected 2 items                                                                                                                                                          

test\test_category.py ..                                                                                                                                             [100%] 

============================================================================ 2 passed in 0.10s ============================================================================ 
```
If you are using Pycharm to run, it will detect the missing package automatically and you need to accept the suggestions from Pycharm.
Make sure you are using the venv that crated before in your IDE
If you get failure inside IDE, mostly it should be caused by python environment settings.
Please refer to the requirement.txt file to manually install. 


**Others:**


`why using .json file as input, not to do hard-code value comparison
`

* Definitely we can do hard-code value comparison for known input, but it will be hard to maintain when input changes 
* It's better to use the similar framework to test more scenarios, so json file as a baseline setting will help us to 
maintain easily


`uncertainty for acceptance 3:`

 The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
 

_I don't know the logical design behind that will influence the test result.
eg.webpage design for "Gallery "changes from ["Promotions"][1] to ["Promotions"][2]. 
So, I provide 2 versions: hardcode/smart but complicated._
