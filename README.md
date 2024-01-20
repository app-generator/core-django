# [Django Core](https://github.com/app-generator/core-django)

Minimal **[Django](https://www.djangoproject.com/)** project with `Docker` support - actively supported by [AppSeed](https://appseed.us/) via `Email` and **[Discord](https://discord.gg/fZC6hup)** `(2k+ Members)`.

> Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Docker`
- ✅ DOCS:
  - `Video`: [Django for Beginners - Simple Codebase Intro](https://www.youtube.com/watch?v=dVybpJRwbmc)
  - `Video`: [Django for Beginners - Go LIVE with Render](https://www.youtube.com/watch?v=JyzjVYMuzBQ)
  - `Video`: [Django for Beginners - Integrate UI (Volt Dashboard)](https://www.youtube.com/watch?v=gqw0Bs67lM4)

<br />

## Start in `Docker`

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/core-django.git
$ cd core-django
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/core-django.git
$ cd core-django
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

---
**[Django Core](https://github.com/app-generator/core-django)** - Minimal **Django** core provided by **[AppSeed](https://appseed.us/)**
