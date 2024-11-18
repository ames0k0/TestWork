from sqlalchemy.orm import Session

from src.core.schemas import InsuranceCalculationRequestIN
from . import models


class InsuranceCalculationRequest:
    @staticmethod
    def add(db: Session, data: InsuranceCalculationRequestIN):
        db.add(
            models.InsuranceCalculationRequest(
                cargo_type=data.cargo_type,
                declared_value=data.declared_value,
                cost_of_insurance=data.cost_of_insurance,
                insurance_rate_date=data.insurance_rate_date,
                insurance_rate=data.insurance_rate,
                request_dt=data.request_dt,
                response_dt=data.response_dt,
            )
        )
        db.commit()

    @staticmethod
    def load_least_n(db: Session, limit: int = 10):
        return db.query(
            models.InsuranceCalculationRequest
        ).order_by(
            models.InsuranceCalculationRequest.id.desc()
        ).limit(limit)
