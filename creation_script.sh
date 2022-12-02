generate_file()
{
  # $1 -> part number
  # $2 -> day number

   echo "from common import *" > part_$1.py
   echo "" >> part_$1.py
   echo "" >> part_$1.py
   echo "class Part_$1(BaseClass):" >> part_$1.py
   echo "" >> part_$1.py
   echo "    def __init__(self):" >> part_$1.py
   echo "        super().__init__("$((10#$2))")" >> part_$1.py
   echo "" >> part_$1.py
   echo "    def execute_internal(self, filepath):" >> part_$1.py
   echo "        print(open_file(filepath))" >> part_$1.py
   echo "" >> part_$1.py
   echo "        return -1" >> part_$1.py
   echo "" >> part_$1.py
   echo "" >> part_$1.py
   echo "p$1 = Part_$1()" >> part_$1.py
   echo "p$1.test(0)" >> part_$1.py
   echo "p$1.execute()" >> part_$1.py
   echo "" >> part_$1.py

}

mkdir "programs"
mkdir "input_files"

for day in $(seq -f "%02g" 1 25)
do
	mkdir "input_files/day_$day"
	cd "input_files/day_$day"
	touch input.txt
	touch example.txt

	cd ../..

	mkdir "programs/day_$day"
	cd "programs/day_$day"
	generate_file "1" "$day"
	generate_file "2" "$day"

	cd ../..
done