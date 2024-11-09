boys_one = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls_one = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


boys_two = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls_two = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


def main(boys: list[str], girls: list[str]) -> None:
  try:
    match_groups(boys, girls)
  except Exception:
    print("Внимание, кто-то может остаться без пары!")
  return

def match_groups(boys: list[str], girls: list[str]):
  if len(boys) != len(girls):
    raise Exception
  print("Идеальные пары:")
  sorted_boys = sorted(boys)
  sorted_girls = sorted(girls)
  for index in range(len(boys)):
    print(f"{sorted_boys[index]} и {sorted_girls[index]}")


print("Результат 1\n")
main(boys_one, girls_one)

print("\n")

print("Результат 2\n")
main(boys_two, girls_two)

