# facebook graph api example

Fetches public data from facebook using facebook's graph API, and loads into a postgres database.

Currently pulls rudimentary data for:

- pages
- posts
- comments
- reactions

Populate a `config.py` file with the following variables:

```python
app_id = 'xxx'
app_secret = 'xxx'

db_user = 'xxx'
db_password = 'xxx'
db_host = 'xxx'
db_name = 'xxx'
```

Then, run:

```
python3 etl.py
```
