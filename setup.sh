touch data/day${1}.txt
touch data/day${1}_test.txt
cp template.py day$1.py
sed -i '' "s/dayN/day$1/g" "day$1.py"
