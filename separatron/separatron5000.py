import os
import argparse
from keys import keybindings
import cv2
import shutil


def list_files(path):
    if not os.path.isdir(path):
        print('Fatal error: {} is not a valid folder'.format(path))
        exit(1)
    array = [x for x in os.listdir(path)]
    array = sorted(array)
    return array


def check_dest_folder(path_to_folder):
    if not os.path.isdir(path_to_folder):
        print('Destination path not found, creating new folder at {}.'.format(path_to_folder))
        os.mkdir(path_to_folder)
    return


def cv2_load_image(image, current_image, total_images):
    img = cv2.imread(image, 1)
    cv2.namedWindow('Separatron 5000', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Separatron 5000', 640, 480)
    cv2.rectangle(img, (0, 0), (100, 50), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, '{}/{}'.format(current_image + 1, total_images), (10, 30), cv2.FONT_HERSHEY_PLAIN, 1.3, 0)
    cv2.imshow('Separatron 5000', img)
    return


def copy_file(src, dest):
    shutil.copy(src, dest)
    print('Copied from {} to {}'.format(src, dest))
    return


def do_main_loop(images, images_source_path, save_folder_path):
    cur_img = 0
    total_images = len(images)
    while 1:
        # First image load
        cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)
        key = cv2.waitKey(1) & 0xFF
        # if key != 255:
        #    print('DEBUG: USER PRESSED {}'.format(key))

        if key == keybindings['advance-1-image']:
            cur_img += 1
            if cur_img >= len(images):
                cur_img -= 1
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['advance-10-images']:
            cur_img += 10
            if cur_img >= len(images):
                cur_img = len(images) - 1
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['advance-100-images']:
            cur_img += 100
            if cur_img >= len(images):
                cur_img = len(images) - 1
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['advance-1000-images']:
            cur_img += 1000
            if cur_img >= len(images):
                cur_img = len(images) - 1
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['return-1-image']:
            cur_img -= 1
            if cur_img < 0:
                cur_img = 0
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['return-10-images']:
            cur_img -= 10
            if cur_img < 0:
                cur_img = 0
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['return-100-images']:
            cur_img -= 100
            if cur_img < 0:
                cur_img = 0
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['return-1000-images']:
            cur_img -= 1000
            if cur_img < 0:
                cur_img = 0
            cv2_load_image(os.path.join(images_source_path, images[cur_img]), cur_img, total_images)

        elif key == keybindings['save-image']:
            copy_file(os.path.join(images_source_path, images[cur_img]), os.path.join(save_folder_path, images[cur_img]))
            dest_folder_files = [x for x in os.listdir(save_folder_path)]
            print('Images on destination folder: {}'.format(len(dest_folder_files)))
        elif key == keybindings['exit-application']:
            cv2.destroyAllWindows()
            return
    return


def main(origin_path, dest_path):
    print('Main received origin path: {}, dest path: {}'.format(origin_path, dest_path))
    files = list_files(origin_path)
    if not files:
        print('Error: empty folder!')
        exit(1)
    check_dest_folder(dest_path)
    do_main_loop(files, origin_path, dest_path)
    return


parser = argparse.ArgumentParser(description='Description')
parser.add_argument('path_origin', type=str, help='Path to source images')
parser.add_argument('path_dest', type=str, help='Destination folder')

args = parser.parse_args()

if __name__ == '__main__':
    main(args.path_origin, args.path_dest)
