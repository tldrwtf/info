from app.extensions import ma
from app.models import Loans

class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loans
        include_fk = True

loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)