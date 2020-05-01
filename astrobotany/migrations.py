import argparse

from peewee import BooleanField
from playhouse import migrate

from .models import init_db


def add_setting_ansi_enabled(migrator):
    migrate.migrate(
        migrator.add_column("user", "ansi_enabled", BooleanField(default=False))
    )


def main():
    parser = argparse.ArgumentParser(
        description="Apply a named migration to the astrobotany database"
    )
    parser.add_argument("migration")
    parser.add_argument("--db", default="/etc/astrobotany/astrobotany.sqlite")
    args = parser.parse_args()

    db = init_db(args.db)
    migrator = migrate.SqliteMigrator(db)

    print(f"Running migration {args.migration}...")
    locals()[args.migration](migrator)
    print(f"Success!")


if __name__ == "__main__":
    main()