## DSI program install guide for Ubuntu (16.04)

Please follow the instructions below step-by-step for each of the programs
we use in the Data Science Immersive.

0) Make sure your system is up-to-date.
    ```bash
    $ sudo apt-get update
    $ sudo apt-get upgrade
    ```

1) Download version control software `git`.
    ```bash
    $ sudo apt-get install git
    ```

2) Download text editor `atom`.
    
    Go to [https://atom.io/](https://atom.io) and click on the Debian (.deb)
    package to download it into your Downloads folder.  Then, in terminal, navigate to
    your Downloads folder and type
    ```bash
    $ sudo dpkg -i atom-amd64.deb
    ```
    In this case the downloaded .deb file was *atom-amd64.deb* but change it in above bash
    command if your file was different (as it may be for the 32 bit version).


3) Download and install the Anaconda Python package that contains utilities for large-scale 
data processing, predictive analytics, and scientific computing.

    a) Navigate to the continuum.io downloads page. 
[www.continuum.io/downloads](https://www.continuum.io/downloads#_unix)

    b) Click on the 32 bit or 64 bit **Python 3.6 version**, depending on
    your system specification.

    c) The anaconda installer will be downloaded to your Downloads folder.
    In terminal, navigate to your Downloads folder.

    d) In terminal in the Downloads folder type:
    ```bash
    $ bash Anaconda3-4.3.1-Linux-x86_64.sh
    ```
    (in this case the downloaded file was *Anaconda3-4.3.1-Linux-x86_64.sh*
    but replace this with actual file downloaded, and **DO** type **bash**
    in the terminal command above.)

### Programs for Week 1

4) Install Postgres SQL

    a) Change to home directory.
    ```bash
    $ cd ~
    ```
    b) Install Postgres SQL.
    ```bash
    $ sudo apt-get install postgresql
    ```
    c) Run postgres.
    ```bash
    $ sudo -i -u postgres
    ```
    d) Create an empty database (readychef) that we will fill will data later.
    ```bash
    $ createdb readychef
    ```
    e) Create a user (you) as a superuser.
    ```bash
    $ createuser --interactive
    ```
    Your username (or "role") should be the same as the root user of your linux account.
    For instance, I'm `frank@frank-computer` so my username for postgres
    should be `frank`.  *When asked if role should be superuser respond 'y'*. 
    
    f) While you're at it, create an empty database with your username so that
    later you can just type `psql` instead of `psql database_name` to start
    psql.
    ```bash
    $ createdb your_user_name
    ```
    For example, I would type `$ createdb frank`.
    
    g) Exit postgres.
    ```bash
    $ exit
    ```
    h) Now, to test if everything is working, fill the empty database `readychef`
    with data. On GitHub, fork the SQL repo from zipfian to your GitHub account
    and then clone it to your laptop.  `cd` into the `data` folder in your cloned 
    directory and make sure `readychef.sql` is present by typing `ls`.
    
    i) If you see `readychef.sql` then import it into the empty postgres sql 
    database created earlier.
    ```bash
    $ psql readychef < readychef.sql
    ```
    j) Now see if you can access the readychef database.
    ```bash
    $ psql readychef
    ```
    k) View the tables in readychef.
    ```bash
    # \d
    ```
    l) See a particular table, `events` for instance.
    ```bash
    # \d events
    ```
    m) Quit psql.
    ```bash
    # \q
    ```
    n) Note: Each time you want to add a new database to postgres, you'll
    need to use the following set of commands:
    ```bash
    $ sudo -i -u postgres
    $ createdb databasename
    $ exit
    ```
    Navigate to where you databasename.sql file is then import the data:
     ```bash
    $ psql databasename < databasename.sql
    ```


5) Install Psycopg2, a Python wrapper for interfacing with Postgres SQL.
    
    a) Use conda to install psycopg2.
    ```bash
    $ conda install psycopg2
    ```
    b) Determine your host (where postgres is looking for a connection).
    ```bash
    $ sudo -u postgres psql -c "SHOW unix_socket_directories;"
    ```
    For me it was `/var/run/postgresql`.
    
    c) In another tab in your terminal, open your psql database.
    ```bash
    $ psql readychef
    ```
    d) In yet another tab in your terminal, start ipython.
    ```bash
    $ ipython
    ```
    e) In ipython, try to import psycopg2.
    ```bash
    In [1]: import psycopg2
    ```
    f) Within ipython, establish a connection with the `readychef` database.
    ```bash
    In [2]: conn = psycopg2.connect(dbname='readychef', user='frank', host = '/var/run/postgresql')
    ```
    Obviously your 'user' and 'host' may be different.
    
    g) Establish a cursor to your connection within ipython.
    ```bash
    In [3]: c = conn.cursor()
    ```
    
    h) To test, write a query:
    ```bash
    In [4]: query_example = '''SELECT * FROM events LIMIT 10;'''
    ```
    
    i) Execute the query.
    ```bash
    In [5]: c.execute(query_example)
    ```
    
    j) Save the query results to a variable within ipython.
    ```bash
    In [6]: results_q1 = c.fetchall()
    ```
    k) Print the results.
    ```bash
    In [7]: print results_q1
    ```
    l) Finally - important! - close your cursor.
    ```bash
    In [8]: c.close()
    ```

