# Insta Bot Using Python

import instaloader
insta = instaloader.Instaloader()
acc = 'ti_kids_fabrics'

insta.download_profile(acc,profile_pic_only=False)