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
