"""create migrations

Revision ID: 789b401726d6
Revises: 
Create Date: 2020-07-05 14:17:13.153060

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash


# revision identifiers, used by Alembic.
revision = '789b401726d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    shiptypes_table = op.create_table('shiptypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=50), nullable=False),
    sa.Column('starship_class', sa.String(length=50), nullable=False),
    sa.Column('manufacturer', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('hyperdrive_rating', sa.Float(), nullable=False),
    sa.Column('mglt', sa.Integer(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.Column('crew', sa.Integer(), nullable=False),
    sa.Column('passenger', sa.Integer(), nullable=False),
    sa.Column('cargo', sa.BigInteger(), nullable=False),
    sa.Column('consumables', sa.String(length=30), nullable=False),
    sa.Column('cost_credits', sa.BigInteger(), nullable=False),
    sa.Column('ship_image', sa.String(length=150), nullable=False),
    sa.Column('unique', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    species_table = op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('species_type', sa.String(length=75), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    users_table = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=100), nullable=False),
    sa.Column('species', sa.Integer(), nullable=False),
    sa.Column('bio', sa.String(length=1000), nullable=True),
    sa.Column('faction', sa.Boolean(), nullable=True),
    sa.Column('credits', sa.BigInteger(), nullable=False),
    sa.Column('user_image', sa.String(length=150), nullable=False),
    sa.Column('force_points', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['species'], ['species.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )

    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ship_type', sa.Integer(), nullable=False),
    sa.Column('custom_name', sa.String(length=75), nullable=True),
    sa.Column('sale_price', sa.BigInteger(), nullable=False),
    sa.Column('lightyears_traveled', sa.Integer(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.Column('for_sale', sa.Boolean(), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
    sa.ForeignKeyConstraint(['ship_type'], ['shiptypes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('buyer', sa.Integer(), nullable=True),
    sa.Column('seller', sa.Integer(), nullable=True),
    sa.Column('starship', sa.Integer(), nullable=True),
    sa.Column('sale_price', sa.BigInteger(), nullable=False),
    sa.Column('sale_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['buyer'], ['users.id'], ),
    sa.ForeignKeyConstraint(['seller'], ['users.id'], ),
    sa.ForeignKeyConstraint(['starship'], ['starships.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.bulk_insert(species_table,
        [
        {'id': 1, 'species_type': 'Human'},
        {'id': 2, 'species_type': 'Driod'},
        {'id': 3, 'species_type': 'Wookie'},
        {'id': 4, 'species_type': 'Rodian'},
        {'id': 5, 'species_type': 'Hutt'},
        {'id': 6, 'species_type': "Yoda's Species"},
        {'id': 7, 'species_type': 'Trandoshan'},
        {'id': 8, 'species_type': 'Mon Calamari'},
        {'id': 9, 'species_type': 'Ewok'},
        {'id': 10, 'species_type': 'Sullustan'},
        {'id': 11, 'species_type': 'Neimodian'},
        {'id': 12, 'species_type': 'Gungan'},
        {'id': 13, 'species_type': 'Toydarian'},
        {'id': 14, 'species_type': 'Dug'},
        {'id': 15, 'species_type': "Twi'lek"},
        {'id': 16, 'species_type': 'Aleena'},
        {'id': 17, 'species_type': 'Vulptereen'},
        {'id': 18, 'species_type': 'Xexto'},
        {'id': 19, 'species_type': 'Toong'},
        {'id': 20, 'species_type': 'Cerean'},
        {'id': 21, 'species_type': 'Nautolan'},
        {'id': 22, 'species_type': 'Zabrak'},
        {'id': 23, 'species_type': 'Tholothian'},
        {'id': 24, 'species_type': 'Iktotchi'},
        {'id': 25, 'species_type': 'Quermian'},
        {'id': 26, 'species_type': 'Kel Dor'},
        {'id': 27, 'species_type': 'Chagrian'},
        {'id': 28, 'species_type': 'Geonosian'},
        {'id': 29, 'species_type': 'Mirialan'},
        {'id': 30, 'species_type': 'Clawdite'},
        {'id': 31, 'species_type': 'Besalisk'},
        {'id': 32, 'species_type': 'Kaminoan'},
        {'id': 33, 'species_type': 'Skakoan'},
        {'id': 34, 'species_type': 'Muun'},
        {'id': 35, 'species_type': 'Togruta'},
        {'id': 36, 'species_type': 'Kaleesh'},
        {'id': 37, 'species_type': "Pau'an"}
        ]
    )

    op.bulk_insert(users_table, 
        [
        {'id': 1, 'name': 'Luke Skywalker', 'email': 'lukeskywalker@aol.com', 'hashed_password': generate_password_hash('force1'), 'species': 1, 'bio': 'Luke Skywalker was a Tatooine farmboy who rose from humble beginnings to become one of the greatest Jedi the galaxy has ever known.',
            'faction': True, 'credits': 1000000, 'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/01.jpg', "force_points": 0},
        {'id': 2, 'name': 'C-3PO', 'email': 'goldguy@gmail.com', 'hashed_password': generate_password_hash('masterluke'), 'species': 2, 'bio': 'C-3PO longs for more peaceful times, but his continued service to the Resistance — and his knowledge of more than seven million forms of communication — keeps the worry-prone droid in the frontlines of galactic conflict.',
             'faction': True, 'credits': 1000, 'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/02.jpg', "force_points": 0},
        {'id': 3, 'name': 'R2-D2', 'email': 'droid1@R2D2.net', 'hashed_password': generate_password_hash('xwingsrule4'), 'species': 2, 'bio': 'A reliable and versatile astromech droid, R2-D2 has served Padmé Amidala, Anakin Skywalker, and Luke Skywalker in turn, showing great bravery in rescuing his masters and their friends from many perils',
             'faction': True, 'credits': 1000000, 'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/03.jpg', "force_points": 0},
        {'id': 4, 'name': 'Darth Vader', 'email': 'darkside4life@hotmail.com', 'hashed_password': generate_password_hash('iamyourfather'), 'species': 1, 'bio': 'Once a heroic Jedi Knight, Darth Vader was seduced by the dark side of the Force, became a Sith Lord, and led the Empire’s eradication of the Jedi Order. But there was still good in him…',
             'faction': False, 'credits': 1500000, 'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/04.jpg', "force_points": 0},
        {'id': 5, 'name': 'Leia Organa', 'email': 'goldenbikini@mac.com', 'hashed_password': generate_password_hash('ewoksarecute'), 'species': 1, 'bio': None, 'faction': False, 'credits': 3000000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/05.jpg', "force_points": 0},
        {'id': 6, 'name': 'Owen Lars', 'email': 'larsevaporators@tatooine.org', 'hashed_password': generate_password_hash('evaporators'), 'species': 1, 'bio': None, 'faction': True, 'credits': 50000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/06.jpg', "force_points": 0},
        {'id': 7, 'name': 'Beru Whitesun Lars', 'email': 'auntberu@optimium.net', 'hashed_password': generate_password_hash('larssmells'), 'species': 1, 'bio': None, 'faction': True, 'credits': 25000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/07.jpg', "force_points": 0},
        {'id': 8, 'name': 'R5-D4', 'email': 'wishiwasr2d2@R2D2.net', 'hashed_password': generate_password_hash('notr2d2'), 'species': 2, 'bio': None, 'faction': True, 'credits': 15000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/08.jpg', "force_points": 0},
        {'id': 9, 'name': 'Biggs Darklighter', 'email': 'biggs@rebels.com', 'hashed_password': generate_password_hash('imbiggs'), 'species': 1, 'bio': None, 'faction': True, 'credits': 34560,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/09.jpg', "force_points": 0},
        {'id': 10, 'name': 'Obi-Wan Kenobi', 'email': 'force2@force.net', 'hashed_password': generate_password_hash('usetheforceluke'), 'species': 1, 'bio': None, 'faction': True, 'credits': 1000000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/10.jpg', "force_points": 0},
        {'id': 11, 'name': 'Anakin Skywalker', 'email': 'anny1@jediturnedsith.org', 'hashed_password': generate_password_hash('imreallyvader'), 'species': 1, 'bio': None, 'faction': True, 'credits': 65000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/11.jpg', "force_points": 0},
        {'id': 12, 'name': 'Wilhuff Tarkin', 'email': 'moftarkin@empirerulez.com', 'hashed_password': generate_password_hash('deathstar1'), 'species': 1, 'bio': None, 'faction': False, 'credits': 2000000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/12.jpg', "force_points": 0},
        {'id': 13, 'name': 'Chewbacca', 'email': 'chewie@falcon.com', 'hashed_password': generate_password_hash('wookie1'), 'species': 3, 'bio': None, 'faction': True, 'credits': 500000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/13.jpg', "force_points": 0},
        {'id': 14, 'name': 'Han Solo', 'email': 'solo1@falcon.com', 'hashed_password': generate_password_hash('12parsecs'), 'species': 1, 'bio': None, 'faction': True, 'credits': 25000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/14.jpg', "force_points": 0},
        {'id': 15, 'name': 'Greedo', 'email': 'greedo@bountyhunters.org', 'hashed_password': generate_password_hash('hanshotme'), 'species': 4, 'bio': None, 'faction': False, 'credits': 125000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/15.jpg', "force_points": 0},
        {'id': 16, 'name': 'Jabba Desilijic Tiure', 'email': 'jabba@hutt.net', 'hashed_password': generate_password_hash('iwillgetyousolo'), 'species': 5, 'bio': None, 'faction': False, 'credits': 7500000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/16.jpg', "force_points": 0},
        {'id': 18, 'name': 'Wedge Antilles', 'email': 'wedge2@rebels.com', 'hashed_password': generate_password_hash('wedgethis'), 'species': 1, 'bio': None, 'faction': True, 'credits': 132500,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/18.jpg', "force_points": 0},
        {'id': 19, 'name': 'Jek Tono Porkins', 'email': 'jek@rebels.com', 'hashed_password': generate_password_hash('vaderkilledme'), 'species': 1, 'bio': None, 'faction': True, 'credits': 500,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/19.jpg', "force_points": 0},
        {'id': 20, 'name': 'Yoda', 'email': 'yoda@force.net', 'hashed_password': generate_password_hash('thereisnotry'), 'species': 6, 'bio': None, 'faction': True, 'credits': 10000000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/20.jpg', "force_points": 0},
        {'id': 21, 'name': 'Palpatine', 'email': 'emperor@jediturnedsith.org', 'hashed_password': generate_password_hash('darkside'), 'species': 1, 'bio': None, 'faction': False, 'credits': 1000000000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/21.jpg', "force_points": 0},
        {'id': 22, 'name': 'Boba Fett', 'email': 'bfett@bountyhunters.org', 'hashed_password': generate_password_hash(''), 'species': 1, 'bio': None, 'faction': False, 'credits': 750000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/22.jpg', "force_points": 0},
        {'id': 23, 'name': 'IG-88', 'email': 'IG@R2D2.net', 'hashed_password': generate_password_hash('imdroid'), 'species': 2, 'bio': None, 'faction': False, 'credits': 50000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/23.jpg', "force_points": 0},
        {'id': 24, 'name': 'Bossk', 'email': 'bossk@bountyhunters.org', 'hashed_password': generate_password_hash('bossk1'), 'species': 7, 'bio': "One of the most feared bounty hunters of the galaxy, Bossk used his natural Trandoshan hunting instincts to capture his prey. During the Clone Wars, the red-eyed reptilian partnered with Aurra Sing, Castas and young Boba Fett. Bossk didn't care much for vendettas or politics. He was in it to get paid. After a brief stint in a Republic prison, Bossk continued his partnership with Fett, becoming a bodyguard to the teen bounty hunter. Decades later, Bossk answered Darth Vader's call to capture the Millennium Falcon after the Battle of Hoth, an assignment that put him in direct competition with Boba.",
            'faction': False, 'credits': 500000, 'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/24.jpg', "force_points": 0},
        {'id': 25, 'name': 'Lando Calrissian', 'email': 'lando@falcon.com', 'hashed_password': generate_password_hash('cloudcity'), 'species': 1, 'bio': None, 'faction': True, 'credits': 3000000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/25.jpg', "force_points": 0},
        {'id': 26, 'name': 'Lobot', 'email': 'lobot@cloudcity.com', 'hashed_password': generate_password_hash('lobot'), 'species': 2, 'bio': None, 'faction': True, 'credits': 25000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/26.jpg', "force_points": 0},
        {'id': 27, 'name': 'Admiral Ackbar', 'email': 'ackie@rebels.com', 'hashed_password': generate_password_hash('itsatrap'), 'species': 8, 'bio': None, 'faction': True, 'credits': 500000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/27.jpg', "force_points": 0},
        {'id': 28, 'name': 'Mon Mothma', 'email': 'mon@rebels.com', 'hashed_password': generate_password_hash('mothma'), 'species': 1, 'bio': None, 'faction': True, 'credits': 250000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/28.jpg', "force_points": 0},
        {'id': 29, 'name': 'Arvel Crynyd', 'email': 'crynyd@rebels.com', 'hashed_password': generate_password_hash('nooneknowsme'), 'species': 1, 'bio': None, 'faction': True, 'credits': 120000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/29.jpg', "force_points": 0},
        {'id': 30, 'name': 'Wicket Systri Warrick', 'email': 'wicket@emok.org', 'hashed_password': generate_password_hash('lublub'), 'species': 9, 'bio': None, 'faction': True, 'credits': 50000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/30.jpg', "force_points": 0},
        {'id': 31, 'name': 'Nien Nunb', 'email': 'nunb@rebels.com', 'hashed_password': generate_password_hash('nubnub'), 'species': 10, 'bio': None, 'faction': True, 'credits': 152000,
            'user_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/characters/31.jpg', "force_points": 0}
        ]
    )


# {'id': , 'name': '', 'email': '', 'hashed_password': generate_password_hash(''), 'species': , 'faction': , 'credits': ,
#  'user_image': '', "force_points": 0},



    op.bulk_insert(shiptypes_table,
        [
        {'id': 2, 'type_name': 'CR90 Corvette', 'starship_class': 'Star Cruiser', 'manufacturer': 'Corellian Engineering Company', 'model': 'CR90 Corvette', 'hyperdrive_rating': 2.0, 'mglt': 60, 'length': 150,
            'crew': 30, 'passenger': 600, 'cargo': 3000000, 'consumables': '1 year', 'cost_credits': 3500000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/02.jpg', 'unique': False },
        {'id': 3, 'type_name': 'Star Destroyer', 'starship_class': 'Star Dreadnought', 'manufacturer': 'Kuat Drive Yard', 'model': 'Imperial I-class Star Destroyer', 'hyperdrive_rating': 2.0, 'mglt': 60, 'length': 1600,
            'crew': 47060, 'passenger': 0, 'cargo': 36000000, 'consumables': '2 years', 'cost_credits': 150000000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/03.jpg', 'unique': False},
        {'id': 5, 'type_name': 'Sentinel-class Landing Craft', 'starship_class': 'Transport', 'manufacturer': 'Sienar Fleet Systems', 'model': 'Sentinel-class Landing Craft', 'hyperdrive_rating': 1.0, 'mglt': 70, 'length': 38,
            'crew': 5, 'passenger': 75, 'cargo': 180000, 'consumables': '1 month', 'cost_credits': 240000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/05.jpg', 'unique': False},
        {'id': 9, 'type_name': 'Death Star', 'starship_class': 'Star Dreadnought', 'manufacturer': 'Sienar Fleet System', 'model': 'D5-1 Orbital Battle Station', 'hyperdrive_rating': 4.0, 'mglt': 10, 'length': 120000,
            'crew': 342953, 'passenger': 843342, 'cargo': 1000000000000, 'consumables': '3 years', 'cost_credits': 1000000000000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/09.jpg', 'unique': True},
        {'id': 10, 'type_name': 'Millennium Falcon', 'starship_class': 'Freighter', 'manufacturer': 'Corellian Engineering Corporation', 'model': 'YT-1300 Light Freighter', 'hyperdrive_rating': 0.5, 'mglt': 75, 'length': 35,
            'crew': 4, 'passenger': 6, 'cargo': 100000, 'consumables': '2 months', 'cost_credits': 100000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/10.jpg', 'unique': True},
        {'id': 11, 'type_name': 'Y-wing', 'starship_class': 'Starfighter', 'manufacturer': 'Koensayr Manufacturing', 'model': 'BTL Y-wing', 'hyperdrive_rating': 1.0, 'mglt': 80, 'length': 14,
            'crew': 2, 'passenger': 0, 'cargo': 110, 'consumables': '1 week', 'cost_credits': 134999, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/11.jpg', 'unique': False},
        {'id': 12, 'type_name': 'X-wing', 'starship_class': 'Starfighter', 'manufacturer': 'Incom Corporation', 'model': 'T-65 X-wing', 'hyperdrive_rating': 1.0, 'mglt': 100, 'length': 13,
            'crew': 1, 'passenger': 0, 'cargo': 110, 'consumables': '1 week', 'cost_credits': 149999, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/12.jpg', 'unique': False},
        {'id': 13, 'type_name': 'TIE Advanced x1', 'starship_class': 'Starfighter', 'manufacturer': 'Sienar Fleet System', 'model': 'Twin Ion Engine Advanced x1', 'hyperdrive_rating': 1.0, 'mglt': 105, 'length': 9,
            'crew': 1, 'passenger': 0, 'cargo': 150, 'consumables': '5 days', 'cost_credits': 79999, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/13.jpg', 'unique': False},
        {'id': 14, 'type_name': "Darth Vader's TIE Fighter", 'starship_class': 'Starfighter', 'manufacturer': 'Sienar Fleet System', 'model': 'Experimental Twin Engine Advnced x2', 'hyperdrive_rating': 1.0, 'mglt': 105, 'length': 10,
            'crew': 1, 'passenger': 0, 'cargo': 150, 'consumables': '5 days', 'cost_credits': 135999, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/14.jpg', 'unique': True},
        {'id': 15, 'type_name': 'Executor', 'starship_class': 'Star Dreadnought', 'manufacturer': 'Kuat Drive Yard', 'model': 'Executor-class Star Dreadnought', 'hyperdrive_rating': 2.0, 'mglt': 40, 'length': 19000,
            'crew': 279144, 'passenger': 38000, 'cargo': 250000000, 'consumables': '6 years', 'cost_credits': 1143350000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/15.jpg', 'unique': True},
        {'id': 17, 'type_name': 'Rebel Transport', 'starship_class': 'Transport', 'manufacturer': 'Gallofree Yards, Inc.', 'model': 'GR-75 Medium Transport', 'hyperdrive_rating': 4.0, 'mglt': 20, 'length': 90,
            'crew': 6, 'passenger': 90, 'cargo': 19000000, 'consumables': '6 months', 'cost_credits': 180000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/17.jpg', 'unique': False},
        {'id': 19, 'type_name': 'ARC-170 Starfighter', 'starship_class': 'Starfighter', 'manufacturer': 'Incom Corporation', 'model': 'ARC-170 Aggressive Reconnaissance Starfighter', 'hyperdrive_rating': 1.5, 'mglt': 70, 'length': 13,
            'crew': 3, 'passenger': 0, 'cargo': 250, 'consumables': '1 month', 'cost_credits': 180000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/19.jpg', 'unique': False},
        {'id': 21, 'type_name': 'Slave 1', 'starship_class': 'Transport', 'manufacturer': 'Kuat Systems Engineering', 'model': 'Firespray-31-class Patroll and Attack', 'hyperdrive_rating': 3.0, 'mglt': 70, 'length': 22,
            'crew': 1, 'passenger': 6, 'cargo': 70000, 'consumables': '1 month', 'cost_credits': 343000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/21.jpg', 'unique': True},
        {'id': 22, 'type_name': 'Imperial Shuttle', 'starship_class': 'Transport', 'manufacturer': 'Sienar Fleet Systems', 'model': 'Lambda-Class T-4a Shuttle', 'hyperdrive_rating': 1.0, 'mglt': 50, 'length': 20,
            'crew': 6, 'passenger': 20, 'cargo': 80000, 'consumables': '2 months', 'cost_credits': 240000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/22.jpg', 'unique': False},
        {'id': 23, 'type_name': 'EF76 Nebulon-9 Escort Frigate', 'starship_class': 'Star Cruiser', 'manufacturer': 'Kuat Drive Yards', 'model': 'EF76 Nebulon-9 Escort Frigate', 'hyperdrive_rating': 2.0, 'mglt': 40, 'length': 300,
            'crew': 854, 'passenger': 75, 'cargo': 6000000, 'consumables': '2 years', 'cost_credits': 8500000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/23.jpg', 'unique': False},
        {'id': 27, 'type_name': 'Calamari Cruiser', 'starship_class': 'Star Cruiser', 'manufacturer': 'Mon Calamari Shipyards', 'model': 'MC80 Liberty Type Star Cruiser', 'hyperdrive_rating': 1.0, 'mglt': 60, 'length': 1200,
            'crew': 5400, 'passenger': 1200, 'cargo': 3000000, 'consumables': '2 years', 'cost_credits': 104000000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/27.jpg', 'unique': False},
        {'id': 28, 'type_name': 'A-wing', 'starship_class': 'Starfighter', 'manufacturer': 'Alliance Underground Engineering', 'model': 'RZ-I A-wing Interceptor', 'hyperdrive_rating': 1.0, 'mglt': 120, 'length': 10,
            'crew': 1, 'passenger': 0, 'cargo': 40, 'consumables': '1 week', 'cost_credits': 175000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/28.jpg', 'unique': False},
        {'id': 29, 'type_name': 'B-wing', 'starship_class': 'Starfighter', 'manufacturer': 'Slayn & Korpil', 'model': 'A/SF-01 B-wing Starfighter', 'hyperdrive_rating': 2.0, 'mglt': 91, 'length': 17,
            'crew': 1, 'passenger': 0, 'cargo': 45, 'consumables': '1 week', 'cost_credits': 220000, 'ship_image': 'https: // starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/29.jpg', 'unique': False},
        {'id': 30, 'type_name': 'U-wing', 'starship_class': 'Starfighter', 'manufacturer': 'Incom Corporation', 'model': 'UT-60D U-wing Starfighter', 'hyperdrive_rating': 1.0, 'mglt': 95, 'length': 24,
            'crew': 2, 'passenger': 8, 'cargo': 25000, 'consumables': '2 weeks', 'cost_credits': 130000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/30.jpg', 'unique': False},
        {'id': 31, 'type_name': 'Republic Frigate', 'starship_class': 'Star Cruiser', 'manufacturer': 'Corellian Engineering Corporation', 'model': 'Consular-Class Cruiser', 'hyperdrive_rating': 2.0, 'mglt': 60, 'length': 115,
            'crew': 9, 'passenger': 16, 'cargo': 120000, 'consumables': '3 months', 'cost_credits': 850000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/31.jpg', 'unique': False},
        {'id': 33, 'type_name': 'Imperial Zeta-Class Cargo Shuttle', 'starship_class': 'Freighter', 'manufacturer': 'Sienar Fleet Systems', 'model': 'Zeta-Class Cargo Shuttle', 'hyperdrive_rating': 2.0, 'mglt': 60, 'length': 35,
            'crew': 2, 'passenger': 20, 'cargo': 450000, 'consumables': '2 weeks', 'cost_credits': 195000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/33.jpg', 'unique': False},
        {'id': 39, 'type_name': 'Naboo Fighter', 'starship_class': 'Starfighter', 'manufacturer': 'Theed Palace Space Vessel Engineering Corps.', 'model': 'N-1 Starfighter', 'hyperdrive_rating': 1.0, 'mglt': 90, 'length': 11,
            'crew': 1, 'passenger': 0, 'cargo': 65, 'consumables': '1 week', 'cost_credits': 200000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/39.jpg', 'unique': False},
        {'id': 40, 'type_name': 'Naboo Royal Starship', 'starship_class': 'Transport', 'manufacturer': 'Theed palace Space Vessel Engineering Corps.', 'model': 'J-type 327 Nubian Royal Starship', 'hyperdrive_rating': 1.8, 'mglt': 95, 'length': 76,
            'crew': 8, 'passenger': 20, 'cargo': 30000, 'consumables': '1 month', 'cost_credits': 535000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/40.jpg', 'unique': False},
        {'id': 41, 'type_name': 'Scimitar', 'starship_class': 'Transport', 'manufacturer': 'Sienar Fleet Systems', 'model': 'Star Courier', 'hyperdrive_rating': 1.5, 'mglt': 75, 'length': 27,
            'crew': 1, 'passenger': 6, 'cargo': 250000, 'consumables': '1 month', 'cost_credits': 5500000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/41.jpg', 'unique': False},
        {'id': 43, 'type_name': 'J-Type Diplomatic Shuttle', 'starship_class': 'Transport', 'manufacturer': 'Theed palace Space Vessel Engineering Corps.', 'model': 'J-Type Diplomatic Shuttle', 'hyperdrive_rating': 0.7, 'mglt': 50, 'length': 39,
            'crew': 5, 'passenger': 10, 'cargo': 175000, 'consumables': '1 year', 'cost_credits': 2000000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/43.jpg', 'unique': False},
        {'id': 47, 'type_name': 'AA-9 Coruscant Freighter', 'starship_class': 'Freighter', 'manufacturer': 'Botajef Shipyards', 'model': 'Botajef AA-9 Freighter-Liner', 'hyperdrive_rating': 0.5, 'mglt': 50, 'length': 390,
            'crew': 15, 'passenger': 30000, 'cargo': 750000, 'consumables': '3 months', 'cost_credits': 825700, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/47.jpg', 'unique': False},
        {'id': 48, 'type_name': 'Jedi Starfighter', 'starship_class': 'Starfighter', 'manufacturer': 'Kuat Systems Engineering', 'model': 'Delta-7 Aethersprite-class Interceptor', 'hyperdrive_rating': 1.0, 'mglt': 95, 'length': 8,
            'crew': 1, 'passenger': 0, 'cargo': 60, 'consumables': '1 week', 'cost_credits': 180000, 'ship_image': 'https://starwars-trader-imgs.s3.us-east-2.amazonaws.com/img/starships/48.jpg', 'unique': False}
        ]
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('starships')
    op.drop_table('users')
    op.drop_table('species')
    op.drop_table('shiptypes')
    # ### end Alembic commands ###
