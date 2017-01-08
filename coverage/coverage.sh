covered=`coverage report -m --skip-covered | grep TOTAL | awk '{print $4}' | tr -d "%"`
coverage report -m > coverage.txt
exit $((100 - ${covered}))

