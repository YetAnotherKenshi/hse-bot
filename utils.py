from datetime import datetime
import os

def save_feedback(cid, text, folder='reports'):
    fn = f'report_{str(cid)}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    path = os.path.join(folder, fn)
    try:
        with open(path, 'w') as f:
            f.write(text)
    except:
        return None
    return path