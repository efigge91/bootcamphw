

```python
from sqlalchemy import create_engine
import pandas as pd
from warnings import filterwarnings
import pymysql
filterwarnings('ignore', category=pymysql.Warning)
import os
```


```python
engine = create_engine('mysql+pymysql://root:kcmo1728@localhost/sakila') 
```


```python
# 1a. Display the first and last names of all actors from the table `actor`. 
sql_query = """
SELECT first_name,last_name 
FROM actor
"""
actor = pd.read_sql_query(sql_query, engine)
actor
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PENELOPE</td>
      <td>GUINESS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NICK</td>
      <td>WAHLBERG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ED</td>
      <td>CHASE</td>
    </tr>
    <tr>
      <th>3</th>
      <td>JENNIFER</td>
      <td>DAVIS</td>
    </tr>
    <tr>
      <th>4</th>
      <td>JOHNNY</td>
      <td>LOLLOBRIGIDA</td>
    </tr>
    <tr>
      <th>5</th>
      <td>BETTE</td>
      <td>NICHOLSON</td>
    </tr>
    <tr>
      <th>6</th>
      <td>GRACE</td>
      <td>MOSTEL</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MATTHEW</td>
      <td>JOHANSSON</td>
    </tr>
    <tr>
      <th>8</th>
      <td>JOE</td>
      <td>SWANK</td>
    </tr>
    <tr>
      <th>9</th>
      <td>CHRISTIAN</td>
      <td>GABLE</td>
    </tr>
    <tr>
      <th>10</th>
      <td>ZERO</td>
      <td>CAGE</td>
    </tr>
    <tr>
      <th>11</th>
      <td>KARL</td>
      <td>BERRY</td>
    </tr>
    <tr>
      <th>12</th>
      <td>UMA</td>
      <td>WOOD</td>
    </tr>
    <tr>
      <th>13</th>
      <td>VIVIEN</td>
      <td>BERGEN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>CUBA</td>
      <td>OLIVIER</td>
    </tr>
    <tr>
      <th>15</th>
      <td>FRED</td>
      <td>COSTNER</td>
    </tr>
    <tr>
      <th>16</th>
      <td>HELEN</td>
      <td>VOIGHT</td>
    </tr>
    <tr>
      <th>17</th>
      <td>DAN</td>
      <td>TORN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>BOB</td>
      <td>FAWCETT</td>
    </tr>
    <tr>
      <th>19</th>
      <td>LUCILLE</td>
      <td>TRACY</td>
    </tr>
    <tr>
      <th>20</th>
      <td>KIRSTEN</td>
      <td>PALTROW</td>
    </tr>
    <tr>
      <th>21</th>
      <td>ELVIS</td>
      <td>MARX</td>
    </tr>
    <tr>
      <th>22</th>
      <td>SANDRA</td>
      <td>KILMER</td>
    </tr>
    <tr>
      <th>23</th>
      <td>CAMERON</td>
      <td>STREEP</td>
    </tr>
    <tr>
      <th>24</th>
      <td>KEVIN</td>
      <td>BLOOM</td>
    </tr>
    <tr>
      <th>25</th>
      <td>RIP</td>
      <td>CRAWFORD</td>
    </tr>
    <tr>
      <th>26</th>
      <td>JULIA</td>
      <td>MCQUEEN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>WOODY</td>
      <td>HOFFMAN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>ALEC</td>
      <td>WAYNE</td>
    </tr>
    <tr>
      <th>29</th>
      <td>SANDRA</td>
      <td>PECK</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>170</th>
      <td>OLYMPIA</td>
      <td>PFEIFFER</td>
    </tr>
    <tr>
      <th>171</th>
      <td>MUCHO GROUCHO</td>
      <td>WILLIAMS</td>
    </tr>
    <tr>
      <th>172</th>
      <td>ALAN</td>
      <td>DREYFUSS</td>
    </tr>
    <tr>
      <th>173</th>
      <td>MICHAEL</td>
      <td>BENING</td>
    </tr>
    <tr>
      <th>174</th>
      <td>WILLIAM</td>
      <td>HACKMAN</td>
    </tr>
    <tr>
      <th>175</th>
      <td>JON</td>
      <td>CHASE</td>
    </tr>
    <tr>
      <th>176</th>
      <td>GENE</td>
      <td>MCKELLEN</td>
    </tr>
    <tr>
      <th>177</th>
      <td>LISA</td>
      <td>MONROE</td>
    </tr>
    <tr>
      <th>178</th>
      <td>ED</td>
      <td>GUINESS</td>
    </tr>
    <tr>
      <th>179</th>
      <td>JEFF</td>
      <td>SILVERSTONE</td>
    </tr>
    <tr>
      <th>180</th>
      <td>MATTHEW</td>
      <td>CARREY</td>
    </tr>
    <tr>
      <th>181</th>
      <td>DEBBIE</td>
      <td>AKROYD</td>
    </tr>
    <tr>
      <th>182</th>
      <td>RUSSELL</td>
      <td>CLOSE</td>
    </tr>
    <tr>
      <th>183</th>
      <td>HUMPHREY</td>
      <td>GARLAND</td>
    </tr>
    <tr>
      <th>184</th>
      <td>MICHAEL</td>
      <td>BOLGER</td>
    </tr>
    <tr>
      <th>185</th>
      <td>JULIA</td>
      <td>ZELLWEGER</td>
    </tr>
    <tr>
      <th>186</th>
      <td>RENEE</td>
      <td>BALL</td>
    </tr>
    <tr>
      <th>187</th>
      <td>ROCK</td>
      <td>DUKAKIS</td>
    </tr>
    <tr>
      <th>188</th>
      <td>CUBA</td>
      <td>BIRCH</td>
    </tr>
    <tr>
      <th>189</th>
      <td>AUDREY</td>
      <td>BAILEY</td>
    </tr>
    <tr>
      <th>190</th>
      <td>GREGORY</td>
      <td>GOODING</td>
    </tr>
    <tr>
      <th>191</th>
      <td>JOHN</td>
      <td>SUVARI</td>
    </tr>
    <tr>
      <th>192</th>
      <td>BURT</td>
      <td>TEMPLE</td>
    </tr>
    <tr>
      <th>193</th>
      <td>MERYL</td>
      <td>ALLEN</td>
    </tr>
    <tr>
      <th>194</th>
      <td>JAYNE</td>
      <td>SILVERSTONE</td>
    </tr>
    <tr>
      <th>195</th>
      <td>BELA</td>
      <td>WALKEN</td>
    </tr>
    <tr>
      <th>196</th>
      <td>REESE</td>
      <td>WEST</td>
    </tr>
    <tr>
      <th>197</th>
      <td>MARY</td>
      <td>KEITEL</td>
    </tr>
    <tr>
      <th>198</th>
      <td>JULIA</td>
      <td>FAWCETT</td>
    </tr>
    <tr>
      <th>199</th>
      <td>THORA</td>
      <td>TEMPLE</td>
    </tr>
  </tbody>
</table>
<p>200 rows × 2 columns</p>
</div>




```python
# 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. 

