

-- Spotlight database views --
---------CMB--------
CREATE VIEW event_time_location AS
  SELECT e.name "event", venue.name venue, start_date, start_time, end_date, end_time
  FROM event_info e
    JOIN venue ON e.venue_id = venue.venue_id
    JOIN event_datetime ON e.event_id = event_datetime.event_id
  ORDER BY start_date, end_date;


--Show which bands bring in the most money based on tickets sold per event--
---------SCS----------------
CREATE VIEW performer_total_income AS
    SELECT ap.name AS name, SUM(ticket.price::numeric)::money AS total
  FROM ticket
    JOIN event_info AS e ON e.event_id = ticket.event_id
      JOIN event_performers AS ep ON ep.event_id = e.event_id
        JOIN performer AS p ON p.user_id = ep.performer_id
			JOIN app_user AS ap ON ap.user_id = p.user_id
  WHERE ticket_sold = TRUE
  GROUP BY ap.name
  ORDER BY total DESC;

--Display tickets that are available for purchase for each event that are under 100 dollars.--
--------IZ-----------------
CREATE VIEW cheap_available_tickets AS
  SELECT t.price, t.ticket_id, e.name AS event_name, v.name AS venue_name, p.band_name
  FROM event_info e
    JOIN ticket t ON e.event_id = t.event_id
    JOIN venue v ON e.venue_id = v.venue_id
    JOIN event_performers ep ON e.event_id = ep.event_id
    JOIN performer p ON p.user_id = ep.performer_id
  WHERE t.price < 100.00 AND t.ticket_sold IS FALSE
  ORDER BY p.band_name;

--Display each performer along with how many tickets remain unsold for their events.--
---------BL----------------
CREATE VIEW performer_unsold_tickets AS
  SELECT
    ap.name,
    e.name AS event_name,
    v.name AS venue_name,
    COUNT(t.ticket_id) AS unsold_tickets
  FROM performer p
    JOIN event_performers ep ON p.user_id = ep.performer_id
    JOIN app_user ap ON ap.user_id = p.user_id
    JOIN event_info e ON ep.event_id = e.event_id
    JOIN venue v ON e.venue_id = v.venue_id
    JOIN ticket t ON e.event_id = t.event_id
  WHERE t.ticket_sold IS FALSE
  GROUP BY ap.name, e.name, v.name
  ORDER BY unsold_tickets DESC;
