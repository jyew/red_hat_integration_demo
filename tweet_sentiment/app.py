from flask import Flask
from flask import Response
from flask_cors import CORS
from flask_cors import CORS
from flask import jsonify
from flask_restful import Api, Resource, reqparse
from nemo.collections import nlp as nemo_nlp
from nemo.collections.nlp.parts.utils_funcs import tensor2list
from nemo.collections.nlp.models.text_classification import TextClassificationModel
from nemo.collections.nlp.data.text_classification import TextClassificationDataset
import numpy as np
import torch
import onnxruntime


app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
checkpointPath = 'model_repository/TextClassification--val_loss=0.4835-epoch=4-last.ckpt'
modelPath = 'model_repository/sentiment_onnx/1/model.onnx'

model = nemo_nlp.models.TextClassificationModel.load_from_checkpoint(checkpoint_path=checkpointPath)
model.eval()
ort_session = onnxruntime.InferenceSession(modelPath)

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

def postprocessing(results, labels):
    return [labels[str(r)] for r in results]

def create_infer_dataloader(model, queries):
    batch_size = len(queries)
    dataset = TextClassificationDataset(tokenizer=model.tokenizer, queries=queries, max_seq_length=512)
    return torch.utils.data.DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=2,
        pin_memory=True,
        drop_last=False,
        collate_fn=dataset.collate_fn,
    )

@app.route('/')
def index():
    # return render_template("index.html")
    return "This is the most amazing app EVER."

class predict_sentiment(Resource):
    """Sample request: 
        curl -H 'Content-type: application/json' -X POST -d '{"queries": ["this is a bad movie", "this is a good movie"]}' http://localhost:8000/predict_sentiment
    """
    def post(self):
        parser.add_argument('queries', type=str, action="append", location='json')
        args = parser.parse_args()
        queries = args['queries']
        if queries is not None:
            results = []
            infer_datalayer = create_infer_dataloader(model, queries)
            for batch in infer_datalayer:
                input_ids, input_type_ids, input_mask, subtokens_mask = batch
                ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(input_ids),
                            ort_session.get_inputs()[1].name: to_numpy(input_mask),
                            ort_session.get_inputs()[2].name: to_numpy(input_type_ids),}
                ologits = ort_session.run(None, ort_inputs)
                alogits = np.asarray(ologits)
                logits = torch.from_numpy(alogits[0])
                preds = tensor2list(torch.argmax(logits, dim = -1))
                processed_results = postprocessing(preds, {"0": "negative", "1": "positive"})
                for query, result in zip(queries, processed_results):
                    print(f'Query : {query}')
                    print(f'Predicted label: {result}')
            response = {'queries': queries, 'results': processed_results}
            return jsonify(response)
        return Response("Please submit a list of strings", status=400)

api.add_resource(predict_sentiment, '/predict_sentiment')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')