from matrix import image_mat_util, matutil
from vector import vecutil
from vec import Vec
from mat import Mat
import math

def task_4_15_1():
  image_mat_location, image_mat_colors = image_mat_util.file2mat('matrix/meme_avatar.png')
  image_mat_util.mat2display(image_mat_location, image_mat_colors)

# task_4_15_1()

def identity():
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}), {
        ("x", "x"): 1,
        ("x", "y"): 0,
        ("x", "u"): 0,

        ("y", "x"): 0,
        ("y", "y"): 1,
        ("y", "u"): 0,

        ("u", "x"): 0,
        ("u", "y"): 0,
        ("u", "u"): 1,
    })

def task_4_15_2():
  test_point = Vec({"x", "y", "u"}, {"x": 2, "y": 1.5, "u": 1})
  against_point = identity() * test_point
  assert(against_point == test_point)

  image_mat_location, image_mat_colors = image_mat_util.file2mat('matrix/meme_avatar.png')
  ident_location = (identity() * image_mat_location)
  assert(ident_location == image_mat_location)

# task_4_15_2()

def translation(alpha, beta):
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}), {
        ("x", "x"): 1,
        ("x", "y"): 0,
        ("x", "u"): alpha,

        ("y", "x"): 0,
        ("y", "y"): 1,
        ("y", "u"): beta,

        ("u", "x"): 0,
        ("u", "y"): 0,
        ("u", "u"): 1,
    })

def task_4_15_3():
  test_point = Vec({"x", "y", "u"}, {"x": 2, "y": 1.5, "u": 1})
  against_point = translation(1, 2) * test_point
  expected = Vec({"x", "y", "u"}, {"x": test_point["x"] + 1, "y": test_point["y"] + 2, "u": 1})
  assert(against_point == expected)
  image_mat_location, image_mat_colors = image_mat_util.file2mat('matrix/meme_avatar.png')
  translated_location = (translation(20, 20) * image_mat_location)
  image_mat_util.mat2display(translated_location, image_mat_colors)  

# task_4_15_3()

def scale(alpha, beta):
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}), {
      ("x", "x"): alpha,
      ("x", "y"): 0,
      ("x", "u"): 0,

      ("y", "x"): 0,
      ("y", "y"): beta,
      ("y", "u"): 0,

      ("u", "x"): 0,
      ("u", "y"): 0,
      ("u", "u"): 1,
  })

def task_4_15_4():
  test_point = Vec({"x", "y", "u"}, {"x": 2, "y": 1.5, "u": 1})
  against_point = scale(2, 2) * test_point
  expected = Vec({"x", "y", "u"}, {"x": test_point["x"] * 2, "y": test_point["y"] * 2, "u": 1})
  assert(against_point == expected)
  image_mat_location, image_mat_colors = image_mat_util.file2mat('matrix/meme_avatar.png')
  scaled_location = (scale(2, 2) * image_mat_location)
  image_mat_util.mat2display(scaled_location, image_mat_colors) 

# task_4_15_4()

def rotation(theta):
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}), {
      ("x", "x"): math.cos(theta),
      ("x", "y"): -math.sin(theta),
      ("x", "u"): 0,

      ("y", "x"): math.sin(theta),
      ("y", "y"): math.cos(theta),
      ("y", "u"): 0,

      ("u", "x"): 0,
      ("u", "y"): 0,
      ("u", "u"): 1,
  })

def task_4_15_5():
  theta = math.pi/4
  test_point = Vec({"x", "y", "u"}, {"x": math.cos(theta), "y": math.sin(theta), "u": 1})
  rotated_point = rotation(theta) * test_point
  expected = Vec({"x", "y", "u"}, {"x": 0, "y": 1, "u": 1})
  print(rotated_point, expected)
  assert(round(rotated_point["x"]) == expected["x"])
  assert(round(rotated_point["y"]) == expected["y"])

  image_mat_location, image_mat_colors = image_mat_util.file2mat('matrix/meme_avatar.png')
  rotated_location = (translation(100, 100) * rotation(math.pi / 4) * image_mat_location)
  image_mat_util.mat2display(rotated_location, image_mat_colors)  

# task_4_15_5()

def rotation_about(theta, x, y):
  return rotation(theta) * translation(x, y)

def reflect_Y():
  return Mat(({"x", "y", "u"}, {"x", "y", "u"}), {
    ("x", "x"): -1,
    ("x", "y"): 0,
    ("x", "u"): 0,

    ("y", "x"): 0,
    ("y", "y"): 1,
    ("y", "u"): 0,

    ("u", "x"): 0,
    ("u", "y"): 0,
    ("u", "u"): 1,
  })

def reflect_X():
  return Mat(({"x", "y", "u"}, {"x", "y", "u"}), {
    ("x", "x"): 1,
    ("x", "y"): 0,
    ("x", "u"): 0,

    ("y", "x"): 0,
    ("y", "y"): -1,
    ("y", "u"): 0,

    ("u", "x"): 0,
    ("u", "y"): 0,
    ("u", "u"): 1,
  })

def scale_color(r, g, b):
  return Mat(({"r", "g", "b"}, {"r", "g", "b"}), {
    ("r", "r"): r,
    ("r", "g"): 0,
    ("r", "b"): 0,

    ("g", "r"): 0,
    ("g", "g"): g,
    ("g", "b"): 0,

    ("b", "r"): 0,
    ("b", "g"): 0,
    ("b", "b"): b,
  })

def grayscale():
  return Mat(({"r", "g", "b"}, {"r", "g", "b"}), {
    ("r", "r"): 77/256,
    ("r", "g"): 151/256,
    ("r", "b"): 28/256,

    ("g", "r"): 77/256,
    ("g", "g"): 151/256,
    ("g", "b"): 28/256,

    ("b", "r"): 77/256,
    ("b", "g"): 151/256,
    ("b", "b"): 28/256,
  })

def test_grayscale():
  image_mat_location, image_mat_colors = image_mat_util.file2mat('matrix/meme_avatar.png')
  gray_colors = grayscale() * image_mat_colors
  image_mat_util.mat2display(image_mat_location, gray_colors)  

test_grayscale()
