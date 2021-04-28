# [Mighty Machine](https://gazroh87-mighty-machine.herokuapp.com/)
## PC Parts E-Commerce Web App

![Mighty Machine Logo](https://github.com/Gazroh87/mighty_machine/blob/master/static/images/mighty-machine-logo.png)

![readmeheroimg](readme_files/images/mm-hero-img.png)

View the live website [here](https://gazroh87-mighty-machine.herokuapp.com/)

## Code Institute - Final Milestone Project 4 - Full Stack Frameworks with Django

*Note: My project builds upon large portions of the code sourced from Code Institute's Django [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) 
project tutorials.*

***

# I N T R O

I've built an E-commerce website for selling PC components/accessories. The reason for choosing the name 
'Mighty Machine' comes from the idea that if someone or something, such as a computer built for a primary purpose 
such as gaming, has a combination of both great power and speed or some other similar attribute(s), it can be called 
mighty, and a user of my website can purchase everything they need to build a 'Mighty Machine' for such purpose from 
my website. Users can 

This application is primarily aimed towards custom PC builders, gamers, tech nerds and video editors and anyone else 
who might require a powerful computer to build themselves or have someone build for them. The overall modern styling 
mixed with tech/scifi font and imagery helps to increase appeal.

The primary aim of this application was to allow users (registered or unregistered) to purchase products, from 
landing on the homepage, to successfully completing a purchase. Registered users are also able to review any product 
available for purchase on the website for others to see. I chose to develop an E-Commerce shop as it is in someways a 
fairly complex but highly flexible application to challenge my understanding, and build upon my knowledge along the 
way, of the technologies involved. Because of the sensitivity surrounding the handling of customer details, a great 
deal of security consciosnous is required during the development of an application like this. 

Users can register an account and change their email address, password and other details relating to their account. 
The website has a login page that directs the user to the main store front where they can browse through different 
categories of products. Once a user adds their product(s) to the cart they can then proceed to the checkout, enter in 
their delivery information and purchase their products using the Stripe online payment method. At the moment the 
website stocks a limited variety of categories of products but in future the store has the potential to grow much 
larger and the inventory be greatly expanded upon. A logged in user can view their order history of purchases, directly 
linked to their username.

The store admin(s) will spend most of their time adding, editing and deleting products and categories among other 
typical activities through the [Django admin](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/) backend site,
but they can also do some of the basic tasks through the website's own frontend UI.

## Testing Purchases

*Note: If you wish to try out the app right away and test the purchasing, for ease of use, you do not need 
to register an account on the website.*

Under 'Pay Method'...

Enter:

* 4242 4242 4242 4242 as the **Card number**
* 04/24 as the **expiration date (MM/YY)**
* 424 as the **CVC**
* 42424 as the **ZIP**

***

# U X (User Experience)

* Does this fit my user's needs?
* Does the user like my website?
* Does the user like being at my website?
* Is this a website a user might want to return to in the future?

These are all questions I asked myself throughout the UX design process.

## User Goals and Expectations

### Customer

#### Products

*	I want to see the full range of your products, and be able to purchase one or quickly change how many I have put 
in my shopping cart.
*	I want to be able to view an individual product and find out more details about that product.
*	I want to be able to see at all times, how much my current cart total is so I can see how much I am spending on 
products.
*	I want to be able to see the different categories and be able to sort through them without having to see all the 
products I might not be interested in.
*	I want to be able to search for a specific product to see if it is available for purchase on the website.
*	(FUTURE) I want to see if the product(s) I want is in stock so I know they are available to purchase.

#### Purchasing

*	Once I have selected the items I want to buy and added them to the cart I want a notification with them shown 
added to my cart.
*	I want to be able to be able to change the items in my cart e.g. change quantity of an item or remove it.
*	I want to be able to enter my payment details for the products as quickly and as easily as possible.
*	I want to be sure that my payment information is secure before confirming my payment details at the checkout.
*	I want a confirmation of my order on the site before confirming just to double check that I have not made any 
mistakes.
*	I then want an email confirmation so I know that you have received the order correctly and are processing it.
*   I want to be able to make a purchase wihtout needing to create an account.

### User

*	I want to be able to easily create an account and be able to see the profile that I have created.
*	I want to be able to login easily to view my account and be able to logout easily when I want to leave the 
website.
*	I want to be able to recover my password in case I forget and be able to change if and when I wish to do so.
*	I want to able to easily access my account so I can see my details, order history etc.
*	I want to receive an email confirmation once I have registered to let me know that I created an account 
successfully.

### Admin

*	I want to be able to add a new product on the site.
*	I want to be able to edit or update an existing product on the site.
*	I want to be able to delete and remove a product which I no longer want users to be able to purchase.
*   I want the ability to limit the creation, editing and deletion of products to the superuser(s) with admin access.

## Design Choices

### Colour Scheme

![#000](https://via.placeholder.com/15/000000/000000?text=+) `#000`
![#100080](https://via.placeholder.com/15/100080/000000?text=+) `#100080`
![#2000ff](https://via.placeholder.com/15/2000ff/000000?text=+) `#2000ff`
![#555](https://via.placeholder.com/15/555555/000000?text=+) `#555`
![#fff](https://via.placeholder.com/15/ffffff/000000?text=+) `#fff`
![#198754](https://via.placeholder.com/15/198754/000000?text=+) `#198754`
![#212529](https://via.placeholder.com/15/212529/000000?text=+) `#212529`
![#6c757d](https://via.placeholder.com/15/6c757d/000000?text=+) `#6c757d`
![#dc3545](https://via.placeholder.com/15/dc3545/000000?text=+) `#dc3545`
![#e9ecef](https://via.placeholder.com/15/e9ecef/000000?text=+) `#e9ecef`
![#ffc107](https://via.placeholder.com/15/ffc107/000000?text=+) `#ffc107`

The website is heavily reliant on [Bootstrap v5 theme colors.](https://getbootstrap.com/docs/5.0/customize/color/)

White, black and dark shades of blue are the primary colours used for the web app's frontend.

Examples of colour usage:

#### White
* Background
* General buttons
#### Black
* Majority of text
* General buttons
#### Dark shades of blue
* Delivery banner
* Shop Now button hover/active/focus states
* Update links
* Breadcrumbs
#### Secondary
#### Success
* Buttons for adding product(s) to the shopping cart
* Success toasts
#### Danger
* Removing/deleting
* Error toasts
#### Warning
* Edit buttons
#### Dark (off black)

### Typography

* My website uses two fonts from the [Google Fonts](https://fonts.google.com/) library called Iceland and Roboto.
* 'Iceland' is used for most headings, some nav links and as part of the logo design. Roboto is used for all other 
text.
* These fonts are imported via the head element of the base HTML file.
* Sans-serif is the fallback font if for some reason the above fonts can't be imported into the site correctly.
* Both fonts are very popular in the developer world and are also easy enough to read, so they are both attractive 
and appropriate.


## Strategy

The focus of this project is on using the knowledge I have learned of Python and Django to build a responsive 
application, in this case, PC Parts E-Commerce web app to demonstrate to anyone my capabilities in Python and Django 
alongside HTML5 and CSS3, and jQuery/JavaScript.

## Scope

My website's main target users are custom PC builders, gamers, tech nerds and video editors and anyone else 
who might require a powerful computer to build themselves or have someone build for them. 

The scope of this app is to provide a place where anyone, on as many different devices/screen sizes as possible, 
can purchase products and share their honest opinions and experiences with their purchases by posting their own 
product reviews.

My app caters to the basic needs of an administrator by including a variety of tools in order to moderate user 
posted reviews and provide updates to the website with more categories of products to browse through and more 
products to purchase.

I bucket my features into separate lists by priority:

1. 'Will Do' features had to be completed by my given submission deadline for this project. These have one or both of 
the following characteristics: 
    * Upper bound: Meet the requirements of a project based on the project specifications. 
    * Lower bound: Show as much prowess in course material as possible. Show that I can use the different facets of 
    each language (HTML/CSS/JS/Python).
2. 'Stretch Goals' are features to try to implement if I had time left at the end of the project. These should be relatively quick and easy to implement but only if the above features have been completed.
3. 'Won't Do' features are features I won't get done before the project deadline but are features I may want to work on in the future and include in future updates.

### Planned Features

* Fully responsive design - The website should function appropriately across mobile, tablet and desktop devices and 
screen sizes.
* The website should provide suitable mobile and desktop navigation which are simple enough and easy to use.
* The website should provide a searching function for users to find the product(s) they are looking for.
* Website information should be clearly layout from the moment a user lands on the homepage.
* The web app should provide functions to add, edit and delete categories and products.
* The products page should utilise some form of standardised E-Commerce feeding of products to the user and allow 
them to sort and filter products.
* Users should be able to add products to their cart as soon as they see it listed on the products page.
* Registered and logged in users should have the added benefit of being able to post a review for a product on the 
website.
* To maintain an accurate and up to date database, only the superuser(s) can perform CRUD operations on categories 
and products etc.
* The website should provide clear links on well structured pages for increased usability.

## Structure

* When the user lands on the homepage, it will be met with a slideshow of attractive imagery behind text invoking 
the websites purpose.
* A user friendly interface to further increase usability and help encourage users to 
return to the website.
* The navigation bar is always fixed to the top of the viewport and is fully responsive in adjusting itself for 
tablet and mobile users.
* Responsive links which change appearance when hovered over, providing the user with feedback as they navigate 
around the website.
* The products page follows a similar layout to the majority of other E-Commerce shops. The default products page 
includes all available products from every category. Each product is represented as a card with an image of the 
whole product, the product name including brand, a short description, a rating and price.
* If a user wants to view a product, they can find a bit more information.
* If a user adds a product to their cart, they will receive a toast pop-up message, towards the top right of the 
viewport under the cart button in the nav, informing them that they have added 'x' amount of product, and if they 
selected a product in a certain colour, it will tell them in which colour they have added the product into their 
cart.
* On the cart page, users can see all the products they have added including the optional colour they might have 
selected and they can modify the quantities.
* Once a user has proceeded to the checkout, they will be presented with a form to fill out in order to complete 
their checkout. Once the user has completed this, the order will be stored in their order history of their account, 
for them to view at any time.
* I have provided users with the ability to exit pop-ups as soon as they appear via a close button.
* Images are responsive to the device screen size.
* I have provided users with breadcrumbs for them to quickly to steps back in the website without clicking a browser's
back button.
* Every time a user submits some information or an action including registering, logging in/out, interacting with 
product quantities, the cart, or completing a transaction, they are notified by a toast pop-up message that describes 
the result of the action that has just taken place.

## Skeleton

### Wireframes

#### Mobile

[Home/Index]()  |
[Products]() |
[Product Details]() |
[Shopping Cart]() |
[Checkout]() |
[Order confirmation]() |
[Registration]() |
[Login/logout]() |
[Profile]() |

#### Tablet

[Home/Index]() |
[Products]() |
[Product Details]() |
[Shopping Cart]() |
[Checkout]() |
[Order confirmation]() |
[Registration]() |
[Login/logout]() |
[Profile]() |

#### Desktop

[Home/Index]() |
[Products]() |
[Product Details]() |
[Shopping Cart]() |
[Checkout]() |
[Order confirmation]() |
[Registration]() |
[Login/logout]() |
[Profile]() |

***

# F E A T U R E S

## Current Features

There are currently and as a required, a minimum of 3 usertypes for my project to function as it should:
- Superuser(s) / site administrator(s)
- Registered users
- Unregistered users

For all users the user experience is going to be much the same, although, there are some extra features/benefits 
available to registered users and superusers, with superusers having all the extra admin functionality restricted 
to themselves.

Web App Section | Feature | Description
----------------|---------|------------
Top Navigation bar | Fixed navigation bar | Visible across every page and on any device screen size. On smaller widths, it transforms into a hamburger menu. This navigation area includes the website logo, search bar and sets of links for each section/subsection of the website.
Homepage | Slideshow | 5 colourful images of inspirational media including products that can be puchased from the website are animated using a slow fade in and out effect.
Homepage | Jumbotron | The website logo and a brief summary of the kind of products the store sells. The message "The latest tech has arrived..." tells the user that the store is up to date and that they don't have to go anywhere else to find the latest PC Parts available. Below this is the "Shop Now" button, that when clicked on will direct the user to the products page.
Footer | Fixed Footer |  Every page contains the same footer with a shop link to the products page, copyright information and social media links.
Products page | Standard E-Commerce feed of products | Options to sort and filter products by name and price. Each product can be added to the shopping cart immediately and links to an individual product detail page.
Product detail page | Product details | Consists of an image of the product, name, description, rating, price and add to cart button.
Product detail page | Quantity selector | Allows users to increase and decrease the quantity of a product they are thinking of adding to their cart. The minus button decrements the value in steps of 1, while the plus button increments the value in steps of 1.
Shopping cart page | Shopping cart | Consists of product info and images of items currently in the cart along with prices, quantities, colours and sub totals. If a user changes their mind about the quantity of a product, they can update this or remove them entirely.
Checkout page | Details form | User enters their personal details including full name and e-mail address.
Checkout page | Delivery form | User enters their delivery details for their order to be sent to the correct address.
Checkout page | Payment form | User enters their card details. If the user enters incorrect card information, they will be notified that the form is invalid.
Checkout page | Order summary | Details of the order the user is about to purchase. Displays image(s), name(s), quantity, sub totals, order total, delivery charge and grand total.
Order confirmation page | Order confirmation | Below the heading, the user will receive a message letting them know that their order has been confirmed and that they will receive an e-mail confirmation aswell. The confirmations contain the unique order number and the date and time of the transaction. Below this is all the order details including the products, delivery and billing info.
User account | Order history | User accounts are only available to registered/super users who are currently logged in. Users can track their order history at any time.
User account | Shipping details | Users can safely store and view their current delivery details at any time for a faster checkout process.

Other:

Feature | Description
--------|------------
Registration | User registration with link to sign in if user already has an account otherwise the user must fill out the form to create an account.
Logging in | Users can log in to their account or click a button to register for an account if they have not already done so.
Logging out | Users can log out of their account.
Password reset | Users can reset their password by entering their associated e-mail address.

## Django Apps

Mighty Machine is a [Django project](https://docs.djangoproject.com/en/3.1/ref/applications/), consisting of 5 Django 
applications listed below:...

- **Home**
- **Products**
- **Cart**
- **Checkout**
- **Profiles**

As Django's documentation explains - A Django app describes a Python package that provides some set features. The 
same applications can be reused in other projects.

* TO BE UPDATED IN FUTURE

## Future features/improvements to be implemented

- A feature that provides authenticated users with the ability to save favourited products for later viewing/purchasing.
Each product of the products page could have a heart-shape icon link to save the item to their favourites list 
accessible from their profile page. Users could manually remove the items from their list and tick a box or tick boxes 
for individual products, to say the wanted the item automatically removed from the list if they have purchased the 
item.
- A contact page featuring a form to fill out.
- A feature that makes items stay in a users shopping cart after they have logged out. 
- Coupon codes and discounts for customer loyalty.
- An E-mail newsletter feature. During the registration process, the user has the option to tick a box to receive a 
regular newsletter containing personalized product recommendations, discounts and new products coming soon to the store.

Working on this project has been an incredible journey of learning. I just wish I had more time to implement the above 
features.

***

# Information Architecture

As SQL databases are used by Django by default, I used [SQLite](https://www.sqlite.org/) during development. However, 
Heroku provides a [PostgreSQL](https://www.postgresql.org/) database for the deployed version.

## Database Models

### User Model

The user model used for my project is the standard one provided by Django's 'django.contrib.auth.models'.

### Profiles App

`UserProfile` Model

Name | Database Key | Field Type | Type Validation
-----|--------------|------------|----------------
User | user | = models.OneToOneField 'User' | (User, on_delete=models.CASCADE)
Default Phone Number | default_phone_number | = models.CharField | (max_length=20, null=True, blank=True)
Default Street Address1 | default_street_address1 | = models.CharField | (max_length=80, null=True, blank=True)
Default Street Address2 | default_street_address2 | = models.CharField | (max_length=80, null=True, blank=True)
Default Town or City | default_town_or_city | = models.CharField | (max_length=40, null=True, blank=True)
Default County | default_county | = models.CharField | (max_length=80, null=True, blank=True)
Default Postcode | default_postcode | = models.CharField | (max_length=20, null=True, blank=True)
Default Country | default_country | = CountryField | (blank_label='Select Country', null=True, blank=True)

### Products App

`Category` Model

Name | Database Key | Field Type | Type Validation
-----|--------------|------------|----------------
Category id | id | primary_key=True | AutoField
Name | name | = models.CharField | (max_length=254)
Friendly Name | friendly_name | = models.CharField| (max_length=254, null=True, blank=True)

`Product` Model

Name | Database Key | Field Type | Type Validation
-----|--------------|------------|----------------
Product id | id | primary_key=True | AutoField
Category | category | = models.ForeignKey | ('Category', null=True, blank=True, on_delete=models.SET_NULL)
SKU | sku | = models.CharField | (max_length=12)
Brand | brand | = models.CharField | (max_length=254)
Part Name | part_name | = models.CharField | (max_length=254)
Description | description | = models.TextField | ()
Has Colours | has_colours | = models.BooleanField | (default=False, null=True, blank=True)
Price | price | = models.DecimalField | (max_digits=7, decimal_places=2)
Rating | rating | = models.DecimalField | (max_digits=3, decimal_places=2, null=True, blank=True)
Image | image | = models.ImageField | (null=True, blank=True)
Part Type | part_type | = models.CharField | (max_length=254)

`Review` Model

Name | Database Key | Field Type | Type Validation
-----|--------------|------------|----------------
Product | product | = models.ForeignKey | ('Product', null=True, blank=True, on_delete=models.CASCADE)
User | user | = models.ForeignKey | (User, on_delete=models.CASCADE)
Title | title | = models.CharField | (max_length=50, blank=True)
Review | review | = models.TextField | (max_length=1000, blank=True)
Rating | rating | = models.IntegerField | (default=1, choices=RATING)
Posted on | post_on | = models.DateTimeField | (auto_now_add=True)
Updated on | update_on | = models.DateTimeField | (auto_now=True)

### Checkout App

`Order` Model

Name | Database Key | Field Type | Type Validation
-----|--------------|------------|----------------
Order Number | order_number | = models.CharField | (max_length=32, null=False, editable=False)
User Profile | user_profile | = models.ForeignKey | (UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
Full Name | full_name | = models.CharField | (max_length=50, null=False, blank=False)
E-mail | email | = models.EmailField | (max_length=254, null=False, blank=False)
Phone Number | phone_number | = models.CharField | (max_length=20, null=False, blank=False)
Country | country | = CountryField | (blank_label='Select Country', null=False, blank=False)
Postcode | postcode | = models.CharField | (max_length=20, null=True, blank=True)
Town or City | town_or_city | = models.CharField | (max_length=40, null=False, blank=False)
Street Address1 | street_address1 | = models.CharField | (max_length=80, null=True, blank=True)
Street Address2 | street_address2 | = models.CharField | (max_length=80, null=True, blank=True)
County | county | = models.CharField | (max_length=80, null=True, blank=True)
Date | date | = models.DateTimeField | (auto_now_add=True)
Delivery Cost | delivery_cost | = models.DecimalField | (max_digits=6, decimal_places=2, null=False, default=0)
Order Total | order_total | = models.DecimalField | (max_digits=10, decimal_places=2, null=False, default=0)
Grand Total | grand_total | = models.DecimalField | (max_digits=10, decimal_places=2, null=False, default=0)
Original Cart | original_cart | = models.TextField | (null=False, blank=False, default='')
Stripe PID | stripe_pid | = models.CharField | (max_length=254, null=False, blank=False, default='')

`OrderLineItem` Model

Name | Database Key | Field Type | Type Validation
-----|--------------|------------|----------------
Order | order | = models.ForeignKey | (Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
Product | product | = models.ForeignKey | (Product, null=False, blank=False, on_delete=models.CASCADE)
Product Colour | product_colour | = models.CharField | (max_length=99, null=True, blank=True)
Quantity | quantity | = models.IntegerField | (null=False, blank=False, default=0)
Line Item Total ! lineitem_total | = models.DecimalField | (max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

### Security

Using configuration variables in Heroku, all SECRET keys are stored safely to prevent unauthorized connections to 
the database. I've incorporated Django Allauth to setup user registratiom and built-in decorators enforce restricted 
access to certain functionalities of my website which are not intended for regular users.

***

# Technologies Used

## Programming languages

* [HTML5](https://www.w3.org/) - I used HTML to build the basic layout of the website.
* [CSS3](https://www.w3.org/) - I used CSS to style and format the website's HTML elements.
* [JavaScript](https://www.javascript.com/) - My project uses JavaScript for the implementation of custom JS, Stripe and EmailJS. This enhances user experience by adding functionality and interactivity to the website.
* [Python](https://www.python.org/) - Handles data provided by the database. Backend functions are written in Python.

## Libraries

* [Font Awesome](https://fontawesome.com) - Font Awesome was used to provide the icons throughout the website for aesthetic and UX design purposes. Icons give the user additional context from the first glance.
* [Google Fonts](https://fonts.google.com/) - Google Fonts were used to embed and link the 'Iceland' and 'Roboto' fonts into the HTML. It was pointless importing them into the CSS file as the base.html file extends all other HTML files with the required head tags.
* [jQuery](https://jquery.com/) - jQuery is a JavaScript library that comes as part of the Bootstrap framework. It is designed to simplify HTML DOM tree traversal and manipulation. 
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja handles the frontend display of data provided by the backend database in addition to HTML code.

## Frameworks / Extensions

* [Bootstrap 5](https://getbootstrap.com/) - Bootstrap provides mobile-first, responsive and simplistic layouts. Bootstrap was used to assist with some of the structuring and responsiveness of the website and build off of or modify some of its existing components and styling to save time.
* [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - I used Django-Allauth for the authentication system of the project as it has the security features I require.
* [EmailJS](https://www.emailjs.com/) - Sends E-mails using only client-side technology. This was used for testing E-mails. It only requires to connect EmailJS to one of the supported email services, create an email template, and use their Javascript library to trigger an email.
* [Stripe](https://stripe.com/ie) - Allows users to make and receive payments over the Internet. This helps manage test transactions.

## Database

* [SQLite](https://www.sqlite.org/) - Django's default database type used during development.
* [PostgreSQL](https://www.heroku.com/postgres/) - PostgreSQL is one of the world's most popular relational database management systems.


## Tools, Editors, Version Control etc.

* [GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git. GitHub is used to store the project's code within a repository including all previous versions or commits of the project after being pushed from Gitpod and can be used to host the deployed website for public viewing.
* [Git](https://git-scm.com/) - Git was used for version control by utilizing the Gitpod IDE terminal to commit files to Git and push them to GitHub.
* [Gitpod](https://gitpod.io/) - Gitpod was the primary development tool for the building and maintenance of the website.
* [Balsamiq Wireframes]() - I used the Balsamiq Wireframes desktop application to create all my wireframes during the design process.
* [Pip](https://pip.pypa.io/en/stable/) - Pip is the software package installer/manager for Python.
* [Django Crispy forms]() - I used Django Crispy Forms to helps to manage the forms and able adjust forms properties in the backend.
* [Django Countries]() - I used Django Countries which was used for the country field for user to be able to selct the contry they are from.
* [Google Chrome DevTools]() - The Chrome DevTools were used throughout the building, testing and debugging of the website to quickly see the result of any changes made to any code via visualization in a live browser tab and/or the developer console.
* [Heroku](https://dashboard.heroku.com/) - Heroku is a cloud platform that lets companies and individuals build, deliver, monitor and scale apps. This is where the web application is deployed.
* [Amazon Web Services S3](https://aws.amazon.com/s3/) - Object storage service that offers industry-leading scalability, data availability, security, and performance. This is used to host the project's media and static files.
* Tiny [jpg](https://tinyjpg.com/)/[png](https://tinypng.com/) - These websites were used to compress the images used throughout the project to reduce data size, decreasing load times without sacrificing the integrity or quality of the original images.
* [Favicon Converter](https://favicon.io/) - This Favicon converter was used to create the favicon based on my brand logo, to be displayed on the browser tab and bookmarks bar.
* [Autoprefixer CSS](https://autoprefixer.github.io/) - Autoprefixer was used to help with making the CSS code compatible and valid for all internet browsers as much as possible by fixing cross-browser CSS issues.
* [Grammarly](https://www.grammarly.com/) - Grammarly is used for checking for and and helping to eliminate spelling and grammatical errors.

You can find any other technologies not listed here that were used in this project in my [requirements.txt](https://github.com/Gazroh87/mighty_machine/blob/master/requirements.txt) file.

***

# T E S T I N G

My process of testing includes:

My process of testing includes:

- Testing my user stories as set out in the UX section.
- Validating all custom HTML, CSS and JavaScript files.
- Reviewing website compatibility on different browsers and devices.
- Reviewing design responsiveness from custom mobile screen sizes of 320 x 480px to desktop 4K resolutions in DevTools.
- Making sure all links function correctly.
- Getting my partner to review my website at different developmental stages and the completed product across multiple
  device sizes for feedback and to point out any obvious bugs or issues with her experience.

My website is to be tested on the latest popular web browsers including:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Apple Safari
- Microsoft Internet Explorer
- Amazon Silk

I've used the following physical devices for development and testing:

- AMD Ryzen 7 2700X PC running Windows 10, Chrome, Firefox and Edge browsers on two monitors; 1920x1200px and 2560x1440px natively.
- Apple iPhone 6S and SE running Safari browser.
- Laptop running Chrome, Internet Explorer and Edge browsers.
- Amazon Fire HD tablet running Silk browser.

The following validators were used to validate all of the HTML, CSS and JavaScript files that make up this project, to
ensure there are no syntax errors in the project code.

- HTML - [W3C Markup Validation Service](https://validator.w3.org/) - No errors.
- CSS - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - No errors.
- JavaScript - [JSHint Validator](https://jshint.com/) - No errors.
- Python - [PEP8 online](http://pep8online.com/) - All right.

## User Story Tests

### Customer

#### Products

*	I want to see the full range of your products, and be able to purchase one or quickly change how many I have put in my shopping cart.
    - Upon entering the shop, the user can naviaget to view all of the products by clicking on the 'All Products' 
    menu link in the navigation bar and in dropdowns, select 'All Products'. Optionally the user can sort and filter 
    products by name, price, rating, category etc.

*	I want to be able to view an individual product and find out more details about that product.
    - Every product can direct the user to it's individual product details page with a bit more info available than 
    the products page. Doing this is as simple as clicking on a product's image from the products page.

*	I want to be able to see at all times, how much my current cart total is so I can see how much I am spending on products.
    - Below the shopping cart icon towards the top right of the viewport, the user can see their current cart total. 
    By clicking on this icon, the user can find out more details about the contents of their cart and how much they 
    could end up spending.

*	I want to be able to see the different categories and be able to sort through them without having to see all the products I might not be interested in.
    - In the top navigation bar, the user can navigate through different categories. There are four main categories; 
    Cases, Internal Components (all the main interal parts that make up a computer), Peripherals (currently only 
    keyboards and mice) and Hot Deals which includes new items and clearance items. By clicking on one of these 
    categories the user will see a dropdown menu appear with subcategories of products.

*	I want to be able to search for a specific product to see if it is available for purchase on the website.
    - The user can search for specific product(s) by clicking within the search box and entering what they are looking 
    for. Depending on the result of the search, the user will either be presented with the product(s) they are looking 
    for or no results if there is no match to their query.

*	(FUTURE) I want to see if the product(s) I want is in stock so I know they are available to purchase.

#### Purchasing

*	Once I have selected the items I want to buy and added them to the cart I want a notification with them shown added to my cart.
    - Once the user has added a product to the cart they will receive a brief toast pop-up success message. They can 
    view their cart by clicking on the cart icon and the user can find out more details about the contents of their 
    cart. They user will also know the product has been added to their cart because the cart icon will change colour 
    and show the value of the contents of the cart below the icon. 

*	I want to be able to be able to change the items in my cart e.g. change quantity of an item or remove it.
    - The user can change the items in their cart at the shopping cart page by updating the quantity or clicking the 
    remove button.

*	I want to be able to enter my payment details for the products as quickly and as easily as possible.
    - Once the user is happy with the contents of their cart and have proceeded to the checkout process then they can 
    enter their payment information. The user can enter in their card details and if they have entered the information 
    correctly they won't receive an error message and the transaction will be successful. If the card payment is 
    invalid, they will receive a notification and be asked to try to enter their correct details to process the payment.

*	I want to be sure that my payment information is secure before confirming my payment details at the checkout.
    - Stripe ensures user's payment information is secure.

*	I want a confirmation of my order on the site before confirming just to double check that I have not made any mistakes and that you have received the order and its being processed.
    - Once the user has completed the checkout process they will then be directed to the order confirmation page. 
    This page lists all the information relating to their order including order details, delivery and billing 
    information.

*	I then want an email confirmation so I know that you have received the order correctly and are processing it.
    - On the order confirmation page, they will see that a confirmation E-mail has been sent to their registered 
    E-mail address.

*   I want to be able to make a purchase wihtout needing to create an account.
    - A user can proceed to the checkout and complete a purchase without needing to create an account.

### User

*	I want to be able to easily create an account and be able to see the profile that I have created.


*	I want to be able to login easily to view my account and be able to logout easily when I want to leave the website.


*	I want to be able to recover my password in case I forget and be able to change if and when I wish to do so.


*	I want to able to easily access my account so I can see my details, order history etc.


*	I want to receive an email confirmation once I have registered to let me know that I created an account successfully.

### Admin

*	I want to be able to add a new product on the site.


*	I want to be able to edit or update an existing product on the site.


*	I want to be able to delete and remove a product which I no longer want users to be able to purchase.


*   I want the ability to limit the creation, editing and deletion of products to the superuser(s) with admin access.

## Committing files to GitHub
When I make changes to each file I push them from GitHub from GitPod and below are the steps I do to do this. This is essential as to not losing any of the work I have done.
1.	On my GitPod project scroll down and click on the command prompt at the bottom.
2. Check status by typing in ‘git status’.
3.	Type ‘git add .’ to add all files for staging or 'git add filepath' to add select files by path.
4.	Type ‘git commit -m "Message" to commit the files.
5.	Type ‘git push’ to push the files to GitHub.


## Credits
Product images - 

Product descptions - 

Logo - Was created in 

Code Institte includeing the Boutique Ado project which helped me alot.