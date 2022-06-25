from flask import render_template
from data import db_session
from data.products import Product
from work_with_sheet.sheet import sheet_func
from app import app
from telega_bot.bot import bot_run
import asyncio


@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    db_sess = db_session.create_session()
    db_sess.query(Product).delete()
    db_sess.commit()
    values = sheet_func()
    for value in values[1:]:
        product = Product(
            id=value[0],
            number=value[1],
            cost_rub=value[2],
            cost_dol=value[3],
            delivery_period=value[4],
        )
        db_sess.add(product)
        db_sess.commit()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot_run('Поставка завершена!')

    products = db_sess.query(Product).order_by(Product.id)
    return render_template('index.html', products=products, data=values[0])
