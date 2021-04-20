![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

<p align="center"> 
<img src="https://github.com/Gazroh87/mighty_machine/blob/master/static/images/mighty-machine-logo.png">
</p>


# ReadMe

Link to view the website - htts://

I'm building an E-commerce website for selling PC components/accessories and is called Mighty Machine. 
Users can browse through different products and will be able to purchase them using Stripe. Initially the website 
will stock a limited number of categories of products but the plan is to expand upon the number down the line.

The website will have a login page that will direct them to the main store front where they will be able to browse 
through all the products or select from different categories. Once a user adds their product(s) to the cart, then 
they will be able to purchase them by entering in shipping and payment details. The user will also be able to view 
their purchase history linked to their username. If the customer currently does not have an account then they will 
be able to create one. When they create an account, they will also be able to change their email address, password 
and other details related to their account.


# UX


# User Stories
## Customer
### Products
*	I want to see the full range of your products, and be able to purchase one or quickly change how many I have put 
in my shopping cart.
*	I want to be able to view an individual product and find out more details about that product.
*	I want to be able to see at all times, how much my current cart total is so I can see how much I am spending on 
products.
*	I want to be able to see the different categories and be able to sort through them without having to see all the 
products I might not be interested in.
*	I want to be able to search for a specific product to see if it is available for purchase on the website.
*	(FUTURE) I want to see if the product(s) I want is in stock so I know they are available to purchase.

### Purchasing
*	Once I have selected the items I want to buy and added them to the cart I want a notification with them shown 
added to my cart.
*	I want to be able to be able to change the items in my cart e.g. change quantity of an item or remove it.
*	I want to be able to enter my payment details for the products as quickly and as easily as possible.
*	I want to be sure that my payment information is secure before confirming my payment details at the checkout.
*	I want a confirmation of my order on the site before confirming just to double check that I have not made any 
mistakes.
*	I then want an email confirmation so I know that you have received the order correctly and are processing it.

## User
*	I want to be able to easily create an account and be able to see the profile that I have created.
*	I want to be able to login easily to view my account and be able to logout easily when I want to leave the 
website.
*	I want to be able to recover my password in case I forget and be able to change if and when I wish to do so.
*	I want to able to easily access my account so I can see my details, order history etc.
*	I want to receive an email confirmation once I have registered to let me know that I created an account 
successfully.

## Admin
*	I want to be able to add a new product on the site.
*	I want to be able to edit or update an existing product on the site.
*	I want to be able to delete and remove a product which I no longer want users to be able to purchase.


# Features
## Existing Features


## Future features to implement


## Technologies Used
* I have used HTML, CSS, JavaScript and Python programming languages.
* I used Gitpod (https://gitpod.io/) to build the website.
* I used Django as I wanted to utilise a python based web framework for this project.
* I used Django-Allauth (https://django-allauth.readthedocs.io/en/latest/installation.html) for the authentication system of the project as it has the security features I require.
* I used Django Crispy Forms to helps to manage the forms and able adjust forms properties in the backend.
* I used Django Countries which was used for the country field for user to be able to selct the contry they are from.
* I used Stripe to set up the payment methods for the site allowing customers to pay by online card transactions.
* I used Bootstrap for its mobile-first, responsive and simplistic layouts.
* I used Pillow to be able to use the image field for the products on the site.
* I used JQuery (https://jquery.com/) to decrease the amount of JavaScript code in the project.
* I used Font Awesome (https://fontawesome.com) to add the icons used in the site.
* Block templates were used so I don’t have to repeat my code to save time.


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