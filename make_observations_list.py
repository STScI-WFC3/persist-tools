#! /usr/bin/env python

import os

from database_interface import session
from database_interface import Master
from database_interface import IR_FLT_0

query = session.query(Master, IR_FLT_0).\
    join(IR_FLT_0, Master.id == IR_FLT_0.id).\
    order_by(IR_FLT_0.EXPSTART).all()


test = True
if test:
    
for record in query[0:25]:
    print os.path.join(record.Master.dir, record.Master.filename)
