
BO_LIBELLES = {
    "booking_id": "ID",
    "ref_guest_id": "Client",
    "check_in_date": "Check in",
    "check_out_date": "Check out",
    "num_guests": "Nbre de clients",
    "is_checked_in": "Est checked in",
    "ref_room_id": "Chambre",
    "ref_invoice_id": "Facture",
}


def get_lib(name: str):
    return BO_LIBELLES[name]