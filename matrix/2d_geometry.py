from matrix import image_mat_util

def task_4_15_1():
  image_mat_location, image_mat_colors = image_mat_util.file2mat('matrix/meme_avatar.png')
  image_mat_util.mat2display(image_mat_location, image_mat_colors)

task_4_15_1()
