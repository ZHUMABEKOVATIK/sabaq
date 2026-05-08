from .db.sessions import async_main

from src.repositories.users import UserRepo
from src.repositories.orders import OrdersRepo





async def main():
    await async_main()
    u = UserRepo()

    data = await u.get_by_id(2)
    user = {
        'id': data.id,
        'name': data.name,
    }
    orders = []
    for i in data.orders:
        orders.append({
            'id': i.id,
            'name': i.name
        })
    user['orders'] = orders
    print(user)
    # o = OrdersRepo()
    # await o.create(2, 'Strawberry')












import asyncio
asyncio.run(main())


{
    'id': 1, 
    'name': 'John', 
    'orders': [
        {
            'id': 1, 
            'name': 'Tomato'
        }, 
        {
            'id': 2, 
            'name': 'Potato'
        }, 
        {
            'id': 3, 
            'name': 'Cucumber'
        }
    ]
}