# Quahog City Council Bulletin Board  

## The Online Bulletin Board of the fictional city of Quahog                                          

The aim with the project is to create a full stack site that allows users to Create, Edit, Read and Delete data in a way that's easily manageable for all users as well as giving them a great user experience.

Please see the link to the live page below:

https://quahog-bulletin.herokuapp.com/


## UX

### Project goals 

The purpose of the project is to create an online platform for the citizens as well as the council (admin) of the fictional city of Quahog to create posts in certain categories- much like they would on a real-life bulletin board. 

This way the registered user can easily get involved in and contribute to the life of their community. They can look for updates from the local council; they can post ads and invitations to events, clubs, goups and so on. They can offer and ask for help and put their possessions up for sale.

Unregistered users can still view the post but the site doesn't allow them to create their own posts or to save them for later.

### User stories

As a user I want to create new posts in different categories

As a user I want to upload photos to my posts.

As a user I want to be able to edit or delete my posts.

As a user I want to see announcements created by the city council.

As a user I want to see what other users posted in each category.

As a user I want to be able to save posts that I find interesting and view them in my profile page.

As a user I want to see who created each post.

As a user who has admin rights I want to be able to add a new category if needed.

As a user who is in a hurry I want to be able to filter the posts in each category for certain keywords.

As a user who is not a resident would like to see what's going on in the city anyway.

As a user who would like to get in touch with the Council directly I am interested in the contact details of the City hall.

### Design

### Wireframes

There are some differences between the wireframes I created initially and the completed project, because sometimes I found a better way to execute the initial ideas during development.

**Homepage**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Index.png" width="400">   <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Index_mobile.png" width="200">   <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/mobile_menu.png" width="200">


**Login**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Login.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Login_mobile.png" width="200">

**Register**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/registration.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/register_mobile.png" width="200">

**Profile**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Profile.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Profile_mobile.png" width="200"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Admin_profile.png" width="400">

**Boards (Categories)**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Boards_Categories.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Boards_mobile.png" width="200">
<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Registered-Market.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Registered-Market_mobile.png" width="200">
<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Registered-announcements.png" width="400">


**CRUD**

**Create post**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Create_post.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Create_post_mobile.png" width="200">

**View post**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/registered-view_post.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/registered-view_post_mobile.png" width="200">

**Edit post**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Edit_post.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Edit_post_mobile.png" width="200">

**Delete post**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Delete_post.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Delete_post_mobile.png" width="200">

**Admin functions**

<img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Admin_Announcement.png" width="400"> <img src="https://github.com/KittiKovacs/Quahog_Bulletin-MS3/blob/master/static/wireframes/Admin_new_board.png" width="400">


## Features

### Existing Features

#### On all pages:

- Navigation Bar: I have created the navigation bar using Materialize Nav bar with Icon Links and I have also included the Mobile Collapse Button. I added a dropdown option to one of the menu items.

- Page title: The page title appears will in the navigation bar on the right throughout the entire website and acts as a link to the home page when clicked.

- Mobile Collapse Button / Sidebar: The Mobile Collapse Button will appear on medium and small screens and shows the side navigation bar.

- Tooltips: Materialize tooltips show up to give the user further explanation on the purpose of certain fields in the registration form and buttons.

- Footer: from Materialize to include the contact details for the City Hall and copyright information.


#### Login

- Contains an input form where the users can enter their username and password.

- Flash message appears if the username is not valid or if the password is incorrect.

- "Register here" link below the form to get redirected to the registration page.


#### Register

- The app is accessible for read only to anyone, registered users have access to more functions such as creating, editing, saving and deleting posts. 

- Contains an input form where the user can enter their details and choose a username and password. A tooltip over each line gives the user helpful tips.

- Flash message appears if the chosen username is already in the database.

- In order to store the passwords securely in MongoDB, the passwords have been hashed.


#### Profile

- After successful login, the user is greeted by a flash message.

- The User's profile page is divided into 2 sections: the top section contains all posts created by the user, the bottom section contains posts created by other users that the current user saved for easier access.

- The User has permission to edit or delete their own posts from here and also to remove posts from the saved section.



#### Boards

- This page has been created to display all categories and to give an idea to the user what each category entails. 

- The content is displayed on cards, each of which has a link on the bottom to the page containing posts within each category.

- Admin is able to add a new category (AKA Board).


#### Categories

- This page has been created to display all posts in each category.

- The truncated content of the post is displayed on the cards, each of which has a link on the bottom that takes the user to a separate page where they can view the full details of each post.

- There is a floating action button in the top left corner of each card which reveals some icons. If someone else created the post, the user can save it into their own collection of posts on their profile page. If the user created the post, the user is able to edit or delete the post by simply clicking on the relevant button which appears on mouse hover.


