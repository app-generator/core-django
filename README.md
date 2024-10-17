# [Django Core](https://github.com/app-generator/core-django)

Minimal **Django** project with `Docker` support - actively supported by [App Generator](https://app-generator.dev/) via `Email` and **[Discord](https://discord.gg/fZC6hup)**. 

---

> For a **complete set of features** and long-term support, check out **[Dynamic Django](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html)**, a powerful starter that incorporates:

- ✅ [Dynamic DataTables](https://app-generator.dev/docs/developer-tools/dynamic-django/datatables.html): using a single line of configuration, the data saved in any table is automatically managed
- ✅ [Dynamic API](https://app-generator.dev/docs/developer-tools/dynamic-django/api.html): any model can become a secure API Endpoint using DRF
- ✅ [Dynamic Charts](https://app-generator.dev/docs/developer-tools/dynamic-django/charts.html): extract relevant charts without coding all major types are supported
- ✅ [CSV Loader](https://app-generator.dev/docs/developer-tools/dynamic-django/csv-loader.html): translate CSV files into Django Models and (optional) load the information
- ✅ Powerful [CLI Tools](https://app-generator.dev/docs/developer-tools/dynamic-django/cli.html) for the GIT interface, configuration editing, updating the configuration and database (create models, migrate DB)

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
