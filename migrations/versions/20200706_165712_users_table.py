"""users table

Revision ID: c1c663f2a230
Revises: 6cd71ed289b7
Create Date: 2020-07-06 16:57:12.125533

"""
from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash

# revision identifiers, used by Alembic.
revision = 'c1c663f2a230'
down_revision = '6cd71ed289b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###