#!/usr/bin/env bash

rm -rf allure-results

mkdir -p allure-results

rm -rf allure-report

pytest tests/search_tests.py

allure_gen/bin/allure generate allure-results