# Klase

A learning management and online assessment system for academic education.

## Features

specify

## [Entity Relationship Diagram] (https://mermaid.live/view#pako:eNrNls1q3DAQx19F6Jy8gG-lSyCEQmHZSzEEVZqsRS3JSKOmYeN372jt9fpDdpOGQn2yNP8Z_UYznt0Tl04BLzj4nRZHL0xpGT17jAosstfX21t3Yvv43egQtLOsYCEtMEyFrTsLP7voA5AIrHd1HfLRuuVOBxkvQaUHgUD6zuPeBvRRovMXpyEygpAVhDXddWcrfh-t9_lkrYtWgkmQBatEyKoo1tFua77QIV6Lel2RTd5ZFNpm9Wv5DC6d0wguVzMPEvTPa_6Xipy6ZXoOh_sdC93-o1bs68PVRgjaHpkVBhabYISu2WGpbkQIz86rhYE6YxmmqRy6brfNdMEcVA-m_4S1r9qIU9P9pq8rR4caa8iBKAjS6wapbNNIfWUe4GXilkzXaxpb20xrjOkUm11cx5uyeDxj361gv41Z0ZeA2sDwkjOBULW2y4hPenyMAqkNfVNG-B9hltyoy_-YnBguIvXMOL1572dSnyFtZLekHYUJKDDOk5jMn7-u0QYTwi9clmk4f5haH-2P93bC4m7b2YAazbxNtj5QmorklWV-R8kH4pCMAlfH0j_Gmw65NxDyG27A05BT9JN-Jio5VtRXJS_oVVFLlry0SSciuv2LlbygI-CGexePFS-eRB1oFZt0Qv-X4CJphP3mnOlF7W85_pjB)


## Tech Stack

1. Django
2. Bootstrap
3. jQuery
4. Chart.js
5. Animate.css

## Run Locally

1. Clone the project

```bash
git clone https://github.com/JivSTuban/lms.git
```

2. Go to the project directory

```bash
cd klase
```

3. Create a virtual environment and activate it (Windows)

```bash
python -m venv env
```

```bash
env\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Make migrations and migrate

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

6. Create admin/superuser

```bash
python manage.py createsuperuser
```

7. Finally run the project

```bash
python manage.py runserver
```

Now the project should be running on http://127.0.0.1:8000/

## License

[The MIT License (MIT)](LICENCE)
