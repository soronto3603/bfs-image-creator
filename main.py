# main.py
import argparse
from PIL import Image
from lib.bfs_image_creator import BFSImageCreator
import time
import os

def main():
    # argparse를 사용하여 커맨드라인 인자 처리
    parser = argparse.ArgumentParser(description="Generate an image with BFS and color adjustments.")
    parser.add_argument("--width", type=int, default=100, help="Width of the image")
    parser.add_argument("--height", type=int, default=100, help="Height of the image")
    parser.add_argument("--start_color", type=int, nargs=3, default=[200, 200, 200], help="Start color (R, G, B)")
    parser.add_argument("--color_adjustment", type=int, nargs=3, default=[4, 4, 4], help="Color adjustment values (R, G, B)")

    args = parser.parse_args()

    # 시작 시간 측정
    start_time = time.time()

    # 인자로부터 파라미터 설정
    image_size = (args.width, args.height)
    start_color = tuple(args.start_color)
    color_adjustment = tuple(args.color_adjustment)

    # BFSImageCreator 인스턴스 생성 및 이미지 생성
    creator = BFSImageCreator(image_size, start_color, color_adjustment)
    image = creator.create_image()
    
    # 종료 시간 측정 및 실행 시간 계산
    end_time = time.time()
    elapsed_time = end_time - start_time

    # 이미지 저장
    timestamp = int(round(time.time() * 1000))  # 현재 시간의 타임스탬프 (밀리초 단위)
    filename = f"output_{timestamp}.png"
    image.save(filename)

    # 요약 정보 출력
    print(f"Image Shape: {image_size[0]}x{image_size[1]}")
    print(f"Size: {os.path.getsize(filename)} bytes")
    print(f"Pixel Count: {image_size[0] * image_size[1]}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"Save Location: {os.getcwd()}/{filename}")
    print(f"File Name: {filename}")

if __name__ == '__main__':
    main()
