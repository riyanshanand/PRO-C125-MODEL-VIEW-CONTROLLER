






from flask import Flask, jsonify, request

from Classifyer import  get_prediction
#api intialize
app = Flask(__name__)

#api of default get request 
@app.route("/")
def show():
    return "riyansh"

#api to pridict digit post request
@app.route("/predict-digit", methods=["POST"])
def predict_data():
  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("digit")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200


#api run
if __name__ == "__main__":
  app.run(debug=True)