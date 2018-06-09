
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
import pandas as pd
from warnings import filterwarnings
import pymysql
filterwarnings('ignore', category=pymysql.Warning)
import os


# In[2]:


engine = create_engine('mysql+pymysql://root:kcmo1728@localhost/sakila') 


# In[3]:


# 1a. Display the first and last names of all actors from the table `actor`. 
sql_query = """
SELECT first_name,last_name 
FROM actor
"""
actor = pd.read_sql_query(sql_query, engine)
actor


# In[4]:


# 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. 

sql_query = """
SELECT CONCAT(first_name, ' ' ,last_name) AS 'Actor Name'
FROM actor
"""
ActorName = pd.read_sql_query(sql_query, engine)
ActorName


# In[5]:


#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
sql_query = """
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe'
"""
joe = pd.read_sql_query(sql_query, engine)
joe


# In[6]:


#2b. Find all actors whose last name contain the letters `GEN`:
sql_query = """
SELECT *
FROM actor
WHERE last_name LIKE '%%gen%%'
"""
gen = pd.read_sql_query(sql_query, engine)
gen


# In[7]:


#2c. Find all actors whose last names contain the letters `LI`. This time, order the rows by last name and first name, in that order:
sql_query = """
SELECT *
FROM actor
WHERE last_name LIKE '%%li%%'
ORDER BY last_name, first_name
"""
li = pd.read_sql_query(sql_query, engine)
li


# In[12]:


#2d. Using `IN`, display the `country_id` and `country` columns of the following countries: Afghanistan, Bangladesh, and China:
sql_query = """
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', and 'China');
"""
df = pd.read_sql_query(sql_query, engine)
df


# In[10]:


#3a. Add a `middle_name` column to the table `actor`. Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.
sql_query = """
ALTER TABLE actor
ADD middle_name VARCHAR(20)
AFTER first_name;
"""
engine.execute(sql_query)


# In[11]:


#3b. You realize that some of these actors have tremendously long last names. Change the data type of the `middle_name` column to `blobs`.
sql_query = """
ALTER TABLE actor
MODIFY COLUMN middle_name blob;
"""
engine.execute(sql_query)


# In[12]:


#3c. Now delete the `middle_name` column.
sql_query = """
ALTER TABLE actor
Drop COLUMN middle_name;
"""
engine.execute(sql_query)


# In[8]:


#4a. List the last names of actors, as well as how many actors have that last name.
sql_query = """
select distinct last_name, count(*) as number
from actor
group by last_name
order by number desc
"""
last_names = pd.read_sql_query(sql_query, engine)
last_names


# In[14]:


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


# In[15]:


#4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
sql_query = """
UPDATE actor
SET first_name = 'HARPO'
where first_name = 'groucho'
and last_name = 'williams'
"""
engine.execute(sql_query)


# In[16]:


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


# In[9]:


sql_query = """
select * 
from actor
where actor_id =172
"""
groucho = pd.read_sql_query(sql_query, engine)
groucho


# In[10]:


#5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it? 
sql_query = """
describe sakila.address
"""
pd.read_sql_query(sql_query, engine)


# In[11]:


#6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
sql_query = """
select staff.first_name,staff.last_name, address.address
from staff
inner join address
on staff.address_id = address.address_id;
"""
staffaddress = pd.read_sql_query(sql_query, engine)
staffaddress


# In[12]:


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


# In[13]:


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


# In[14]:


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


# In[15]:


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


# In[16]:


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


# In[17]:


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


# In[18]:


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


# In[19]:


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


# In[20]:


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


# In[21]:


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


# In[22]:


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


# In[23]:


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


# In[24]:


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


# In[25]:


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


# In[26]:


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


# In[27]:


#8b. How would you display the view that you created in 8a?
top_genres = pd.read_sql_query('select * from top_genres', engine)
top_genres


# In[28]:


#8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
RunSQL('drop view top_genres')

