import argparse
import os
from os import path as osp
import requests



def download_pretrained_models(method, file_urls):
    save_path_root = f'./weights/{method}'
    os.makedirs(save_path_root, exist_ok=True)

    for file_name, file_url in file_urls.items():
        save_path = load_file_from_url(url=file_url, root=save_path_root, file_name=file_name)
        if save_path != "error":
            print(f"File downloaded successfully to {save_path}")
        else:
            print(f"Failed to download file {file_name} from {file_url}.")


def load_file_from_url(url, root, file_name):
    save_path = os.path.join(root, file_name)
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        return save_path
    else:
        print(f"Failed to download file from {url}. Status code: {response.status_code}")
        return "error"



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'method',
        type=str,
        help=("Options: 'CodeFormer' 'facelib' 'dlib'. Set to 'all' to download all the models."))
    args = parser.parse_args()

    file_urls = {
        'CodeFormer': {
            'codeformer.pth': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth'
        },
        'facelib': {
            # 'yolov5l-face.pth': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/yolov5l-face.pth',
            'detection_Resnet50_Final.pth': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/detection_Resnet50_Final.pth',
            'parsing_parsenet.pth': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/parsing_parsenet.pth'
        },
        'dlib': {
            'mmod_human_face_detector-4cb19393.dat': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/mmod_human_face_detector-4cb19393.dat',
            'shape_predictor_5_face_landmarks-c4b1e980.dat': 'https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/shape_predictor_5_face_landmarks-c4b1e980.dat'
        }
    }

    if args.method == 'all':
        for method in file_urls.keys():
            download_pretrained_models(method, file_urls[method])
    else:
        download_pretrained_models(args.method, file_urls[args.method])