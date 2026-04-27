from sqlalchemy_utils import JSONType

try:
    from sqlalchemy.dialects.postgresql import JSONB

    has_postgres_jsonb = True
except ImportError:
    has_postgres_jsonb = False


class JSONBType(JSONType):
    def load_dialect_impl(self, dialect):
        pass
