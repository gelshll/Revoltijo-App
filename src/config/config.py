import json

class Config:
    try:
        with open('src/config/config.json', 'r', encoding='utf8') as f:
            data = json.load(f)

            token = data['token']
            prefix = data['prefix']
    except Exception as e:
        print(f'Error: {e}')
      
    