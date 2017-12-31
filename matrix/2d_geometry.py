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

task_4_15_4()
