class User:
    def __init__(self, data):
        self.id = data.id
        self.is_self = data.is_self
        self.is_contact = data.is_contact
        self.is_mutual_contact = data.is_mutual_contact
        self.is_deleted = data.is_deleted
        self.is_bot = data.is_bot
        self.is_verified = data.is_verified
        self.is_restricted = data.is_restricted
        self.is_scam = data.is_scam
        self.is_fake = data.is_fake
        self.is_support = data.is_support
        self.is_premium = data.is_premium
        self.first_name = data.first_name
        self.last_name = data.last_name
        self.status = data.status
        self.username = data.username
        self.language_code = data.language_code
        self.emoji_status = data.emoji_status
        self.dc_id = data.dc_id
        self.photo = data.photo

