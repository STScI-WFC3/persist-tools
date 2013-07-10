#! /usr/bin/env python

import glob
import os

from database_interface import session
from database_interface import Master
from database_interface import IR_FLT_0

query = session.query(Master, IR_FLT_0).\
    join(IR_FLT_0, Master.id == IR_FLT_0.id).\
    order_by(IR_FLT_0.EXPSTART)

test = True
if test:
    
    sorted_local_files = []
    local_file_list = glob.glob('../data/*/Visit*/*.fits')
    for local_file in local_file_list:
        local_query = query.filter(Master.filename == os.path.basename(local_file)).one()
        sorted_local_files.append((local_file, local_query.IR_FLT_0.EXPSTART)) 
    #for record in query[0:25]:
    #    print os.path.join(record.Master.dir, record.Master.filename)


    sorted_local_files = sorted(sorted_local_files, key=lambda item : item[1])

    with open('per_list.txt', 'w') as f:
        for line in sorted_local_files:
            f.write(line[0] + '\n')