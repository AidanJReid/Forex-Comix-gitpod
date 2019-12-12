import os

from flask import Flask, render_template, request, url_for, redirect, flash, Markup
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = os.urandom(24) #Creates a random string to use as session key

# MongoDB URI / Assign Database

app.config["MONGO_DBNAME"] = 'ForexComix'
app.config["MONGO_URI"] = 'mongodb+srv://natureboy:ttDFW9m3@myfirstcluster-fbekj.mongodb.net/ForexComix?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Home Page

@app.route('/')
def index():
    return render_template('index.html')

# Learner Section

@app.route('/learner')
def learner():
    return render_template('learner.html', page_title='Learner')

# Bookseller Section

@app.route('/bookseller')
def bookseller():
    return render_template('bookseller.html', page_title='Bookseller')

# School Section

@app.route('/school')
def school():
    return render_template('school.html', page_title='School')

# Add Comic Section

@app.route('/addcomic')
def addcomic():
    """
    Allows web visitor to add their own comic to the database.
    Updates on both the database page upon addition and passes the completed comic
    through to MongoDB
    """
    return render_template('addcomic.html', page_title='Add Comic', 
    languages=mongo.db.Languages.find(),
    condition=mongo.db.condition.find(),
    genre=mongo.db.genre.find(),
    difficulty=mongo.db.difficulty.find(),
    description=mongo.db.description.find(),
    owner=mongo.db.owner.find())

@app.route('/insert_comic', methods=['POST'])
def insert_comic():
    """
    Adds Comic to collection
    """
    DBComix = mongo.db.DBComix
    DBComix.insert_one(request.form.to_dict())
    return redirect(url_for('database'))

# Comic Database Section

@app.route('/database', methods=['GET', 'POST'])
def database():
    genres=mongo.db.genre.find()
    languages=mongo.db.Languages.find()
    conditions=mongo.db.condition.find()
    difficultys=mongo.db.difficulty.find()
    # This is true if form has been submitted.
    if request.method == "POST":
        # Get restrictions provided by user through the form
        # These are in the form of a MultiDict. Convert to normal dictionary.
        filter_restrictions = request.form.to_dict()
        non_empty_restrictions = dict()
        if len(filter_restrictions) == 0:
            print("0 values filled in")
            flash(Markup("D'Oh! You didn't select a filter option."))
            return redirect(url_for('database'))

        if len(filter_restrictions) != 0:
            for restriction_key, restriction_value in filter_restrictions.items():
                non_empty_restrictions[restriction_key] = restriction_value
            comics = mongo.db.DBComix.find(non_empty_restrictions)
            print("Filter(s) applied", restriction_key, restriction_value, non_empty_restrictions)
            return render_template('database.html',
            DBComix=comics,
            genres=genres,
            languages=languages,
            difficultys=difficultys,
            conditions=conditions,
            page_title='Database')
    
    else:
        comics = mongo.db.DBComix.find()
    
    return render_template('database.html',
    DBComix=comics,
    genres=genres,
    languages=languages,
    difficultys=difficultys,
    conditions=conditions,
    page_title='Database')
    
# Specific Comic View

@app.route('/get_comic/<DBComix_id>', methods=['GET'])
def get_comic(DBComix_id):
    """
    Data returned from drilldown to comic card,
    returning specific comic fields.
    """
    get_comic=mongo.db.DBComix.find_one({'_id': ObjectId(DBComix_id)})
    print(get_comic)
    return render_template('comic.html', comic=get_comic)

# Edit Comic Page

@app.route('/edit_comic/<DBComix_id>')
def edit_comic(DBComix_id):
    """
    Accessible from edit button on Database card
    Displays all pre-loaded values which can be iterated through
    and submitted to update card on Database page.
    """
    the_comic = mongo.db.DBComix.find_one({'_id': ObjectId(DBComix_id)})
    all_languages = mongo.db.Languages.find() 
    all_genres = mongo.db.genre.find()
    all_difficulty = mongo.db.difficulty.find()
    all_condition = mongo.db.condition.find()
    all_description = mongo.db.description.find()
    return render_template('editcomic.html',
            comic=the_comic, 
            languages=all_languages, 
            genres=all_genres, 
            difficulty=all_difficulty, 
            condition=all_condition, 
            description=all_description, 
        page_title='Edit Comic')
        
# Update Comic / Insert Section

@app.route('/update_comic/<DBComix_id>', methods=['POST'])
def update_comic(DBComix_id):
    DBComix = mongo.db.DBComix
    DBComix.update({'_id': ObjectId(DBComix_id)},
    {
        'language': request.form.get('language'),
        'genre': request.form.get('genre'),
        'condition': request.form.get('condition'),
        'difficulty': request.form.get('difficulty'),
        'is_owner': request.form.get('is_owner'),
        'description': request.form.get('description'),
        'title': request.form.get('title'),
        'character': request.form.get('character'),
        'image_source': request.form.get('image_source')
    })
    return redirect(url_for('database'))

# Delete Comic

@app.route('/delete_comic/<DBComix_id>')
def delete_comic(DBComix_id):
    """
    Clicking 'Delete' on Database comic card prompts
    immediate deletion of card and return to
    database page.
    """
    mongo.db.DBComix.remove({'_id': ObjectId(DBComix_id)})
    return redirect(url_for('database'))
                
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
# Debug=true should be removed on submission!