import azure.functions as func

import logging
import os
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['OPENBLAS_NUM_THREADS'] = '1'

import numpy as np
import implicit
from scipy.sparse import csr_matrix
import json


# Load data
csr_article_popularity = np.load('csr_article_popularity.npz')
csr_article_popularity = csr_matrix((csr_article_popularity['data'], csr_article_popularity['indices'], csr_article_popularity['indptr']), shape=csr_article_popularity['shape'])

# Load Implicit model
model = implicit.als.AlternatingLeastSquares()
model = model.load('als_implicit_model.npz')


def recommend_collaborative_articles(user_id):
    article_ids, scores = model.recommend(user_id, csr_article_popularity[user_id], N=5, filter_already_liked_items=True)

    return article_ids


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    user_id = req.params.get('user_id')
    if not user_id:
        try:
            req_body = req.get_json()
            user_id = req_body.get('user_id')
        except ValueError:
            pass

    if user_id:
        article_ids = recommend_collaborative_articles(int(user_id))
        articles = ", ".join([str(x) for x in article_ids])
        return func.HttpResponse(json.dumps(articles))
    else:
        return func.HttpResponse(
             "Lol This HTTP triggered function executed successfully. Pass a user_id in the query string or in the request body for a personalized response.",
             status_code=200
        )