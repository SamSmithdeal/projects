"""Generate fake data for the database."""

import faker
import random
from datetime import datetime, timedelta
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


ADJECTIVES = [
    "Silent",
    "Golden",
    "Electric",
    "Burning",
    "Crimson",
    "Silver",
    "Wild",
    "Neon",
    "Velvet",
    "Lunar",
    "Midnight",
    "Blazing",
    "Radiant",
    "Stormy",
    "Shadowy",
    "Violet",
    "Celestial",
    "Iron",
    "Mystic",
    "Frozen",
    "Glorious",
    "Eternal",
    "Thunderous",
    "Scarlet",
    "Cosmic",
    "Feral",
    "Sapphire",
    "Enchanted",
    "Twilight",
]

EVENT_SPECIALTIES = [
    "Concert Promotion",
    "Music Festival Planning",
    "Charity & Fundraising",
]

EVENT_TYPES = [
    "Show",
    "Performance",
    "Experience",
    "Jam",
    "Session",
    "Night",
    "Rave",
    "Ceremony",
    "Celebration",
    "Spectacle",
    "Extravaganza",
    "Tour",
    "Live",
    "Festival",
    "Concert",
]

MUSIC_SENTENCES = [
    "Experience an unforgettable night with the best live performances.",
    "Get ready to dance to electrifying beats from top artists.",
    "A celebration of music, lights, and energy for fans of all ages.",
    "Join us for a sensational showcase of emerging talent.",
    "Feel the rhythm and vibe as world-class musicians take the stage.",
    "An epic gathering of music lovers, beats, and unforgettable memories.",
    "Enjoy a night filled with soul-stirring melodies and high-energy tracks.",
    "A spectacular event featuring live bands, DJs, and surprise performances.",
    "Celebrate the art of music with immersive sounds and spectacular visuals.",
    "A musical journey that will leave you singing and dancing all night.",
]

NOUNS = [
    "Echo",
    "Horizon",
    "Shadow",
    "Rocket",
    "Wave",
    "Light",
    "Flame",
    "Dream",
    "Sky",
    "Star",
    "Voice",
    "Heart",
    "Dragon",
    "Knight",
    "Thunder",
    "Mirror",
    "Phantom",
    "Lion",
    "Wind",
    "Fire",
    "Serpent",
    "Cloud",
    "Ember",
    "Ocean",
    "Comet",
    "Sun",
    "Moon",
    "Spark",
    "Horizon",
]

STADIUM_ADJECTIVES = [
    "Liberty",
    "National",
    "Grand",
    "Champion",
    "Victory",
    "Eagle",
    "Falcon",
    "Crystal",
    "Electric",
]

STADIUM_TYPES = ["Stadium", "Field", "Arena", "Park", "Dome", "Center"]

VENUE_TYPES = [
    "Theater",
    "Hall",
    "Arena",
    "Pavilion",
    "Center",
    "Lounge",
    "Auditorium",
    "Club",
    "Studio",
]

VENUE_ADJECTIVES = ["Grand", "Royal", "Neon", "Crystal", "Electric", "Silent", "Golden"]

fake = faker.Faker()


def pluralize(word):
    """Simple pluralizer"""
    if word.endswith("s") or word.endswith("x") or word.endswith("z"):
        return word + "es"
    elif word.endswith("y") and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    else:
        return word + "s"


def generate_band_name():
    pattern = random.choice(["the_noun", "adj_noun", "word_and_word", "adj_adj_noun"])

    if pattern == "the_noun":
        noun = random.choice(NOUNS)
        if random.random() < 0.7:
            noun = pluralize(noun)
        return "The " + noun
    elif pattern == "adj_noun":
        return random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
    elif pattern == "word_and_word":
        noun1 = random.choice(NOUNS)
        noun2 = random.choice(NOUNS)
        if random.random() < 0.5:
            noun1 = pluralize(noun1)
        if random.random() < 0.5:
            noun2 = pluralize(noun2)
        return f"{noun1} & {noun2}"
    else:
        return (
            random.choice(ADJECTIVES)
            + " "
            + random.choice(ADJECTIVES)
            + " "
            + random.choice(NOUNS)
        )


def generate_capacity(venue_type=None):
    if venue_type in ["Theater", "Auditorium"]:
        return random.randint(200, 1500)
    elif venue_type in ["Club", "Lounge", "Studio"]:
        return random.randint(50, 300)
    elif venue_type in ["Arena", "Pavilion", "Center"]:
        return random.randint(500, 5000)
    elif venue_type == "Stadium":
        return random.randint(10000, 80000)
    else:
        return random.randint(50, 500)


def generate_music_description(num_sentences=3):
    return " ".join(random.sample(MUSIC_SENTENCES, num_sentences))


