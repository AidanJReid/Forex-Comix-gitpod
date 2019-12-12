# Forex Comix - The go-to resource for language learning for comic-book lovers

Forex-Comix: Foreign Exchange Comics.

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

---




## UX

![Responsiveness Test](/static/assets/images/wireframe/screencap.JPG)

This is the third milestone project of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies. 
The objective for this project is to "*Create a web platorm to enable the exchange of foreign language comic books*", 
using the **CRUD** operations of **C**reate, **R**ead, **U**pdate, and **D**elete.

It is designed for three types of users (broadly defined as language learners, booksellers and schools/colleges). 
This particular project is underpinned by my own love of learning languages and comic books/graphic novels.
In fact, I spent three years living in Colombia and picked up Spanish quite quickly through the aid of Los Muertos Vivientes (The Walking Dead), 
which accelerated my language skills as well as introduced me to fellow nerds with whom I could practice with.

It is my conviction that language learning can be fun, and with the abundance of comics readily available, 
they can introduce readers to various languages in a way that rote textbooks and stolid boring list tables cannot.


### User Stories

1. **User story 1**: A language learner who wants to improve their proficiency in a specific language.
2. **User story 2**: A bookseller who wants to sell their comic books/raise awareness of their store (digital or physical).
3. **User story 3**: A language school/college that wishes to supply novel language comics to the classroom and curriculum to attract and engage students.
4. **User story 4**: Comic book fans in general who want to read widely.
5. **User story 5**: Comic book fans who want to meet likeminded people and or others from different cultures/countries.

### Design

I wanted to adopt a comic-book style theme with this project. Somewhat 'blocky' to mimic a comic strip layout, and with vibrant colours to make it more fun.

#### Framework

