"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from Models.SensorManage import SensorManage
from __main__ import db
from operator import and_, or_

class SensorManageRepository:

    def get_manage_status():
        filter_group = SensorManage.deleted_at.is_(None)
        s_manage_status = SensorManage.query.filter(filter_group).first()

        return s_manage_status