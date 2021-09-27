# BOOK A BAND


[&#127926;  &nbsp; **View Live Website**  &nbsp; &#127926;](https://bookaband.herokuapp.com/)

[&#127928;  &nbsp; **View GitHub Repository** &nbsp; &#127928;](https://github.com/OliHickie/book_a_band)

![Image of website](media/responsive.png)

Book a Band is an e-commerce website designed to help users plan and book musical entertainment for their wedding day. The site offers users an easy booking system which allows them to book a variety of acts, as well as view all bookings in one easy place. 

The website is built using the Django framework alongside Bootstrap and jQuery, with the checkout process provided by Stripe. Static files are hosted by Amazon Web Services and the site is deployed on Heroku. This website was created as part of my Full Stack Web Developer Diploma with Code Institute.

# Contents

1) [User Experience](#user-experience)
2) [Features](#features)
3) [Technologies](#technologies)
4) [Testing](#testing)
5) [Deployment](#deployment)
6) [Credits](#credits)

<br>

# User Experience

The layout of the site is clear, clean and relatively simple. The idea behind this is for users to understand the functionality of the site and navigate to their desired destination quickly. The site will offer a number of different acts and to make the searching easier, there are a number of different categories that the user may reduce the amount of search results and, in turn, find an appropriate band or act. 
The checkout process is quick and clear, made easy by the use of Stripe. Once all bands or acts have been paid for, the booking is marked as confirmed. 
Many of the site actions are supported by notifications at the top of the screen to confirm the users actions and keep a clean feel to the sight. 

## User Stories

| # | User | Would want to |
| :----- | :------- | --------- |
| US01 | New User | Quickly understand the purpose of the  website |
| US02 | New User | Navigate to a list of bands |
| US03 | New User | Navigate to a list of blogs |
| US04 | New User | Search for bands depending on category or keyword |
| US05 | New User | View bands depending on location or price |
| US06 | New User | View a band's details, cost, ratings and location |
| US07 | New User | View user reviews for the band |
| US08 | New User | View suggestions for similar bands |
| US09 | New User | Read blogs about wedding music |
| US10 | New User | Share blogs on social media |
| US11 | New User | Visit website's socials |
| US12 | New User | View website's contact information |
| US13 | New User | Register for an account |
| US14 | Registered User | Create a booking for a band |
| US15 | Registered User | View all bookings in one place |
| US16 | Registered User | Confirm bookings through making a payment |
| US17 | Registered User | View confirmation of bookings and payments made |
| US18 | Registered User | Leave a review on bands that I have booked |
| US19 | Registered User | Delete any bookings that aren't confirmed |
| US20 | Registered User | Update and recover account information |
| US21 | Site Owner | Add and Update new bands to the site |
| US22 | Site Owner | Add, update and delete blogs from the site |

## Design

The site is aimed at those planning on getting married, although a future step would be to open the site up to attract people planning events in general. With the focus, for now, being on weddings, the color scheme, imagery and design reflects this.  

### Color Scheme

![Image of color scheme](media/babcolor1.png)

I used a lot of pinks in the site as a soft color and that often associated with weddings. THe two contrasting shades of pink are used as both backdrops as well as for the logo, text and buttons. Blue offered a nice contrast to this so if often used for headings and bold text. 
I wanted to keep the color scheme relatively simple as there is a lot of color introduced to pages through busy imagery. 

### Typography

Throughout the site I used two types of font, both downloaded from Google Fonts. For titles and large text, including the logo, I used Abril Fatface and for the rest of the site I used Playfair Display, a very easy to read font, which has a smart and fun look about it. 

### Wireframes

INSERT WIREFRAMES HERE!

### Database Schema
![Image of schema](media/schema.png)

Schema created on [dbdiagram.io](https://dbdiagram.io/)

# Features

- Site is fully responsive across all screen sizes.
- Navigation menu and search bar reduce into a collapsable menu on smaller screen sizes. 
- Users can log in and log out using an email and passwrod which can be recovered and updated. All emails are authorised with a confirmation email. 
- Users can search for Band using keywords. They can also use quick links to view bands depending on location, price or sort alphabetically or by price. The bands are displayed in card format and paginated.
- Bookings can be made easily and viewed, before committing through making a payment. Bookings can also be deleted before they are confirmed. Due to bands being booked for wedding days, once successful payment confirms the booking, any changes need to be done via email with the site owner. 
- The my bookings page acts as a 'cart' and 'order history' page to keep all user's bookings in one place.
- Once a booking is confirmed, the user is then able to leave a review and a rating for the band, which will be added to the band profile. 
- Payments made easily through the use of Stripe. 
- All blogs are readable and also include quick links to post directly to social media channels. 
- Certain CRUD features are available on the site for users and the site owner. These include being uble to add bookings, reviews, blogs and bands, editing teh information for both bands and blogs (by the site owner) and removing blogs and bookings (before payment has been made). 
- Notifications are all delivered using Bootstrap toasts and any delete functions are protected by confirmation modals. 

# Technologies

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python3](https://www.python.org/) 
- [Javascript](https://www.javascript.com/) / [JQuery](https://jquery.com/)
- [Django](https://www.djangoproject.com/) - the framework used for the site.
- [Amazon Web Services](https://aws.amazon.com/) - used to store static and media files. 
- [Git](https://git-scm.com/) - used for version control.
- [Bootstrap5](https://getbootstrap.com/) - Features and componants were used across the site, such as the collapsible nav bar, toasts, modals, dropdowns and accordians. 
- [SQLite](https://www.sqlite.org/index.html) - used as the database whilst in development.
- [PostgreSQL](https://www.postgresql.org/) - used as the database when the site is deployed. 
- [Stripe](https://stripe.com/gb) - used to handle payment feature on the site. 
- [GitPod](https://gitpod.io/) - IDE used.
- [GitHub](https://github.com/) - used to house the repository.
- [Heroku](https://id.heroku.com/) - used for deploying the website.
- [FontAwesome](https://fontawesome.com/) - used to import icons.
- [Google Fonts](https://fonts.google.com/) - used to import fonts.
- [Balsamiq](https://balsamiq.com/) - used to build wireframes.
- [Tiny JPG](https://tinyjpg.com/) - used to compress images.


# Testing
# Deployment
# Credits




