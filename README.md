# location-finder

Create virtual environment
```bash
$ python -m venv venv 
```
Activate Virtual Environment
```bash
$ source venv/bin/activate 
```
Install Requirements
```bash
$ pip install -r requirements.txt 
```
Run application
```bash
$ python finder.py 
```
For making executable file, run this command where python script is located
```bash
$ pyinstaller --add-data="assets/*;assets/" --noconsole --onefile finder.py 
```