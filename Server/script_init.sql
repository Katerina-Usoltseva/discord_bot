CREATE SCHEMA __python__;
CREATE USER super_user PASSWORD 'qwerty';

CREATE TABLE __python__.writer (writer_id SERIAL PRIMARY KEY, name VARCHAR(64) NOT NULL);

CREATE TABLE __python__.book (book_id SERIAL PRIMARY KEY, writer_id INTEGER NOT NULL, name VARCHAR(64) NOT NULL, 
CONSTRAINT book_writer_id_fkey FOREIGN KEY (writer_id)
REFERENCES __python__.writer (writer_id) MATCH SIMPLE ON UPDATE CASCADE ON DELETE CASCADE);

INSERT INTO __python__.writer (name) 
VALUES 
('Чехов'),
('Толстой'),
('Достоевский');

INSERT INTO __python__.book (writer_id, name) SELECT unnest(array(SELECT writer_id FROM __python__.writer)), 'Интересная книга';

GRANT ALL ON SEQUENCE __python__.book_book_id_seq TO super_user;
GRANT ALL ON SEQUENCE __python__.writer_writer_id_seq TO super_user;
GRANT ALL ON TABLE __python__.book TO super_user;
GRANT ALL ON TABLE __python__.writer TO super_user;
