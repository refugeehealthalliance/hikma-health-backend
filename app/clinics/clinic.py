from dataclasses import dataclass
from language_strings.language_string import LanguageString
from client_object import ClientObject
from datetime import datetime
from util import identity, parse_client_timestamp
import clinics.data_access as db


@dataclass
class Clinic(ClientObject):
    id: str
    name: LanguageString
    edited_at: datetime

    def client_insert_values(self):
        return [self.id, self.name.id.replace('-', ''), self.format_ts(self.edited_at)]

    @classmethod
    def client_insert_sql(cls):
        return """INSERT INTO clinics (id, name, edited_at) VALUES (?, ?, ?)"""

    def client_update_values(self):
        return [self.name.id.replace('-', ''), self.format_ts(self.edited_at), self.id]
    
    @classmethod
    def from_id(cls, clinic_id):
        return cls.from_db_row(db.clinic_data_by_id(clinic_id))

    @classmethod
    def from_db_row(cls, db_row):
        id, name, edited_at = db_row
        return cls(id, LanguageString.from_id(name), edited_at)

    @classmethod
    def client_update_sql(cls):
        return """UPDATE clinics SET name = ?, edited_at = ? WHERE id = ?"""    

    def server_insert_values(self):
        return [self.id, self.name.id, self.edited_at]

    @classmethod
    def server_insert_sql(cls):
        return """INSERT INTO clinics (id, name, edited_at) VALUES (%s, %s, %s)"""

    def server_update_values(self):
        return [self.name.id, self.edited_at, self.id]

    @classmethod
    def server_update_sql(cls):
        return """UPDATE clinics SET name =%s, edited_at = %s WHERE id = %s"""

    @classmethod
    def db_columns_from_server(cls):
        return [('id', lambda s: s.replace('-', '')),
                ('name', cls.make_language_string),
                ('edited_at', identity)]

    @classmethod
    def db_columns_from_client(cls):
        return [('id', identity),
                ('name', cls.make_language_string),
                ('edited_at', parse_client_timestamp)]

    @classmethod
    def table_name(cls):
        return "clinics"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name.to_dict(),
            'edited_at': self.edited_at,
        }