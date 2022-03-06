"""empty message

Revision ID: 5ba37b496074
Revises: 
Create Date: 2021-12-10 02:23:25.708202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ba37b496074'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balance',
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('balance')
    )
    op.create_table('users',
    sa.Column('idUsers', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('clientName', sa.String(length=45), nullable=True),
    sa.Column('firstName', sa.String(length=45), nullable=True),
    sa.Column('lastName', sa.String(length=45), nullable=True),
    sa.Column('status', sa.Enum('user', 'manager'), nullable=True),
    sa.PrimaryKeyConstraint('idUsers')
    )
    op.create_table('credit',
    sa.Column('idCredit', sa.Integer(), nullable=False),
    sa.Column('loan_status', sa.String(length=45), nullable=True),
    sa.Column('loan_date', sa.String(length=45), nullable=True),
    sa.Column('loan_amount', sa.Integer(), nullable=True),
    sa.Column('interest_rate', sa.Integer(), nullable=True),
    sa.Column('id_borrower', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_borrower'], ['users.idUsers'], ),
    sa.PrimaryKeyConstraint('idCredit')
    )
    op.create_table('User_Credit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('credit_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['credit_id'], ['credit.idCredit'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.idUsers'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User_Credit')
    op.drop_table('credit')
    op.drop_table('users')
    op.drop_table('balance')
    # ### end Alembic commands ###