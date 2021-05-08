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


# @app.route("/recipe/large/<int:category_id>", methods=['GET'])
# def resMedRainking(category_id):
#     # 大カテゴリを受け取り、中カテゴリIdが何なのかを調べるためカテゴリ一覧API利用
#     # 中カテゴリId分をforで繰り返し、ランキングを取得
#
#     url_list = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&categoryType=medium&applicationId=1031497863777776898'
#     category_list = requests.get(url_list).json()
#     med_category = []
#     for it in category_list['result']['medium']:
#         if category_id == int(it['parentCategoryId']):
#             med_category.append(it['categoryId'])
#
#     med_ranking = []
#     for med_id in med_category:
#         url_med_ranking = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?categoryId=' \
#                           + str(category_id) + '-' + str(med_id) + '&applicationId=1031497863777776898'
#         category_ranking = requests.get(url_med_ranking).json()
#         # print(str(category_id) + '-' + str(med_id))
#         # pprint.pprint(category_ranking)
#         it = category_ranking['result']
#         for i in range(4):
#             recipe_elem = {'title': it[i]['recipeTitle'], 'foodImageUrl': it[i]['foodImageUrl'], 'recipeUrl': it[i]['recipeUrl']}
#             # print(it[0]['recipeTitle'], it[0]['foodImageUrl'], it[0]['recipeUrl'])
#             med_ranking.append(recipe_elem)
#         time.sleep(1)
#
#     return jsonify(med_ranking)


with open("rakutenAPI_data/medium.json") as file:
    med_split_ranking = json.load(file)
index = -1
pre_category_id = -1


@app.route("/recipe/large/<int:category_id>/<int:to_next>", methods=['GET'])
def resSplitMedRanking(category_id, to_next):
    global med_split_ranking
    global index, pre_category_id
    print(index)

    # 大カテゴリ毎の中カテゴリ一覧を作成
    # 呼ばれ方（ex . to_next == 1: index++, to_next == 0: index--みたいな）
    # によって中カテゴリ群のインデックスの位置変化の向きを変える
    # 前回カテゴリIDと比較して、変化してたら、index = -1
    if pre_category_id != category_id:
        index = -1
        pre_category_id = category_id

    if to_next:
        index += 1
    else:
        index -= 1

    url_med_ranking = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?categoryId=' \
                      + str(category_id) + '-' + str(med_split_ranking[str(category_id)][index]) \
                      + '&applicationId=1031497863777776898'
    category_ranking = requests.get(url_med_ranking).json()
    # pprint.pprint(category_ranking)
    med_ranking = []
    it = category_ranking['result']
    for i in range(4):
        recipe_elem = {'title': it[i]['recipeTitle'],
                       'foodImageUrl': it[i]['foodImageUrl'],
                       'recipeUrl': it[i]['recipeUrl']}
        med_ranking.append(recipe_elem)

    return jsonify(med_ranking)


# url_list = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&categoryType=medium&applicationId=1031497863777776898'
# category_list = requests.get(url_list).json()
# med_list_of_large_category = dict()
# for it in category_list['result']['medium']:
#     if it['parentCategoryId'] not in med_list_of_large_category:
#         med_list_of_large_category[it['parentCategoryId']] = []
#     med_list_of_large_category[it['parentCategoryId']].append(it['categoryId'])
#
# with open('rakutenAPI_data/medium.json', 'w') as file:
#     json.dump(med_list_of_large_category, file, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(host="localhost", debug=True, port=8080)