sql_query = """
SELECT CONCAT(first_name, ' ' ,last_name) AS 'Actor Name'
FROM actor
"""
ActorName = pd.read_sql_query(sql_query, engine)
ActorName
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Actor Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PENELOPE GUINESS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NICK WAHLBERG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ED CHASE</td>
    </tr>
    <tr>
      <th>3</th>
      <td>JENNIFER DAVIS</td>
    </tr>
    <tr>
      <th>4</th>
      <td>JOHNNY LOLLOBRIGIDA</td>
    </tr>
    <tr>
      <th>5</th>
      <td>BETTE NICHOLSON</td>
    </tr>
    <tr>
      <th>6</th>
      <td>GRACE MOSTEL</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MATTHEW JOHANSSON</td>
    </tr>
    <tr>
      <th>8</th>
      <td>JOE SWANK</td>
    </tr>
    <tr>
      <th>9</th>
      <td>CHRISTIAN GABLE</td>
    </tr>
    <tr>
      <th>10</th>
      <td>ZERO CAGE</td>
    </tr>
    <tr>
      <th>11</th>
      <td>KARL BERRY</td>
    </tr>
    <tr>
      <th>12</th>
      <td>UMA WOOD</td>
    </tr>
    <tr>
      <th>13</th>
      <td>VIVIEN BERGEN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>CUBA OLIVIER</td>
    </tr>
    <tr>
      <th>15</th>
      <td>FRED COSTNER</td>
    </tr>
    <tr>
      <th>16</th>
      <td>HELEN VOIGHT</td>
    </tr>
    <tr>
      <th>17</th>
      <td>DAN TORN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>BOB FAWCETT</td>
    </tr>
    <tr>
      <th>19</th>
      <td>LUCILLE TRACY</td>
    </tr>
    <tr>
      <th>20</th>
      <td>KIRSTEN PALTROW</td>
    </tr>
    <tr>
      <th>21</th>
      <td>ELVIS MARX</td>
    </tr>
    <tr>
      <th>22</th>
      <td>SANDRA KILMER</td>
    </tr>
    <tr>
      <th>23</th>
      <td>CAMERON STREEP</td>
    </tr>
    <tr>
      <th>24</th>
      <td>KEVIN BLOOM</td>
    </tr>
    <tr>
      <th>25</th>
      <td>RIP CRAWFORD</td>
    </tr>
    <tr>
      <th>26</th>
      <td>JULIA MCQUEEN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>WOODY HOFFMAN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>ALEC WAYNE</td>
    </tr>
    <tr>
      <th>29</th>
      <td>SANDRA PECK</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>170</th>
      <td>OLYMPIA PFEIFFER</td>
    </tr>
    <tr>
      <th>171</th>
      <td>MUCHO GROUCHO WILLIAMS</td>
    </tr>
    <tr>
      <th>172</th>
      <td>ALAN DREYFUSS</td>
    </tr>
    <tr>
      <th>173</th>
      <td>MICHAEL BENING</td>
    </tr>
    <tr>
      <th>174</th>
      <td>WILLIAM HACKMAN</td>
    </tr>
    <tr>
      <th>175</th>
      <td>JON CHASE</td>
    </tr>
    <tr>
      <th>176</th>
      <td>GENE MCKELLEN</td>
    </tr>
    <tr>
      <th>177</th>
      <td>LISA MONROE</td>
    </tr>
    <tr>
      <th>178</th>
      <td>ED GUINESS</td>
    </tr>
    <tr>
      <th>179</th>
      <td>JEFF SILVERSTONE</td>
    </tr>
    <tr>
      <th>180</th>
      <td>MATTHEW CARREY</td>
    </tr>
    <tr>
      <th>181</th>
      <td>DEBBIE AKROYD</td>
    </tr>
    <tr>
      <th>182</th>
      <td>RUSSELL CLOSE</td>
    </tr>
    <tr>
      <th>183</th>
      <td>HUMPHREY GARLAND</td>
    </tr>
    <tr>
      <th>184</th>
      <td>MICHAEL BOLGER</td>
    </tr>
    <tr>
      <th>185</th>
      <td>JULIA ZELLWEGER</td>
    </tr>
    <tr>
      <th>186</th>
      <td>RENEE BALL</td>
    </tr>
    <tr>
      <th>187</th>
      <td>ROCK DUKAKIS</td>
    </tr>
    <tr>
      <th>188</th>
      <td>CUBA BIRCH</td>
    </tr>
    <tr>
      <th>189</th>
      <td>AUDREY BAILEY</td>
    </tr>
    <tr>
      <th>190</th>
      <td>GREGORY GOODING</td>
    </tr>
    <tr>
      <th>191</th>
      <td>JOHN SUVARI</td>
    </tr>
    <tr>
      <th>192</th>
      <td>BURT TEMPLE</td>
    </tr>
    <tr>
      <th>193</th>
      <td>MERYL ALLEN</td>
    </tr>
    <tr>
      <th>194</th>
      <td>JAYNE SILVERSTONE</td>
    </tr>
    <tr>
      <th>195</th>
      <td>BELA WALKEN</td>
    </tr>
    <tr>
      <th>196</th>
      <td>REESE WEST</td>
    </tr>
    <tr>
      <th>197</th>
      <td>MARY KEITEL</td>
    </tr>
    <tr>
      <th>198</th>
      <td>JULIA FAWCETT</td>
    </tr>
    <tr>
      <th>199</th>
      <td>THORA TEMPLE</td>
    </tr>
  </tbody>
</table>
<p>200 rows × 1 columns</p>
</div>




```python
#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
sql_query = """
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe'
"""
joe = pd.read_sql_query(sql_query, engine)
joe
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>JOE</td>
      <td>SWANK</td>
    </tr>
  </tbody>
</table>
</div>




```python
#2b. Find all actors whose last name contain the letters `GEN`:
sql_query = """
SELECT *
FROM actor
WHERE last_name LIKE '%%gen%%'
"""
gen = pd.read_sql_query(sql_query, engine)
gen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>last_update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14</td>
      <td>VIVIEN</td>
      <td>BERGEN</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41</td>
      <td>JODIE</td>
      <td>DEGENERES</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>2</th>
      <td>107</td>
      <td>GINA</td>
      <td>DEGENERES</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>3</th>
      <td>166</td>
      <td>NICK</td>
      <td>DEGENERES</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
  </tbody>
</table>
</div>




