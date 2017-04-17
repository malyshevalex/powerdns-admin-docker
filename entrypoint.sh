#!/bin/bash

sed -i "s|__DB_HOST__|${PDNS_DB_HOST}|g" "${WORK_DIR}/config.py"
sed -i "s|__DB_PASSWORD__|${PDNS_DB_PASSWORD}|g" "${WORK_DIR}/config.py"
sed -i "s|__DB_NAME__|${PDNS_DB_NAME}|g" "${WORK_DIR}/config.py"
sed -i "s|__API_URL__|${PDNS_API_URL}|g" "${WORK_DIR}/config.py"
sed -i "s|__API_KEY__|${PDNS_API_KEY}|g" "${WORK_DIR}/config.py"
sed -i "s|__PDNS_VERSION__|${PDNS_VERSION}|g" "${WORK_DIR}/config.py"

exec "${WORK_DIR}/run.py"

