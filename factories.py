import random
from faker import Faker
from sqlalchemy import create_engine, text

COUNTRIES = set()
MEDAL_TYPES = ("None", "GOLD", "SILVER", "BRONZE")

faker = Faker()
engine = create_engine("postgresql://postgres:postgres@localhost/avtrokhachev", echo=True)


def create_new_country() -> str:
    while True:
        ans = faker.country_code()
        if ans in COUNTRIES:
            continue

        COUNTRIES.add(ans)
        conn = engine.connect()
        with conn.begin():
            conn.execute(text("INSERT INTO countries "
                                 "(name, country_id, area_sqkm, population) VALUES "
                                 f"('{faker.name()}', '{ans}', {random.randint(0, 100)}, {random.randint(100, 100000)})"))

        return ans


def create_new_player() -> str:
    id = str(faker.unique.random_int(min=111111, max=999999))
    country_id = random.choice(tuple(COUNTRIES))

    conn = engine.connect()
    with conn.begin():
        conn.execute(text("INSERT INTO players "
                             "(name, player_id, country_id, birthdate) VALUES "
                             f"('{faker.name()}', '{id}', '{country_id}', '{faker.date()}')"))

    return id


def create_new_olimpic() -> str:
    id = str(faker.unique.random_int(min=111111, max=999999))
    country_id = random.choice(tuple(COUNTRIES))
    year = random.randint(2000, 2000)
    start = f"01-01-{year}"
    end = f"05-05-{year}"

    conn = engine.connect()
    with conn.begin():
        conn.execute(text("INSERT INTO olympics "
                             "(olympic_id, country_id, city, year, startdate, enddate) VALUES "
                             f"('{id}', '{country_id}', '{faker.city()}', {year}, '{start}', '{end}')"))

    return id


def create_new_event(n, olimpic_id) -> str:
    event_id = str(faker.unique.random_int(min=111111, max=999999))

    conn = engine.connect()
    with conn.begin():
        conn.execute(text("INSERT INTO events "
                             "(event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES "
                             f"('{str(event_id)}', '{faker.name()}', 'eventType', '{olimpic_id}', 0, {n}, 'bookResult')"))

    return event_id


def create_result(event_id, player_id):
    conn = engine.connect()
    with conn.begin():
        conn.execute(text("INSERT INTO results "
                             "(event_id, player_id, medal, result) VALUES "
                             f"('{event_id}', '{player_id}', '{random.choice(MEDAL_TYPES)}', {float(random.randint(0, 100))})"))


def create_new_record_in_db():
    n = random.randint(3, 10)
    players = []

    # 1. create new countries
    for _ in range(n // 2):
         create_new_country()

    # 2. create new players
    for _ in range(n):
        players.append(create_new_player())

    # 3. create olympiad
    olimpic_id = create_new_olimpic()

    # 4. create event
    event_id = create_new_event(n, olimpic_id)

    # 5. create result
    for player_id in players:
        create_result(event_id, player_id)


def seed(n):
    for _ in range(n):
        create_new_record_in_db()
