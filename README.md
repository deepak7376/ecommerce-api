Here’s how you can run database migrations and test the API:

---

### 1. **Run Database Migrations**
Flask-Migrate helps manage migrations.

#### Install Dependencies
Ensure you have Flask-Migrate installed:
```bash
pip install flask-migrate
```

#### Initialize Flask-Migrate
Run the following commands in the root directory of your project:

1. **Initialize migrations folder**:
   ```bash
   flask db init
   ```

2. **Generate migration scripts**:
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply migrations to the database**:
   ```bash
   flask db upgrade
   ```

This creates the database and applies your models to it.

---

### 2. **Run the API**
Run the Flask application:
```bash
python run.py
```

The API should now be accessible at `http://127.0.0.1:5000`.

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
       "name": "Laptop",
       "description": "High-performance laptop",
       "price": 999.99,
       "stock": 10
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
If you’ve written test cases in `app/tests/`, use `pytest` to run them:

#### Install `pytest`:
```bash
pip install pytest
```

#### Run Tests:
```bash
pytest app/tests/
```

This will execute all the test cases and provide a summary of results.

---

Let me know if you need any additional help or examples!