import base64
from flask import request
from flask import Flask
import os
import uuid
import time
app=Flask(__name__)

@app.route("/photo", methods=['POST'])
def get_frame():
    upload_file = request.files['file']
    file_name = str(uuid.uuid1()) + upload_file.filename
    file_path = "/home/vmuser/agentforP/savePicture/"
    if upload_file:
        file_paths = os.path.join(file_path, file_name)
        print(file_path)
        upload_file.save(file_paths)
        command1 = "python3 object_detection_grpc_client.py --server=localhost:9000 --input_image="+file_paths +" --output_directory=/home/vmuser/agentforP/returnPicture --label_map=/home/vmuser/examples/object_detection/serving_script/models/research/object_detection/data/pet_label_map.pbtxt  --model_name=pets-model"
        os.system(command1)
        time.sleep(20)
        file_path_out = "/home/vmuser/agentforP/returnPicture/"
        file_paths_out = file_path_out + file_name[:-4] + "_output" + file_name[-4:]
        with open(file_paths_out, 'rb') as f:
            res = base64.b64encode(f.read())
            return res

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
