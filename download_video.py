import os
import youtube_dl
import get_data # 동일 폴더 내에 생성한 youtube top 100 리스트 추출 코드!

VIDEO_DOWNLOAD_PATH = '/Users/janet/Desktop/youtube/video'  # 다운로드 경로

def download_video_and_subtitle(output_dir, youtube_video_list):

    download_path = os.path.join(output_dir, '%(id)s-%(title)s.%(ext)s')

    for video_url in youtube_video_list:

        # youtube_dl options
        ydl_opts = {
            'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
            'outtmpl': download_path, # 다운로드 경로 설정
            'writethumbnail': 'best',  # 영상 thumbnail 다운로드
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            print('error', e)


if __name__ == '__main__':

    youtube_url_list=[]
    youtube_url_list.append(get_data.tester_url[0])
    youtube_url_list.append(get_data.tester_url[1])

    download_video_and_subtitle(VIDEO_DOWNLOAD_PATH, youtube_url_list)
    print('Complete download!')