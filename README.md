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

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

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
*	I want to see if the product(s) I want is in stock so I know they are available to purchase.

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
*	I want to be able to delete and remove an item which I no longer want on the site.