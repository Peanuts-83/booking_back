
BO_LIBELLES = {
    "booking_id": "ID",
    "ref_guest_id": "client",
    "check_in_date": "check in",
    "check_out_date": "check out",
    "num_guests": "nbre de clients",
    "is_checked_in": "est checked in",
    "ref_room_id": "chambre",
    "ref_invoice_id": "facture",
}


def get_lib(name: str):
    try:
        return BO_LIBELLES[name]
    except Exception:
        return 'libellé manquant'