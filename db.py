import sqlite3

global path
path = 'history'

# 创建数据库
def create_db():
    conn = sqlite3.connect(f'{path}.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS history (
    user_id TEXT,
    role TEXT,
    content TEXT
    )
    ''')
    conn.commit()
    conn.close()

# 添加历史记录
def add_history(user_id, role, content):
    conn = sqlite3.connect(f'{path}.db')
    c = conn.cursor()
    c.execute('INSERT INTO history (user_id, role, content) VALUES (?, ?, ?)', (user_id, role, content))
    conn.commit()
    conn.close()

# 获取历史记录
def get_history(user_id):
    try:
        # 建立数据库连接（假设 'path' 是数据库路径）
        conn = sqlite3.connect(f'{path}.db')
        c = conn.cursor()
        
        # 查询数据库
        c.execute('SELECT role, content FROM history WHERE user_id=? ORDER BY rowid', (user_id,))
        history = c.fetchall()
        
        # 将结果转换为字典列表
        history_dict = [{'role': row[0], 'content': row[1]} for row in history]
        
        # 关闭数据库连接
        conn.close()
        
        return history_dict
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"General error: {e}")
        return []