```python
#2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
sql_query = """
SELECT *
FROM actor
WHERE last_name LIKE '%%li%%'
ORDER BY last_name, first_name
"""
li = pd.read_sql_query(sql_query, engine)
li
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>last_update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>86</td>
      <td>GREG</td>
      <td>CHAPLIN</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>82</td>
      <td>WOODY</td>
      <td>JOLIE</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>AUDREY</td>
      <td>OLIVIER</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>CUBA</td>
      <td>OLIVIER</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>137</td>
      <td>MORGAN</td>
      <td>WILLIAMS</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>5</th>
      <td>172</td>
      <td>MUCHO GROUCHO</td>
      <td>WILLIAMS</td>
      <td>2018-02-21 19:39:12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>72</td>
      <td>SEAN</td>
      <td>WILLIAMS</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>7</th>
      <td>83</td>
      <td>BEN</td>
      <td>WILLIS</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>8</th>
      <td>96</td>
      <td>GENE</td>
      <td>WILLIS</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
    <tr>
      <th>9</th>
      <td>164</td>
      <td>HUMPHREY</td>
      <td>WILLIS</td>
      <td>2018-02-21 18:18:09</td>
    </tr>
  </tbody>
</table>
</div>




```python
#2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
sql_query = """
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', and 'China');
"""
df = pd.read_sql_query(sql_query, engine)
df
```


    ---------------------------------------------------------------------------

    ProgrammingError                          Traceback (most recent call last)

    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
       1181                         parameters,
    -> 1182                         context)
       1183         except BaseException as e:


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/default.py in do_execute(self, cursor, statement, parameters, context)
        469     def do_execute(self, cursor, statement, parameters, context=None):
    --> 470         cursor.execute(statement, parameters)
        471 


    /anaconda3/lib/python3.6/site-packages/pymysql/cursors.py in execute(self, query, args)
        164 
    --> 165         result = self._query(query)
        166         self._executed = query


    /anaconda3/lib/python3.6/site-packages/pymysql/cursors.py in _query(self, q)
        320         self._last_executed = q
    --> 321         conn.query(q)
        322         self._do_get_result()


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in query(self, sql, unbuffered)
        859         self._execute_command(COMMAND.COM_QUERY, sql)
    --> 860         self._affected_rows = self._read_query_result(unbuffered=unbuffered)
        861         return self._affected_rows


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in _read_query_result(self, unbuffered)
       1060             result = MySQLResult(self)
    -> 1061             result.read()
       1062         self._result = result


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in read(self)
       1348         try:
    -> 1349             first_packet = self.connection._read_packet()
       1350 


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in _read_packet(self, packet_type)
       1017         packet = packet_type(buff, self.encoding)
    -> 1018         packet.check_error()
       1019         return packet


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in check_error(self)
        383             if DEBUG: print("errno =", errno)
    --> 384             err.raise_mysql_exception(self._data)
        385 


    /anaconda3/lib/python3.6/site-packages/pymysql/err.py in raise_mysql_exception(data)
        106     errorclass = error_map.get(errno, InternalError)
    --> 107     raise errorclass(errno, errval)
    

    ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '{'Afghanistan', 'Bangladesh', and 'China'}' at line 3")

    
    The above exception was the direct cause of the following exception:


    ProgrammingError                          Traceback (most recent call last)

    <ipython-input-12-892e3771dcdb> in <module>()
          5 WHERE country IN {'Afghanistan', 'Bangladesh', and 'China'};
          6 """
    ----> 7 df = pd.read_sql_query(sql_query, engine)
          8 df


    /anaconda3/lib/python3.6/site-packages/pandas/io/sql.py in read_sql_query(sql, con, index_col, coerce_float, params, parse_dates, chunksize)
        330     return pandas_sql.read_query(
        331         sql, index_col=index_col, params=params, coerce_float=coerce_float,
    --> 332         parse_dates=parse_dates, chunksize=chunksize)
        333 
        334 


    /anaconda3/lib/python3.6/site-packages/pandas/io/sql.py in read_query(self, sql, index_col, coerce_float, parse_dates, params, chunksize)
       1085         args = _convert_params(sql, params)
       1086 
    -> 1087         result = self.execute(*args)
       1088         columns = result.keys()
       1089 


    /anaconda3/lib/python3.6/site-packages/pandas/io/sql.py in execute(self, *args, **kwargs)
        976     def execute(self, *args, **kwargs):
        977         """Simple passthrough to SQLAlchemy connectable"""
    --> 978         return self.connectable.execute(*args, **kwargs)
        979 
        980     def read_table(self, table_name, index_col=None, coerce_float=True,


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/base.py in execute(self, statement, *multiparams, **params)
       2062 
       2063         connection = self.contextual_connect(close_with_result=True)
    -> 2064         return connection.execute(statement, *multiparams, **params)
       2065 
       2066     def scalar(self, statement, *multiparams, **params):


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/base.py in execute(self, object, *multiparams, **params)
        937         """
        938         if isinstance(object, util.string_types[0]):
    --> 939             return self._execute_text(object, multiparams, params)
        940         try:
        941             meth = object._execute_on_connection


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_text(self, statement, multiparams, params)
       1095             statement,
       1096             parameters,
    -> 1097             statement, parameters
       1098         )
       1099         if self._has_events or self.engine._has_events:


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
       1187                 parameters,
       1188                 cursor,
    -> 1189                 context)
       1190 
       1191         if self._has_events or self.engine._has_events:


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _handle_dbapi_exception(self, e, statement, parameters, cursor, context)
       1400                 util.raise_from_cause(
       1401                     sqlalchemy_exception,
    -> 1402                     exc_info
       1403                 )
       1404             else:


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/util/compat.py in raise_from_cause(exception, exc_info)
        201     exc_type, exc_value, exc_tb = exc_info
        202     cause = exc_value if exc_value is not exception else None
    --> 203     reraise(type(exception), exception, tb=exc_tb, cause=cause)
        204 
        205 if py3k:


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/util/compat.py in reraise(tp, value, tb, cause)
        184             value.__cause__ = cause
        185         if value.__traceback__ is not tb:
    --> 186             raise value.with_traceback(tb)
        187         raise value
        188 


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
       1180                         statement,
       1181                         parameters,
    -> 1182                         context)
       1183         except BaseException as e:
       1184             self._handle_dbapi_exception(


    /anaconda3/lib/python3.6/site-packages/sqlalchemy/engine/default.py in do_execute(self, cursor, statement, parameters, context)
        468 
        469     def do_execute(self, cursor, statement, parameters, context=None):
    --> 470         cursor.execute(statement, parameters)
        471 
        472     def do_execute_no_params(self, cursor, statement, context=None):


    /anaconda3/lib/python3.6/site-packages/pymysql/cursors.py in execute(self, query, args)
        163         query = self.mogrify(query, args)
        164 
    --> 165         result = self._query(query)
        166         self._executed = query
        167         return result


    /anaconda3/lib/python3.6/site-packages/pymysql/cursors.py in _query(self, q)
        319         conn = self._get_db()
        320         self._last_executed = q
    --> 321         conn.query(q)
        322         self._do_get_result()
        323         return self.rowcount


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in query(self, sql, unbuffered)
        858                 sql = sql.encode(self.encoding, 'surrogateescape')
        859         self._execute_command(COMMAND.COM_QUERY, sql)
    --> 860         self._affected_rows = self._read_query_result(unbuffered=unbuffered)
        861         return self._affected_rows
        862 


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in _read_query_result(self, unbuffered)
       1059         else:
       1060             result = MySQLResult(self)
    -> 1061             result.read()
       1062         self._result = result
       1063         if result.server_status is not None:


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in read(self)
       1347     def read(self):
       1348         try:
    -> 1349             first_packet = self.connection._read_packet()
       1350 
       1351             if first_packet.is_ok_packet():


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in _read_packet(self, packet_type)
       1016 
       1017         packet = packet_type(buff, self.encoding)
    -> 1018         packet.check_error()
       1019         return packet
       1020 


    /anaconda3/lib/python3.6/site-packages/pymysql/connections.py in check_error(self)
        382             errno = self.read_uint16()
        383             if DEBUG: print("errno =", errno)
    --> 384             err.raise_mysql_exception(self._data)
        385 
        386     def dump(self):


    /anaconda3/lib/python3.6/site-packages/pymysql/err.py in raise_mysql_exception(data)
        105         errval = data[3:].decode('utf-8', 'replace')
        106     errorclass = error_map.get(errno, InternalError)
    --> 107     raise errorclass(errno, errval)
    

    ProgrammingError: (pymysql.err.ProgrammingError) (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '{'Afghanistan', 'Bangladesh', and 'China'}' at line 3") [SQL: "\nSELECT country_id, country\nFROM country\nWHERE country IN {'Afghanistan', 'Bangladesh', and 'China'};\n"]



```python
#3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.
sql_query = """
ALTER TABLE actor
ADD middle_name VARCHAR(20)
AFTER first_name;
"""
engine.execute(sql_query)
```




    <sqlalchemy.engine.result.ResultProxy at 0x10c69dcc0>




```python
#3b. You realize that some of these actors have tremendously long last names. Change the data type of the `middle_name` column to `blobs`.
sql_query = """
ALTER TABLE actor
MODIFY COLUMN middle_name blob;
"""
engine.execute(sql_query)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1092c7fd0>




```python
#3c. Now delete the `middle_name` column.
sql_query = """
ALTER TABLE actor
Drop COLUMN middle_name;
"""
engine.execute(sql_query)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1092c79b0>




```python
#4a. List the last names of actors, as well as how many actors have that last name.
sql_query = """
select distinct last_name, count(*) as number
from actor
group by last_name
order by number desc
"""
last_names = pd.read_sql_query(sql_query, engine)
last_names
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>last_name</th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KILMER</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NOLTE</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TEMPLE</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PECK</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TORN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>AKROYD</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>HOFFMAN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>GUINESS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>WILLIAMS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>BERRY</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>GARLAND</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>HOPKINS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>ZELLWEGER</td>
      <td>3</td>
    </tr>
    <tr>
      <th>13</th>
      <td>HARRIS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>14</th>
      <td>DAVIS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>ALLEN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>KEITEL</td>
      <td>3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>WILLIS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18</th>
      <td>DEGENERES</td>
      <td>3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>JOHANSSON</td>
      <td>3</td>
    </tr>
    <tr>
      <th>20</th>
      <td>WINSLET</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>BOLGER</td>
      <td>2</td>
    </tr>
    <tr>
      <th>22</th>
      <td>GOODING</td>
      <td>2</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NEESON</td>
      <td>2</td>
    </tr>
    <tr>
      <th>24</th>
      <td>FAWCETT</td>
      <td>2</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MCKELLEN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>26</th>
      <td>DEPP</td>
      <td>2</td>
    </tr>
    <tr>
      <th>27</th>
      <td>CHASE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>28</th>
      <td>WOOD</td>
      <td>2</td>
    </tr>
    <tr>
      <th>29</th>
      <td>BRODY</td>
      <td>2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>91</th>
      <td>HUDSON</td>
      <td>1</td>
    </tr>
    <tr>
      <th>92</th>
      <td>PITT</td>
      <td>1</td>
    </tr>
    <tr>
      <th>93</th>
      <td>CHAPLIN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>94</th>
      <td>HESTON</td>
      <td>1</td>
    </tr>
    <tr>
      <th>95</th>
      <td>WITHERSPOON</td>
      <td>1</td>
    </tr>
    <tr>
      <th>96</th>
      <td>BRIDGES</td>
      <td>1</td>
    </tr>
    <tr>
      <th>97</th>
      <td>GRANT</td>
      <td>1</td>
    </tr>
    <tr>
      <th>98</th>
      <td>NICHOLSON</td>
      <td>1</td>
    </tr>
    <tr>
      <th>99</th>
      <td>BERGMAN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>100</th>
      <td>GABLE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>101</th>
      <td>BALL</td>
      <td>1</td>
    </tr>
    <tr>
      <th>102</th>
      <td>DERN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>103</th>
      <td>MANSFIELD</td>
      <td>1</td>
    </tr>
    <tr>
      <th>104</th>
      <td>SOBIESKI</td>
      <td>1</td>
    </tr>
    <tr>
      <th>105</th>
      <td>CRUISE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>106</th>
      <td>HURT</td>
      <td>1</td>
    </tr>
    <tr>
      <th>107</th>
      <td>PRESLEY</td>
      <td>1</td>
    </tr>
    <tr>
      <th>108</th>
      <td>CLOSE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>109</th>
      <td>HOPE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>110</th>
      <td>PFEIFFER</td>
      <td>1</td>
    </tr>
    <tr>
      <th>111</th>
      <td>WRAY</td>
      <td>1</td>
    </tr>
    <tr>
      <th>112</th>
      <td>BULLOCK</td>
      <td>1</td>
    </tr>
    <tr>
      <th>113</th>
      <td>BIRCH</td>
      <td>1</td>
    </tr>
    <tr>
      <th>114</th>
      <td>GIBSON</td>
      <td>1</td>
    </tr>
    <tr>
      <th>115</th>
      <td>BASINGER</td>
      <td>1</td>
    </tr>
    <tr>
      <th>116</th>
      <td>BACALL</td>
      <td>1</td>
    </tr>
    <tr>
      <th>117</th>
      <td>LEIGH</td>
      <td>1</td>
    </tr>
    <tr>
      <th>118</th>
      <td>DAMON</td>
      <td>1</td>
    </tr>
    <tr>
      <th>119</th>
      <td>RYDER</td>
      <td>1</td>
    </tr>
    <tr>
      <th>120</th>
      <td>PINKETT</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>121 rows × 2 columns</p>
