# encoding: utf-8

from django import db
from django.db.models.signals import post_syncdb
from django.dispatch import receiver

import auf.django.references.models


@receiver(post_syncdb, sender=auf.django.references.models)
def creer_vues(sender, **kwargs):
    """Création des vues vers datamaster."""

    verbosity = kwargs.get('verbosity', 1)

    # On ne crée des vues que si on est sur une BD MySQL.
    # L'attribut db.connection.vendor n'est présent qu'à partir de Django
    # 1.3
    if (hasattr(db.connection, 'vendor')
        and db.connection.vendor != 'mysql') or \
       'mysql' not in db.backend.__name__:
        return

    cursor = db.connection.cursor()

    # Vérifions qu'on a une BD qui s'appelle 'datamaster'
    if not cursor.execute("SHOW DATABASES LIKE 'datamaster'"):
        return

    # Déterminons la liste de tables de référence dans datamaster
    cursor.execute("SHOW TABLES IN datamaster LIKE 'ref\\_%%'")
    datamaster_tables = set(row[0] for row in cursor)

    # Déterminons la liste de tables que nous avons déjà et
    # enlevons-les des tables de datamaster
    cursor.execute("SHOW FULL TABLES WHERE Table_type != 'VIEW'")
    my_tables = set(row[0] for row in cursor)
    datamaster_tables.difference_update(my_tables)

    # On peut maintenant créer les vues
    if verbosity > 0:
        print ("Création des vues vers datamaster")
    for table in datamaster_tables:
        if verbosity > 1:
            print ("Création d'une vue vers datamaster.%s" % table)
        cursor.execute(
            'CREATE OR REPLACE VIEW `%s` AS SELECT * FROM datamaster.`%s`' %
            (table, table)
        )


@receiver(post_syncdb)
def supprimer_cles_etrangeres(sender, **kwargs):
    """
    Supprime les contraintes de clé étrangère qui pointent vers les vues de
    datamaster.
    """
    verbosity = kwargs.get('verbosity', 1)

    # Tout ça ne s'applique qu'à des BDs MySQL.  L'attribut
    # db.connection.vendor n'est présent qu'à partir de Django 1.3
    if (hasattr(db.connection, 'vendor')
        and db.connection.vendor != 'mysql') or \
       'mysql' not in db.backend.__name__:
        return

    # Cherchons toute foreign key qui pointe vers une vue d'une table de
    # référence.
    cursor = db.connection.cursor()
    cursor.execute(
        """
        SELECT c.CONSTRAINT_SCHEMA, c.TABLE_NAME, c.CONSTRAINT_NAME
        FROM
            information_schema.REFERENTIAL_CONSTRAINTS c
            INNER JOIN information_schema.VIEWS v
                ON v.TABLE_SCHEMA = c.CONSTRAINT_SCHEMA
                AND v.TABLE_NAME = c.REFERENCED_TABLE_NAME
        WHERE c.REFERENCED_TABLE_NAME LIKE 'ref\\_%%'
        """
    )
    for schema, table, constraint in cursor:
        if verbosity > 0:
            print ("Suppression de la contrainte %s sur la table %s.%s..." % (
                constraint, schema, table
            ))
        db.connection.cursor().execute(
            'ALTER TABLE `%s`.`%s` DROP FOREIGN KEY `%s`' %
            (schema, table, constraint)
        )

# Supprimer les clés étrangères aussi après un migrate
try:
    from south.signals import post_migrate
except ImportError:
    pass
else:
    post_migrate.connect(supprimer_cles_etrangeres)
