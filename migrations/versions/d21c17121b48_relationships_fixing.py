"""Relationships fixing

Revision ID: d21c17121b48
Revises: 835235c42519
Create Date: 2023-03-07 05:52:11.212391

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd21c17121b48'
down_revision = '835235c42519'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('theatre_surgeon_ibfk_2', 'theatre_surgeon', type_='foreignkey')
    with op.batch_alter_table('surgeons', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('surgeons')
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('patients')
    op.drop_table('patient_booking')
    with op.batch_alter_table('procedures', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('procedures')
    op.drop_table('theatres')
    op.drop_table('theatre_procedure')
    op.drop_table('theatre_patient')
    op.drop_table('theatre_surgeon')
    op.drop_table('anaesthetists')
    op.drop_table('theatre_anaesthetist')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('theatre_anaesthetist',
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('anaesthetist_id', mysql.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['anaesthetist_id'], ['anaesthetists.id'], name='theatre_anaesthetist_ibfk_2'),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='theatre_anaesthetist_ibfk_1'),
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
    op.create_table('theatre_surgeon',
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('surgeon_id', mysql.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['surgeon_id'], ['surgeons.id'], name='theatre_surgeon_ibfk_2'),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='theatre_surgeon_ibfk_1'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('theatre_patient',
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('patient_id', mysql.VARCHAR(length=60), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name='theatre_patient_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='theatre_patient_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('theatre_id', 'patient_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('theatre_procedure',
    sa.Column('theatre_id', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('procedure_id', mysql.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], name='theatre_procedure_ibfk_2'),
    sa.ForeignKeyConstraint(['theatre_id'], ['theatres.id'], name='theatre_procedure_ibfk_1'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
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
    sa.Column('procedure_id', mysql.VARCHAR(length=60), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name='patient_booking_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedures.id'], name='patient_booking_ibfk_2', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('patient_id', 'procedure_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('patients',
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('contact_info', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('id', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

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
    op.create_foreign_key('theatre_surgeon_ibfk_2', 'theatre_surgeon', 'surgeons', ['surgeon_id'], ['id'])
    # ### end Alembic commands ###
