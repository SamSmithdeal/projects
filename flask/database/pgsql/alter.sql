ALTER TABLE "venue" ADD FOREIGN KEY ("address_id") REFERENCES "address" ("address_id");

ALTER TABLE "venue" ADD FOREIGN KEY ("owner_id") REFERENCES "app_user" ("user_id");

ALTER TABLE "dates_unavailable" ADD FOREIGN KEY ("venue_id") REFERENCES "venue" ("venue_id");

ALTER TABLE "performer" ADD FOREIGN KEY ("user_id") REFERENCES "app_user" ("user_id");

ALTER TABLE "event_performers" ADD FOREIGN KEY ("performer_id") REFERENCES "performer" ("user_id");

ALTER TABLE "event_performers" ADD FOREIGN KEY ("event_id") REFERENCES "event_info" ("event_id");

ALTER TABLE "event_info" ADD FOREIGN KEY ("venue_id") REFERENCES "venue" ("venue_id");

ALTER TABLE "event_info" ADD FOREIGN KEY ("organizer") REFERENCES "event_organizer" ("user_id");

ALTER TABLE "event_datetime" ADD FOREIGN KEY ("event_id") REFERENCES "event_info" ("event_id");

ALTER TABLE "ticket" ADD FOREIGN KEY ("event_id") REFERENCES "event_info" ("event_id");

ALTER TABLE "event_organizer" ADD FOREIGN KEY ("user_id") REFERENCES "app_user" ("user_id");
