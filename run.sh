#!/bin/bash
streamlit run app.py --server.port=${PORT:-8080} --server.address=0.0.0.0 --server.headless=true