- [Materialize 1.0.0](https://materializecss.com/)
    - Despite instructions to the contrary in a Code Institute video, I decided to adopt the most recent version of Materialize which behaved itself pretty well.
    - Used Parallax theme because it closely resembled my wireframe mockup, had an elegant style and I wanted to try a new CSS framework having previously worked with Bootstrap.
    - A grid layout system was similary used in Materialize although there were a few differences in naming conventions expecially in making content responsive.
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - I used the most recent version of jQuery for my Javascripts framework.
- [Flask 1.1.1](http://flask.pocoo.org/)
    - Flask is a web framework that enable web applications builds which I was determined to use make backend coding easier.

### Wireframes

I used **Balsamiq for desktop** wireframes for two reasons:
- Students have free access to the desktop version until the end of 2019.
- I really enjoyed how simple and easy it is to use for mockups especially in conversations with my assigned mentor for brainstorming.

![forex-comix.png](/static/assets/images/wireframe/forex-comix.png)


## Features

### Existing features

##### Navbar
- Used Materialize's **Parallax Template** for its ease of use and simple design.
- **Sticky navbar** which makes navigation better for the user, especially on mobile.
- Containing navigation items from left to right:
  *  **Logo** - Simple logo which will act as link to home page on smaller devices.
  *  **Home** - Link back to the home page.
  *  **Learner** - Link to learner (students) section of website
  *  **Bookseller** - Link to the Bookseller section of site.
  *  **School** - Link to the School section of site.
  *  **Database** - The place where my comics reside. 
  *  **Add Comic** - Grant users the ability to add comics.

Sidenav pops out on small to medium devices (max-width 992 px) and contain the aforementioned nav links.


##### Parallax
- Two parallexs run across the home page and subsequent user profile sections. Images fit the criteria required by Materialize to render correctly.

##### Images
- The comic explosions and images for Parallaxes were procured from various stock photo sites (references at the bottom).

##### Cards
- Simple grid system allowed me to center align and effectively communicate to the user, the next steps based on their profile of Learner, School or Bookseller.
Their choice is of course dependent on their user profile and interest.

##### Modal
- Displayed with the request for deletion of comic on the comic page.

#### Footer
- Used Parallax theme footer and simply indicated purpose of site, share my Github and linking to Facebook.

## CRUD
**Add Comic**
- [**C**RUD] Add a new comic. Selecting this option in the navbar or at the bottom of the database will lead to a repsonsive form where a user can complete requisite fields.
Changes are updated to MongoDB, and are immediately reflected in the Database section of the site.

**View Comic**
- [C**R**UD] Read/Review comic, either from the database page (display all), filter, or by drilling into the comic in question to find its appropriate page.

**Edit/Update Comic**
- [CR**U**D] Update a comic by clicking the relevant button on the card in the Database section. 
Current values are shown to the user on the edit comic page.

**Delete Comic**
- [CRU**D**] Delete a comic. By clicking the 'Delete' button within the specific comic page, it prompts a modal which (when user wants to delete) will bring the 
user back to (updated) database page.

### Features Left to Implement

I have a strong desire to fully flesh out this micro-site to become a business. 
To that end, there will need to be many more features to reward and ensure the customer journey and exchange is seamless.

**Pagination**
I've purposely kept the database small to dsiplay my prowess in manipulating the data for the users needs. 
As needs evolve, and more people (especially sellers and schools) become involved, then a much more comprehensive database and a way to effectively display 
these comics will be required.

**Calendar**
The lynchpin for this site is the ability for learners to meet in person, exchange comics and practice their language skills. 
I propose a calendar of events where learners are are notified of events in their area.

**Comic Page | Affiliate Links**
Affiliate links which connect to either 3rd party vendors and/or booksellers who are registered and have a digital online store.
Currently, this is set on all comic pages to point to the Amazon site. It makes no sense to make 'affiliate' a form field for users,
therefore this would be something that either the comic bookseller, and/or website administrator would input either on the 'Add Comic' or 'Edit Comic' component.
Access and rights to use that feature would be enabled via their login rights - the affiliate option only visible to the aforementioned parties.

**Registration/Log-in**
Hugely important for future progress. The current ability for every visitor to add/delete comic could cause havoc to my database. 
For the purposes of this project, I decided against setting up a reg page as it was not part of the requirements. 
Suffice to say, it will be added in due course once Django is covered in our syllabus. 

**Add Comic/Image**
I would like users to be able to upload comic images from their phone or device, instead of linking to an image source online. 

## Technologies Used

- [AWSCloud9](https://aws.amazon.com/cloud9/) Primary IDE for coding and enabled me to connect and push to Github/Heroku as needed.
- [Gitpod](https://www.gitpod.io/) Used for the closing stages of my project because I ran out of credits on AWS.
- [GitHub](https://github.com/) - Used to store code in a remote repository, hosting and for successful deployment of site.

### Front-End Tech
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used to structure pages, forms and associated content with user profiles as well as database. 
It also featured in the nav and footer sections of the page.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used to improve and simplify Javascript code.
- [Materialize 1.0.0](https://materializecss.com/) - Used as the overall CSS design framework.

### Back-End
- **Flask**
    - [Flask 1.1.1](http://flask.pocoo.org/) - Used as a microframework.
    - [Jinja 2.10.3](http://jinja.pocoo.org/docs/2.10/) - Used as a template engine w/ Flask.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.
    - [MongoDB Atlas](https://www.mongodb.com/) - Storage of my online remote database.
    - [PyMongo 3.9.0](https://api.mongodb.com/python/current/) - Python API for MongoDB.


## Testing

#### User Stories

Testing for each user scenario:

1. **User story 1**: A language learner who wants to improve their proficiency in a specific language.
| Site serves its purpose allowing exchange of comics. :white_check_mark:
2. **User story 2**: A bookseller who wants to sell their comic books/raise awareness of their store (digital or physical).
| Booksellers can add their comics, clarify that it is 'NOT' owned by individual, and denote their biz/shop in Description field. :white_check_mark:
3. **User story 3**: A language school/college that wishes to supply novel language comics to the classroom and curriculum to attract and engage students.
| Achieved. School can access database of comics. Subscription will be a future requirement to be built. :white_check_mark:
4. **User story 4**: Comic book fans in general who want to read widely.
| Multiple languages, interests covered as well as meetups which will be organised at a future date. :white_check_mark:
5. **User story 5**: Comic book fans who want to meet likeminded people and or others from different cultures/countries.
| Meetings forthcoming as discussed above. As a reference, comic book fans will be served by site which displays various comic themes appealing to comic fans. :white_check_mark:

**Add | Edit | Delete a Comic**

All the comics listed have been created by myself via mobile device (Samsung Galaxy A10) and on desktop. I have also shared the site with friends and family to test, both for responsiveness, and ease of use.
The feedback I received revealed that the user experience, trialling as either a learner, seller or school was overwhelmingly positive.
Adding, Editing and Deletion of various comics was successfully completed by multiple users.

#### General

Regular testing was conducted throughout the course of this project, especially before commits to Github.

**Responsive/Mobile-first design** was tested using Chrome developer tools to ensure desired layout was achieved. 
As well as Chrome, I also used Safari (12.0) and Firefox (68.0.2) which collectively successfully affirmed my project's responsiveness.
To test responsiveness, the following mobiles were tested Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5/SE 6/7/8 Plus X, iPad and iPad Pro. All successfully passed in mobile responsiveness of the page.

[HTML Checker]

![HTML Tester]

#### Issues


| Number | Issue            | Resolution   |
|--------|------------------|--------------|
|  1  | Source image not displaying for added comic  | Fixed  |
|  2  | Pagination  | Not a priority for this project  |
|  3  | Comics aren't being drilled into correctly  | Fixed w/ help from mentor  |
|  4  | No filters applied to comics  | Finally achieved w/ help from mentor  |
|  5  | Modal affecting deletion of chosen comic  | Changed button from it being on the card to it being on page - works fine  |
|  6  | Stock image provided if none supplied  | TBC  |
|  7  | Buttons on cards askew in iPad mode  | Changed grid layout to m4 to accommodate and changed card type  |

## Deployment

### Github

Deployed using the Master Branch on hosting platform GitHub Pages. 

The following steps were taken:

  1. Create a `master` branch in Github repository 
  2. Use Local AWS Cloud9 environment to build the site
  3. Commit files to the staging area using bash terminal commands: `git status`; `git add (specify directory)`; `git commit -m "add message"`
  4. Push files to the working environment using `git push`, which updates the repository
  5. Publish site from `master` branch using `settings` tab in the main page of the repository, select `source` as `master branch`, then `save`

### Heroku

Deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/AidanJReid/Forex-Comix-gitpod/blob/master/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here](https://github.com/AidanJReid/Forex-Comix-gitpod/blob/master/Procfile).
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `8080`
5. App should be successfully deployed to Heroku at this point.


## Credits

### Content

* I have taken liberties with the specification of the comics, instead wanting to demonstrate a range of fields allowing easy filter for users.
* The content of the various user profile sections is my own.

### Media

* Responsiveness and device images from [Responsive Design](http://ami.responsivedesign.is/)
* Favicon created at [Favicon.io](https://favicon.io/)
* Logo created at [Logohub.io](https://logohub.io/)
* Image Gallery:
    - [bookshelf.jpg](https://unsplash.com/photos/ydHrpfgJNPo)
    - [marvel.jpg](https://pixabay.com/photos/marvel-comics-cartoon-entertainment-1641554/)
    - [pow.png](https://pixabay.com/illustrations/pow-comic-comic-book-fight-1601674/) 
    - [zap.png](https://pixabay.com/illustrations/zap-comic-comic-book-fight-1601678/)
    - [thewalkingdead.jpg](https://www.thepeoplespace.com/sites/default/files/content/thewalkingdead-2393903_1280.jpg)
    - [haddock.jpg](https://cdn.pixabay.com/photo/2018/12/23/09/30/adult-3890780_960_720.jpg)
* Comic Database covers - the source for these have all been stated in the appropriate field (a requirement).
To see these, the user can 'Edit' comic.

### Acknowledgements

* Modal Code via Andreas Molle on [JS Fiddle](https://jsfiddle.net/AndreasMolle/7f6hmgcf/13/).
* CI Slack Channel where I've lurked for answers to many questions throughout this project, especially when it comes to the move to Gitpod
and filtering of comics (Hat tip to ShaneMuir)
* Inspiration for this README from [Travel Tim's project](https://github.com/TravelTimN/ci-milestone04-dcd)
* Brian Macharia, my CI mentor, for his support and patience.
