
# Short Links

Short links is a url shortener service, it takes a link and responds back with a short link. When you go to the short link it will redirect you to the original url. You can also view the number of clicks that was made on your short link in the stats endpoint.


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Run Locally

Clone the project

```bash
  git clone git@github.com:saadbinakhlaq/short-links.git
```

Go to the project directory

```bash
  cd short-links
```

Install dependencies

```bash
  docker-compose build
```

Start the server

```bash
  docker-compose up
```

Run Migrations

```bash
  docker-compose run api alembic upgrade head
```

visit http://localhost:8090


## Running Tests

To run tests, run the following command

```bash
  docker-compose run api createdb -h db -U postgres short_links_test
  password: postgres

  docker-compose run api pytest
```


## Tech Stack

**Database:** Postgres

**Server:** Python, FastAPI


## API Docs

[swagger doc](http://localhost:8090/docs)


## Assumptions

For redirecting Http status code 307 was considered as it is a temporary redirect and better for counting clicks

## Usage
#### Create a short link
```bash
curl -X 'POST' \
  'http://localhost:8090/api/v1/links' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "original_url": "https://www.youtube.com/watch?v=DYvhC_RdIwQ"
}'
```

#### Check stats

```bash
curl -X 'GET' \
  'http://localhost:8090/stats?short_link_id=DYvhCSAD' \
  -H 'accept: application/json'
```
