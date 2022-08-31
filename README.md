#Project FPF - API DJANGO REST

## Instalação

1. Instale o python 3 aqui <a href="https://www.python.org/" target="_blank">here</a> 
1. cd django-rest
1. python -m venv .venv
1. source .venv/Scripts/Activate - bash
1. .venv/Scripts/Activate - shell
1. python -m pip install -U pip
1. pip install -r requirements.txt
1. python contrib/env_gen.py
1. python manage.py migrate
1. python manage.py createsuperuser
1. python manage.py runserver

---

# API Endpoints
* [**products/**](#products)		
    * [**/products/games/**](#games)
        * [**/products/games/?title={query}&category__name={query}&company__name={query}**](#gamesearchquery)
    * [**/products/categories/**](#category)
        * [**/products/categories/?name={query}**](#categorysearch)
    * [**/products/companies/**](#company) 
        * [**/products/companies/?name={query}**](#companysearch)
    
---

# JSON Model - Post

## Game
```JSON
    {
        "title": "string",
        "slug": "string",
        "description": "string",
        "release_date": "YYYY-MM-DD",
        "category": 0,
        "company": 0,
        "price": 0,
        "quantity": 0,
        "is_activate": false,
        "picture": null
    }
```
## Category
```JSON
    {
        "name": "string"
    }
```

## Company
```JSON
    {
        "name": "string"
    }
```
    