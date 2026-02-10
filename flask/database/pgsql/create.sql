CREATE TABLE "app_user" (
  "user_id" integer PRIMARY KEY,
  "name" text,
  "phone_number" text,
  "email" text,
  "is_admin" bool,
  "venue_owner" bool
);

CREATE TABLE "address" (
  "address_id" integer PRIMARY KEY,
  "street_address" text,
  "address_line2" text,
  "city" text,
  "state_province" text,
  "postal_code" text,
  "country" text
);

CREATE TABLE "venue" (
  "venue_id" integer PRIMARY KEY,
  "address_id" integer UNIQUE,
  "name" text,
  "capacity" int,
  "owner_id" int
);

CREATE TABLE "dates_unavailable" (
  "availability_id" integer PRIMARY KEY,
  "venue_id" integer,
  "start_date" date,
  "end_date" date
);

CREATE TABLE "performer" (
  "user_id" integer PRIMARY KEY,
  "band_name" text,
  "type" text,
  "crewsize" integer
);

CREATE TABLE "event_performers" (
  "performer_id" integer,
  "event_id" integer,
  PRIMARY KEY ("performer_id", "event_id")
);

CREATE TABLE "event_info" (
  "event_id" integer PRIMARY KEY,
  "venue_id" integer,
  "name" text,
  "description" text,
  "organizer" integer
);

CREATE TABLE "event_datetime" (
  "event_id" int PRIMARY KEY,
  "start_date" date,
  "end_date" date,
  "start_time" text,
  "end_time" text
);

CREATE TABLE "ticket" (
  "event_id" integer,
  "ticket_id" integer,
  "price" float,
  "ticket_sold" bool,
  PRIMARY KEY ("event_id", "ticket_id")
);

CREATE TABLE "event_organizer" (
  "user_id" integer PRIMARY KEY,
  "speciality" text
);