def generate_stadium_name(city):
    pattern = random.choice(["adj_type", "city_type", "sponsor_type"])
    if pattern == "adj_type":
        return f"{random.choice(STADIUM_ADJECTIVES)} {random.choice(STADIUM_TYPES)}"
    elif pattern == "city_type":
        return f"{city} {random.choice(STADIUM_TYPES)}"
    else:
        return f"{fake.company()} {random.choice(STADIUM_TYPES)}"


def generate_venue_name():
    pattern = random.choice(["adj_name_type", "name_type", "company_type"])
    if pattern == "adj_name_type":
        return f"{random.choice(VENUE_ADJECTIVES)} {fake.last_name()} {random.choice(VENUE_TYPES)}"
    elif pattern == "name_type":
        return f"{fake.last_name()} {random.choice(VENUE_TYPES)}"
    else:
        return f"{fake.company()} {random.choice(VENUE_TYPES)}"


def main():
    random.seed(0)

    people = []
    event_organizers = []
    admins = []
    performers = []
    venue_owners = []
    addresses = []
    venues = []
    unavs = []
    events = []
    event_performers = []
    tickets = []
    event_dts = []
    avail_ids_used = []

    engine = create_engine("postgresql+psycopg://team24@localhost/team24", echo=False)
    with Session(engine) as session:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        # Adding basic users (not performers/admins/event organizers)
        for x in range(50):
            first_name = fake.first_name()
            last_name = fake.last_name()
            p_name = f"{first_name} {last_name}"

            # creating phone number manually
            area_code = random.randint(100, 999)
            cent_off_code = random.randint(100, 999)
            sub_number = random.randint(1000, 9999)

            p_phone = f"({area_code}) {cent_off_code}-{sub_number}"

            # creating email manually
            p_email = (
                first_name.lower()
                + last_name.lower()
                + str(random.randint(1, 99))
                + "@"
                + fake.free_email_domain()
            )

            p = AppUser(
                name=p_name,
                phone_number=p_phone,
                email=p_email,
                is_admin=False,
                venue_owner=False,
            )
            session.add(p)
            people.append(p)
            session.commit()

        # Adding event organizers
        for x in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            eo_name = f"{first_name} {last_name}"

            # creating phone number manually
            area_code = random.randint(100, 999)
            cent_off_code = random.randint(100, 999)
            sub_number = random.randint(1000, 9999)

            eo_phone = f"({area_code}) {cent_off_code}-{sub_number}"

            # creating email manually
            eo_email = (
                first_name.lower()
                + last_name.lower()
                + str(random.randint(1, 99))
                + "@"
                + fake.free_email_domain()
            )

            eo_specialty = random.choice(EVENT_SPECIALTIES)

            eo = EventOrganizer(
                name=eo_name,
                phone_number=eo_phone,
                email=eo_email,
                is_admin=False,
                venue_owner=False,
                speciality=eo_specialty,
            )
            session.add(eo)
            event_organizers.append(eo)
            session.commit()

        # Adding venue owners
        for x in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            v_name = f"{first_name} {last_name}"

            # creating phone number manually
            area_code = random.randint(100, 999)
            cent_off_code = random.randint(100, 999)
            sub_number = random.randint(1000, 9999)

            v_phone = f"({area_code}) {cent_off_code}-{sub_number}"

            # creating email manually
            v_email = (
                first_name.lower()
                + last_name.lower()
                + str(random.randint(1, 99))
                + "@"
                + fake.free_email_domain()
            )

            v = AppUser(
                name=v_name,
                phone_number=v_phone,
                email=v_email,
                is_admin=False,
                venue_owner=True,
            )
            session.add(v)
            venue_owners.append(v)
            session.commit()

        # Adding admins
        for x in range(5):
            first_name = fake.first_name()
            last_name = fake.last_name()
            a_name = f"{first_name} {last_name}"

            # creating phone number manually
            area_code = random.randint(100, 999)
            cent_off_code = random.randint(100, 999)
            sub_number = random.randint(1000, 9999)

            a_phone = f"({area_code}) {cent_off_code}-{sub_number}"

            # creating email manually
            a_email = (
                first_name.lower()
                + last_name.lower()
                + str(random.randint(1, 99))
                + "@"
                + fake.free_email_domain()
            )

            a = AppUser(
                name=a_name,
                phone_number=a_phone,
                email=a_email,
                is_admin=True,
                venue_owner=False,
            )
            session.add(a)
            admins.append(a)
            session.commit()

        # Adding performers
        for x in range(30):
            # deciding whether solo or band
            if random.random() < 0.5:
                p_type = "Solo Artist"
                first_name = fake.first_name()
                last_name = fake.last_name()
                p_name = f"{first_name} {last_name}"
                p_band_name = None
                p_crew_size = 1
            else:
                p_type = "Band"
                p_name = generate_band_name()
                p_band_name = p_name
                p_crew_size = random.randint(2, 10)

            # creating phone number manually
            area_code = random.randint(100, 999)
            cent_off_code = random.randint(100, 999)
            sub_number = random.randint(1000, 9999)

            p_phone = f"({area_code}) {cent_off_code}-{sub_number}"

            # creating email manually
            if p_type == "Musician":
                p_email = f"{first_name.lower()}{last_name.lower()}{random.randint(1, 99)}@{fake.free_email_domain()}"
            else:
                email_name = (
                    p_name.replace(" ", "").replace("&", "and").replace(".", "").lower()
                )
                p_email = (
                    f"{email_name}{random.randint(1, 99)}@{fake.free_email_domain()}"
                )

            p = Performer(
                name=p_name,
                email=p_email,
                phone_number=p_phone,
                type=p_type,
                crewsize=p_crew_size,
                band_name=p_band_name,
                is_admin=False,
                venue_owner=False,
            )
            session.add(p)
            performers.append(p)
            session.commit()

        # Adding addresses
        for _ in range(10):
            street_num = random.randint(1, 9999)
            street_name = fake.street_name()
            street_suffix = fake.street_suffix()

            address = f"{street_num} {street_name} {street_suffix}"

            addr = Address(
                street_address=address,
                city=fake.city(),
                state_province=fake.state_abbr(),
                postal_code=fake.postalcode(),
                country=fake.current_country(),
            )
            addresses.append(addr)
        session.add_all(addresses)
        session.commit()

        # Adding venues
        for x in range(10):
            if random.random() < 0.2:
                name = generate_stadium_name(addresses[x].city)
                venue_type = "Stadium"
            else:
                name = generate_venue_name()
                venue_type = next((t for t in VENUE_TYPES if t in name), None)

            capacity = generate_capacity(venue_type)

            ven = Venue(
                name=name,
                capacity=capacity,
                address_id=addresses[x].address_id,
                owner_id=venue_owners[x].user_id,
            )
            venues.append(ven)
        session.add_all(venues)
        session.commit()

        # Adding dates unavailable
        for _ in range(9):
            for ven in venues:
                start_date = datetime.datetime(2026, 1, 1) + timedelta(
                    days=random.randint(0, 365)
                )
                end_date = start_date + timedelta(weeks=1)
                unav = DatesUnavailable(
                    venue_id=ven.venue_id,
                    start_date=start_date,
                    end_date=end_date,
                )
                unavs.append(unav)
        session.add_all(unavs)
        session.commit()

        # Adding events
        for _ in range(20):
            venue = random.choice(venues)
            event_organizer = random.choice(event_organizers)

            event_type = random.choice(EVENT_TYPES)
            event_name = f"{fake.word().capitalize()} {event_type}"

            event = EventInfo(
                venue_id=venue.venue_id,
                name=event_name,
                description=generate_music_description(
                    num_sentences=random.randint(1, 3)
                ),
                organizer=event_organizer.user_id,
            )

            events.append(event)
        session.add_all(events)
        session.commit()

        # Adding event performers
        for event in events:
            num_performers = random.randint(1, 5)
            assigned = set()
            while len(assigned) < num_performers:
                performer = random.choice(performers)
                if performer not in assigned:
                    event.performer.append(performer)
                    assigned.add(performer)
        session.commit()

        # Tickets
        for event in events:
            venue = next(v for v in venues if v.venue_id == event.venue_id)

            # Determine price based on venue size
            if venue.capacity >= 10000:  # stadium
                event_price = round(random.triangular(50, 300, 150), 2)
            elif venue.capacity >= 500:  # medium
                event_price = round(random.triangular(25, 175, 100), 2)
            else:  # small
                event_price = round(random.triangular(15, 100, 50), 2)

            # Create tickets for this event
            for ticket_id in range(1, venue.capacity // 3):
                ticket = Ticket(
                    event_id=event.event_id,
                    ticket_id=ticket_id,
                    price=event_price,
                    ticket_sold=random.random() < 0.7,
                )
                tickets.append(ticket)
        session.add_all(tickets)
        session.commit()

        # Event_datetime
        for event in events:
            venue_unavs = [u for u in unavs if u.venue_id == event.venue_id]

            # Try to find a date not in any unavailable period
            for attempt in range(50):
                start_date = (
                    datetime.datetime(2026, 1, 1)
                    + timedelta(days=random.randint(0, 364))
                ).date()
                duration_days = random.randint(1, 3)
                end_date = start_date + timedelta(days=duration_days - 1)

                # Check if it overlaps any unavailable date
                overlap = False
                for u in venue_unavs:
                    if start_date <= u.end_date and end_date >= u.start_date:
                        overlap = True
                        break

                if not overlap:
                    start_hour = random.randint(12, 18)
                    end_hour = random.randint(start_hour + 2, min(start_hour + 8, 23))
                    start_time = f"{start_hour:02d}:00"
                    end_time = f"{end_hour:02d}:59"

                    dt = EventDatetime(
                        event_id=event.event_id,
                        start_date=start_date,
                        end_date=end_date,
                        start_time=start_time,
                        end_time=end_time,
                    )
                    event_dts.append(dt)
                    break
        session.add_all(event_dts)
        session.commit()


if __name__ == "__main__":
    main()