</div>




```python
#4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
sql_query = """
select distinct last_name, count(*) as number
from actor
group by last_name
having number >= 2
order by number desc
"""
last_names = pd.read_sql_query(sql_query, engine)
last_names
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>last_name</th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KILMER</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NOLTE</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TEMPLE</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PECK</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TORN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>AKROYD</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>HOFFMAN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>GUINESS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>WILLIAMS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>BERRY</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>GARLAND</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>HOPKINS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>ZELLWEGER</td>
      <td>3</td>
    </tr>
    <tr>
      <th>13</th>
      <td>HARRIS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>14</th>
      <td>DAVIS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>ALLEN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>KEITEL</td>
      <td>3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>WILLIS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18</th>
      <td>DEGENERES</td>
      <td>3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>JOHANSSON</td>
      <td>3</td>
    </tr>
    <tr>
      <th>20</th>
      <td>WINSLET</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>BOLGER</td>
      <td>2</td>
    </tr>
    <tr>
      <th>22</th>
      <td>GOODING</td>
      <td>2</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NEESON</td>
      <td>2</td>
    </tr>
    <tr>
      <th>24</th>
      <td>FAWCETT</td>
      <td>2</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MCKELLEN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>26</th>
      <td>DEPP</td>
      <td>2</td>
    </tr>
    <tr>
      <th>27</th>
      <td>CHASE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>28</th>
      <td>WOOD</td>
      <td>2</td>
    </tr>
    <tr>
      <th>29</th>
      <td>BRODY</td>
      <td>2</td>
    </tr>
    <tr>
      <th>30</th>
      <td>DEE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>31</th>
      <td>JACKMAN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>32</th>
      <td>CAGE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>33</th>
      <td>PALTROW</td>
      <td>2</td>
    </tr>
    <tr>
      <th>34</th>
      <td>MOSTEL</td>
      <td>2</td>
    </tr>
    <tr>
      <th>35</th>
      <td>BENING</td>
      <td>2</td>
    </tr>
    <tr>
      <th>36</th>
      <td>BAILEY</td>
      <td>2</td>
    </tr>
    <tr>
      <th>37</th>
      <td>DENCH</td>
      <td>2</td>
    </tr>
    <tr>
      <th>38</th>
      <td>SILVERSTONE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>39</th>
      <td>CRONYN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>40</th>
      <td>PENN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>41</th>
      <td>WEST</td>
      <td>2</td>
    </tr>
    <tr>
      <th>42</th>
      <td>MCQUEEN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>43</th>
      <td>TRACY</td>
      <td>2</td>
    </tr>
    <tr>
      <th>44</th>
      <td>TANDY</td>
      <td>2</td>
    </tr>
    <tr>
      <th>45</th>
      <td>DEAN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>46</th>
      <td>HACKMAN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>47</th>
      <td>OLIVIER</td>
      <td>2</td>
    </tr>
    <tr>
      <th>48</th>
      <td>MONROE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>49</th>
      <td>WAHLBERG</td>
      <td>2</td>
    </tr>
    <tr>
      <th>50</th>
      <td>DUKAKIS</td>
      <td>2</td>
    </tr>
    <tr>
      <th>51</th>
      <td>MCCONAUGHEY</td>
      <td>2</td>
    </tr>
    <tr>
      <th>52</th>
      <td>STREEP</td>
      <td>2</td>
    </tr>
    <tr>
      <th>53</th>
      <td>CRAWFORD</td>
      <td>2</td>
    </tr>
    <tr>
      <th>54</th>
      <td>HOPPER</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
#4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
sql_query = """
UPDATE actor
SET first_name = 'HARPO'
where first_name = 'groucho'
and last_name = 'williams'
"""
engine.execute(sql_query)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1092299b0>




```python
#4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, HOWEVER! (Hint: update the record using a unique identifier.)
sql_query = """
UPDATE actor
SET first_name = 
CASE 
WHEN first_name = 'HARPO' 
THEN 'GROUCHO'
ELSE 'MUCHO GROUCHO'
END 
WHERE actor_id = 172;
"""
engine.execute(sql_query)
```




    <sqlalchemy.engine.result.ResultProxy at 0x10c6a90f0>




```python
sql_query = """
select * 
from actor
where actor_id =172
"""
groucho = pd.read_sql_query(sql_query, engine)
groucho
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>last_update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>172</td>
      <td>MUCHO GROUCHO</td>
      <td>WILLIAMS</td>
      <td>2018-02-21 19:39:12</td>
    </tr>
  </tbody>
</table>
</div>




```python
#5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it? 
sql_query = """
describe sakila.address
"""
pd.read_sql_query(sql_query, engine)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Type</th>
      <th>Null</th>
      <th>Key</th>
      <th>Default</th>
      <th>Extra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>address_id</td>
      <td>smallint(5) unsigned</td>
      <td>NO</td>
      <td>PRI</td>
      <td>None</td>
      <td>auto_increment</td>
    </tr>
    <tr>
      <th>1</th>
      <td>address</td>
      <td>varchar(50)</td>
      <td>NO</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>address2</td>
      <td>varchar(50)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>district</td>
      <td>varchar(20)</td>
      <td>NO</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>city_id</td>
      <td>smallint(5) unsigned</td>
      <td>NO</td>
      <td>MUL</td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>postal_code</td>
      <td>varchar(10)</td>
      <td>YES</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>phone</td>
      <td>varchar(20)</td>
      <td>NO</td>
      <td></td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <td>location</td>
      <td>geometry</td>
      <td>NO</td>
      <td>MUL</td>
      <td>None</td>
      <td></td>
    </tr>
    <tr>
      <th>8</th>
      <td>last_update</td>
      <td>timestamp</td>
      <td>NO</td>
      <td></td>
      <td>CURRENT_TIMESTAMP</td>
      <td>on update CURRENT_TIMESTAMP</td>
    </tr>
  </tbody>
</table>
</div>




```python
#6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
sql_query = """
select staff.first_name,staff.last_name, address.address
from staff
inner join address
on staff.address_id = address.address_id;
"""
staffaddress = pd.read_sql_query(sql_query, engine)
staffaddress
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Hillyer</td>
      <td>23 Workhaven Lane</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jon</td>
      <td>Stephens</td>
      <td>1411 Lillydale Drive</td>
    </tr>
  </tbody>
</table>
</div>




```python
#6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`. 
sql_query = """
select staff.first_name, staff.last_name, sum(amount) as 'Total Amount Paid'
from payment
inner join staff
on staff.staff_id = payment.staff_id
group by staff.staff_id;
"""
staffpayment = pd.read_sql_query(sql_query, engine)
staffpayment
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>Total Amount Paid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Hillyer</td>
      <td>33489.47</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jon</td>
      <td>Stephens</td>
      <td>33927.04</td>
    </tr>
  </tbody>
</table>
</div>




