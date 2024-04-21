from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()

prompt = '''[지시]
이미지를 보고 가장 창의적이고 재미있는 제목을 만들어줘. 실제 상황과 반전이 있으면 더 좋아.

[예시 이미지1]
스포츠 이벤트를 관람하고 있는 젊은 남성이 있어. 그의 얼굴에서는 눈물이 흐르고 있고, 카메라를 들고 있어. 스포츠를 보며 감동적인 순간을 포착한 것처럼 보여

[예시 제목1]
경기 막바지 즈음 누른 버튼이 촬영종료 버튼이 아니라 촬영취소 버튼이었다.

[예시 이미지2]
병상에 누워 있는 환자와 그를 둘러싸고 있는 여러 사람이 있어. 환자는 침대에 앉아 있고, 상태는 좋지 않아 보여. 주변 사람 중 한 명은 환자의 손을 잡고 있고, 나머지 사람은 환자를 바라보고 있어.

[예시 제목2]
내가 막 잠든 순간에 '임종하셨습니다'라고 한 녀석 누구야?
'''

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "system",
            "content": "너는 창의력이 뛰어난 AI비서야.",
        }, 
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                "type": "image_url",
                "image_url": {
                    "url": "https://mblogthumb-phinf.pstatic.net/20160511_248/easy-drive_1462941604617zF6SX_JPEG/20160511-125800-013.jpg?type=w800",
                },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])
