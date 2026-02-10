--------------------IZ-------------------------------
SELECT * FROM User
    JOIN performer ON user.user_id = performer.id
WHERE performer.crew_size < 20

SELECT * FROM Venue
WHERE capacity > 1000
ORDER BY name DESC LIMIT 20

--------------------CB-------------------------------
SELECT user_id, COUNT(*) AS 'venues owned' 
FROM venue_owner
GROUP BY user_id
ORDER BY COUNT(*) DESC

SELECT user_id, venue.capacity
FROM venue_owner
    JOIN venue ON venue.venue_id = venue_owner.venue
ORDER BY venue.capacity DESC
LIMIT 10

--------------------SS-------------------------------
--selects all events where the ticket price is less than $200
--and the date is sept 1st 2025
SELECT * FROM event
  JOIN ticket ON event.event_id = ticket.event_id
WHERE event.date = '2025-09-01' AND ticket.price < 200.00


--selects all events that elton john is preforming at
SELECT * FROM event 
  JOIN event_preformers ON event.event_id = event_preformers.event_id
  JOIN preformer ON event_preformers.preformer_id = preformer.user_id 
  JOIN user ON preformer.user_id = user.user_id
WHERE user.name = 'Elton John'

--------------------BL-------------------------------
SELECT venue.name, address.street_address
FROM venue
    JOIN venue_availability USING (venue_id)
    JOIN address USING (address_id)
WHERE start_date > '2025-10-01'
ORDER BY start_date

SELECT tickets_sold, name
FROM event
WHERE tickets_sold > 10000
ORDER BY tickets_sold DESC