```python
#6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
sql_query = """
select film.title, count(film_actor.actor_id) as 'Number of Actors'
from film_actor
inner join film
on film.film_id = film_actor.film_id
group by film.title
"""
actorsinfilm = pd.read_sql_query(sql_query, engine)
actorsinfilm.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>Number of Actors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ACADEMY DINOSAUR</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ACE GOLDFINGER</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ADAPTATION HOLES</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AFFAIR PREJUDICE</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AFRICAN EGG</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
#6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`. 
sql_query = """
select film.title, count(*) as 'Inventory'
from inventory
inner join film
on film.film_id = inventory.film_id
group by inventory.film_id
"""
filmcopies = pd.read_sql_query(sql_query, engine)
filmcopies
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>Inventory</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ACADEMY DINOSAUR</td>
      <td>8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ACE GOLDFINGER</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ADAPTATION HOLES</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AFFAIR PREJUDICE</td>
      <td>7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AFRICAN EGG</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>AGENT TRUMAN</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>AIRPLANE SIERRA</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>AIRPORT POLLOCK</td>
      <td>4</td>
    </tr>
    <tr>
      <th>8</th>
      <td>ALABAMA DEVIL</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ALADDIN CALENDAR</td>
      <td>7</td>
    </tr>
    <tr>
      <th>10</th>
      <td>ALAMO VIDEOTAPE</td>
      <td>7</td>
    </tr>
    <tr>
      <th>11</th>
      <td>ALASKA PHANTOM</td>
      <td>7</td>
    </tr>
    <tr>
      <th>12</th>
      <td>ALI FOREVER</td>
      <td>4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>ALIEN CENTER</td>
      <td>6</td>
    </tr>
    <tr>
      <th>14</th>
      <td>ALLEY EVOLUTION</td>
      <td>4</td>
    </tr>
    <tr>
      <th>15</th>
      <td>ALONE TRIP</td>
      <td>6</td>
    </tr>
    <tr>
      <th>16</th>
      <td>ALTER VICTORY</td>
      <td>6</td>
    </tr>
    <tr>
      <th>17</th>
      <td>AMADEUS HOLY</td>
      <td>6</td>
    </tr>
    <tr>
      <th>18</th>
      <td>AMELIE HELLFIGHTERS</td>
      <td>3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>AMERICAN CIRCUS</td>
      <td>6</td>
    </tr>
    <tr>
      <th>20</th>
      <td>AMISTAD MIDSUMMER</td>
      <td>7</td>
    </tr>
    <tr>
      <th>21</th>
      <td>ANACONDA CONFESSIONS</td>
      <td>5</td>
    </tr>
    <tr>
      <th>22</th>
      <td>ANALYZE HOOSIERS</td>
      <td>4</td>
    </tr>
    <tr>
      <th>23</th>
      <td>ANGELS LIFE</td>
      <td>6</td>
    </tr>
    <tr>
      <th>24</th>
      <td>ANNIE IDENTITY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>25</th>
      <td>ANONYMOUS HUMAN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>26</th>
      <td>ANTHEM LUKE</td>
      <td>3</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ANTITRUST TOMATOES</td>
      <td>2</td>
    </tr>
    <tr>
      <th>28</th>
      <td>ANYTHING SAVANNAH</td>
      <td>2</td>
    </tr>
    <tr>
      <th>29</th>
      <td>APACHE DIVINE</td>
      <td>8</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>928</th>
      <td>WHALE BIKINI</td>
      <td>4</td>
    </tr>
    <tr>
      <th>929</th>
      <td>WHISPERER GIANT</td>
      <td>6</td>
    </tr>
    <tr>
      <th>930</th>
      <td>WIFE TURN</td>
      <td>8</td>
    </tr>
    <tr>
      <th>931</th>
      <td>WILD APOLLO</td>
      <td>2</td>
    </tr>
    <tr>
      <th>932</th>
      <td>WILLOW TRACY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>933</th>
      <td>WIND PHANTOM</td>
      <td>6</td>
    </tr>
    <tr>
      <th>934</th>
      <td>WINDOW SIDE</td>
      <td>3</td>
    </tr>
    <tr>
      <th>935</th>
      <td>WISDOM WORKER</td>
      <td>3</td>
    </tr>
    <tr>
      <th>936</th>
      <td>WITCHES PANIC</td>
      <td>7</td>
    </tr>
    <tr>
      <th>937</th>
      <td>WIZARD COLDBLOODED</td>
      <td>5</td>
    </tr>
    <tr>
      <th>938</th>
      <td>WOLVES DESIRE</td>
      <td>6</td>
    </tr>
    <tr>
      <th>939</th>
      <td>WOMEN DORADO</td>
      <td>7</td>
    </tr>
    <tr>
      <th>940</th>
      <td>WON DARES</td>
      <td>3</td>
    </tr>
    <tr>
      <th>941</th>
      <td>WONDERFUL DROP</td>
      <td>2</td>
    </tr>
    <tr>
      <th>942</th>
      <td>WONDERLAND CHRISTMAS</td>
      <td>7</td>
    </tr>
    <tr>
      <th>943</th>
      <td>WONKA SEA</td>
      <td>6</td>
    </tr>
    <tr>
      <th>944</th>
      <td>WORDS HUNTER</td>
      <td>4</td>
    </tr>
    <tr>
      <th>945</th>
      <td>WORKER TARZAN</td>
      <td>5</td>
    </tr>
    <tr>
      <th>946</th>
      <td>WORKING MICROCOSMOS</td>
      <td>6</td>
    </tr>
    <tr>
      <th>947</th>
      <td>WORLD LEATHERNECKS</td>
      <td>2</td>
    </tr>
    <tr>
      <th>948</th>
      <td>WORST BANGER</td>
      <td>5</td>
    </tr>
    <tr>
      <th>949</th>
      <td>WRATH MILE</td>
      <td>4</td>
    </tr>
    <tr>
      <th>950</th>
      <td>WRONG BEHAVIOR</td>
      <td>7</td>
    </tr>
    <tr>
      <th>951</th>
      <td>WYOMING STORM</td>
      <td>3</td>
    </tr>
    <tr>
      <th>952</th>
      <td>YENTL IDAHO</td>
      <td>6</td>
    </tr>
    <tr>
      <th>953</th>
      <td>YOUNG LANGUAGE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>954</th>
      <td>YOUTH KICK</td>
      <td>2</td>
    </tr>
    <tr>
      <th>955</th>
      <td>ZHIVAGO CORE</td>
      <td>2</td>
    </tr>
    <tr>
      <th>956</th>
      <td>ZOOLANDER FICTION</td>
      <td>5</td>
    </tr>
    <tr>
      <th>957</th>
      <td>ZORRO ARK</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
<p>958 rows × 2 columns</p>
</div>




