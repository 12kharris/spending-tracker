# Generated by Django 4.2.13 on 2024-06-29 16:06

from django.db import migrations, models
import sys


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_transaction_transaction_date'),
    ]
    if 'test' not in sys.argv:
        operations = [
            migrations.CreateModel(
                name='Daily_Transactions',
                fields=[
                    ('unique_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                    ('day_of_year', models.DateField()),
                    ('mnth', models.IntegerField()),
                    ('username', models.CharField(max_length=150)),
                    ('cat_name', models.CharField()),
                    ('total_expenditure', models.DecimalField(decimal_places=2, max_digits=10)),
                ],
                options={
                    'db_table': 'Daily_Transactions',
                    'managed': (False,),
                },
            ),
            #gets every day since 2023-01-01 and the total expenditure that day per category for each user
            #include columns for month and year for easier filtering for views
            migrations.RunSQL(
                """
                CREATE VIEW Daily_Transactions AS
                    SELECT	bas.trk_date AS day_of_year
                            ,EXTRACT(MONTH FROM bas.trk_date) AS mnth 
                            ,users.username AS username
                            ,cat.name AS cat_name
                            ,SUM(CASE WHEN amount IS NULL THEN 0 ELSE amount END)AS total_expenditure
                    FROM (
                        --https://stackoverflow.com/questions/58769145/postgresql-with-recursive
                        select t.dt::date AS trk_date
                        from generate_series(date '2023-01-01', CURRENT_DATE, interval '1 day') as t(dt)
                    ) AS bas
                    CROSS JOIN (SELECT username, id FROM auth_user) AS users
                    CROSS JOIN (SELECT id, name FROM tracker_category) AS cat
                    LEFT JOIN tracker_transaction AS trk ON users.id = trk.user_id 
                        AND cat.id = trk.category_id 
                        AND bas.trk_date = trk.transaction_date
                    GROUP BY bas.trk_date, users.username, cat.name
                    ORDER BY users.username, bas.trk_date, cat.name;
                """,
                "DROP VIEW Daily_Transactions;"
            )
        ]
