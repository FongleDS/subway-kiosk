from flask import Flask, request, jsonify
from google.cloud import dialogflow

app = Flask(__name__)

@app.route('/send-message', methods=['POST'])
def send_message():
    # Dialogflow 세션 클라이언트 설정
    session_client = dialogflow.SessionsClient()

    # 요청에서 메시지 추출
    message = request.json['message']

    # Dialogflow 세션 ID와 프로젝트 ID 설정
    project_id = 'your-google-cloud-project-id'
    session_id = 'your-dialogflow-session-id'
    session = session_client.session_path(project_id, session_id)

    # 텍스트 입력 설정
    text_input = dialogflow.TextInput(text=message, language_code="ko-KR")
    query_input = dialogflow.QueryInput(text=text_input)

    # Dialogflow에 요청 보내기
    response = session_client.detect_intent(session=session, query_input=query_input)
    response_text = response.query_result.fulfillment_text

    return jsonify({'reply': response_text})

if __name__ == '__main__':
    app.run(debug=True)
