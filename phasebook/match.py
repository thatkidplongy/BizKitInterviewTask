import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    new_fave_numbers_1 = set(fave_numbers_1)
    new_fave_numbers_2 = set(fave_numbers_2)
    if(new_fave_numbers_2.issubset(new_fave_numbers_1)):
        return True
    
    return False