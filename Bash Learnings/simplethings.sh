!/bin/bash
Hello, My name is sweatharaji

greeting="Hello, "
name="sweatharaji"
echo "$greeting My name is $name"

str="Hello"
length=$((expr length '$str))
echo "Length of '$str' is $length"

str="Hello"
length=$(expr length "$str")
echo "Length of '$str' is $length"

a=10
b=15
result=$((a+b))
echo "sum is $result"

result=$(expr 5 / 3)  # using expr keep space arounf the operator 
echo "Output: $result"

a=10
b=20
result=$(expr $a \< $b)
echo "$result"

# new comment added

#!/bin/bash

echo "Choose an option:"
echo "1) Greetings"
echo "2) Show uptime"
echo "3) Exit"

read -p "Enter the Option: " choice
case $choice in
  1)
    echo "Hello, $(whoami)"
    ;;
  2)
    uptime
    ;;
  3)
    exit
    ;;
  *)
    echo "Invalid choice!"
    ;;
esac

# for arithmetic operation must be in (()) eg. count++ is wrong ((cout++)) is correct
#While loop
sum=0
counter=1
 
while [ $counter -le 10 ]; do
  sum=$((sum + counter))
  echo "$counter"
  ((counter++))
  
done
 
echo "The sum of the first 10 natural numbers is: $sum"

#For loop 2 methods

for i in {1..5}
do
    echo "Value: $i"
done

for ((i=0;i<=5;i++)) do
    echo "Count: $i Obtained"
done

#also there is until loop ( until loop repeats till it gets the true value, other loops repeat till they get false value)
# while [ $counter -le 10 ] and until [ $counter -ge 11 ] are same
#Key Difference:
# The while loop runs as long as the condition is true (in this case, counter being less than or equal to 10).
# The until loop runs as long as the condition is false (in this case, counter being less than 10).
