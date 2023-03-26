#!/bin/bash
echo "Adding users to the system..."
if [[ "`hostname`" == "headnode" ]]; then
    echo "headnode."
    USERADD_FLAG="-m"
else
    echo "computenode."
    USERADD_FLAG="-M"
fi
USERADD_FLAG="${USERADD_FLAG} -N -g users"

# for i in range(100):
#     print(f"useradd ${{USERADD_FLAG}} -u {10000+i:d} -s /bin/bash user{i:03d} && echo 'user{i:03d}:user' |chpasswd")
useradd ${USERADD_FLAG} -u 10001 -s /bin/bash user-001 && echo 'user-001:user' |chpasswd
useradd ${USERADD_FLAG} -u 10002 -s /bin/bash user-002 && echo 'user-002:user' |chpasswd
useradd ${USERADD_FLAG} -u 10003 -s /bin/bash user-003 && echo 'user-003:user' |chpasswd
useradd ${USERADD_FLAG} -u 10004 -s /bin/bash user-004 && echo 'user-004:user' |chpasswd
useradd ${USERADD_FLAG} -u 10005 -s /bin/bash user-005 && echo 'user-005:user' |chpasswd

