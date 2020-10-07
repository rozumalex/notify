async def create_task(conn, task):
    await conn.execute(f'''
        INSERT INTO id_{task.account_id}_tasks(name, enabled) VALUES(
$1, $2) RETURNING *
    ''', task.name, task.enabled)


async def get_all_tasks(conn, account_id):
    result = await conn.fetch(f'''
        SELECT * FROM id_{account_id}_tasks
    ''')
    return result


async def get_task_by_id(conn, task):
    result = await conn.fetchrow(f'''
        SELECT * FROM id_{task.account_id}_tasks WHERE id=$1''', task.id)
    return result


async def delete_task(conn, task):
    await conn.execute(
        f'''DELETE FROM id_{task.account_id}_tasks WHERE id = $1''', task.id)


async def update_task(conn, task):
    await conn.execute(
        f'''UPDATE id_{task.account_id}_tasks SET name = $2,
enabled = $3 WHERE id = $1''',
        task.id, task.name, task.enabled)
    print(f'''UPDATE id_{task.account_id}_tasks SET name = $2,
enabled = $3 WHERE id = $1''', task.id, task.name, task.enabled)
