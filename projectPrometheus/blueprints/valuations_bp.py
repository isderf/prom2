from flask import Blueprint, render_template
from dao import valuations_dao

valuations_bp = Blueprint('valuations', __name__)

@valuations_bp.route('/valuations')
def valuations():
    valuations = valuations_dao.getCurrentValutionsBySector()
    return render_template('valuations.html', results=valuations)
