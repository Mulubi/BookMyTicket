"""New Models

Revision ID: 1cb031848bde
Revises: 84b670cc5052
Create Date: 2023-03-08 13:20:44.815102

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1cb031848bde'
down_revision = '84b670cc5052'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_roles_default'), ['default'], unique=False)

    with op.batch_alter_table('theatres', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('theatres')
    with op.batch_alter_table('anaesthetists', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('anaesthetists')
    op.drop_table('patient_booking')
    with op.batch_alter_table('procedures', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('procedures')
    with op.batch_alter_table('surgeons', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('surgeons')
    op.drop_table('theatre_procedure')
    op.drop_table('theatre_anaesthetist')
    op.drop_table('theatre_surgeon')
    op.drop_table('patients')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role_id', sa.String(length=60), nullable=False))
        batch_op.create_foreign_key(None, 'roles', ['role_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('role_id')

    op.create_table('patients',
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('contact_info', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='patients_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('theatre_surgeon',
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('surgeon_id', mysql.VARCHAR(length=60), nullable=False),
    sa.ForeignKeyConstraint(['surgeon_id'], ['surgeons.id'], name='theatre_surgeon_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='theatre_surgeon_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('theatre_id', 'surgeon_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('theatre_anaesthetist',
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('anaesthetist_id', mysql.VARCHAR(length=60), nullable=False),
    sa.ForeignKeyConstraint(['anaesthetist_id'], ['anaesthetists.id'], name='theatre_anaesthetist_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='theatre_anaesthetist_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('theatre_id', 'anaesthetist_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('theatre_procedure',
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('procedure_id', mysql.VARCHAR(length=60), nullable=False),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], name='theatre_procedure_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='theatre_procedure_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('theatre_id', 'procedure_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('surgeons',
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('contact_info', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('speciality', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('surgeons', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

    op.create_table('procedures',
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('requirements', mysql.VARCHAR(length=1024), nullable=True),
    sa.Column('id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('procedures', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

    op.create_table('patient_booking',
    sa.Column('patient_id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('procedure_id', mysql.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name='patient_booking_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], name='patient_booking_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('patient_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('anaesthetists',
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('contact_info', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('anaesthetists', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

    op.create_table('theatres',
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('theatres', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_default'))

    op.drop_table('roles')
    # ### end Alembic commands ###
