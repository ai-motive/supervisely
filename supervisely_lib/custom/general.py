# coding: utf-8
from python_utils.image import coordinates as ic
import supervisely_lib as sly


def generate_json_template(img_shape=None):
    if img_shape:
        h, w, c = img_shape
    else:
        h, w, c = None, None, None

    template = {
        'description': '',
        'size': {
            'height': h,
            'width' : w,
        },
        'tags'   : [],
        'objects': []
    }

    return template


def save_json_from_results(results_dict, label_dict, rst_json_path):
    for key, vals in results_dict.items():
        if results_dict.get(key):
            for val in vals:
                min_x, max_x, min_y, max_y = ic.convert_rect4_to_rect2(val[0])
                text = val[1]
                obj_class = sly.ObjClass(key.lower(), sly.Rectangle)
                label = sly.Label(sly.Rectangle(top=min_y, left=min_x, bottom=max_y, right=max_x),
                                  obj_class,
                                  description=text)

                label_dict['objects'].append(label.to_json())

    sly.io.json.dump_json_file(label_dict, rst_json_path)

    return True