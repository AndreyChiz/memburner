"""empty message

Revision ID: e1b1c0277ada
Revises: 
Create Date: 2024-07-29 16:37:43.002861

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e1b1c0277ada"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "document",
        sa.Column("owner", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("code", sa.String(length=100), nullable=True),
        sa.Column(
            "id",
            sa.Uuid(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_document")),
        sa.UniqueConstraint(
            "owner", "name", "code", name="document_owner_name_code_key"
        ),
    )
    op.create_table(
        "section",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("document_id", sa.Uuid(), nullable=False),
        sa.Column(
            "id",
            sa.Uuid(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["document_id"],
            ["document.id"],
            name=op.f("fk_section_document_id_document"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_section")),
        sa.UniqueConstraint("name", name=op.f("uq_section_name")),
    )
    op.create_table(
        "question",
        sa.Column("question_text", sa.String(), nullable=False),
        sa.Column("answers", sa.ARRAY(sa.String()), nullable=False),
        sa.Column("section_id", sa.Uuid(), nullable=False),
        sa.Column("number_in_chapter", sa.SmallInteger(), nullable=False),
        sa.Column(
            "id",
            sa.Uuid(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["section_id"],
            ["section.id"],
            name=op.f("fk_question_section_id_section"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_question")),
        sa.UniqueConstraint(
            "question_text", name=op.f("uq_question_question_text")
        ),
    )



def downgrade() -> None:
    op.drop_table("question")
    op.drop_table("section")
    op.drop_table("document")

