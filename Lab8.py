"""
Lab 8: Functions
"""
#3.1
def word_count(input_str):
    return len(input_str.split())
#3.2
demo_str = "Hello, World!"
print(word_count(demo_str))
#3.2: Extra Practice
the_batman = "Scarecrow and the Riddler"
print(word_count(the_batman))
#3.3
def min_item(input_list):
  min_item = input_list[0]
  for num in input_list:
      if type(num) is not str:
       if min_item>= num:
          min_item = num
  return min_item
#3.4
demo_list = [1, 2, 3, 4, 5, 6]
print(min_item(demo_list))
#3.5
mix_list = [1, 2, 3, 4, "a", 5, 6]
print(min_item(mix_list))
    