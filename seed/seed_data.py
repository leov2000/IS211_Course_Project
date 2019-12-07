import sqlite3
import json
from werkzeug.security import generate_password_hash

def hashed_user_password(user_dict):
    return {
            k: generate_password_hash(v) if k == 'password' else v for k,v in user_dict.items()
        }

def iterate_and_hash(user_list):
    return [hashed_user_password(user) for user in user_list]

def seed_user_data():
    with open('user_keys.json') as user_info:
        users_json = json.load(user_info)
    
    user_list = users_json['users']
    hashed_list = iterate_and_hash(user_list)
    [user_one, user_two] = hashed_list

    user_insert = f"""
    INSERT INTO users
    (user_name, users_password)    
    VALUES
    ('{user_one['username']}','{user_one['password']}'),
    ('{user_two['username']}','{user_one['password']}');
    """

    return user_insert

def seed_blog_posts_data():
    blog_insert = """
    INSERT INTO posts
    (users_id, title, category, ishidden, published, content)
    VALUES
    (1, 'The first time I saw basketball on TV', 'sports', 'true', '2019-11-28',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat. Faucibus pulvinar elementum integer enim neque volutpat. Tincidunt eget nullam non nisi est sit amet facilisis. Aliquet porttitor lacus luctus accumsan tortor posuere ac ut. In aliquam sem fringilla ut morbi tincidunt augue. Etiam erat velit scelerisque in dictum non consectetur. Morbi tristique senectus et netus et malesuada fames. Molestie nunc non blandit massa enim. Vivamus arcu felis bibendum ut. Eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis. Tristique senectus et netus et malesuada fames. Ut sem viverra aliquet eget sit amet tellus cras. Nibh sed pulvinar proin gravida. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus.

    Magna fringilla urna porttitor rhoncus dolor purus non enim praesent. Semper eget duis at tellus. Ullamcorper malesuada proin libero nunc. Ipsum dolor sit amet consectetur adipiscing elit. Odio pellentesque diam volutpat commodo sed. Nibh ipsum consequat nisl vel pretium lectus quam id. Dolor morbi non arcu risus quis. Velit dignissim sodales ut eu. Amet massa vitae tortor condimentum lacinia quis vel eros. Consequat mauris nunc congue nisi vitae. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. Ultrices eros in cursus turpis massa tincidunt. Sollicitudin nibh sit amet commodo nulla facilisi nullam. Sagittis id consectetur purus ut. Sed turpis tincidunt id aliquet. Ut lectus arcu bibendum at varius vel pharetra vel turpis.'),
    (1, 'acrylic socks vs cotton socks', 'lifestyle', 'true', '2019-11-26',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat. Faucibus pulvinar elementum integer enim neque volutpat. Tincidunt eget nullam non nisi est sit amet facilisis. Aliquet porttitor lacus luctus accumsan tortor posuere ac ut. In aliquam sem fringilla ut morbi tincidunt augue. Etiam erat velit scelerisque in dictum non consectetur. Morbi tristique senectus et netus et malesuada fames. Molestie nunc non blandit massa enim. Vivamus arcu felis bibendum ut. Eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis. Tristique senectus et netus et malesuada fames. Ut sem viverra aliquet eget sit amet tellus cras. Nibh sed pulvinar proin gravida. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus.

    Magna fringilla urna porttitor rhoncus dolor purus non enim praesent. Semper eget duis at tellus. Ullamcorper malesuada proin libero nunc. Ipsum dolor sit amet consectetur adipiscing elit. Odio pellentesque diam volutpat commodo sed. Nibh ipsum consequat nisl vel pretium lectus quam id. Dolor morbi non arcu risus quis. Velit dignissim sodales ut eu. Amet massa vitae tortor condimentum lacinia quis vel eros. Consequat mauris nunc congue nisi vitae. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. Ultrices eros in cursus turpis massa tincidunt. Sollicitudin nibh sit amet commodo nulla facilisi nullam. Sagittis id consectetur purus ut. Sed turpis tincidunt id aliquet. Ut lectus arcu bibendum at varius vel pharetra vel turpis.'),
    (2, 'rural gas station voted best pizza in the world', 'global', 'true', '2019-11-27',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat. Faucibus pulvinar elementum integer enim neque volutpat. Tincidunt eget nullam non nisi est sit amet facilisis. Aliquet porttitor lacus luctus accumsan tortor posuere ac ut. In aliquam sem fringilla ut morbi tincidunt augue. Etiam erat velit scelerisque in dictum non consectetur. Morbi tristique senectus et netus et malesuada fames. Molestie nunc non blandit massa enim. Vivamus arcu felis bibendum ut. Eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis. Tristique senectus et netus et malesuada fames. Ut sem viverra aliquet eget sit amet tellus cras. Nibh sed pulvinar proin gravida. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus.

    Magna fringilla urna porttitor rhoncus dolor purus non enim praesent. Semper eget duis at tellus. Ullamcorper malesuada proin libero nunc. Ipsum dolor sit amet consectetur adipiscing elit. Odio pellentesque diam volutpat commodo sed. Nibh ipsum consequat nisl vel pretium lectus quam id. Dolor morbi non arcu risus quis. Velit dignissim sodales ut eu. Amet massa vitae tortor condimentum lacinia quis vel eros. Consequat mauris nunc congue nisi vitae. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. Ultrices eros in cursus turpis massa tincidunt. Sollicitudin nibh sit amet commodo nulla facilisi nullam. Sagittis id consectetur purus ut. Sed turpis tincidunt id aliquet. Ut lectus arcu bibendum at varius vel pharetra vel turpis.'),
    (2, 'a new whole foods location opens up', 'local', 'true', '2019-11-28',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat. Faucibus pulvinar elementum integer enim neque volutpat. Tincidunt eget nullam non nisi est sit amet facilisis. Aliquet porttitor lacus luctus accumsan tortor posuere ac ut. In aliquam sem fringilla ut morbi tincidunt augue. Etiam erat velit scelerisque in dictum non consectetur. Morbi tristique senectus et netus et malesuada fames. Molestie nunc non blandit massa enim. Vivamus arcu felis bibendum ut. Eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis. Tristique senectus et netus et malesuada fames. Ut sem viverra aliquet eget sit amet tellus cras. Nibh sed pulvinar proin gravida. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus.

    Magna fringilla urna porttitor rhoncus dolor purus non enim praesent. Semper eget duis at tellus. Ullamcorper malesuada proin libero nunc. Ipsum dolor sit amet consectetur adipiscing elit. Odio pellentesque diam volutpat commodo sed. Nibh ipsum consequat nisl vel pretium lectus quam id. Dolor morbi non arcu risus quis. Velit dignissim sodales ut eu. Amet massa vitae tortor condimentum lacinia quis vel eros. Consequat mauris nunc congue nisi vitae. Eget nunc scelerisque viverra mauris in aliquam sem fringilla ut. Ultrices eros in cursus turpis massa tincidunt. Sollicitudin nibh sit amet commodo nulla facilisi nullam. Sagittis id consectetur purus ut. Sed turpis tincidunt id aliquet. Ut lectus arcu bibendum at varius vel pharetra vel turpis.');
    """

    return blog_insert