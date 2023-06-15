from flask import Blueprint, render_template
from dao import addHolding_dao 

addHolding_bp = Blueprint('addHolding', __name__)

@addHolding_bp.route('/addHolding', methods=['GET'])
def addHolding():
    addHolding = addHolding_dao.getAllStockInfo()
    return render_template('addHolding_form.html', results=addHolding)
