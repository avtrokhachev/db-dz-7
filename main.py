from factories import seed
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost/avtrokhachev", echo=True)


if __name__ == "__main__":
    seed(10)

    # 1
    conn = engine.connect()
    with conn.begin():
        print(conn.execute(text("""
        SELECT extract(year from birthdate) as year, COUNT(1) as cnt, sum(sum_medals) as sum_medals
        FROM (
            SELECT p.player_id as player_id, p.birthdate as birthdate, COUNT(1) as sum_medals FROM (
                SELECT * FROM
                (
                    SELECT * FROM events e
                    JOIN results r
                    ON e.event_id = r.event_id
                    WHERE medal = 'GOLD'
                ) r
                JOIN olympics o
                ON r.olympic_id = o.olympic_id
                WHERE o.year = 2004
            ) r
            JOIN players p
            ON p.player_id = r.player_id
            GROUP BY p.player_id, p.birthdate
        )
        GROUP BY extract(year from birthdate)
        """)).fetchall())

    with conn.begin():
        print(conn.execute(text("""
        SELECT e.event_id as event_id, COUNT(1) as medals_count FROM events e
        JOIN results r
        ON e.event_id = r.event_id
        WHERE r.medal = 'GOLD' and e.is_team_event = 0
        GROUP BY e.event_id
        HAVING COUNT(1) >= 2
        """)).fetchall())

    with conn.begin():
        print(conn.execute(text("""
        SELECT DISTINCT p.player_id FROM players p
        JOIN results r
        ON r.player_id = r.player_id
        WHERE r.medal != 'None'
        """)).fetchall())

    with conn.begin():
        print(conn.execute(text("""
        SELECT country_id FROM (
            SELECT p.country_id as country_id, COUNT(1) as cnt FROM players p
            GROUP BY p.country_id
        ) 
        ORDER BY cnt DESC
        LIMIT 1
        """)).fetchall())

    with conn.begin():
        print(conn.execute(text("""
        SELECT c.country_id, sum(sum_medals) / c.population as koef
        FROM (
            SELECT p.country_id as country_id, COUNT(1) as sum_medals FROM (
                SELECT * FROM
                (
                    SELECT * FROM events e
                    JOIN results r
                    ON e.event_id = r.event_id
                    WHERE medal != 'None'
                ) r
                JOIN olympics o
                ON r.olympic_id = o.olympic_id
                WHERE o.year = 2000
            ) r
            JOIN players p
            ON p.player_id = r.player_id
            GROUP BY p.country_id
        ) r
        JOIN countries c
        ON c.country_id = r.country_id
        GROUP BY c.country_id, c.population
        ORDER BY koef ASC
        LIMIT 5
        """)).fetchall())


