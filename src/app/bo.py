
BO_LIBELLES = {
    "id": "ID",
    "guest_id": "client",
    "room_id": "chambre",
    "invoice_id": "facture",
    "check_in_date": "check in",
    "check_out_date": "check out",
    "num_guests": "nbre de clients",
    "is_checked_in": "est checked in",
    "room_id": "chambre",
    "comment_date": "date",
    "comment_rating": "note",
    "comment_text": "commentaire",
    "first_name": "prénom",
    "last_name": "nom",
    "age": "age",
    "country": "pays",
    "phone_number": "téléphone",
    "email": "email",
    "gold_card_member": "membre gold",
    "invoice_date": "date de facturation",
    "total_amount": "montant",
    "payment_method": "mode de paiement",
    "due_date": "aaa",
    "item_description": "détails",
    "quantity": "quantité",
    "room_type": "type de chambre",
    "price_per_night": "prix unitaire",
    "availability": "disponibilité",
}


def get_lib(name: str):
    try:
        return BO_LIBELLES[name]
    except Exception:
        return 'libellé manquant'