```python
#6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
sql_query = """
select f.title, count(*) as 'Number of Copies'
from film f
inner join inventory i 
on f.film_id = i.film_id
where title = 'Hunchback Impossible'
"""
number = pd.read_sql_query(sql_query,engine)
number
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>Number of Copies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HUNCHBACK IMPOSSIBLE</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
#6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:
sql_query = """
select c.first_name, c.last_name, sum(amount) as 'Total Amount Paid'
from payment p
inner join customer c
on c.customer_id = p.customer_id
group by c.customer_id
order by c.last_name;
"""
customers = pd.read_sql_query(sql_query,engine)
customers
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>Total Amount Paid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RAFAEL</td>
      <td>ABNEY</td>
      <td>97.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NATHANIEL</td>
      <td>ADAM</td>
      <td>133.72</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KATHLEEN</td>
      <td>ADAMS</td>
      <td>92.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>DIANA</td>
      <td>ALEXANDER</td>
      <td>105.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GORDON</td>
      <td>ALLARD</td>
      <td>160.68</td>
    </tr>
    <tr>
      <th>5</th>
      <td>SHIRLEY</td>
      <td>ALLEN</td>
      <td>126.69</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CHARLENE</td>
      <td>ALVAREZ</td>
      <td>114.73</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LISA</td>
      <td>ANDERSON</td>
      <td>106.76</td>
    </tr>
    <tr>
      <th>8</th>
      <td>JOSE</td>
      <td>ANDREW</td>
      <td>96.75</td>
    </tr>
    <tr>
      <th>9</th>
      <td>IDA</td>
      <td>ANDREWS</td>
      <td>76.77</td>
    </tr>
    <tr>
      <th>10</th>
      <td>OSCAR</td>
      <td>AQUINO</td>
      <td>99.80</td>
    </tr>
    <tr>
      <th>11</th>
      <td>HARRY</td>
      <td>ARCE</td>
      <td>157.65</td>
    </tr>
    <tr>
      <th>12</th>
      <td>JORDAN</td>
      <td>ARCHULETA</td>
      <td>132.70</td>
    </tr>
    <tr>
      <th>13</th>
      <td>MELANIE</td>
      <td>ARMSTRONG</td>
      <td>92.75</td>
    </tr>
    <tr>
      <th>14</th>
      <td>BEATRICE</td>
      <td>ARNOLD</td>
      <td>119.74</td>
    </tr>
    <tr>
      <th>15</th>
      <td>KENT</td>
      <td>ARSENAULT</td>
      <td>134.73</td>
    </tr>
    <tr>
      <th>16</th>
      <td>CARL</td>
      <td>ARTIS</td>
      <td>106.77</td>
    </tr>
    <tr>
      <th>17</th>
      <td>DARRYL</td>
      <td>ASHCRAFT</td>
      <td>76.77</td>
    </tr>
    <tr>
      <th>18</th>
      <td>TYRONE</td>
      <td>ASHER</td>
      <td>112.76</td>
    </tr>
    <tr>
      <th>19</th>
      <td>ALMA</td>
      <td>AUSTIN</td>
      <td>151.65</td>
    </tr>
    <tr>
      <th>20</th>
      <td>MILDRED</td>
      <td>BAILEY</td>
      <td>98.75</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PAMELA</td>
      <td>BAKER</td>
      <td>95.77</td>
    </tr>
    <tr>
      <th>22</th>
      <td>MARTIN</td>
      <td>BALES</td>
      <td>103.73</td>
    </tr>
    <tr>
      <th>23</th>
      <td>EVERETT</td>
      <td>BANDA</td>
      <td>110.72</td>
    </tr>
    <tr>
      <th>24</th>
      <td>JESSIE</td>
      <td>BANKS</td>
      <td>91.74</td>
    </tr>
    <tr>
      <th>25</th>
      <td>CLAYTON</td>
      <td>BARBEE</td>
      <td>96.74</td>
    </tr>
    <tr>
      <th>26</th>
      <td>ANGEL</td>
      <td>BARCLAY</td>
      <td>115.68</td>
    </tr>
    <tr>
      <th>27</th>
      <td>NICHOLAS</td>
      <td>BARFIELD</td>
      <td>145.68</td>
    </tr>
    <tr>
      <th>28</th>
      <td>VICTOR</td>
      <td>BARKLEY</td>
      <td>91.76</td>
    </tr>
    <tr>
      <th>29</th>
      <td>RACHEL</td>
      <td>BARNES</td>
      <td>84.78</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>569</th>
      <td>THERESA</td>
      <td>WATSON</td>
      <td>99.70</td>
    </tr>
    <tr>
      <th>570</th>
      <td>SHELLY</td>
      <td>WATTS</td>
      <td>113.74</td>
    </tr>
    <tr>
      <th>571</th>
      <td>JAMIE</td>
      <td>WAUGH</td>
      <td>118.75</td>
    </tr>
    <tr>
      <th>572</th>
      <td>MIKE</td>
      <td>WAY</td>
      <td>166.65</td>
    </tr>
    <tr>
      <th>573</th>
      <td>YOLANDA</td>
      <td>WEAVER</td>
      <td>110.73</td>
    </tr>
    <tr>
      <th>574</th>
      <td>ETHEL</td>
      <td>WEBB</td>
      <td>135.68</td>
    </tr>
    <tr>
      <th>575</th>
      <td>RONALD</td>
      <td>WEINER</td>
      <td>132.70</td>
    </tr>
    <tr>
      <th>576</th>
      <td>MARLENE</td>
      <td>WELCH</td>
      <td>117.74</td>
    </tr>
    <tr>
      <th>577</th>
      <td>SHEILA</td>
      <td>WELLS</td>
      <td>73.82</td>
    </tr>
    <tr>
      <th>578</th>
      <td>EDNA</td>
      <td>WEST</td>
      <td>107.74</td>
    </tr>
    <tr>
      <th>579</th>
      <td>MITCHELL</td>
      <td>WESTMORELAND</td>
      <td>134.68</td>
    </tr>
    <tr>
      <th>580</th>
      <td>FRED</td>
      <td>WHEAT</td>
      <td>88.75</td>
    </tr>
    <tr>
      <th>581</th>
      <td>LUCY</td>
      <td>WHEELER</td>
      <td>91.74</td>
    </tr>
    <tr>
      <th>582</th>
      <td>BETTY</td>
      <td>WHITE</td>
      <td>117.72</td>
    </tr>
    <tr>
      <th>583</th>
      <td>ROY</td>
      <td>WHITING</td>
      <td>143.71</td>
    </tr>
    <tr>
      <th>584</th>
      <td>JON</td>
      <td>WILES</td>
      <td>87.76</td>
    </tr>
    <tr>
      <th>585</th>
      <td>LINDA</td>
      <td>WILLIAMS</td>
      <td>135.74</td>
    </tr>
    <tr>
      <th>586</th>
      <td>GINA</td>
      <td>WILLIAMSON</td>
      <td>111.72</td>
    </tr>
    <tr>
      <th>587</th>
      <td>BERNICE</td>
      <td>WILLIS</td>
      <td>145.67</td>
    </tr>
    <tr>
      <th>588</th>
      <td>SUSAN</td>
      <td>WILSON</td>
      <td>92.76</td>
    </tr>
    <tr>
      <th>589</th>
      <td>DARREN</td>
      <td>WINDHAM</td>
      <td>108.76</td>
    </tr>
    <tr>
      <th>590</th>
      <td>VIRGIL</td>
      <td>WOFFORD</td>
      <td>107.73</td>
    </tr>
    <tr>
      <th>591</th>
      <td>LORI</td>
      <td>WOOD</td>
      <td>141.69</td>
    </tr>
    <tr>
      <th>592</th>
      <td>FLORENCE</td>
      <td>WOODS</td>
      <td>126.70</td>
    </tr>
    <tr>
      <th>593</th>
      <td>TYLER</td>
      <td>WREN</td>
      <td>88.79</td>
    </tr>
    <tr>
      <th>594</th>
      <td>BRENDA</td>
      <td>WRIGHT</td>
      <td>104.74</td>
    </tr>
    <tr>
      <th>595</th>
      <td>BRIAN</td>
      <td>WYMAN</td>
      <td>52.88</td>
    </tr>
    <tr>
      <th>596</th>
      <td>LUIS</td>
      <td>YANEZ</td>
      <td>79.80</td>
    </tr>
    <tr>
      <th>597</th>
      <td>MARVIN</td>
      <td>YEE</td>
      <td>75.79</td>
    </tr>
    <tr>
      <th>598</th>
      <td>CYNTHIA</td>
      <td>YOUNG</td>
      <td>111.68</td>
    </tr>
  </tbody>
</table>
<p>599 rows × 3 columns</p>
</div>




```python
#7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English. 
sql_query = """
SELECT title
FROM film
WHERE title LIKE 'Q%%'
OR title LIKE 'K%%'
AND language_id IN
    (
     SELECT language_id
     FROM language
     WHERE name = 'English'
     )
"""
films = pd.read_sql_query(sql_query,engine)
films
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KANE EXORCIST</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KARATE MOON</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KENTUCKIAN GIANT</td>
    </tr>
    <tr>
      <th>3</th>
      <td>KICK SAVANNAH</td>
    </tr>
    <tr>
      <th>4</th>
      <td>KILL BROTHERHOOD</td>
    </tr>
    <tr>
      <th>5</th>
      <td>KILLER INNOCENT</td>
    </tr>
    <tr>
      <th>6</th>
      <td>KING EVOLUTION</td>
    </tr>
    <tr>
      <th>7</th>
      <td>KISS GLORY</td>
    </tr>
    <tr>
      <th>8</th>
      <td>KISSING DOLLS</td>
    </tr>
    <tr>
      <th>9</th>
      <td>KNOCK WARLOCK</td>
    </tr>
    <tr>
      <th>10</th>
      <td>KRAMER CHOCOLATE</td>
    </tr>
    <tr>
      <th>11</th>
      <td>KWAI HOMEWARD</td>
    </tr>
    <tr>
      <th>12</th>
      <td>QUEEN LUKE</td>
    </tr>
    <tr>
      <th>13</th>
      <td>QUEST MUSSOLINI</td>
    </tr>
    <tr>
      <th>14</th>
      <td>QUILLS BULL</td>
    </tr>
  </tbody>
</table>
</div>




