from billy.models.base import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.schema import ForeignKey

from pytz import UTC
from datetime import datetime




class ChargeInvoice(Base):
    __tablename__ = 'charge_invoices'

    invoice_id = Column(Integer, primary_key=True)
    customer_id = Column(String, ForeignKey('customers.customer_id'))
    marketplace = Column(String)
    relevant_plan = Column(String, ForeignKey('plans.plan_id'))
    relevant_coupon = Column(String, ForeignKey('coupons.coupon_id'))
    created_at = Column(DateTime(timezone=UTC), default=datetime.now(UTC))
    start_dt = Column(DateTime(timezone=UTC))
    end_dt = Column(DateTime(timezone=UTC))
    due_dt = Column(DateTime(timezone=UTC))
    amount_base_cents = Column(Integer)
    amount_after_coupon_cents = Column(Integer)
    amount_paid_cents = Column(Integer)
    remaining_balance_cents = Column(Integer)


    def __init__(self, customer_id, marketplace, relevant_plan, relevant_coupon,
                 start_dt, end_dt, due_dt,
                 amount_base_cents, amount_after_coupon_cents,
                 amount_paid_cents, remaining_balance_cents ):
        self.customer_id = customer_id
        self.marketplace = marketplace
        self.relevant_plan = relevant_plan
        self.relevant_coupon = relevant_coupon
        self.start_dt = start_dt
        self.due_dt = due_dt
        self.end_dt = end_dt
        self.amount_base_cents = amount_base_cents
        self.amount_after_coupon_cents = amount_after_coupon_cents
        self.amount_paid_cents = amount_paid_cents
        self.remaining_balance_cents = remaining_balance_cents


class PayoutInvoice(Base):
    __tablename__ = 'payout_invoices'

    invoice_id = Column(Integer, primary_key=True)
    customer_id = Column(String, ForeignKey('customers.customer_id'))
    marketplace = Column(String)
    relevant_payout = Column(String, ForeignKey('plans.plan_id'))
    created_at = Column(DateTime(timezone=UTC), default=datetime.now(UTC))
    payout_date = Column(DateTime(timezone=UTC))
    payout_amount = Column(Integer)
    amount_payed_out = Column(Integer)
    remaining_balance_cents = Column(Integer)


    def __init__(self, customer_id, marketplace, relevant_payout, payout_date,
                 payout_amount, amount_payed_out, remaining_balance_cents):
        self.customer_id = customer_id
        self.marketplace = marketplace
        self.payout_date = payout_date
        self.relevant_payout = relevant_payout
        self.payout_amount = payout_amount
        self.amount_payed_out = amount_payed_out
        self.remaining_balance_cents = remaining_balance_cents