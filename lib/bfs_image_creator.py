from PIL import Image
from queue import Queue
import random
from random import choice

class BFSImageCreator:
  def __init__(self, image_size, start_color, color_adjustment):
      self.image_size = image_size
      self.start_color = start_color
      self.color_adjustment = color_adjustment
      self.image = Image.new('RGB', image_size, "white")
      self.visited = set()

  def adjust_color(self, color):
      # 색상 조정 로직에 랜덤성 추가
      adjusted_color = []
      for c, a in zip(color, self.color_adjustment):
          random_adjustment = random.randint(-a, a)  # 색상 조정값을 랜덤하게 결정 (-a ~ a)
          new_color = min(max(0, c + random_adjustment), 255)  # 색상 값이 0과 255 사이의 값을 유지하도록 조정
          adjusted_color.append(new_color)
      return tuple(adjusted_color)
  
  def is_valid_pixel(self, position):
      # 픽셀 위치가 유효한지 확인
      x, y = position
      return 0 <= x < self.image_size[0] and 0 <= y < self.image_size[1]

  

  def create_image(self):
      start_position = (self.image_size[0] // 2, self.image_size[1] // 2)
      queue = [(start_position, self.start_color)]
      self.visited.add(start_position)

      total_pixels = self.image_size[0] * self.image_size[1]
      processed_pixels = 0

      while queue:
          # 리스트에서 랜덤한 위치의 아이템 선택 및 제거
          index = random.randrange(len(queue))
          (x, y), color = queue.pop(index)
          self.image.putpixel((x, y), color)
          new_color = self.adjust_color(color)
          processed_pixels += 1

          # 진행 상황 출력 (옵션)
          if processed_pixels % (total_pixels // 100) == 0:
              print(f"Progress: {(processed_pixels / total_pixels) * 100:.2f}%")

          for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
              new_position = (x + dx, y + dy)
              if self.is_valid_pixel(new_position) and new_position not in self.visited:
                  queue.append((new_position, new_color))
                  self.visited.add(new_position)

      return self.image
