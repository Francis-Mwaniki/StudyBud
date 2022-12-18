<p align="center">
  <p align="center">
    <a href="https://www.youtube.com/channel/UC7m0x5NHiHz4VemPFVaS98A" target="_blank">
      <img src="https://raw.githubusercontent.com/codingforinnovations/Django-on-Vercel/main/.static/Logo-Light.png?token=GHSAT0AAAAAABXU4AJBD6OH7Z33MGA7X2EYY3HPGAA" height="72" />    
    </a>
  </p>
  <p align="center">
    For Programmers, By Programmers.
  </p>
</p>

# Django with Vercel

This repository is the final code for the Django with Studybud.

---

## Running the Project

#### Create a Folder & Clone the Repository.
```
mkdir ~/Dev/studybud
cd ~/Dev/studybud
```

#### Create A Virtual Environment.
```
python3.9 -m virtualenv .
```

#### Activate the Virtual Environment.
```
source bin/activate
```

**In Windows use `.\Scripts\activate`**

#### Install Required Dependencies 
```
pip install -r requirements.txt
```

#### Make Migrations
```
python manage.py migrate
```

#### Run the Server
```
python manage.py runserver localhost:8000
```

_Open [localhost:8000](http://localhost:8000) in Your Browser_
