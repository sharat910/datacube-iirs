# Datacube for Uttarakhand Data

### To install

install GDAL and pbzip2 before configuring the datacube

```bash
sudo python setup.py develop
```

# Setting up the datacube

* Use the cloned environment.
* Run the setup.py file.

There are many library issues, specifically version issues if the second method is chosen.

If postgres import error in sqlalchemy then 
> Change in datacube/index/postgres/tables/\_schema.py, replace "postgres" with "postgresql"

If GDAL error, use GDAL-2.0.0 ONLY. Dont use GDAL-2.1.0

If application_name error (psycopg2), install latest version of libpq and ensure that psql version 9.5 is being used.
