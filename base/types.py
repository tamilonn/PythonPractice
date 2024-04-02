from typing import TypeAlias

Scalar = int
Vector = list[Scalar]

print(type(Scalar), type(Vector))

print('------------------------------')

#Type aliases
Scalar: TypeAlias = int
Vector: TypeAlias = list[float]

print(type(Scalar), type(Vector))

print('--------------------------')

#Parameter with return values
Scalar: TypeAlias = int
Vector: TypeAlias = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
  return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

print('--------------------------')

#Generics: needs python 3.12 or newer
# def first[T](l: list[T]) -> T:
#   return l[0]

# print(first[list[int]]([1, 2, 3])
# print(first[list[float]]([1.0, 2.0, 3.0])
# print(first[tuple[int]]((1, 2, 3))