```python
#7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
sql_query = """
SELECT first_name, last_name
FROM actor
WHERE actor_id IN
    (
     SELECT actor_id
     FROM film_actor
     WHERE film_id IN
         (
         SELECT film_id
         FROM film
         WHERE title = 'Alone Trip'
         )
     )
"""
alonetripactors = pd.read_sql_query(sql_query,engine)
alonetripactors
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ED</td>
      <td>CHASE</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KARL</td>
      <td>BERRY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>UMA</td>
      <td>WOOD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WOODY</td>
      <td>JOLIE</td>
    </tr>
    <tr>
      <th>4</th>
      <td>SPENCER</td>
      <td>DEPP</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CHRIS</td>
      <td>DEPP</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LAURENCE</td>
      <td>BULLOCK</td>
    </tr>
    <tr>
      <th>7</th>
      <td>RENEE</td>
      <td>BALL</td>
    </tr>
  </tbody>
</table>
</div>




```python
#7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
sql_query = """
SELECT c.first_name, c.last_name, c.email
FROM customer c
INNER JOIN address a ON c.address_id = a.address_id
INNER JOIN city ci ON a.city_id = ci.city_id
INNER JOIN country co ON co.country_id = ci.country_id
WHERE country = 'Canada'
"""
canadians = pd.read_sql_query(sql_query,engine)
canadians
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DERRICK</td>
      <td>BOURQUE</td>
      <td>DERRICK.BOURQUE@sakilacustomer.org</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DARRELL</td>
      <td>POWER</td>
      <td>DARRELL.POWER@sakilacustomer.org</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LORETTA</td>
      <td>CARPENTER</td>
      <td>LORETTA.CARPENTER@sakilacustomer.org</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CURTIS</td>
      <td>IRBY</td>
      <td>CURTIS.IRBY@sakilacustomer.org</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TROY</td>
      <td>QUIGLEY</td>
      <td>TROY.QUIGLEY@sakilacustomer.org</td>
    </tr>
  </tbody>
</table>
</div>




```python
#7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
sql_query = """
SELECT f.title
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Family'
"""
familyfilms = pd.read_sql_query(sql_query,engine)
familyfilms
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AFRICAN EGG</td>
    </tr>
    <tr>
      <th>1</th>
      <td>APACHE DIVINE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ATLANTIS CAUSE</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BAKED CLEOPATRA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BANG KWAI</td>
    </tr>
    <tr>
      <th>5</th>
      <td>BEDAZZLED MARRIED</td>
    </tr>
    <tr>
      <th>6</th>
      <td>BILKO ANONYMOUS</td>
    </tr>
    <tr>
      <th>7</th>
      <td>BLANKET BEVERLY</td>
    </tr>
    <tr>
      <th>8</th>
      <td>BLOOD ARGONAUTS</td>
    </tr>
    <tr>
      <th>9</th>
      <td>BLUES INSTINCT</td>
    </tr>
    <tr>
      <th>10</th>
      <td>BRAVEHEART HUMAN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>CHASING FIGHT</td>
    </tr>
    <tr>
      <th>12</th>
      <td>CHISUM BEHAVIOR</td>
    </tr>
    <tr>
      <th>13</th>
      <td>CHOCOLAT HARRY</td>
    </tr>
    <tr>
      <th>14</th>
      <td>CONFUSED CANDLES</td>
    </tr>
    <tr>
      <th>15</th>
      <td>CONVERSATION DOWNHILL</td>
    </tr>
    <tr>
      <th>16</th>
      <td>DATE SPEED</td>
    </tr>
    <tr>
      <th>17</th>
      <td>DINOSAUR SECRETARY</td>
    </tr>
    <tr>
      <th>18</th>
      <td>DUMBO LUST</td>
    </tr>
    <tr>
      <th>19</th>
      <td>EARRING INSTINCT</td>
    </tr>
    <tr>
      <th>20</th>
      <td>EFFECT GLADIATOR</td>
    </tr>
    <tr>
      <th>21</th>
      <td>FEUD FROGMEN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>FINDING ANACONDA</td>
    </tr>
    <tr>
      <th>23</th>
      <td>GABLES METROPOLIS</td>
    </tr>
    <tr>
      <th>24</th>
      <td>GANDHI KWAI</td>
    </tr>
    <tr>
      <th>25</th>
      <td>GLADIATOR WESTWARD</td>
    </tr>
    <tr>
      <th>26</th>
      <td>GREASE YOUTH</td>
    </tr>
    <tr>
      <th>27</th>
      <td>HALF OUTFIELD</td>
    </tr>
    <tr>
      <th>28</th>
      <td>HOCUS FRIDA</td>
    </tr>
    <tr>
      <th>29</th>
      <td>HOMICIDE PEACH</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>MAGUIRE APACHE</td>
    </tr>
    <tr>
      <th>40</th>
      <td>MANCHURIAN CURTAIN</td>
    </tr>
    <tr>
      <th>41</th>
      <td>MOVIE SHAKESPEARE</td>
    </tr>
    <tr>
      <th>42</th>
      <td>MUSIC BOONDOCK</td>
    </tr>
    <tr>
      <th>43</th>
      <td>NATURAL STOCK</td>
    </tr>
    <tr>
      <th>44</th>
      <td>NETWORK PEAK</td>
    </tr>
    <tr>
      <th>45</th>
      <td>ODDS BOOGIE</td>
    </tr>
    <tr>
      <th>46</th>
      <td>OPPOSITE NECKLACE</td>
    </tr>
    <tr>
      <th>47</th>
      <td>PILOT HOOSIERS</td>
    </tr>
    <tr>
      <th>48</th>
      <td>PITTSBURGH HUNCHBACK</td>
    </tr>
    <tr>
      <th>49</th>
      <td>PRESIDENT BANG</td>
    </tr>
    <tr>
      <th>50</th>
      <td>PRIX UNDEFEATED</td>
    </tr>
    <tr>
      <th>51</th>
      <td>RAGE GAMES</td>
    </tr>
    <tr>
      <th>52</th>
      <td>RANGE MOONWALKER</td>
    </tr>
    <tr>
      <th>53</th>
      <td>REMEMBER DIARY</td>
    </tr>
    <tr>
      <th>54</th>
      <td>RESURRECTION SILVERADO</td>
    </tr>
    <tr>
      <th>55</th>
      <td>ROBBERY BRIGHT</td>
    </tr>
    <tr>
      <th>56</th>
      <td>RUSH GOODFELLAS</td>
    </tr>
    <tr>
      <th>57</th>
      <td>SECRETS PARADISE</td>
    </tr>
    <tr>
      <th>58</th>
      <td>SENSIBILITY REAR</td>
    </tr>
    <tr>
      <th>59</th>
      <td>SIEGE MADRE</td>
    </tr>
    <tr>
      <th>60</th>
      <td>SLUMS DUCK</td>
    </tr>
    <tr>
      <th>61</th>
      <td>SOUP WISDOM</td>
    </tr>
    <tr>
      <th>62</th>
      <td>SPARTACUS CHEAPER</td>
    </tr>
    <tr>
      <th>63</th>
      <td>SPINAL ROCKY</td>
    </tr>
    <tr>
      <th>64</th>
      <td>SPLASH GUMP</td>
    </tr>
    <tr>
      <th>65</th>
      <td>SUNSET RACER</td>
    </tr>
    <tr>
      <th>66</th>
      <td>SUPER WYOMING</td>
    </tr>
    <tr>
      <th>67</th>
      <td>VIRTUAL SPOILERS</td>
    </tr>
    <tr>
      <th>68</th>
      <td>WILLOW TRACY</td>
    </tr>
  </tbody>
</table>
<p>69 rows × 1 columns</p>
</div>




```python
#7e. Display the most frequently rented movies in descending order.
sql_query = """
select f.title, count(*) as Number
from film f
inner join inventory i
on f.film_id = i.film_id
inner join rental r
on i.inventory_id = r.inventory_id
group by f.title
order by Number desc
"""
popular = pd.read_sql_query(sql_query,engine)
popular
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BUCKET BROTHERHOOD</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ROCKETEER MOTHER</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RIDGEMONT SUBMARINE</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>SCALAWAG DUCK</td>
      <td>32</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GRIT CLOCKWORK</td>
      <td>32</td>
    </tr>
    <tr>
      <th>5</th>
      <td>FORWARD TEMPLE</td>
      <td>32</td>
    </tr>
    <tr>
      <th>6</th>
      <td>JUGGLER HARDLY</td>
      <td>32</td>
    </tr>
    <tr>
      <th>7</th>
      <td>ZORRO ARK</td>
      <td>31</td>
    </tr>
    <tr>
      <th>8</th>
      <td>ROBBERS JOON</td>
      <td>31</td>
    </tr>
    <tr>
      <th>9</th>
      <td>RUSH GOODFELLAS</td>
      <td>31</td>
    </tr>
    <tr>
      <th>10</th>
      <td>HOBBIT ALIEN</td>
      <td>31</td>
    </tr>
    <tr>
      <th>11</th>
      <td>WIFE TURN</td>
      <td>31</td>
    </tr>
    <tr>
      <th>12</th>
      <td>GOODFELLAS SALUTE</td>
      <td>31</td>
    </tr>
    <tr>
      <th>13</th>
      <td>TIMBERLAND SKY</td>
      <td>31</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NETWORK PEAK</td>
      <td>31</td>
    </tr>
    <tr>
      <th>15</th>
      <td>APACHE DIVINE</td>
      <td>31</td>
    </tr>
    <tr>
      <th>16</th>
      <td>WITCHES PANIC</td>
      <td>30</td>
    </tr>
    <tr>
      <th>17</th>
      <td>FROST HEAD</td>
      <td>30</td>
    </tr>
    <tr>
      <th>18</th>
      <td>MARRIED GO</td>
      <td>30</td>
    </tr>
    <tr>
      <th>19</th>
      <td>MUSCLE BRIGHT</td>
      <td>30</td>
    </tr>
    <tr>
      <th>20</th>
      <td>RUGRATS SHAKESPEARE</td>
      <td>30</td>
    </tr>
    <tr>
      <th>21</th>
      <td>MASSACRE USUAL</td>
      <td>30</td>
    </tr>
    <tr>
      <th>22</th>
      <td>BUTTERFLY CHOCOLAT</td>
      <td>30</td>
    </tr>
    <tr>
      <th>23</th>
      <td>SUSPECTS QUILLS</td>
      <td>30</td>
    </tr>
    <tr>
      <th>24</th>
      <td>IDOLS SNATCHERS</td>
      <td>30</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PULP BEVERLY</td>
      <td>30</td>
    </tr>
    <tr>
      <th>26</th>
      <td>CAT CONEHEADS</td>
      <td>30</td>
    </tr>
    <tr>
      <th>27</th>
      <td>HARRY IDAHO</td>
      <td>30</td>
    </tr>
    <tr>
      <th>28</th>
      <td>ENGLISH BULWORTH</td>
      <td>30</td>
    </tr>
    <tr>
      <th>29</th>
      <td>SHOCK CABIN</td>
      <td>30</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>928</th>
      <td>RUSHMORE MERMAID</td>
      <td>6</td>
    </tr>
    <tr>
      <th>929</th>
      <td>BED HIGHBALL</td>
      <td>6</td>
    </tr>
    <tr>
      <th>930</th>
      <td>JERSEY SASSY</td>
      <td>6</td>
    </tr>
    <tr>
      <th>931</th>
      <td>WILD APOLLO</td>
      <td>6</td>
    </tr>
    <tr>
      <th>932</th>
      <td>HAUNTED ANTITRUST</td>
      <td>6</td>
    </tr>
    <tr>
      <th>933</th>
      <td>WARLOCK WEREWOLF</td>
      <td>6</td>
    </tr>
    <tr>
      <th>934</th>
      <td>OKLAHOMA JUMANJI</td>
      <td>6</td>
    </tr>
    <tr>
      <th>935</th>
      <td>GRACELAND DYNAMITE</td>
      <td>6</td>
    </tr>
    <tr>
      <th>936</th>
      <td>ITALIAN AFRICAN</td>
      <td>6</td>
    </tr>
    <tr>
      <th>937</th>
      <td>SLING LUKE</td>
      <td>6</td>
    </tr>
    <tr>
      <th>938</th>
      <td>DESPERATE TRAINSPOTTING</td>
      <td>6</td>
    </tr>
    <tr>
      <th>939</th>
      <td>COMANCHEROS ENEMY</td>
      <td>6</td>
    </tr>
    <tr>
      <th>940</th>
      <td>LADYBUGS ARMAGEDDON</td>
      <td>6</td>
    </tr>
    <tr>
      <th>941</th>
      <td>MANNEQUIN WORST</td>
      <td>5</td>
    </tr>
    <tr>
      <th>942</th>
      <td>INFORMER DOUBLE</td>
      <td>5</td>
    </tr>
    <tr>
      <th>943</th>
      <td>FULL FLATLINERS</td>
      <td>5</td>
    </tr>
    <tr>
      <th>944</th>
      <td>GLORY TRACY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>945</th>
      <td>FEVER EMPIRE</td>
      <td>5</td>
    </tr>
    <tr>
      <th>946</th>
      <td>SEVEN SWARM</td>
      <td>5</td>
    </tr>
    <tr>
      <th>947</th>
      <td>MUSSOLINI SPOILERS</td>
      <td>5</td>
    </tr>
    <tr>
      <th>948</th>
      <td>BUNCH MINDS</td>
      <td>5</td>
    </tr>
    <tr>
      <th>949</th>
      <td>PRIVATE DROP</td>
      <td>5</td>
    </tr>
    <tr>
      <th>950</th>
      <td>CONSPIRACY SPIRIT</td>
      <td>5</td>
    </tr>
    <tr>
      <th>951</th>
      <td>BRAVEHEART HUMAN</td>
      <td>5</td>
    </tr>
    <tr>
      <th>952</th>
      <td>TRAFFIC HOBBIT</td>
      <td>5</td>
    </tr>
    <tr>
      <th>953</th>
      <td>FREEDOM CLEOPATRA</td>
      <td>5</td>
    </tr>
    <tr>
      <th>954</th>
      <td>HUNTER ALTER</td>
      <td>5</td>
    </tr>
    <tr>
      <th>955</th>
      <td>HARDLY ROBBERS</td>
      <td>4</td>
    </tr>
    <tr>
      <th>956</th>
      <td>MIXED DOORS</td>
      <td>4</td>
    </tr>
    <tr>
      <th>957</th>
      <td>TRAIN BUNCH</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>958 rows × 2 columns</p>
