# location-finder

Create virtual environment
```bash
$ python -m venv venv 
```
Activate Virtual Environment
```bash
$ source venv/bin/activate 
```
Run
```bash
$ python finder.py 
```
Install Requirement
```bash
$ pip install -r requirements.txt 
```
For making exe file run this command where python script placed
```bash
$ pyinstaller --add-data="assets/*;assets/" --noconsole --onefile finder.py 
```