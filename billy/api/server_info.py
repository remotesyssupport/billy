from __future__ import unicode_literals

from pyramid.view import view_config

from billy.models.transaction import TransactionModel
from billy.utils.generic import get_git_rev


@view_config(route_name='server_info', 
             request_method='GET', 
             renderer='json')
def server_info(request):
    """Get server information

    """
    tx_model = TransactionModel(request.session)
    last_transaction = tx_model.get_last_transaction()
    last_transaction_dt = None
    if last_transaction is not None:
        last_transaction_dt = last_transaction.created_at.isoformat()
    return dict(
        server='Billy - The recurring payment server',
        powered_by='BalancedPayments.com',
        revision=get_git_rev(),
        last_transaction_created_at=last_transaction_dt,
    )