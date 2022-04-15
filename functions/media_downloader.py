from urllib.parse import urlparse

# DOWNLOADING MEDIAS
# ------------------------------------
# download an image from an url.
def download_image(link, media_folder):
    pass
# download multiple image from a list
def download_multiple_image(links, media_folder):
    pass
# download 
def download_video(video, audio, media_folder):
    pass

# FETCHING LINKS
# ------------------------------------
# explore reddit gallery and return links to media
def galery_explorer(sumission, max=4):
    pass
# explore reddit video and return links to the right stream.
def video_explorer(submission, max=512):
    # 512 MB masx
    pass

# ROOTING
# ------------------------------------
# returns links to the media.
def media_rooter(submission):
    hostame = urlparse(submission['url']).hostname
    
    if 'v.redd.it' in hostame:
        return {
            'type': 'video',
            'audio': 'tbd',
            'video': video_explorer(submission)
        }
    elif 'i.redd.it' in hostame:
        return {
            'type': 'image',
            'link': hostame
        }
    elif 'i.imgur.com' in hostame:
        return {
            'type': 'imgure',
            'link': hostame
        }
    elif 'gallery' in hostame:
        return {
            'type': 'gallery',
            'links': galery_explorer(submission)
        }
    else:
        return {
            'type': 'unsupported',
            'error': f"{hostame} is unsupported"
        }
    