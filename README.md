## Python Scrapper Stackoverflow - Seed
This is a basic scrapper (without any GUI) that fetches answers from a given stackoverflow post url and exports them as a csv file in the same root directory.

Data is exported in following format

| Comment           | User  |  User Profile Url | Date  |
| :------------- |:-----|:------------|:-----|
| \<Text of the comment> | \<Name of the user who commented> | \<Profile link of the user who commented> | \<Date and Time> 

#### Note
You must have `python` installed on your machine in order to run this project.
## Quick Start
To execute this scrapper, open up any CLI (e.g cmd) in the same directory as this file and enter,
```python
python scrap.py
```

#### Side Note: 
This scrapper uses `requests`, `beautilful4` and `pandas` imports. So make sure you have those installed first
```python
pip install requests
```
```python
pip install beautilful4
```
```python
pip install pandas
```

### Contact me
If you have any questions or ideas about this scrapper, please feel free to contact me at <a href="mailto:usafhassan@gmail.com">usafhassan@gmail.com</a>
