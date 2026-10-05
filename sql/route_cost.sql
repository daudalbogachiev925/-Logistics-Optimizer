-- Стоимость маршрута
SELECT r.id,
    SUM(s.distance_km * v.cost_per_km + v.base_fee) AS cost
FROM routes r
JOIN shipments s ON s.route_id = r.id
JOIN vehicles v ON v.id = r.vehicle_id
GROUP BY r.id
ORDER BY cost DESC;
