# Online Shop Backend (Lab 9 & 10)

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Superuser (pre-created in db.sqlite3)
- Username: `admin`
- Password: `admin123`

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/categories/ | List all categories |
| POST | /api/categories/ | Create category |
| GET | /api/categories/{id}/ | Get category |
| PUT | /api/categories/{id}/ | Update category |
| DELETE | /api/categories/{id}/ | Delete category |
| GET | /api/categories/{id}/products/ | Get products by category |
| GET | /api/products/ | List all products |
| POST | /api/products/ | Create product |
| GET | /api/products/{id}/ | Get product |
| PUT | /api/products/{id}/ | Update product |
| DELETE | /api/products/{id}/ | Delete product |

## Lab 10 — View Levels

All 4 implementations are in `api/views/`:

| File | Level | Approach |
|------|-------|----------|
| `fbv.py` | Level 2 | Function-Based Views with @api_view |
| `cbv.py` | Level 3 | Class-Based Views with APIView |
| `mixins.py` | Level 4 | Mixins + GenericAPIView |
| `generics.py` | Level 5 | Generic Views (active) |

To switch levels, edit `api/views/__init__.py` and change the import.

## Postman
Import `OnlineShopAPI.postman_collection.json` into Postman to test all endpoints.
