from database import new_session, TaskOrm
from schemas import STaskAdd
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump() #Превращает класс к виду словаря

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush() #Отправит изменения в базу, получит все необходимые данные и только потом завершит запрос
            await session.commit()
            return task.id



    @classmethod
    async def find_all(cls):
        async with new_session() as session: 
            query = select(
                TaskOrm
            )
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
        