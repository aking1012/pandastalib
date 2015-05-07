#StockDbSync
A simple python3 package to slurp all the data from the yahoo CSV api
and keep it in a local csv database.  It uses SQLAlchemy and flask to
shovel it in to an SQL database.

NASDAQ, AMEX, and NYSE are all built in.

It takes a considerable amount of time for initial run.  Staying synced is meant
to be run as a background task via cron or whatever, not a watch and wait.

**Scripts**  
Browse the scripts folder to see example creation of the database and where
the package stores configuration data.

**Examples**  
There's really only one example.  It's in the module's example folder...
