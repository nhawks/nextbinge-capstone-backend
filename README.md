<div id="top"></div>

<br />

<h3 align="center">NextBinge</h3>

  <p align="center">
    For my 10-day capstone, I built a full-stack mobile-friendly web application named NextBinge. NextBinge helps users find their favorite shows in one place and keep up with currently streaming shows.
    <br>
    It is increasingly complicated to keep up with what’s on TV and where shows are streaming now that networks have developed unique streaming platforms. Users can view the latest trending shows and other popular shows categorized by genre or search by filter/genre. The app also displays the TV show’s details like where the show is streaming, summary, IMDb rating, and season information. 
    From here, you can add/remove the show to your watchlist, favorites, like, dislike, and mark the show as watched. 
    This page also features a discussion section allowing users to comment on a show and reply, like, or dislike posted comments.
    <br />
    <a href="https://github.com/nhawks/nextbinge-capstone-frontend"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://www.youtube.com/watch?v=44NRQpq7yDc">Video Demo</a>
    ·
    <a href="https://github.com/nhawks/nextbinge-capstone-frontend/issues">Report Bug</a>
    ·
    <a href="https://github.com/nhawks/nextbinge-capstone-frontend/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![NextBinge](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/NextBinge.png)

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [React.js](https://reactjs.org/)
* [JavaScript](https://www.javascript.com/)
* [Bootstrap](https://getbootstrap.com)
* [Material Design Bootstrap](https://mdbootstrap.com/docs/b5/react/)
* [React Bootstrap](https://react-bootstrap.github.io/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [MySQL](https://www.mysql.com/)
* [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)
* [Movie of the Night API](https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Install [MySQL Workbench](https://www.mysql.com/products/workbench/). 
* Install the latest version of [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/nhawks/nextbinge-capstone-backend.git
    $ cd nextbinge-capstone-backend
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

## After

* Clone the frontend repository and follow the instructions located [here](https://github.com/nhawks/nextbinge-capstone-frontend). 


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

## Search by Genre
![Search by Genre](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/genre-search.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## Search by Title
![Search by Title](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/title-search.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## View the TV Show's details
![Show Details](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/show-details.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## Play Trailer
![Play Trailer](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/play-trailer.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## Season Information
![Season Info](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/season-info.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## Discuss the show with others!
![Discussion](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/discussions.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## My Watchlist
![Watchlist](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/watchlist.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## My Favorites
![Favorites](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/favorites.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>


## Watched Shows Table
![Watched Shows](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/watched.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>



## Mobile Friendly
![Mobile Home](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/mobile-home.PNG)
![Mobile Navbar](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/mobile-nav.PNG)
![Mobile Search](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/mobile-search.PNG)
![Mobile Show Details](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/mobile-details.PNG)
![Mobile Show Discussion](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/mobile-discussion.PNG)
![Mobile Favorites](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/mobile-favorites.PNG)
<p align="right">(<a href="#top">back to top</a>)</p>

## About NextBinge
![About](https://github.com/nhawks/nextbinge-capstone-frontend/blob/master/project-images/about.PNG)

_For more examples, please refer to the [Project Video Demo](https://vimeo.com/648685904?embedded=true&source=video_title&owner=41163184)_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

NiGeanya Hawkins - nmhawkins@outlook.com


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/nhawks/nextbinge-capstone-frontend.svg?style=for-the-badge
[contributors-url]: https://github.com/nhawks/nextbinge-capstone-frontend/graphs/contributors
[linkedin-url]: https://linkedin.com/in/nmhawkins
[product-screenshot]: (./project-images/NextBinge.png)