</div>




```python
#7f. Write a query to display how much business, in dollars, each store brought in.
sql_query = """
select a.address, sum(amount) as 'Total Brought In'
from payment p
inner join customer c
on c.customer_id = p.customer_id
inner join store s
on s.store_id = c.store_id
inner join address a
on a.address_id = s.address_id
group by s.address_id
"""
stores = pd.read_sql_query(sql_query,engine)
stores
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>Total Brought In</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>47 MySakila Drive</td>
      <td>37001.52</td>
    </tr>
    <tr>
      <th>1</th>
      <td>28 MySQL Boulevard</td>
      <td>30414.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
#7g. Write a query to display for each store its store ID, city, and country.
sql_query = """
select s.store_id, c.city, co.country
from store s
inner join address a
on s.address_id = a.address_id
inner join city c
on a.city_id = c.city_id
inner join country co
on c.country_id = co.country_id
"""
stores = pd.read_sql_query(sql_query,engine)
stores
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>city</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Lethbridge</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Woodridge</td>
      <td>Australia</td>
    </tr>
  </tbody>
</table>
</div>




```python
#7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
sql_query = """
select c.name, sum(amount) as Revenue
from payment p
inner join rental r
on r.rental_id = p.rental_id
inner join inventory i
on i.inventory_id = r.inventory_id
inner join film_category fc
on fc.film_id = i.film_id
inner join category c
on c.category_id = fc.category_id
group by c.name
order by Revenue desc
limit 5
"""
genres = pd.read_sql_query(sql_query,engine)
genres
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sports</td>
      <td>5314.21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sci-Fi</td>
      <td>4756.98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Animation</td>
      <td>4656.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Drama</td>
      <td>4587.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Comedy</td>
      <td>4383.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
def RunSQL(sql_command):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='kcmo1728',
                             db='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            commands = sql_command.split(';')
            for command in commands:
                if command == '\n': continue
                cursor.execute(command + ';')
                connection.commit()
    except Exception as e: 
        print(e)
    finally:
        connection.close()
```


```python
#8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
sql_query = """
create view top_genres as
select c.name, sum(amount) as Revenue
from payment p
inner join rental r
on r.rental_id = p.rental_id
inner join inventory i
on i.inventory_id = r.inventory_id
inner join film_category fc
on fc.film_id = i.film_id
inner join category c
on c.category_id = fc.category_id
group by c.name
order by Revenue desc
limit 5
"""
RunSQL(sql_query)
```


```python
#8b. How would you display the view that you created in 8a?
top_genres = pd.read_sql_query('select * from top_genres', engine)
top_genres
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sports</td>
      <td>5314.21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sci-Fi</td>
      <td>4756.98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Animation</td>
      <td>4656.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Drama</td>
      <td>4587.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Comedy</td>
      <td>4383.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
RunSQL('drop view top_genres')
```