#### Creating Posts

- The user first selects a category for the post. They can choose from all categories except Announcements which is reserved for Admin.

- The user can give a description, add contact details (name, phone number, address website etc.) if they wish.

- The user can upload a photo to their post by which will be saved in the database as well.

- The new post is created when the User clicks the Save button. The app displays a flash message to let the user know that the post has been created.


#### Updating Posts

- The user can select any post that they created. They are taken to the Edit post page.

- The user can change every input field or upload a different image. 

- The post is updated when the User clicks the Done button. The app displays a flash message to let the user know that the post has been updated.


#### Deleting Posts

- The user can delete any post that they created. 

- The delete icon appears when they hover over the Floating Action Button.

- The app displays a flash message to let the user know that the post has been deleted.


#### Admin

- Admin user is able to create posts on the Announcements page. They don't have access to any other options from the dropdown list.

- They are also able to create, edit or delete categories as well as posts. There is an additional menu item available for Admin only named Create Board that serves this purpose.


### Features left to implement

- Allow users to upload multiple images to each posts.

- Add a comment section whereby the users can have a conversation with each other.

## Information architecture

### Database Choice

### Data modelling

![Schema](static/schema/Schema_MS3.JPG)

## Technologies Used

### Languages

- HTML5 

- CSS3 

- JavaScript

- Python3

- Jinja templating language

### Libraries and frameworks

- Flask framework

- Materialize style library

### Tools

- Balsamiq for creating wireframes

- Font Awesome

- Google Fonts

- Icons 8 for certain icons

### Databases

- MongoDB Atlas



## Testing

### Testing in different browsers

I used Google Chrome throughout the development. The app has been tested and works well on Firefox and Microsoft Edge.


### Testing against the user stories

As user 1 I am able to create new posts in different categories from my profile or the category's page.

As user 2 I am able to upload a photo to my post from my computer when creating or editing the post.

As user 3 I can edit or delete my posts.

As user 4 I can see announcements created by the city council by clicking on the relevant link on the Boards page.

As user 5 I can to see what other users posted in each category by selecting the relevant category's page.

As user 6 I can save other users' posts by moving my mouse over the floating action button and clicking on the save icon. They are displayed in my profile page from where I can remove them

As user 7 I can see who created each post just by looking at each card or if clicking on view post.

As Admin I can create a new category from the Boards page.

As user 9 who is in a hurry I can use the search field on the categor's page to filter the posts for certain keywords.

As  user 10 who is not a resident I am allowed see what's going on in the city without logging in.

As user 11 who would like to get in touch with the Council directly I can find the contact details and opening hours in the footer of each page.


### Validation

I used https://validator.w3.org/ to validate the HTML code.

I used https://jigsaw.w3.org/css-validator/ to validate the CSS code.

I used https://jshint.com/  to check the JavaScript code.

### Problems encountered

Image upload
Saving posts
Categories page

## Deployment

### Local deployment

I have used Gitpod to develop the app, more specifically I used Code Institute's Gitpod full template as my basis.

I have used Gitpod to track changes in the website by making regular commits with descriptive titles and pushed them to my GitHub repository.

### Heroku deployment

The project is deployed to Heroku. https://quahog-bulletin.herokuapp.com/ . In order to do this I closely followed the tutorial videos on Heroku which are part of the course.

1. First I created a new app in Heroku called quahog-bulletin. 

2. I created my repository on GitHub. I installed Heroku in my project by using the Heroku CLI in the terminal and logged into Heroku. 

3. I created requirements.txt and Procfile that Heroku requires to run the app:

  pip3 freeze -- local > requirements.txt

  echo web: python app.py > Procfile
  
  I pushed both files to GitHub then enabled automatic deploys to the master branch.
 
4. I connected Git remote to Heroku and pushed everything to Heroku master: git push -u heroku master

5. Within my repository I've created an env.py file that contains my environmental variables. I added env.py to gitignore file along with __pycache__/

6. In the  Heroku app's settings (Config Vars) I've added my environmental variables for the IP, PORT, MONGODB_URI and SECRET_KEY

7. Now the automatic deployment is set up I removed Heroku remote on Github: git remote rm heroku.


## Credits

### Code

### Content and Media

The user's names and images are from the following website: https://familyguy.fandom.com/wiki/Family_Guy:_The_Top_20_Characters



## Acknowledgements

Many thanks to my Mentor Guido Cecilio Garcia Bernal for offering guidance and constructive crticism.
Similarly, the Tutors at Code Institue were a big help when I got stuck in the process.

## Disclaimer 

The page has been created for educational purpose, not for commercial use. 



### Acknowledgements
