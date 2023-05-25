from PIL import Image
from flaskblog import app
import secrets,os


# ========================================================
# ===============REDUCE PICTURE QUALITY AND SAVE =========
# ========================================================



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profilePic',picture_fn)
    
    output_size = (70,70)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

