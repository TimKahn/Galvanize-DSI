MongoDB installation Guide
==============================

remove anything old
---------------------

  ~$ sudo rm /var/lib/mongodb/mongod.lock
  ~$ sudo apt-get purge mongodb mongodb-clients mongodb-server mongodb-dev
  ~$ sudo apt-get purge mongodb-*
  ~$ sudo apt-get autoremove 
                              
install
-------------

  (1) ~$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

  (2) Open  `/etc/apt/sources.list`  in your favorite editor
      Then add these two lines to the end of the file    

      ## mongodb 
      deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse

  (3) ~$ sudo apt-get install -y mongodb-org
      ~$ conda install pymongo


Create the data dir in home
--------------------------------

  ## if you want to use a custom directory
  ~$ mkdir ~/mongo-data 
  ~$ sudo chmod 0755 ~/mongo-data
  ~$ mongod --dbpath ~/mongo-data

  ## if you want to use the default data/db directory
  ~$ sudo mkdir -p /data/db
  ~$ sudo chmod 0755 /data/db
  ~$ sudo chown -R username:username /data/db

Run the daemon manually
---------------------------

   ~$ mongod --dbpath ~/mongo-data

   or

   ~$ mongod
   
      
If you want to use the sevice version of the deaemon
------------------------------------------------------

   Start the daemon
   
      ~$ sudo service mongod start

   Turn off the deamon

      ~$ sudo service mongod stop

   Check that the daemon is listening

      ~$ less /var/log/mongodb/mongod.log

If you want to start the shell
--------------------------------

   Ensure that you have the daemon running either as a service or manually

   ~$ mongo 
  
      
