# from instaloader import Instaloader, Profile
import instaloader
from dotenv import load_dotenv
import itertools

import os, glob
# L = instaloader.Instaloader()
load_dotenv()

def fetch_recent_K_photos(K, handle, loader_instance):
    profile = instaloader.Profile.from_username(loader_instance.context, handle)
    posts = profile.get_posts()
    top_K_posts = []
    for p in itertools.islice(posts, K):
        top_K_posts.append(p)

    return top_K_posts


def clean_old_photos(path, num_photos):
    for i in range(num_photos):
        files = glob.glob(path + "/post_" + str(i) + "/*")
        for f in files:
            os.remove(f)

if __name__ == "__main__":

    L = instaloader.Instaloader(dirname_pattern="instagram_posts/{target}", filename_pattern="post")
    handle_to_consider = os.getenv("INSTAGRAM_PUBLIC_HANDLE")
    print(handle_to_consider)
    recent_posts = fetch_recent_K_photos(3, handle_to_consider, L)
    clean_old_photos("instagram_posts", 3)
    
    index = 0
    for post in recent_posts:
        L.download_post(post, target=("post_" + str(index)))
        index += 1
