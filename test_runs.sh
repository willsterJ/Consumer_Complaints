# run tests
python3 -m src.consumer_complaints --input ./insight_testsuite/tests/test_1/input/1000set.csv --output ./insight_testsuite/tests/test_1/output/report.csv
echo -e '\n'
sleep 1
python3 -m src.consumer_complaints --input ./insight_testsuite/tests/test_2/input/empty.csv --output ./insight_testsuite/tests/test_2/output/report.csv
echo -e '\n'
sleep 1
python3 -m src.consumer_complaints --input ./insight_testsuite/tests/test_3/input/missingheadings.csv --output ./insight_testsuite/tests/test_3/output/report.csv
echo -e '\n'
sleep 1
python3 -m src.consumer_complaints --input ./insight_testsuite/tests/test_4/input/badcells.csv --output ./insight_testsuite/tests/test_4/output/report.csv