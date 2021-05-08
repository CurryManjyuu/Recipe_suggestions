# from api.test import test
from flask import Flask, render_template, request, jsonify, blueprints
from flask_restful import Api, Resource
from flask_cors import CORS

# from flask_cors import CORS
import json
import pprint
import requests
import time

# from redis import Redis
app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
# app.register_blueprint(test, url_prefix='/api')

@app.route('/')
def hello():
    # redis.incr('hits')
    return "Hello"


@app.route("/hoge", methods=['GET'])
def resMedRainking(category_id = 10):
    # 大カテゴリを受け取り、中カテゴリIdが何なのかを調べるためカテゴリ一覧API利用
    # 中カテゴリId分をforで繰り返し、ランキングを取得
    #

    url_list = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&categoryType=medium&applicationId=1031497863777776898'
    category_list = requests.get(url_list).json()
    # pprint.pprint(category_list)
    cnt_med_cate = dict()
    med_category = []
    for it in category_list['result']['medium']:
        # if it['parentCategoryId'] not in cnt_med_cate:
        #     cnt_med_cate[it['parentCategoryId']] = 0
        # else:
        #     cnt_med_cate[it['parentCategoryId']] += 1
        if category_id == int(it['parentCategoryId']):
            med_category.append(it['categoryId'])

    for med_id in med_category:
        url_med_ranking = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?categoryId=' \
                          + str(category_id) + '-' + str(med_id) + '&applicationId=1031497863777776898'
        category_rank = requests.get(url_med_ranking).json()
        print(str(category_id) + '-' + str(med_id))
        pprint.pprint(category_rank)
        time.sleep(1)



    # print(med_category)

    # pprint.pprint(cnt_med_cate)
    return jsonify(category_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(host="localhost", debug=True, port=8080)
