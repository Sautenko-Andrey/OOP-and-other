BEGIN TRANSACTION;CREATE TABLE cars (
                car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                price INTEGER);DELETE FROM "sqlite_sequence";COMMIT;