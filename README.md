A long time ago in a galaxy far far away...

They needed a platform to sell used starships...

# WELCOME TO STAR TRADER 

# MVP
- Ability to create new users and have user login with authorization
- Users can buy and sell starships (include unique special ships)
- Users can add new starships for sale (only basic not unique)
- Users can search for starships by starship class interface bar

# BONUS / STRETCH GOALS
- user comments on starships up for sale
- user ratings (⭐️⭐️⭐️⭐️)
- light and dark side (light/dark mode)
- language translation (yoda speak and sith speak)
- mapping for where in galaxy starships are located
- way to earn credit (mingame?)


## TECHNOLOGIES USED
- Python/Flask
- React
- PSQL Database
- ARWES Front End Library (https://arwes.dev/)
- SWAPI Star Wars API (https://swapi.dev/)


## DATABASE SCHEMA

### TABLE USERS
- Id (primarykey, integer)
- Name (string)
- Species (string)
- Rebel/Empire tag (boolean)
- Age (integar)
- Credits Balance (float)
- Seller Rating (integer)
- Image URL (string)

### TABLE STARSHIPS
- Id (primaryhey, integer)
- Name (string)
- Model (string)
- Manufacturer (string)
- Starship Class (string)
- Crew Size (integer)
- Cargo Capicity (integer)
- HyperDrive Rating (float)
- Price (float)
- Image URL (string)
- Sold (boolean)

### TABLE COMMENTS
- UserId (integer)
- StarshipId (integer)
- Comment (string)



