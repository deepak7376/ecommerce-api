### 1. **Run Database Migrations**

#### Initialize Flask-Migrate
Run the following commands in the root directory of your project:

1. **Initialize migrations folder**:
   ```bash
   docker exec -it flask_app flask db init
   ```

2. **Generate migration scripts**:
   ```bash
   docker exec -it flask_app flask db migrate -m "Initial migration"

   ```

3. **Apply migrations to the database**:
   ```bash
   docker exec -it flask_app flask db upgrade
   ```
docker exec -it postgres_db psql -U postgres -d mydatabase

---

### 3. **Test the API**
You can use tools like **Postman**, **cURL**, or **pytest** to test your API endpoints.

#### Using cURL
1. **Test GET /products**:
   ```bash
   curl -X GET http://127.0.0.1:5000/products
   ```

2. **Test POST /products**:
   ```bash
   curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{
       "name": "Table",
       "description": "High-performance",
       "price": 200.99,
       "stock": 30
   }'
   ```

3. **Test POST /orders**:
   ```bash
   curl -X POST http://127.0.0.1:5000/orders -H "Content-Type: application/json" -d '{
       "products": [
           {"id": 1, "quantity": 2}

       ]
   }'
   ```

---

### 4. **Run Automated Tests**

#### Install `pytest`:
```bash
pip install pytest
```

#### Run Tests:
```bash
pytest app/tests/
```

### 5. **Database setup**

docker pull postgres
docker run --name my-postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres
docker exec -it my-postgres psql -U myuser -d mydatabase
docker run --name my-postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -v my_pgdata:/var/lib/postgresql/data -d postgres

/d

/dt