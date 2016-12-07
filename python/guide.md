https://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/<br>
http://www.oschina.net/translate/open-sourcing-a-python-project-the-right-way

http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
![](https://i.stack.imgur.com/LUyfq.png)


PEP 8 -- Style Guide for Python Code<br>
https://www.python.org/dev/peps/pep-0008/

Lib/HTMLParser.py source code<br>
https://docs.python.org/2/library/htmlparser.html<br>
http://fulerbakesi.iteye.com/blog/1589102

## python database

### SQLAlchemy
pip install SQLAlchemy

http://www.sqlalchemy.org/<br>
http://docs.sqlalchemy.org/<br>
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0014021031294178f993c85204e4d1b81ab032070641ce5000

url = 'mysql+mysqlconnector://root:password@localhost:3306/test?charset=utf8'

### DBUtils
Python数据库连接池DBUtils.PooledDB<br>
https://pypi.python.org/pypi/DBUtils/


### MySQLdb(only support python 2)
https://pypi.python.org/pypi/MySQL-python<br>
pip install MySQL-python<br>
id = cursor.lastrowid<br>
cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

基于DBUtils和MySQLdb连接池简洁封装<br>
http://blog.csdn.net/amandaxy/article/details/7327981


### PyMySQL
pip install PyMySQL<br>
https://github.com/PyMySQL/PyMySQL