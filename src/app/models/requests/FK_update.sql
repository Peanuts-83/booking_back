--  Update invoice
ALTER TABLE `invoice`
DROP FOREIGN KEY `invoice_ibfk_1`;
ALTER TABLE `invoice`
ADD CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`ref_guest_id`) REFERENCES `guest` (`guest_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `invoice`
DROP FOREIGN KEY `invoice_ibfk_2`;
ALTER TABLE `invoice`
ADD CONSTRAINT `invoice_ibfk_2` FOREIGN KEY (`ref_room_id`) REFERENCES `room` (`room_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--  Update comment
ALTER TABLE `comment`
DROP FOREIGN KEY `comment_ibfk_1`;

ALTER TABLE `comment`
ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`ref_guest_id`) REFERENCES `guest` (`guest_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `comment`
ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`ref_room_id`) REFERENCES `room` (`room_id`) ON DELETE SET NULL ON UPDATE CASCADE;


-- Update booking
ALTER TABLE `booking`
DROP FOREIGN KEY `booking_ibfk_1`;

ALTER TABLE `booking`
ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`ref_guest_id`) REFERENCES `guest` (`guest_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `booking`
DROP FOREIGN KEY `booking_ibfk_2`;

ALTER TABLE `booking`
ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`ref_invoice_id`) REFERENCES `invoice` (`invoice_id`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `booking`
DROP FOREIGN KEY `booking_ibfk_3`;

ALTER TABLE `booking`
ADD CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`ref_room_id`) REFERENCES `room` (`room_id`) ON DELETE SET NULL ON UPDATE CASCADE;
